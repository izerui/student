---
name: manim-video
description: 用 ManimCE 把任意内容做成带中文配音的教学动画视频。适用于题目讲解、知识点讲解、概念讲解、公式推导、流程演示、数据解读等任何"需要讲明白"的内容。当用户要求生成讲解视频、教学视频、解题视频、动画演示，或提供题目/知识点/文档并希望做成视频时，必须使用此 skill。即使用户只说"做个视频"、"把这个讲一下"、"做成动画"、"生成一个教学片段"，也应触发本 skill。输入可以是自由文本、题目、知识点、文档、流程或数据，内容由调用方给定，本 skill 只负责把它做成视频。
---

# 教学视频生成

用 ManimCE 动画引擎 + 中文 TTS 配音（OpenAI 兼容接口，默认 tts.style520.com，音色云健），把任意内容做成一条完整的教学动画视频（`final_output.mp4`）。

## 必须按顺序读取的文件

触发本 skill 后，**按以下顺序读取**，不要跳过任何一步：

1. **本文件**（你正在读）—— 流程总览、命令速查、核心约束
2. **`references/production-guide.md`** —— 制作指南：讲解风格、旁白设计、空间布局铁律、音画同步、完成门槛。**这是出片质量的核心，必须完整读取**
3. **`references/content-types.md`** —— 内容指南（从头到尾读完）：内容分析、视觉设计、片子结构、画布管理、特定内容形态的额外要求、质量守卫、工具速查

4. **叙事模型**（按需从 `references/story-models.md` 挑 1–2 个）
5. **写代码前**读 `references/manim-index.md`，按它的指引读取需要的 ManimCE 规则——**不要凭记忆写 API，必须从规则文件确认 API 确实存在**

## 核心约束（即使不读 production-guide.md 也必须遵守）

### 动画是讲解本身

**这是动画教学，不是配音幻灯片。** 变化必须连续——每帧都和上一帧不同，不在几个定格之间跳。标题淡入、卡片滑入、要点依次出现都**不算动画**。自检：关掉旁白随便挑一秒，能不能指着某个对象说"它正在变成……"？不能就重做。

### 音画同步

旁白说到哪一步，画面就做到哪一步。每个 `wait_for_cue()` 触发时，注意力必须被引向旁白正在讲的内容。每段旁白开口后 2 秒内必须出现第一个视觉动作。相邻 cue 不超过 10 秒。

### 布局硬闸门

`layout` 命令做三项检查，**三项全零才能渲染**：
- **越界**：元素包围盒必须全在安全区 x∈[-6.3,6.3] y∈[-3.5,3.5] 内
- **重叠**：可见元素两两包围盒不相交（装饰类型和图表数据元素除外——Dot/曲线在坐标轴上的重叠是正常的，守卫会自动跳过）
- **旁白静止**：每段旁白区间内画面不能超过 8 秒没有 `play()` 推进

守卫对同一位置的同一对象只报一次（`always_redraw` 每帧重建不会产生重复报告）。

### 教学正确性

- **位置关系由内容驱动**——对象之间的空间关系（距离、角度、包含、相邻）是教学内容本身。布局要服务于这些关系，不能为了避开检测而破坏。空间冲突时优先调整整体尺度或分阶段展示
- **数值必须可验证**——公式里写的数、图上标的数、旁白念的数必须一致且正确。涉及计算的要自己算一遍

### ManimCE 语法红线

- **中文绝不进 LaTeX**：`MathTex` 只放数学记号，中文一律 `Text(..., font=CJK_FONT)`
- **不要在 `Text()` 里写 `$` 或 LaTeX 命令**——那是 Markdown 语法
- **`BulletedList` 不能装中文**——用 `VGroup` 装多个 `Text` 再 `arrange(DOWN)`
- **不用 ManimGL 专属 API**（`TexText`、`set_backstroke`、`fix_in_frame`）
- `tex_to_color_map` 属于 `MathTex`，`t2c` 属于 `Text`，不要混
- **中文引号嵌套会导致语法错误**——`"弹簧的"硬度""` 会被 Python 误解。用单引号包裹或去掉内层引号

