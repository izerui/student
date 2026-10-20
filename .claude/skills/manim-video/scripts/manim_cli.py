#!/usr/bin/env python3
"""ManimCE 讲解视频工具箱 —— 新建项目 / 布局检测 / 渲染 / 抽帧 / 验收。

这些命令是这条流水线的唯一入口。不要绕过它们直接敲 `manim` ——
它们负责注入运行时路径、串起检查闸门、解析报告、定位产物。

    python3 scripts/manim_cli.py new      <slug>            新建视频项目
    python3 scripts/manim_cli.py check    <slug>            结构 + LaTeX + 旁白 + cue 检查
    python3 scripts/manim_cli.py layout   <slug>            dry_run 跑完动画，报越界/重叠/静止
    python3 scripts/manim_cli.py render   <slug> [-q draft|final] [-r WxH]
    python3 scripts/manim_cli.py stills   <slug> <秒数…>     从成片抽关键帧
    python3 scripts/manim_cli.py verify   <slug>            成片机械验收
    python3 scripts/manim_cli.py doctor                     环境依赖预检

渲染前必须先 layout 通过：回执按输入指纹绑定（script.py + durations.json + .narration-manifest.json），任一文件变化就得重测。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
RUNTIME_DIR = SKILL_DIR / "runtime"
SCRIPTS_DIR = SKILL_DIR / "scripts"


def _project_root() -> Path:
    """找到项目根。skill 只放代码和文档，视频产物一律落在项目根下。

    顺序：显式指定 > 向上找 .git > skill 的上三级（`<root>/.claude/skills/<name>/`）。
    """
    override = os.environ.get("TEACHING_VIDEO_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve().parent

    for parent in SKILL_DIR.parents:
        if (parent / ".git").exists():
            return parent
    # 没有 git 仓库时按目录布局回推：scripts/ -> skill -> skills/ -> .claude/ -> 根
    return SKILL_DIR.parent.parent.parent


def _videos_dir() -> Path:
    override = os.environ.get("TEACHING_VIDEO_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return _project_root() / "videos"


VIDEOS_DIR = _videos_dir()

LAYOUT_RECEIPT = ".layout-check.json"
CHECK_RECEIPT = ".manim-check.json"

DRY_RUN_TIMEOUT = 10 * 60
RENDER_TIMEOUT = 30 * 60
CHECK_TIMEOUT = 5 * 60


# ---------------------------------------------------------------------------
# 通用
# ---------------------------------------------------------------------------

class Fail(Exception):
    """预期内的失败：只打印消息，不打印 traceback。"""


def info(message: str) -> None:
    print(message, flush=True)


def run(cmd, *, cwd=None, timeout=None, env=None):
    """跑一条命令，返回 (returncode, 合并输出)。永不抛异常。"""
    merged = os.environ.copy()
    # 让 script.py 能 `from teaching_runtime import ...`，不必把运行时复制进项目。
    merged["PYTHONPATH"] = os.pathsep.join(
        [str(RUNTIME_DIR), merged.get("PYTHONPATH", "")]
    ).rstrip(os.pathsep)
    if env:
        merged.update(env)
    try:
        proc = subprocess.run(
            cmd, cwd=cwd, timeout=timeout, env=merged,
            capture_output=True, text=True, check=False,
        )
        return proc.returncode, f"{proc.stdout}\n{proc.stderr}".strip()
    except subprocess.TimeoutExpired as exc:
        tail = ""
        for stream in (exc.stdout, exc.stderr):
            if stream:
                tail += stream if isinstance(stream, str) else stream.decode("utf8", "replace")
        return 124, f"超时（{timeout}s）\n{tail}"
    except FileNotFoundError:
        return 127, f"找不到可执行文件: {cmd[0]}"


def _resolve_python() -> str:
    """找到可用的 Python 解释器。优先级：环境变量 > venv > PATH。"""
    override = os.environ.get("MANIM_VIDEO_PYTHON", "").strip()
    if override and shutil.which(override):
        return override
    venv_python = RUNTIME_DIR / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def uv_run(args, *, cwd, timeout):
    """在 skill 自带的 Python 环境里跑命令。所有项目共用这一个 venv。

    统一用 `python -m manim` 而不是直接调 manim 可执行文件——后者的 shebang
    包含绝对路径，换目录或换机器就会失效。
    """
    python = _resolve_python()
    cmd = list(args)
    if cmd and cmd[0] in ("manim", "manimce"):
        cmd[0:1] = [python, "-m", "manim"]
    elif cmd and cmd[0] == "python":
        cmd[0] = python
    return run(cmd, cwd=cwd, timeout=timeout)


def resolve_workspace(raw: str) -> Path:
    """项目可以写全路径，也可以只写 slug（则在 videos/ 下找）。"""
    candidate = Path(raw).expanduser()
    if candidate.is_dir():
        return candidate.resolve()
    nested = VIDEOS_DIR / raw
    if nested.is_dir():
        return nested.resolve()
    raise Fail(f"项目不存在: {raw}\n  可用: {', '.join(p.name for p in sorted(VIDEOS_DIR.glob('*'))) or '（无）'}")


def script_path(workspace: Path, name: str = "script.py") -> Path:
    target = (workspace / name).resolve()
    if not str(target).startswith(str(workspace.resolve())):
        raise Fail("脚本必须位于项目内")
    if not target.exists():
        raise Fail(f"找不到 {target}")
    return target


def _file_hash(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def input_fingerprint(workspace: Path, script: Path) -> str:
    """script.py + durations.json + .narration-manifest.json 的联合指纹。
    任何一个文件变化，旧回执自动失效。"""
    parts = [
        _file_hash(script),
        _file_hash(workspace / "durations.json"),
        _file_hash(workspace / ".narration-manifest.json"),
    ]
    return hashlib.sha256("|".join(parts).encode()).hexdigest()


def write_receipt(workspace: Path, name: str, payload: dict) -> None:
    payload = {**payload, "checkedAt": datetime.now(timezone.utc).isoformat()}
    (workspace / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", "utf8")


def valid_receipt(workspace: Path, name: str, script: Path) -> bool:
    """回执按输入指纹绑定：脚本、配音时长、旁白清单任一变化，旧回执立刻失效。"""
    try:
        receipt = json.loads((workspace / name).read_text("utf8"))
    except (OSError, json.JSONDecodeError):
        return False
    return receipt.get("inputFingerprint") == input_fingerprint(workspace, script)


def detect_scene_class(path: Path) -> str:
    """从脚本里找出唯一的 Scene 子类名，省得每次手敲。"""
    source = path.read_text("utf8")
    names = re.findall(
        r"^class\s+(\w+)\s*\(\s*(?:\w+\.)?(\w*Scene\w*)\s*[),]", source, re.MULTILINE
    )
    candidates = [name for name, _ in names]
    if not candidates:
        raise Fail(f"{path.name} 里没有找到 Scene 子类。至少要有一个 `class X(Scene):`。")
    return candidates[-1]


# ---------------------------------------------------------------------------
# new：建项目
# ---------------------------------------------------------------------------

STARTER = '''"""{slug} —— 讲解视频场景。

