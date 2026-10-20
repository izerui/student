"""通用 ManimCE 讲解视频运行时。

与题材无关，只提供四项运行时支撑：

1. `AudioManager`  —— 旁白音画同步（按语义 cue 对齐画面动作）
2. 布局守卫        —— 每次 play() 后检测越界与重叠，收场时检测「有旁白但画面不动」
3. `CJK_FONT`      —— 自动探测系统中文字体
4. `SafeMathTex`   —— 把「中文喂进 LaTeX」这类错误在构造时就拦下
5. `add_background`—— 可选背景层，自带一张黑板纹理，也可换任意图或纯色

本模块**不规定视觉风格**：配色、构图、动画、场景类名全部由作者决定，
背景也是可选的（不调用就没有）。

用法（script.py 放在工作区，PYTHONPATH 由 CLI 注入）：

    from manim import *
    from teaching_runtime import (
        AudioManager, CJK_FONT, add_background, enable_layout_guard, find_free_pos,
    )

    class Lesson(Scene):
        def construct(self):
            add_background(self)          # 想要黑板底就调，不想要就删掉这行
            enable_layout_guard(self)
            audio = AudioManager(self)
            d = audio.start("s1")
            audio.wait_for_cue("c1")
            self.play(Write(Text("你好", font=CJK_FONT)))
            audio.end(d)
"""

# pyright: reportMissingImports=false, reportUndefinedVariable=false
from manim import *

import json
import os
import re
import subprocess

__all__ = [
    "AudioManager",
    "CJK_FONT",
    "SafeMathTex",
    "add_background",
    "BLACKBOARD",
    "enable_layout_guard",
    "find_free_pos",
    "safe_area",
    "SAFE_LEFT",
    "SAFE_RIGHT",
    "SAFE_TOP",
    "SAFE_BOTTOM",
    "STATIC_INTERVAL_THRESHOLD",
]


# --------------------------------------------------------------------------
# 中文字体
# --------------------------------------------------------------------------

def _has_cjk(text):
    return bool(re.search(r"[一-鿿㐀-䶿　-〿＀-￯]", str(text)))


class SafeMathTex(MathTex):
    """中文误入 LaTeX 时立刻失败，而不是渲染出空白或半截公式。

    这是 LaTeX 本身的限制（未配置 CJK 支持时不接受汉字），不是 ManimCE 的怪癖。
    中文一律用 ``Text(..., font=CJK_FONT)``。
    """

    def __init__(self, *tex_strings, **kwargs):
        for value in tex_strings:
            if _has_cjk(str(value)):
                raise ValueError(
                    f"MathTex 不支持中文: {value!r}。中文请用 Text(..., font=CJK_FONT)。"
                )
        super().__init__(*tex_strings, **kwargs)