### 开场与结束（每条视频都必须有）

- **开场**：单独一段旁白（自己的 `audio.start`/`audio.end`），5–10 秒内让观众能用一句话说出「这条视频讲什么」：标题卡、一个具体问题或一个场景都可以。卡片退出与主线进入重叠，不留空白板。
- **结束画面**：总结讲完后要有明确的结束状态——定格最终结论（或结束卡），配一句收束旁白，静止停留 3–5 秒。讲完最后一点就停、让观众自己猜「完了没有」，不算有结尾。

### 完成门槛

声称完成前**全部满足**：
1. `script.py` 是完整场景代码（不是起步模板）
2. `durations.json` 存在且非空
3. `public/audio/` 中有 wav 文件
4. `check` 全项通过
5. `layout` 三项全零
6. `stills` 已抽帧看过真实画面，其中包括**第一帧和最后一帧**：开场能说出讲什么，最后一帧是明确的结束状态
7. `final_output.mp4` 存在、有视频流、有音轨、通过 `verify`

**写完 storyboard 不是完成。生成旁白不是完成。只有渲染出 `final_output.mp4` 并通过 `verify` 才是完成。**

## 六阶段流程

| 阶段 | 做什么 | 产物 |
|---|---|---|
| 1. 分析 | 内容分析 + 写分镜（复杂视觉设计推荐先做 `visual-research.md` 和 `plan.md`） | `storyboard.md` |
| 2. 配音 | 写 `segments.json` → 调 TTS | `durations.json` + `public/audio/*.wav` |
| 3. 编码 | `scaffold` 出分段骨架 → **一次 Edit 填一个方法** | `script.py` |
| 4. 检查 | `check` → `layout`（三项全零）→ `render draft` | `draft.mp4` |
| 5. 审查 | `stills --cues` 抽帧 → Read 看 PNG → 修复 → 重跑 4 | `stills/*.png` |
| 6. 出片 | `render final` → `verify` | `final_output.mp4` |

每步细节见 `references/production-guide.md`。

**阶段 3 必须分段写。** 成稿通常 26–37KB，是整条流水线唯一要一次性产出大块文本的地方，
而它又排在读完参考文档之后、上下文最满的时候——实测连续三个智能体卡死在这一步、写入 0 字节。
先 `scaffold` 生成骨架（每段旁白一个方法、每个 cue 一个 TODO），再一个方法一次 Edit 填进去。
需要现成的 API 用法时，**读一条已完工项目的 `script.py` 比通读 references 便宜得多**。

**阶段 5 用 `--cues`，别手填秒数。** cue 点就是画面的状态迁移表，按它取样每次切换都会被看到一眼；
手挑时间点只能碰运气。重点查**上一状态的标注有没有留在屏幕上**——过期的读数、标签、结论
与新画面并置，机械闸门全绿却会把人讲错，这类错误只有看画面才能发现。

## 命令速查

`<slug>` 是视频项目名（也接受完整路径），可以用中文（如 `E15-柯西二项与柯西分式`，check、layout 已实测可用），也可以用 ASCII 短横线连接；重做同一内容加 `-v2` 后缀，不覆盖旧项目。脚本路径相对于 skill 目录（`.claude/skills/manim-video/`）。