运行顺序：
  1. 写 segments.json（分段旁白 + cue）
  2. node  scripts/narrate.mjs   videos/{slug}
  3. 写本文件
  4. python3 scripts/manim_cli.py check  {slug}
  5. python3 scripts/manim_cli.py layout {slug}     ← 必须零问题
  6. python3 scripts/manim_cli.py render {slug} -q draft
  7. python3 scripts/manim_cli.py stills {slug} 3 8 15   ← 看真实画面
  8. python3 scripts/manim_cli.py render {slug} -q final
"""

# pyright: reportMissingImports=false, reportUndefinedVariable=false
from manim import *

from teaching_runtime import (
    AudioManager,
    CJK_FONT,
    LATIN_FONT,              # 纯拉丁文本用它；中英混排的行仍用 CJK_FONT
    add_background,
    enable_layout_guard,
    find_free_pos,
    pulse,                   # 强调用它，别用 Indicate（会把容器里的文字染没）
    safe_area,
    # 语义色板：已在黑板底上验过对比度，按语义取用，不要写死十六进制或用 ManimCE 原色
    INK, ACCENT, CORRECT, SECOND, DATA, WRONG, MUTED,
)


class Lesson(Scene):
    def construct(self):
        add_background(self)        # 黑板底；不想要就删这行
        enable_layout_guard(self)   # 越界/重叠/静止检测，必须开
        audio = AudioManager(self)

        # —— 每段旁白一个 block ——
        # duration = audio.start("s1")
        # audio.wait_for_cue("c1")
        # self.play(...)
        # audio.end(duration)
'''

SEGMENTS_STARTER = [
    {
        "id": "s1",
        "text": "把这一段换成真正的旁白。marker 必须逐字出现在这段文字里。",
        "cues": [{"id": "c1", "marker": "marker 必须逐字出现"}],
    }
]


SCAFFOLD_HEAD = '''"""{slug} —— 讲解视频场景。