def _detect_cjk_font():
    """按优先级挑一个系统已装的中文字体；都没有时退回一个常见名字。"""
    candidates = [
        "PingFang SC",
        "Heiti SC",
        "Hiragino Sans GB",
        "Noto Sans CJK SC",
        "Noto Sans SC",
        "Source Han Sans SC",
        "WenQuanYi Micro Hei",
        "Microsoft YaHei",
        "SimHei",
        "STHeiti",
    ]
    override = os.environ.get("TEACHING_CJK_FONT", os.environ.get("EXPLAINER_CJK_FONT", "")).strip()
    if override:
        return override
    try:
        result = subprocess.run(
            ["fc-list", ":lang=zh", "family"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        available = result.stdout if result.returncode == 0 else ""
    except Exception:
        available = ""
    for font in candidates:
        if font.lower() in available.lower():
            return font
    if available.strip():
        return available.strip().split("\n")[0].split(",")[0].strip()
    return "PingFang SC"


CJK_FONT = _detect_cjk_font()


def _detect_latin_font():
    """纯拉丁文本用的字体。

    中文字体在排拉丁文时字距与字重都不理想（尤其是全大写和数字混排），
    而讲解视频里常有整段英文——英语类题目的教学载荷本身就是英文句式。
    中英混排的行仍然用 CJK_FONT，让 Pango 去回退；**纯拉丁**的行用这个。
    """
    candidates = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"]
    try:
        result = subprocess.run(
            ["fc-list", ":lang=en", "family"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        available = result.stdout if result.returncode == 0 else ""
    except Exception:
        available = ""
    for font in candidates:
        if font.lower() in available.lower():
            return font
    return "Helvetica"


LATIN_FONT = _detect_latin_font()


# --------------------------------------------------------------------------
# 语义色板
# --------------------------------------------------------------------------
#
# 为什么运行时要管颜色：不给就每个项目自己配一套。实测五条成片里出现了 16 个
# 互不相同的十六进制色值，且 ManimCE 的原色在绿色黑板上普遍偏灰——
# 按 WCAG 相对亮度对黑板最亮区（RGB 60,102,83）计算：
#
#     GREEN 3.04   TEAL 3.46   BLUE 3.22   RED 2.18   GREY 1.84
#
# 下面这组是照同一口径挑的，**按语义取用，不要直接写十六进制，也不要用 ManimCE 原色**。

INK = "#F0F0EC"       # 正文、默认前景                     对比度 5.71
ACCENT = "#FFD23F"    # 强调：此刻的焦点                    对比度 4.52
CORRECT = "#A8E85C"   # 正确、结论、通过                    对比度 4.46
SECOND = "#FFC978"    # 第二组对照（与 ACCENT 并置时用）     对比度 4.31
DATA = "#4FE3C8"      # 数据、量、测量值                    对比度 4.09
WRONG = "#FFB0B0"     # 错误、否定                          对比度 3.76
MUTED = "#8FA09A"     # 次要、已讲过、退到背景               对比度 2.38（故意低）

# 饱和红在绿底上无论怎么调都到不了 4.5，再提就褪成粉色、丢掉"红＝错"的语义。
# 因此约定：**错误不能只靠颜色表达**，WRONG 必须与划掉、叉号或"错→对"的改写同时出现。
# 同理 MUTED 的低对比是有意的（它的作用就是退场），不要用它承载需要被读到的信息。

PALETTE = {
    "INK": INK, "ACCENT": ACCENT, "CORRECT": CORRECT,
    "SECOND": SECOND, "DATA": DATA, "WRONG": WRONG, "MUTED": MUTED,
}


# --------------------------------------------------------------------------
# 旁白音画同步
# --------------------------------------------------------------------------

class AudioManager:
    """把场景时间轴钉在真实旁白音频上。

    `durations.json` 由 `scripts/narrate.mjs` 产出，形如::

        {"s1": {"file": "audio/s1.wav", "durationSec": 12.3,
                "speechStartSec": 0.2, "speechEndSec": 11.8,
                "cuePoints": [{"id": "c1", "marker": "第一步", "timeSec": 3.4}]}}

    典型用法::

        d = audio.start("s1")       # 挂上音频，返回该段总时长
        audio.wait_for_cue("c1")    # 等到旁白讲到 marker 那句
        self.play(...)              # 画面在这一刻响应
        audio.end(d)                # 补齐剩余时长，保证音画等长
    """

    def __init__(self, scene, durations_file="durations.json", audio_dir="public"):
        self.scene = scene
        self._scene_start = 0.0
        self._current_id = None
        self._safety_margin = 0.2

        if not os.path.exists(durations_file):
            raise FileNotFoundError(
                f"找不到 {durations_file}；请先运行 scripts/narrate.mjs 生成旁白。"
            )
        with open(durations_file, "r", encoding="utf-8") as handle:
            self._data = json.load(handle)

        self._cues = {}
        for scene_id, item in self._data.items():
            self._cues[scene_id] = {
                cue["id"]: float(cue["timeSec"])
                for cue in item.get("cuePoints", [])
                if cue.get("id") and cue.get("timeSec") is not None
            }
        self._audio_dir = audio_dir

    @property
    def scene_ids(self):
        """durations.json 里的全部场景 id，按文件顺序。"""
        return list(self._data.keys())

    def duration_of(self, scene_id):
        entry = self._data.get(scene_id)
        if not entry:
            raise KeyError(f"durations.json 缺少场景: {scene_id}")
        return float(entry["durationSec"])

    def start(self, scene_id):
        entry = self._data.get(scene_id)
        if not entry:
            raise KeyError(f"durations.json 缺少场景: {scene_id}")
        audio_path = os.path.join(self._audio_dir, entry["file"])
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"音频文件不存在: {audio_path}")
        self._current_id = scene_id
        self._scene_start = self.scene.time
        self.scene.add_sound(audio_path)
        duration = float(entry["durationSec"])
        # 记录旁白时间轴，供收场时比对「有旁白但画面没推进」的区间。
        narration = getattr(self.scene, "_guard_narration", None)
        if narration is not None:
            narration.append((scene_id, self._scene_start, duration))
        return duration

    def end(self, expected_duration=0.0):
        """补齐到该段旁白结束，保证画面不早于语音收尾。"""
        elapsed = self.scene.time - self._scene_start
        remaining = max(0.0, float(expected_duration)) + self._safety_margin - elapsed
        if remaining > 0.01:
            self.scene.wait(remaining)

    def wait_for_cue(self, cue_id):
        """等到旁白讲到该 cue 的位置；已经讲过了就立刻返回。"""
        target = self._cues.get(self._current_id, {}).get(cue_id)
        if target is None:
            raise KeyError(f"场景 {self._current_id} 缺少 cue: {cue_id}")
        remaining = target - (self.scene.time - self._scene_start)
        if remaining > 0.05:
            self.scene.wait(remaining)

    def wait_until(self, seconds):
        remaining = seconds - (self.scene.time - self._scene_start)
        if remaining > 0.05:
            self.scene.wait(remaining)


# --------------------------------------------------------------------------
# 布局守卫：越界 / 重叠 / 旁白静止
# --------------------------------------------------------------------------

# 有旁白但画面连续静止超过这个秒数即报告。
STATIC_INTERVAL_THRESHOLD = 8.0

# 安全区：四周各留 6% 边距，给播放器控件和屏幕边缘留余量。
_MARGIN_RATIO = float(os.environ.get("TEACHING_SAFE_MARGIN", os.environ.get("EXPLAINER_SAFE_MARGIN", "0.06")))
SAFE_LEFT = -config.frame_width / 2 * (1 - 2 * _MARGIN_RATIO)
SAFE_RIGHT = config.frame_width / 2 * (1 - 2 * _MARGIN_RATIO)
SAFE_TOP = config.frame_height / 2 * (1 - 2 * _MARGIN_RATIO)
SAFE_BOTTOM = -config.frame_height / 2 * (1 - 2 * _MARGIN_RATIO)


def safe_area():
    """返回 (left, right, bottom, top)，方便场景代码直接算位置。"""
    return SAFE_LEFT, SAFE_RIGHT, SAFE_BOTTOM, SAFE_TOP


# 这些标注类型本来就该压在目标身上，重叠检测跳过它们。
_DECORATION_TYPES = (
    SurroundingRectangle, BackgroundRectangle, Brace, BraceLabel, Cross, Underline,
    RightAngle, Angle,
)

# 图表数据元素——它们天然位于坐标系内部，与轴线"重叠"是正常的。
_GRAPH_DATA_TYPES = (
    Dot, ParametricFunction, FunctionGraph,
)

# 坐标系组件——与 _GRAPH_DATA_TYPES 之间的重叠不报告。
_COORDINATE_TYPES = (
    Axes, NumberLine, NumberPlane, CoordinateSystem,
)

# 场类型（ArrowVectorField、StreamLines）——按定义就铺满一整片区域的底衬，
# 和坐标系一样属于空间填充物而不是争夺位置的离散对象，画在它上面的任何东西
# 都不构成重叠缺陷。越界检测仍对它生效：场本身画出安全区是真实缺陷。
_FIELD_SUBSTRATE_TYPES = (VectorField,)


def _boxes_overlap(a, b, tol=0.05):
    al, ar = a.get_left()[0], a.get_right()[0]
    ab, at_ = a.get_bottom()[1], a.get_top()[1]
    bl, br = b.get_left()[0], b.get_right()[0]
    bb, bt = b.get_bottom()[1], b.get_top()[1]
    return al < br - tol and ar > bl + tol and ab < bt - tol and at_ > bb + tol


def _is_decoration(mob):
    return isinstance(mob, _DECORATION_TYPES)


def _is_graph_data(mob):
    """图表数据元素（数据点、曲线），或包含这些元素的小容器。"""
    if isinstance(mob, _GRAPH_DATA_TYPES):
        return True
    if isinstance(mob, VGroup) and mob.width < 0.3 and mob.height < 0.3:
        return True
    return False


def _is_coordinate_part(mob):
    """坐标系或其组成部分（包括包含 NumberLine 的 VGroup）。"""
    if isinstance(mob, _COORDINATE_TYPES):
        return True
    if isinstance(mob, VGroup):
        for child in mob.submobjects[:8]:
            if isinstance(child, _COORDINATE_TYPES):
                return True
    return False


def _is_on_graph(mob):
    """在坐标系区域内的小元素：数据点、曲线、数据标签。"""
    if _is_graph_data(mob):
        return True
    if isinstance(mob, (MathTex, Tex, Text, MarkupText)) and mob.font_size <= 24:
        return True
    return False


def _is_field_substrate(mob):
    """向量场/流线：铺满一片区域的底衬，重叠检测中视同背景。"""
    return isinstance(mob, _FIELD_SUBSTRATE_TYPES)


def _is_empty_container(mob):
    """always_redraw 在条件不满足时返回空 VGroup 或只含 VectorizedPoint 的占位容器。"""
    if isinstance(mob, VGroup):
        if len(mob.submobjects) == 0:
            return True
        if all(isinstance(c, VectorizedPoint) for c in mob.submobjects):
            return True
    return False


def _is_geometry(mob):
    """几何图形、向量、构造线、集合运算或三维实体——它们之间的重叠通常是有教学意义的
    （嵌套、交叉、平行四边形等）。三维对象投影到二维后包围盒必然互相重叠，一律跳过。"""
    if isinstance(mob, (
        Polygon, Circle, Ellipse, Rectangle, Square, Triangle,
        Annulus, AnnularSector, Sector, Arc, ArcBetweenPoints,
        Intersection, Union, Difference, Exclusion,
        Arrow, Line, DashedLine, Vector, DoubleArrow,
        Surface, ThreeDVMobject, Dot3D, Sphere, Cube, Cone,
        Cylinder, Prism, Line3D, Arrow3D, Polyhedron,
    )):
        return True
    # 容器含几何子元素就算几何，不看自己的 fill/stroke。
    # `VGroup.set_opacity()` 会把容器自身的 fill_opacity 一起改掉（实测 0.0 -> 0.3），
    # 于是下面那条 stroke-only 判据失配，一整组几何图形忽然不再被当作几何内容，
    # 转而被报成重叠。容器自身从不绘制任何东西，它的 fill/stroke 不该参与判定。
    #
    # 这里只增不减：命中就返回 True，不命中继续走原有判据。用 any 而不是 all，
    # 因为"圆 + 标签"这种带文字的结点仍然是图上的一个几何单元——连线与它相接是
    # 有教学意义的，不该报重叠。（改成 all 会让树形图里每条边都与结点冲突。）
    if mob.submobjects and any(_is_geometry(c) for c in mob.submobjects):
        return True
    # stroke-only VMobject（路径、高亮线等）也视为几何内容
    if isinstance(mob, VMobject) and mob.stroke_width > 0 and mob.fill_opacity == 0:
        return True
    return False


def _should_skip_overlap(a, b):
    """图表数据与坐标系之间、几何嵌套之间的重叠是正常的，不报告。"""
    if _is_empty_container(a) or _is_empty_container(b):
        return True
    if _is_field_substrate(a) or _is_field_substrate(b):
        return True
    if _is_on_graph(a) and _is_coordinate_part(b):
        return True
    if _is_coordinate_part(a) and _is_on_graph(b):
        return True
    if _is_graph_data(a) and _is_graph_data(b):
        return True
    if _is_on_graph(a) and _is_graph_data(b):
        return True
    if _is_graph_data(a) and _is_on_graph(b):
        return True
    if _is_geometry(a) and _is_geometry(b):
        return True
    # 几何对象画在坐标系内、或与绘制的曲线/数据点相交，都是正常的
    if _is_geometry(a) and (_is_coordinate_part(b) or _is_graph_data(b)):
        return True
    if (_is_coordinate_part(a) or _is_graph_data(a)) and _is_geometry(b):
        return True
    # 几何标签（向量名、顶点名等小公式）紧贴几何对象是正常的
    if _is_geometry(a) and isinstance(b, (MathTex, Tex)) and b.font_size <= 36:
        return True
    if isinstance(a, (MathTex, Tex)) and a.font_size <= 36 and _is_geometry(b):
        return True
    return False


def _mob_label(mob, max_chars=25):
    """人类可读的元素标签：类别 + 内容预览，让报告能指名道姓。"""
    if isinstance(mob, (MathTex, Tex)):
        kind, content = "公式", getattr(mob, "tex_string", "")
    elif isinstance(mob, (Text, MarkupText)):
        kind = "文本"
        content = getattr(mob, "text", "") or getattr(mob, "original_text", "")
    elif isinstance(mob, SurroundingRectangle):
        kind, content = "标注:框", ""
    elif isinstance(mob, (Brace, BraceLabel)):
        kind, content = "标注:括号", ""
    elif isinstance(mob, (Arrow, Line, DashedLine)):
        kind, content = "标注:箭头/线", ""
    elif isinstance(mob, (Cross, Underline)):
        kind, content = "标注:装饰", ""
    elif isinstance(mob, VGroup):
        child_kinds = set()
        for c in mob.submobjects[:5]:
            if isinstance(c, (MathTex, Tex)):
                child_kinds.add("公式")
            elif isinstance(c, (Text, MarkupText)):
                child_kinds.add("文本")
            elif _is_decoration(c):
                child_kinds.add("标注")
            else:
                child_kinds.add(type(c).__name__)
        kind = "容器"
        content = "+".join(sorted(child_kinds)) if child_kinds else f"{len(mob.submobjects)}个子元素"
    else:
        kind, content = type(mob).__name__, ""
    preview = content[:max_chars].replace("\n", " ") if content else ""
    return f'{kind}("{preview}")' if preview else kind


def _is_camera_frame(mob, scene):
    """MovingCameraScene / ZoomedScene 的 camera.frame 是取景框，不是画面内容。

    它铺满整个画幅，若参与检测会永远判越界、且与每个元素都重叠。
    """
    camera = getattr(scene, "camera", None)
    frame = getattr(camera, "frame", None)
    if frame is not None and mob is frame:
        return True
    # ZoomedScene 还有一个 zoomed_camera.frame
    zoomed = getattr(scene, "zoomed_camera", None)
    zoomed_frame = getattr(zoomed, "frame", None)
    if zoomed_frame is not None and mob is zoomed_frame:
        return True
    return False


def _visible_layout_units(scene, exclude=None):
    """参与检测的顶层元素。

    VGroup 容器自身 fill/stroke 都是透明的，但子元素可见——所以按宽高判断，不按不透明度。
    z_index <= -100 视为背景层，跳过。camera.frame 是取景框不是内容，跳过。
    """
    return [
        m for m in scene.mobjects
        if m is not exclude
        and getattr(m, "z_index", 0) > -100
        and m.width > 0.1
        and m.height > 0.1
        and not _is_decoration(m)
        and not _is_empty_container(m)
        and not _is_camera_frame(m, scene)
    ]


def _find_nearest_free(mob, predecessors, anchor=None, step=0.3):
    """从 anchor 起按阅读顺序扫描，找第一个不与既有元素冲突的中心点。"""
    if anchor is None:
        anchor = mob.get_center()
    orig = mob.get_center().copy()

    start_x = max(anchor[0], SAFE_LEFT + mob.width / 2)
    y = min(anchor[1], SAFE_TOP - mob.height / 2)

    while y >= SAFE_BOTTOM + mob.height / 2:
        x = start_x
        while x <= SAFE_RIGHT - mob.width / 2:
            mob.move_to([x, y, 0])
            if not any(_boxes_overlap(mob, p) for p in predecessors):
                pos = mob.get_center().copy()
                mob.move_to(orig)
                return pos
            x += step
        start_x = SAFE_LEFT + mob.width / 2
        y -= step

    mob.move_to(orig)
    return None


def _current_safe_area(scene):
    """画布安全区——始终基于默认画幅，不跟随镜头缩放。

    越界检测的语义是"元素是否画在画布之外"，不是"元素是否在当前镜头视野内"。
    镜头推近时全局内容在视野外是正常的，不应判越界。
    """
    return SAFE_LEFT, SAFE_RIGHT, SAFE_BOTTOM, SAFE_TOP


def _check_out_of_bounds(mob, bounds=None):
    left, right, bottom, top = bounds if bounds else (SAFE_LEFT, SAFE_RIGHT, SAFE_BOTTOM, SAFE_TOP)
    oob = []
    tol = 0.05
    if mob.get_left()[0] < left - tol:
        oob.append("左")
    if mob.get_right()[0] > right + tol:
        oob.append("右")
    if mob.get_top()[1] > top + tol:
        oob.append("上")
    if mob.get_bottom()[1] < bottom - tol:
        oob.append("下")
    return oob


def _check_layout_violations(scene):
    """扫描可见元素的越界与重叠。

    只检测和报告，绝不自动挪动——自动纠正会掩盖根因（比如同一 mobject
    挂在两个 VGroup 上），让问题在下一轮换个地方冒出来。
    """
    units = _visible_layout_units(scene)
    if not units:
        return
    issues = 0

    # 安全区跟随当前镜头（MovingCameraScene 推近后可见范围会变）
    bounds = _current_safe_area(scene)

    # 去重：同一对象在同一位置只报一次（always_redraw 每帧重建会产生重复）
    reported = getattr(scene, "_guard_reported", None)
    if reported is None:
        reported = set()
        scene._guard_reported = reported

    for mob in units:
        oob = _check_out_of_bounds(mob, bounds)
        if oob:
            cur = mob.get_center()
            key = (f"oob:{_mob_label(mob)}", round(cur[0], 0), round(cur[1], 0))
            if key in reported:
                continue
            reported.add(key)
            issues += 1
            edges = "、".join(oob)
            print(
                f"[layout-guard] 越界: {_mob_label(mob)} 在 ({cur[0]:.1f}, {cur[1]:.1f}) 超出安全区{edges}边界。"
                f"安全区 x∈[{bounds[0]:.1f},{bounds[1]:.1f}] y∈[{bounds[2]:.1f},{bounds[3]:.1f}]。"
                f"如有关联的标注工具(框/括号/箭头等)需一并调整"
            )

    if len(units) >= 2:
        for i, mob in enumerate(units):
            predecessors = [u for u in units[:i] if not _is_decoration(u)]
            if not predecessors:
                continue
            conflicts = [
                p for p in predecessors
                if _boxes_overlap(mob, p) and not _should_skip_overlap(mob, p)
            ]
            if not conflicts:
                continue
            cur = mob.get_center()
            key = (f"overlap:{_mob_label(mob)}", round(cur[0], 0), round(cur[1], 0))
            if key in reported:
                continue
            reported.add(key)
            issues += 1
            new_pos = _find_nearest_free(mob, predecessors, cur)
            hint = f"建议移到 ({new_pos[0]:.1f}, {new_pos[1]:.1f})" if new_pos is not None else "安全区内无空位，需缩小或清理"
            conflict_labels = ", ".join(_mob_label(c) for c in conflicts)
            print(
                f"[layout-guard] 重叠: {_mob_label(mob)} 在 ({cur[0]:.1f}, {cur[1]:.1f}) "
                f"与 [{conflict_labels}] 冲突 → {hint}。如有关联的标注工具(框/括号/箭头等)需一并调整"
            )

    if issues:
        print(f"[layout-guard] 本次 play() 后检测到 {issues} 个问题（详见上方，请在代码中调整）")


def find_free_pos(mob, scene, anchor=ORIGIN):
    """在 play() 之前主动挑一个不冲突的位置。守卫内部也用它算建议坐标。"""
    predecessors = list(_visible_layout_units(scene, exclude=mob))
    if not predecessors or not any(_boxes_overlap(mob, p) for p in predecessors):
        return mob.get_center()
    result = _find_nearest_free(mob, predecessors, anchor)
    return result if result is not None else mob.get_center()


# --------------------------------------------------------------------------
# 背景层（可选）
# --------------------------------------------------------------------------

#: 自带的黑板纹理。深墨绿底、带粉笔擦痕，适合板书式推导；也可以换任意图片或纯色。
BLACKBOARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "blackboard.jpg")


def add_background(scene, image=BLACKBOARD, color=None):
    """铺一层铺满画幅的背景，并把它压在 z_index=-100（布局守卫会跳过背景层）。

    三种用法::

        add_background(scene)                      # 自带黑板纹理
        add_background(scene, "public/bg.png")     # 自选图片
        add_background(scene, image=None, color="#0f172a")   # 纯色

    图片按「铺满不留白」缩放：先等比放大到覆盖画幅，超出部分裁掉，
    所以任何比例的图都不会被拉变形、也不会露出底色。
    在 ``construct()`` 里要第一个调用，否则后续元素会被背景盖住。
    """
    if color is not None:
        scene.camera.background_color = color
    if image and os.path.exists(image):
        bg = ImageMobject(image)
        # 等比覆盖：取宽高两个方向所需缩放的较大者，保证铺满且不变形。
        scale = max(config.frame_width / bg.width, config.frame_height / bg.height)
        bg.scale(scale)
        bg.move_to(ORIGIN)
        bg.set_z_index(-100)
        scene.add(bg)
    elif image:
        print(f"[teaching-runtime] 背景图不存在，已跳过: {image}")
    return scene


def _has_active_updaters(scene):
    """updater 驱动的动效发生在 wait() 期间：没有 play() 画面照样在变。"""
    for mob in scene.mobjects:
        if getattr(mob, "updaters", None):
            return True
        for sub in mob.get_family():
            if getattr(sub, "updaters", None):
                return True
    return False


def _report_static_intervals(scene):
    """比对旁白时间轴与画面活动时间轴，报告「有旁白但画面长时间不动」。

    这是确定性计算，不需要抽帧比像素：守卫记下了每次 play()（以及挂着 updater 的
    wait()）的时间区间，AudioManager 记下了每段旁白的起点与时长，两者相减即可。
    """
    narration = getattr(scene, "_guard_narration", None)
    activity = getattr(scene, "_guard_activity", None)
    if not narration or activity is None:
        return

    issues = 0
    for scene_id, start, duration in narration:
        end = start + duration
        spans = sorted(
            (max(a0, start), min(a1, end)) for a0, a1 in activity if a1 > start and a0 < end
        )
        cursor = start
        for a0, a1 in spans:
            if a0 - cursor >= STATIC_INTERVAL_THRESHOLD:
                issues += 1
                print(
                    f"[layout-guard] 静止: 场景 {scene_id} 在旁白第 "
                    f"{cursor - start:.1f}s–{a0 - start:.1f}s（约 {a0 - cursor:.1f} 秒）"
                    f"画面没有任何推进，请加入与当前讲解对应的出场、变换或焦点强调"
                )
            cursor = max(cursor, a1)
        if end - cursor >= STATIC_INTERVAL_THRESHOLD:
            issues += 1
            print(
                f"[layout-guard] 静止: 场景 {scene_id} 在旁白第 "
                f"{cursor - start:.1f}s–{duration:.1f}s（约 {end - cursor:.1f} 秒）"
                f"画面没有任何推进，请加入与当前讲解对应的出场、变换或焦点强调"
            )
    if issues:
        print(f"[layout-guard] 全片检测到 {issues} 段旁白静止（详见上方，请在代码中补充动画）")


def _dissolve_animation_containers(scene):
    """溶解编排类动画留在场景顶层的裸 ``Group``。

    ``AnimationGroup`` / ``LaggedStart`` / ``Circumscribe`` 这类动画执行完，会把参与
    对象收进一个裸 ``Group`` 留在 ``scene.mobjects`` 顶层。实测三个 Dot 走一次
    ``LaggedStart`` 之后，顶层只剩 ``['Group']``——三个原对象全被吞了进去。

    两重后果：

    1. 这个容器的包围盒横跨全部成员，布局守卫把它当成一个巨型元素，与画面上几乎
       所有东西判重叠（一条片子实测报出 32 处假重叠）。
    2. 更要紧的是它不报错、直接毁画面：``Scene.add`` 会先 restructure 现有列表，
       把"包含被加入对象"的容器拆散。作者建的 ``VGroup(圆, 数字)`` 被拆成散件后
       重新入列，层序错乱——圆盖住数字，结点里的权值就这样消失。

    判别只看一条：**裸 ``Group`` 从来不是作者写的布局单元**。作者用 ``VGroup``
    表达"这几个东西是一个整体"，它应当整体参与重叠检测；裸 ``Group`` 是编排类动画的
    副产物，应当溶解。这条区分不依赖动画类的名字，对以后新增的编排动画同样成立。

    用原地替换而不是 remove + add：后者会把成员追加到列表末尾、打乱绘制顺序，
    而且 add 本身又会触发一次 restructure。
    """
    dissolved = 0
    for _ in range(8):  # 嵌套的编排动画会套好几层，逐层剥，留个上限防意外
        ghosts = [m for m in scene.mobjects if type(m) is Group]
        if not ghosts:
            break
        for ghost in ghosts:
            try:
                idx = scene.mobjects.index(ghost)
            except ValueError:
                continue
            members = list(ghost.submobjects)
            # 已经在场景其它地方出现过的成员不要再放一份，否则一个对象占两个位置
            elsewhere = set()
            for m in scene.mobjects:
                if m is ghost:
                    continue
                elsewhere.update(id(x) for x in m.get_family())
            fresh = [m for m in members if id(m) not in elsewhere]
            scene.mobjects[idx:idx + 1] = fresh
            dissolved += 1
    return dissolved


def _restore_layout_topology(scene, before):
    """把一次 ``play()`` 打乱的顶层结构复原成作者写的样子。

    ``before`` 是动画前的 ``scene.mobjects`` 快照。两步：

    1. 溶解编排动画留下的裸 ``Group``（见上）。
    2. 把被 ``Scene.add`` 的 restructure 逐出的**作者容器**接回去。

    第 2 步是第 1 步的必要补充。``LaggedStart(circle.animate…)`` 会把 ``circle``
    收进一个 Group 再 add，restructure 于是判定"``VGroup(圆, 数字)`` 含有正在被加入的
    对象"，把整个 ``VGroup`` 从场景里摘掉。此时即便把 ``circle`` 放回顶层，``VGroup``
    里的数字也已经不在渲染列表上了——画面上数字凭空消失，而且不报任何错。

    判据：动画前在顶层、动画后不在，且它的后代此刻散落在顶层——这就是 restructure
    干的，不是作者的本意（作者真要移除，用的是 FadeOut/remove，那种情况后代不会留在顶层）。
    """
    _dissolve_animation_containers(scene)

    current = scene.mobjects
    for mob in before:
        if any(m is mob for m in current):
            continue
        descendants = {id(x) for x in mob.get_family() if x is not mob}
        stray = [c for c in current if id(c) in descendants]
        if not stray:
            continue  # 作者真的移除了它，别多事
        idx = current.index(stray[0])
        for s in stray:
            current.remove(s)
        current.insert(idx, mob)


def pulse(mob, color=ACCENT, scale=1.12, run_time=0.6, dim=INK):
    """强调一个对象，替代 ``Indicate``。

    ``Indicate`` 把整个家族染成同一个颜色：容器里的浅色文字和被染色的填充融成一片，
    强调反而把信息盖掉了（实测结点里的权值数字在每次强调时整段消失）。

    这里只给"外壳"（非文字子元素，或没有子元素时的对象自身）上强调色，文字子元素
    换成 ``dim`` 保持可读，整体同步放大后原样弹回。返回一个动画，可直接进 ``self.play``。
    """
    _TEXTISH = (Text, MarkupText, MathTex, Tex, SingleStringMathTex)
    target = mob.copy()
    target.scale(scale)
    parts = list(target.submobjects) or [target]
    for part in parts:
        part.set_color(dim if isinstance(part, _TEXTISH) else color)
    return Transform(mob, target, rate_func=there_and_back, run_time=run_time)


def enable_layout_guard(scene):
    """挂钩 scene.play()，每次动画后检测布局；收场时汇报旁白静止区间。

    在 `construct()` 的开头调用一次即可。不调用则不做任何检测，
    但 `scripts/check_layout.mjs` 会因为拿不到报告而判定未检查。
    """
    if getattr(scene, "_guard_installed", False):
        return
    scene._guard_installed = True

    orig_play = scene.play
    orig_tear_down = scene.tear_down
    guard_active = False
    scene._guard_activity = []
    scene._guard_narration = []

    def guarded_play(*args, **kwargs):
        nonlocal guard_active
        started = scene.time
        # Scene.wait() 内部也是 play(Wait(...))，这类空动画不算画面推进——
        # 除非此刻挂着 updater，它会在 Wait 期间持续改变画面。
        idle = bool(args) and all(isinstance(a, Wait) for a in args)
        advances = not idle or _has_active_updaters(scene)
        before = list(scene.mobjects)
        orig_play(*args, **kwargs)
        # 必须紧跟在动画之后、检测之前：既消掉假重叠，也赶在下一次 Scene.add
        # 再触发一轮 restructure 之前，把顶层结构恢复成作者写的样子。
        _restore_layout_topology(scene, before)
        if advances:
            scene._guard_activity.append((started, scene.time))
        if not guard_active:
            guard_active = True
            try:
                _check_layout_violations(scene)
            finally:
                guard_active = False

    def guarded_tear_down(*args, **kwargs):
        try:
            _report_static_intervals(scene)
        finally:
            orig_tear_down(*args, **kwargs)

    scene.play = guarded_play
    scene.tear_down = guarded_tear_down