```bash
# 阶段 1：新建视频项目
python3 scripts/manim_cli.py new <slug>

# 阶段 2：生成旁白（需要 TTS_API_KEY，配置在项目 .claude/settings.local.json 的 env）
node scripts/narrate.mjs <slug>

# 阶段 3：生成分段骨架（每段旁白一个方法），然后一次 Edit 填一个方法
python3 scripts/manim_cli.py scaffold <slug>

# 阶段 4：依次过闸门
python3 scripts/manim_cli.py check  <slug>
python3 scripts/manim_cli.py layout <slug>       # 必须三项全零
python3 scripts/manim_cli.py render <slug> -q draft

# 阶段 5：抽帧（按 cue 自动取样，覆盖每次状态切换）
python3 scripts/manim_cli.py stills <slug> --cues
python3 scripts/manim_cli.py stills <slug> --cues --max 60   # 想看更密
python3 scripts/manim_cli.py stills <slug> 3 8 15 22         # 也可手填时间点

# 阶段 6：出片 + 验收
python3 scripts/manim_cli.py render <slug> -q final [-r 1920x1080]
python3 scripts/manim_cli.py verify <slug>

# 环境预检（首次搭建或换机器时跑一次）
python3 scripts/manim_cli.py doctor
```

**闸门是硬的**：`render` 要求 `check` 和 `layout` 都通过，否则拒绝。回执按输入指纹绑定（`script.py` + `durations.json` + `.narration-manifest.json`）——改过代码或重新生成配音都得重跑。

**`durations.json` 是产物，任何情况下都不许手改。** 里面的时长和 cue 时间是从真实音频量出来的，手填的数字必然和音频对不上，而几何闸门（`check` / `layout`）只看画面不看时间轴，查不出这类错位——要等渲完二十多分钟抽帧才发现。改了 `segments.json`（包括只加一个 cue）就重跑 `narrate.mjs`：它按段做 hash 缓存，只有变动的那一段会重新合成，其余直接复用，代价就是一次 TTS 调用。

## 运行时 API

`script.py` 里直接 `from teaching_runtime import ...`，PYTHONPATH 由 CLI 自动注入。

```python
from manim import *
from teaching_runtime import (
    AudioManager, CJK_FONT, LATIN_FONT, add_background,
    enable_layout_guard, find_free_pos, pulse, safe_area,
    INK, ACCENT, CORRECT, SECOND, DATA, WRONG, MUTED,
)

class Lesson(Scene):
    def construct(self):
        add_background(self)          # 可选：默认黑板纹理，可传图片或 color=
        enable_layout_guard(self)     # 必需：不开就检测不到越界/重叠/静止
        audio = AudioManager(self)

        d = audio.start("s1")         # 挂上这段旁白，返回总时长
        audio.wait_for_cue("c1")      # 等到旁白讲到 marker 那句
        self.play(Write(Text("中文必须带 font", font=CJK_FONT)))
        audio.end(d)                  # 补齐到旁白结束
```

| API | 作用 |
|---|---|
| `AudioManager(scene)` | 读 `durations.json`，把时间轴钉在真实音频上 |
| `.start(id)` / `.end(d)` | 开始一段旁白 / 补齐到这段结束 |
| `.wait_for_cue(id)` | 等到旁白讲到该 cue |
| `enable_layout_guard(scene)` | 越界/重叠/旁白静止检测（**必需**） |
| `add_background(scene, image=…, color=…)` | 可选背景层，默认黑板纹理 |
| `CJK_FONT` | 自动探测的系统中文字体。**所有 `Text(...)` 都必须带** |
| `LATIN_FONT` | 纯拉丁文本用它；中英混排的行仍用 `CJK_FONT` 走 Pango 回退 |
| `pulse(mob, …)` | 强调一个对象。**不要用 `Indicate`**：它会把容器里的文字连同填充一起染成同色，强调反而把字盖掉 |
| `find_free_pos(mob, scene, anchor=…)` | 在 `play()` 前主动挑一个不冲突的位置 |
| `safe_area()` | 返回 `(left, right, bottom, top)` |
| `SafeMathTex` | `MathTex` 的中文保护版，误传中文时立刻报错 |