由 `manim_cli.py scaffold` 依 durations.json 生成骨架：每段旁白一个方法。
**一次只填一个方法**，用 Edit 逐段落盘，不要试图一次写出整个文件——
实测一条 9 场景的片子成稿 26–37KB，读完参考文档后再一次性吐出这么大一坨，
连续三个智能体都卡在这里、写入 0 字节。分段写就不会。
"""

# pyright: reportMissingImports=false, reportUndefinedVariable=false
from manim import *

from teaching_runtime import (
    AudioManager,
    CJK_FONT,
    LATIN_FONT,              # 纯拉丁文本用它；中英混排的行仍用 CJK_FONT
    add_background,
    enable_layout_guard,
    find_free_pos,
    pulse,                   # 强调用它，别用 Indicate（会把容器里的文字染没）
    safe_area,
    # 语义色板：已在黑板底上验过对比度，按语义取用，不要写死十六进制或用 ManimCE 原色
    INK, ACCENT, CORRECT, SECOND, DATA, WRONG, MUTED,
)


class Lesson(Scene):
    def construct(self):
        add_background(self)        # 黑板底；不想要就删这行
        enable_layout_guard(self)   # 越界/重叠/静止检测，必须开
        audio = AudioManager(self)

{calls}
'''

SCAFFOLD_METHOD = '''    def {sid}(self, audio):
        """{sid} · {dur:.1f}s · cue: {cues}"""
        d = audio.start("{sid}")
{body}        audio.end(d)
'''


def cmd_scaffold(args) -> int:
    """按 durations.json 生成分段骨架，每段旁白一个方法。

    这不是为了省打字，是为了绕开一个真实的失败模式：写 script.py 是整条流水线里
    唯一需要一次性产出大块文本的步骤，而它又恰好排在"读完参考文档"之后、
    上下文最满的时候。把它拆成"先出骨架，再一段一段填"，单次产出就降到一两千字节。
    """
    workspace = resolve_workspace(args.workspace)
    path = workspace / "durations.json"
    if not path.exists():
        raise Fail(f"找不到 {path}。先写 segments.json 并跑配音，再来 scaffold。")
    data = json.loads(path.read_text("utf8"))

    script = workspace / "script.py"
    if script.exists() and len(script.read_text("utf8")) > 2000 and not args.force:
        raise Fail(f"{script} 已有内容（{len(script.read_text('utf8'))} 字节），"
                   "不覆盖。确认要重来请加 --force")

    methods, calls = [], []
    for sid, seg in data.items():
        cues = [c["id"] for c in seg.get("cuePoints", [])]
        body = "".join(
            f'        audio.wait_for_cue("{c}")\n'
            f'        # TODO {c}: 这里放这句旁白对应的画面动作\n'
            f'        self.wait(0.1)\n'
            for c in cues
        ) or "        # TODO: 这一段的画面\n        self.wait(0.1)\n"
        methods.append(SCAFFOLD_METHOD.format(
            sid=sid, dur=seg["durationSec"],
            cues=", ".join(cues) or "无", body=body))
        calls.append(f"        self.{sid}(audio)")

    script.write_text(
        SCAFFOLD_HEAD.format(slug=workspace.name, calls="\n".join(calls))
        + "\n" + "\n".join(methods),
        "utf8",
    )
    info(
        f"骨架已生成: {script}\n"
        f"  {len(data)} 段，共 {sum(len(s.get('cuePoints', [])) for s in data.values())} 个 cue，"
        f"每段一个方法、每个 cue 一个 TODO\n"
        f"  接下来**一次 Edit 填一个方法**，从 {next(iter(data))} 开始，填完一个再填下一个"
    )
    return 0


def cmd_new(args) -> int:
    slug = args.slug.strip()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", slug):
        raise Fail("slug 只能用字母、数字、下划线、连字符")
    workspace = VIDEOS_DIR / slug
    if workspace.exists() and any(workspace.iterdir()) and not args.force:
        raise Fail(f"项目已存在且非空: {workspace}\n  要重建请加 --force")

    (workspace / "public" / "audio").mkdir(parents=True, exist_ok=True)
    shutil.copy(RUNTIME_DIR / "manim.cfg", workspace / "manim.cfg")

    script = workspace / "script.py"
    if not script.exists() or args.force:
        script.write_text(STARTER.format(slug=slug), "utf8")
    segments = workspace / "segments.json"
    if not segments.exists() or args.force:
        segments.write_text(json.dumps(SEGMENTS_STARTER, indent=2, ensure_ascii=False) + "\n", "utf8")

    info(
        f"项目就绪: {workspace}\n"
        f"  script.py     场景代码\n"
        f"  segments.json 分段旁白（先写这个）\n"
        f"  manim.cfg     渲染配置\n"
        f"  public/audio/ 旁白音频（由 narrate.mjs 产出）"
    )
    return 0


# ---------------------------------------------------------------------------
# check：结构 / LaTeX / 旁白 / cue
# ---------------------------------------------------------------------------

def cmd_check(args) -> int:
    workspace = resolve_workspace(args.workspace)
    script = script_path(workspace, args.script)

    checks_py = str(SCRIPTS_DIR / "checks.py")
    checks = [
        ("Python 语法", [sys.executable, "-m", "py_compile", str(script)], False),
        ("ManimCE 结构与 API", [sys.executable, checks_py, str(script)], False),
        ("LaTeX 预编译", ["python", checks_py, "--preflight-tex", str(script)], True),
        ("旁白产物清单", [sys.executable, checks_py, "--validate-audio", str(workspace)], False),
        ("cue 消费完整性", [sys.executable, checks_py, "--validate-cues",
                            str(workspace), script.name], False),
    ]

    failures = []
    for name, cmd, needs_manim in checks:
        code, output = (uv_run(cmd, cwd=workspace, timeout=CHECK_TIMEOUT) if needs_manim
                        else run(cmd, cwd=workspace, timeout=CHECK_TIMEOUT))
        if code == 0:
            info(f"  ✓ {name}")
            if output.strip() and args.verbose:
                info("    " + output.strip().replace("\n", "\n    "))
        else:
            failures.append(name)
            info(f"  ✗ {name}")
            info("    " + (output.strip()[-4000:] or "（无输出）").replace("\n", "\n    "))

    if failures:
        info(f"\n检查未通过: {'、'.join(failures)}")
        return 1

    write_receipt(workspace, CHECK_RECEIPT, {"script": script.name, "inputFingerprint": input_fingerprint(workspace, script)})
    info("\n工程检查全部通过。")
    return 0


# ---------------------------------------------------------------------------
# layout：dry_run 布局检测
# ---------------------------------------------------------------------------

BOUNDARY_RE = re.compile(r"^\[layout-guard\] 越界: (.+)$", re.MULTILINE)
OVERLAP_RE = re.compile(r"^\[layout-guard\] 重叠: (.+)$", re.MULTILINE)
STATIC_RE = re.compile(r"^\[layout-guard\] 静止: (.+)$", re.MULTILINE)


def cmd_layout(args) -> int:
    workspace = resolve_workspace(args.workspace)
    script = script_path(workspace, args.script)
    scene = args.scene or detect_scene_class(script)

    info(f"dry_run 执行全部动画（不编码视频）… 场景 {scene}")
    code, output = uv_run(
        ["manim", "-ql", "--disable_caching", "--dry_run", script.name, scene],
        cwd=workspace, timeout=DRY_RUN_TIMEOUT,
    )

    boundaries = BOUNDARY_RE.findall(output)
    overlaps = OVERLAP_RE.findall(output)
    statics = STATIC_RE.findall(output)

    # dry_run 本身崩了（语法错、import 失败、LaTeX 编译不过）——先修这个。
    if code != 0 and not (boundaries or overlaps or statics):
        info(f"\ndry_run 执行失败（退出码 {code}）：\n{output[-6000:]}")
        return 1

    if not any([boundaries, overlaps, statics]):
        if "[layout-guard]" not in output and "enable_layout_guard" not in script.read_text("utf8"):
            info(
                "\n未检测到布局守卫输出。请在 construct() 开头调用 enable_layout_guard(self)，"
                "否则越界、重叠和旁白静止都不会被发现。"
            )
            return 1
        write_receipt(workspace, LAYOUT_RECEIPT, {"script": script.name, "inputFingerprint": input_fingerprint(workspace, script)})
        info("\n布局检测通过：零越界、零重叠、零旁白静止。")
        return 0

    info("")
    if boundaries:
        info(f"越界 {len(boundaries)} 处 —— 元素超出安全区（中心在区内但边缘出界也算）：")
        for item in boundaries:
            info(f"  · {item}")
    if overlaps:
        info(f"\n重叠 {len(overlaps)} 处 —— 先找根因（同一 mobject 挂在两个 VGroup、"
             f"阶段结束没整体退出、结论链没重排），别只挪坐标或缩字号：")
        for item in overlaps:
            info(f"  · {item}")
    if statics:
        info(f"\n旁白静止 {len(statics)} 段 —— 有旁白但画面不动：")
        for item in statics:
            info(f"  · {item}")

    info(
        "\n两类问题会互相影响：补动画可能压到别的元素，挪位置可能腾出新的静止区间。"
        "每轮都要一起看，改完重跑 layout，直到三项全零才能渲染。"
    )
    return 1


# ---------------------------------------------------------------------------
# render
# ---------------------------------------------------------------------------

def parse_resolution(value: str | None):
    if not value:
        return None
    match = re.fullmatch(r"(\d+)\s*[x×]\s*(\d+)", value.strip())
    if not match:
        raise Fail(f"分辨率格式应为 宽x高，例如 1920x1080；收到: {value}")
    # ManimCE 的 -r 用逗号分隔，和 ManimGL 的 WIDTHxHEIGHT 不同。
    return f"{int(match.group(1))},{int(match.group(2))}"


def find_output(root: Path, name: str) -> Path | None:
    matches = sorted(root.rglob(name), key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0] if matches else None


def cmd_render(args) -> int:
    workspace = resolve_workspace(args.workspace)
    script = script_path(workspace, args.script)
    scene = args.scene or detect_scene_class(script)
    draft = args.quality == "draft"
    output_name = "draft.mp4" if draft else "final_output.mp4"

    if not args.skip_gates:
        if not valid_receipt(workspace, CHECK_RECEIPT, script):
            raise Fail("渲染前先跑 `check`（或 script.py 在检查后又改过，需要重跑）。")
        if not valid_receipt(workspace, LAYOUT_RECEIPT, script):
            raise Fail("渲染前先跑 `layout` 并通过（或 script.py 在检测后又改过，需要重测）。")

    cmd = ["manim", "-qh" if not draft else "-ql", "--disable_caching",
           "-o", output_name, script.name, scene]
    resolution = parse_resolution(args.resolution)
    if resolution and not draft:
        cmd[3:3] = ["-r", resolution]

    info(f"渲染 {output_name}（{'低清草稿' if draft else '高清成片'}，场景 {scene}）…")
    code, output = uv_run(
        cmd,
        cwd=workspace, timeout=RENDER_TIMEOUT,
    )

    log_path = workspace / f"render-{'draft' if draft else 'final'}.log"
    log_path.write_text(output, "utf8")

    produced = find_output(workspace / "media", output_name)
    if code != 0 or not produced:
        info(f"\n渲染失败（退出码 {code}）。完整日志: {log_path}\n{output[-6000:]}")
        return 1

    target = workspace / output_name
    shutil.copy(produced, target)

    # 真实渲染里守卫仍可能报问题（dry_run 与实渲的浮点路径有细微差别）——让它浮出来，别只留在日志里。
    leftovers = BOUNDARY_RE.findall(output) + OVERLAP_RE.findall(output)
    if leftovers:
        info(f"\n注意：渲染过程中布局守卫仍报了 {len(leftovers)} 条问题：")
        for item in leftovers[:10]:
            info(f"  · {item}")

    if not args.no_subtitles:
        srt = generate_srt(workspace)
        if srt:
            subtitled = workspace / f"subtitled-{output_name}"
            sub_cmd = [
                "ffmpeg", "-y", "-v", "error",
                "-i", str(target),
                "-vf", f"subtitles={srt}:force_style='FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,MarginV=30'",
                "-c:a", "copy",
                str(subtitled),
            ]
            info("烧入字幕…")
            result = subprocess.run(sub_cmd, capture_output=True, text=True, timeout=RENDER_TIMEOUT)
            if result.returncode == 0 and subtitled.exists():
                shutil.move(str(subtitled), str(target))
                info(f"字幕已烧入: {target}")
            else:
                info(f"字幕烧入失败（退出码 {result.returncode}），保留无字幕版本。\n{result.stderr[-2000:]}")
        else:
            info("未找到 segments.json 或 durations.json，跳过字幕。")

    info(f"\n完成: {target}")
    return probe_and_report(target, strict=not draft)


# ---------------------------------------------------------------------------
# 字幕：从 segments.json + durations.json 生成 SRT
# ---------------------------------------------------------------------------

def _fmt_srt_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


_SENTENCE_END = re.compile(r"(?<=[。！？；])")


def _split_sentences(text: str) -> list[str]:
    """按中文句末标点拆句。连续短句（<6 字）合并到前一句，避免太碎。"""
    parts = [s.strip() for s in _SENTENCE_END.split(text) if s.strip()]
    if len(parts) <= 1:
        return parts or [text]
    merged: list[str] = [parts[0]]
    for p in parts[1:]:
        if len(p) < 6:
            merged[-1] += p
        else:
            merged.append(p)
    return merged


_SILENCE_RE = re.compile(
    r"silence_end:\s*([\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)"
)


def _detect_silences(audio_path: Path) -> list[tuple[float, float]]:
    """用 ffmpeg silencedetect 找音频中的静音区间，返回 [(midpoint, duration), …]。"""
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", str(audio_path),
             "-af", "silencedetect=noise=-30dB:d=0.12",
             "-f", "null", os.devnull],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []

    silences: list[tuple[float, float]] = []
    for m in _SILENCE_RE.finditer(result.stderr):
        silence_end = float(m.group(1))
        silence_dur = float(m.group(2))
        midpoint = silence_end - silence_dur / 2
        silences.append((midpoint, silence_dur))
    return silences


def _align_sentences_to_silences(
    sentences: list[str], silences: list[tuple[float, float]],
    speech_start: float, speech_end: float,
) -> list[tuple[float, float, str]]:
    """把 N 句话对齐到音频的静音间隔。

    先按字符比例估算每个句子边界的大致时间，再把每个边界
    吸附到最近的静音中点——线性估算给方向，静音检测给精度。
    """
    n = len(sentences)
    if n == 0:
        return []
    if n == 1:
        return [(speech_start, speech_end, sentences[0])]

    speech_dur = speech_end - speech_start
    total_chars = max(1, sum(len(s) for s in sentences))

    margin = 0.1
    candidates = [mid for mid, _ in silences
                  if speech_start + margin < mid < speech_end - margin]

    char_offset = 0
    boundaries = [speech_start]
    used: set[int] = set()
    for i in range(n - 1):
        char_offset += len(sentences[i])
        estimated = speech_start + (char_offset / total_chars) * speech_dur

        best_idx = -1
        best_dist = float("inf")
        for ci, c in enumerate(candidates):
            if ci in used:
                continue
            dist = abs(c - estimated)
            if dist < best_dist:
                best_dist = dist
                best_idx = ci

        if best_idx >= 0 and best_dist < speech_dur * 0.15:
            boundaries.append(candidates[best_idx])
            used.add(best_idx)
        else:
            boundaries.append(estimated)

    boundaries.append(speech_end)

    return [(boundaries[i], boundaries[i + 1], sentences[i]) for i in range(n)]


def generate_srt(workspace: Path) -> Path | None:
    """按句生成 SRT 字幕文件，每条字幕一句话。

    用 ffmpeg silencedetect 检测音频中的停顿来定位句子边界。
    TTS 语音的句间停顿非常规律，静音检测精度远高于字符位置线性估算。
    """
    segments_path = workspace / "segments.json"
    durations_path = workspace / "durations.json"
    if not segments_path.exists() or not durations_path.exists():
        return None

    segments = json.loads(segments_path.read_text("utf8"))
    durations = json.loads(durations_path.read_text("utf8"))

    srt_lines: list[str] = []
    index = 1
    base = 0.0
    for seg in segments:
        sid = seg["id"]
        text = seg.get("text", "").strip()
        dur = durations.get(sid)
        if not dur or not text:
            if dur:
                base += float(dur["durationSec"])
            continue

        speech_start = float(dur["speechStartSec"])
        speech_end = float(dur["speechEndSec"])
        sentences = _split_sentences(text)

        audio_file = workspace / "public" / dur["file"]
        if audio_file.exists():
            silences = _detect_silences(audio_file)
        else:
            silences = []

        entries = _align_sentences_to_silences(
            sentences, silences, speech_start, speech_end,
        )

        for t0, t1, sentence in entries:
            srt_lines.append(f"{index}")
            srt_lines.append(f"{_fmt_srt_time(base + t0)} --> {_fmt_srt_time(base + t1)}")
            srt_lines.append(sentence)
            srt_lines.append("")
            index += 1

        base += float(dur["durationSec"])

    if not srt_lines:
        return None

    srt_path = workspace / "subtitles.srt"
    srt_path.write_text("\n".join(srt_lines), "utf8")
    return srt_path


# ---------------------------------------------------------------------------
# stills：从成片抽帧
# ---------------------------------------------------------------------------

def cue_timeline(workspace: Path, offset: float = 1.0) -> list[tuple[float, str]]:
    """把 durations.json 的 cue 点摊平成成片上的绝对秒数。

    cue 点是旁白讲到某句话的时刻，也就是画面该切到下一个状态的时刻——换句话说，
    **它们就是这条片子的状态迁移表**。手填时间点抽帧只能碰运气；按 cue 抽，
    每一次状态切换都会被看到一眼。

    实测教训：一条片子在「单叶双曲面」出现的同时留着上一状态的特征值读数
    （内容错了，但不越界、不重叠、不静止，所有机械闸门全绿），
    就因为没人抽到那 2.3 秒而漏进成片。
    """
    path = workspace / "durations.json"
    if not path.exists():
        raise Fail(f"找不到 {path}，--cues 需要它。先跑配音。")
    data = json.loads(path.read_text("utf8"))

    marks: list[tuple[float, str]] = []
    base = 0.0
    for seg_id, seg in data.items():
        marks.append((base + offset, f"{seg_id}起"))
        for cue in seg.get("cuePoints", []):
            marks.append((base + float(cue["timeSec"]) + offset, f"{seg_id}/{cue['id']}"))
        base += float(seg["durationSec"])
    return marks


def cmd_stills(args) -> int:
    workspace = resolve_workspace(args.workspace)
    video = workspace / args.video
    if not video.exists():
        raise Fail(f"找不到 {video}。先渲染 draft。")

    labels: dict[float, str] = {}
    if getattr(args, "cues", False):
        marks = cue_timeline(workspace, args.cue_offset)
        if len(marks) > args.max:
            step = len(marks) / args.max
            picked = [marks[int(i * step)] for i in range(args.max)]
            info(f"共 {len(marks)} 个 cue，按 --max={args.max} 等距抽稀。"
                 f"要全看就加 --max {len(marks)}")
            marks = picked
        args.seconds = [round(t, 2) for t, _ in marks]
        labels = {round(t, 2): name for t, name in marks}

    if not args.seconds:
        raise Fail("至少给一个时间点，例如: stills myslug 3 8 15；"
                   "或用 --cues 按旁白 cue 自动取样")

    out_dir = workspace / "stills"
    out_dir.mkdir(exist_ok=True)
    produced = []
    for second in args.seconds:
        target = out_dir / f"t{str(second).replace('.', '_')}s.png"
        code, output = run(
            ["ffmpeg", "-y", "-v", "error", "-ss", str(second), "-i", str(video),
             "-frames:v", "1", str(target)],
            timeout=120,
        )
        if code != 0 or not target.exists():
            info(f"  ✗ {second}s 抽帧失败: {output[-500:]}")
            continue
        produced.append(target)
        tag = labels.get(second)
        info(f"  ✓ {second}s -> {target}" + (f"   [{tag}]" if tag else ""))

    if not produced:
        return 1
    info(
        f"\n抽了 {len(produced)} 帧。用 Read 工具逐张看真实画面——"
        "几何检测查不出的问题都在这里：笔画挤在一起、标注框贴死边缘、"
        "LaTeX 渲染结果和预期不符、画面过空或信息堆成一团。"
    )
    if labels:
        info(
            "每帧对应一次旁白 cue，也就是一次画面状态切换。逐张对照这一刻旁白在讲什么，"
            "重点看**上一状态的标注有没有留在屏幕上**——过期的读数、标签、结论与新画面并置，"
            "是机械闸门永远查不出、却会把人讲错的一类错误。"
        )
    return 0


# ---------------------------------------------------------------------------
# verify：成片验收
# ---------------------------------------------------------------------------

def ffprobe_value(path: Path, args: list[str]) -> float:
    code, output = run(["ffprobe", "-v", "error", *args, "-of", "default=nk=1:nw=1", str(path)], timeout=60)
    if code != 0:
        return 0.0
    try:
        return float(output.strip().splitlines()[0])
    except (ValueError, IndexError):
        return 0.0


def mean_volume_db(path: Path):
    """整片平均响度。真人中文旁白通常 -30~-15 dBFS；纯数字静音是 -91 dB。"""
    code, output = run(
        ["ffmpeg", "-i", str(path), "-vn", "-af", "volumedetect", "-f", "null", os.devnull],
        timeout=300,
    )
    if code != 0:
        return None
    match = re.search(r"mean_volume:\s*(-?\d+(?:\.\d+)?) dB", output)
    return float(match.group(1)) if match else None


SILENT_DB = -80.0


def probe_and_report(video: Path, *, strict: bool) -> int:
    """机械验收。strict=True 时任一硬条件不满足即失败。"""
    video_dur = ffprobe_value(video, ["-select_streams", "v:0", "-show_entries", "stream=duration"])
    container_dur = ffprobe_value(video, ["-show_entries", "format=duration"])
    audio_dur = ffprobe_value(video, ["-select_streams", "a:0", "-show_entries", "stream=duration"])

    problems, warnings = [], []

    if video_dur < 0.5:
        problems.append(
            f"没有有效视频流（{video_dur:.1f}s）" if video.exists() else f"成片不存在: {video}"
        )
    if audio_dur < 0.5:
        problems.append(f"没有有效音轨（{audio_dur:.1f}s）—— 没有旁白的讲解视频不可用")

    if video_dur >= 0.5:
        db = mean_volume_db(video)
        if db is None:
            warnings.append("音轨解不出响度")
        elif db < SILENT_DB:
            problems.append(f"音轨疑似静音（平均响度 {db:.1f} dB < {SILENT_DB} dB）")

        # 容器时长应约等于视频流时长；差太多说明旁白被截断或音画错位。
        if abs(video_dur - container_dur) > 1.5:
            warnings.append(
                f"音画长度不齐：视频流 {video_dur:.1f}s vs 容器 {container_dur:.1f}s，旁白可能被截断"
            )
        if video_dur < 15:
            warnings.append(f"仅 {video_dur:.1f}s，可能过短")
        if video_dur > 900:
            warnings.append(f"长达 {video_dur:.1f}s，确认是否需要拆分")

        code, res = run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height", "-of", "csv=p=0", str(video)],
            timeout=60,
        )
        if code == 0 and "," in res:
            width, _, height = res.strip().partition(",")
            info(f"  分辨率 {width}x{height} | 时长 {video_dur:.1f}s | 大小 {video.stat().st_size / 1048576:.1f}MB")
            if height.isdigit() and int(height) < 720:
                warnings.append(f"分辨率 {width}x{height} 低于 720p")

    for item in warnings:
        info(f"  ! {item}")
    for item in problems:
        info(f"  ✗ {item}")

    if problems and strict:
        return 1
    if not problems:
        info("  ✓ 成片可播、有旁白")
    return 0


def cmd_verify(args) -> int:
    workspace = resolve_workspace(args.workspace)
    video = workspace / args.video
    info(f"验收 {video}")
    return probe_and_report(video, strict=True)


# ---------------------------------------------------------------------------
# doctor：环境依赖预检
# ---------------------------------------------------------------------------

def _check_cmd(_name: str, cmd: list[str], *, extract_version: bool = True) -> tuple[bool, str]:
    code, output = run(cmd, timeout=30)
    if code != 0:
        return False, "未安装"
    if extract_version:
        ver = output.strip().splitlines()[0][:80]
        return True, ver
    return True, "可用"


def cmd_doctor(_args) -> int:
    python = _resolve_python()
    checks = []

    # Python
    ok, ver = _check_cmd("Python", [python, "--version"])
    checks.append(("Python", ok, ver, python))

    # ManimCE
    ok, ver = _check_cmd("ManimCE", [python, "-c", "import manim; print(manim.__version__)"])
    checks.append(("ManimCE", ok, ver, ""))

    # ffmpeg
    ok, ver = _check_cmd("ffmpeg", ["ffmpeg", "-version"])
    checks.append(("ffmpeg", ok, ver, ""))

    # ffprobe
    ok, ver = _check_cmd("ffprobe", ["ffprobe", "-version"])
    checks.append(("ffprobe", ok, ver, ""))

    # xelatex
    ok, ver = _check_cmd("xelatex", ["xelatex", "--version"])
    checks.append(("xelatex", ok, ver, ""))

    # dvisvgm
    ok, ver = _check_cmd("dvisvgm", ["dvisvgm", "--version"])
    checks.append(("dvisvgm", ok, ver, ""))

    # Node.js
    ok, ver = _check_cmd("Node.js", ["node", "--version"])
    checks.append(("Node.js", ok, ver, ""))

    # CJK 字体
    code, output = run([python, "-c",
        "from teaching_runtime import CJK_FONT; print(CJK_FONT)"],
        timeout=30, env={"PYTHONPATH": str(RUNTIME_DIR)})
    if code == 0 and output.strip():
        checks.append(("CJK 字体", True, output.strip().splitlines()[0], ""))
    else:
        checks.append(("CJK 字体", False, "未找到中文字体", ""))

    failures = 0
    for name, ok, ver, extra in checks:
        mark = "✓" if ok else "✗"
        line = f"  {mark} {name}: {ver}"
        if extra:
            line += f"  ({extra})"
        info(line)
        if not ok:
            failures += 1

    if failures:
        info(f"\n{failures} 项未通过，请先安装缺失的依赖。")
        return 1
    info("\n环境就绪。")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="manim_cli.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="新建项目")
    p_new.add_argument("slug")
    p_new.add_argument("--force", action="store_true", help="覆盖已有项目")
    p_new.set_defaults(func=cmd_new)

    p_check = sub.add_parser("check", help="结构 / LaTeX / 旁白 / cue 检查")
    p_check.add_argument("workspace")
    p_check.add_argument("--script", default="script.py")
    p_check.add_argument("-v", "--verbose", action="store_true")
    p_check.set_defaults(func=cmd_check)

    p_layout = sub.add_parser("layout", help="dry_run 布局检测（越界/重叠/静止）")
    p_layout.add_argument("workspace")
    p_layout.add_argument("--script", default="script.py")
    p_layout.add_argument("--scene", default=None, help="场景类名，默认自动识别")
    p_layout.set_defaults(func=cmd_layout)

    p_render = sub.add_parser("render", help="渲染 draft 或 final")
    p_render.add_argument("workspace")
    p_render.add_argument("-q", "--quality", choices=["draft", "final"], default="draft")
    p_render.add_argument("-r", "--resolution", default=None, help="仅 final 生效，如 1920x1080")
    p_render.add_argument("--script", default="script.py")
    p_render.add_argument("--scene", default=None)
    p_render.add_argument("--skip-gates", action="store_true", help="跳过检查闸门（调试用）")
    p_render.add_argument("--no-subtitles", action="store_true", help="不烧入字幕")
    p_render.set_defaults(func=cmd_render)

    p_scaffold = sub.add_parser("scaffold", help="按 durations.json 生成分段骨架")
    p_scaffold.add_argument("workspace")
    p_scaffold.add_argument("--force", action="store_true", help="覆盖已有的 script.py")
    p_scaffold.set_defaults(func=cmd_scaffold)

    p_stills = sub.add_parser("stills", help="从成片抽关键帧")
    p_stills.add_argument("workspace")
    p_stills.add_argument("seconds", nargs="*", type=float)
    p_stills.add_argument("--video", default="draft.mp4")
    p_stills.add_argument("--cues", action="store_true",
                          help="按 durations.json 的 cue 点自动取样（画面状态切换处），不用手填秒数")
    p_stills.add_argument("--cue-offset", type=float, default=1.0,
                          help="每个 cue 之后多少秒取帧，默认 1.0（等切换动画走完）")
    p_stills.add_argument("--max", type=int, default=40,
                          help="--cues 时最多抽多少帧，超出按等距抽稀，默认 40")
    p_stills.set_defaults(func=cmd_stills)

    p_verify = sub.add_parser("verify", help="成片机械验收")
    p_verify.add_argument("workspace")
    p_verify.add_argument("--video", default="final_output.mp4")
    p_verify.set_defaults(func=cmd_verify)

    p_doctor = sub.add_parser("doctor", help="环境依赖预检")
    p_doctor.set_defaults(func=cmd_doctor)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except Fail as exc:
        print(f"\n{exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n已中断", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