**配色按语义取用，不要自己配。** `INK`（正文）/ `ACCENT`（当前焦点）/ `CORRECT`（结论）/
`SECOND`（第二组对照）/ `DATA`（数据量值）/ `WRONG`（否定）/ `MUTED`（退到背景）。
这七个是在黑板底上按 WCAG 相对亮度验过的；ManimCE 原色在绿底上普遍偏灰
（实测 `GREEN` 3.04、`TEAL` 3.46、`BLUE` 3.22、`RED` 2.18、`GREY` 1.84），`check` 会拦。
饱和红在绿底上到不了 4.5，所以**错误不能只靠颜色表达**，`WRONG` 必须与划掉或叉号同时出现。

`enable_layout_guard` 还会在每次 `play()` 后把顶层结构复原：溶解编排类动画
（`AnimationGroup` / `LaggedStart` / `Circumscribe`）留下的裸 `Group`，并把被
`Scene.add` 的 restructure 逐出的作者容器接回去。所以**不必自己覆盖 `play()` 或 `Scene.add`**。

## segments.json 格式

```json
[
  {
    "id": "s1",
    "text": "这个概念的关键在于理解变化过程。我们先从最简单的情况出发，一步步看它是怎么工作的。",
    "cues": [
      { "id": "c1", "marker": "关键在于" },
      { "id": "c2", "marker": "一步步看" }
    ]
  }
]
```

- `id`：字母/数字/下划线/连字符，全局唯一
- `marker`：必须**逐字出现**在该段 `text` 里（脚本校验，对不上直接失败）
- 相邻 cue 间隔不超过 10 秒

## 环境变量

| 变量 | 必需 | 默认值 |
|---|---|---|
| `TTS_API_KEY` | 是（配音时） | — |
| `TTS_BASE_URL` | 否 | `https://tts.style520.com/v1` |
| `TTS_MODEL` | 否 | `tts-1` |
| `TTS_VOICE` | 否 | `zh-CN-YunjianNeural`（云健）；可选值用 `GET <TTS_BASE_URL>/audio/voices` 查 |
| `VIDEO_TTS_RATE` | 否 | `1.0`（0.5–2） |

TTS 相关变量配置在项目 `.claude/settings.local.json` 的 `env` 里（该文件不进 git），Claude Code 会把它注入命令环境；在 Claude Code 之外手动运行时需自行 `export`。该接口每个 key 最多同时处理 10 个请求，`narrate.mjs` 是逐段串行合成，不会超。
| `TEACHING_CJK_FONT` | 否 | 自动探测 |

**系统依赖**：`ffmpeg`、`ffprobe`、LaTeX（`xelatex` + `dvisvgm`）、Node.js（≥18）。
**Python 环境**：skill 自带（`runtime/.venv`，ManimCE 0.21.0）。首次使用需在 `runtime/` 下执行 `uv sync --frozen`。

## 目录结构

```
.claude/skills/manim-video/
├── SKILL.md                      ← 你正在读的文件
├── references/                   按需加载的文档
│   ├── production-guide.md      ★ 制作指南 + 审查员（必须完整读）
│   ├── content-types.md          内容指南（从头到尾读完）
│   ├── story-models.md           七种叙事模型（按需）
│   ├── manim-index.md            ManimCE 规则入口（按任务选读）
│   ├── manim-basics.md           场景/对象/布局/样式
│   ├── manim-animations.md       动画/变换/编排 + 完整参考表
│   ├── manim-objects.md          文字/公式/坐标系/3D
│   ├── manim-teaching.md         教学设计/分镜/舞台/音频同步
│   └── examples/                 代码示例
├── templates/                    场景模板
├── scripts/
│   ├── manim_cli.py              主入口（new/check/layout/render/stills/verify）
│   ├── checks.py                 工程检查（结构/LaTeX/旁白/cue，由 CLI 调用）
│   └── narrate.mjs               TTS 旁白生成
└── runtime/                      Python 环境 + 运行时库 + 黑板底图

<项目根>/videos/<slug>/           ← 视频项目目录（产物在项目根下）
```
