# ManimCE 规则库

Manim Community Edition 最佳实践。**只适用于 ManimCE**（`from manim import *`），不适用于 ManimGL。

规则按主题合并为 4 个文件。按下面的指引读需要的部分，不必全量通读。

## 按任务选读

### 做一条完整的教学视频

1. 先读 `manim-teaching.md` 的"教学设计"和"分镜"章节——确定学习目标和视觉证据
2. 按分镜需要的技术能力读对应文件（见下表）
3. 渲染前读 `manim-teaching.md` 的"成片复审"章节

### 写某个具体动画 / 修 bug

直接读对应主题的文件，不必走完整流程。

### 视觉不够好，想改进

从 `manim-teaching.md` 的"教学设计"开始——确认场景是否展示了目标关系，然后看 `manim-basics.md` 的定位、配色和时间控制。

## 4 个文件的内容

| 文件 | 包含的主题 | 什么时候读 |
|---|---|---|
| `manim-basics.md` | 场景结构、Mobject 类型、定位与布局、VGroup、形状、线与箭头、配色、样式、配置、CLI | 第一次写 ManimCE 代码时通读一遍 |
| `manim-animations.md` | 动画类（Create/Write/FadeIn…）、变换（Transform/TransformMatchingTex…）、文字动画、编排（AnimationGroup/LaggedStart）、时间与缓动、**完整动画参考表**（73 个动画类 + 54 个标注工具） | 需要用哪种动画时查 |
| `manim-objects.md` | 文字与字体、LaTeX/MathTex/公式拆分(`{{ }}`)、坐标系(Axes)、函数图、3D(ThreeDScene)、相机控制 | 涉及公式、图表、3D 时读 |
| `manim-teaching.md` | 教学设计、分镜、舞台归属与生命周期（解题线）、旁白音频同步（AudioManager）、updater/ValueTracker、成片复审 | 做教学视频的设计和收尾阶段 |

## 核心原则

动画的目的是**让一个关系更容易被看见**。先确定"观众需要看见什么证据"，再从中挑 ManimCE 技术——不要反过来先选效果再往里塞内容。

优先级：技术正确性 > 解释意图 > 通用默认值。

## 代码示例

`examples/` 下有完整可运行的示例：

- `basic_animations.py` — 形状、文字、路径动画
- `math_visualization.py` — LaTeX 公式、着色、推导
- `updater_patterns.py` — ValueTracker、动态动画
- `graph_plotting.py` — Axes、函数、面积、极坐标
- `3d_visualization.py` — ThreeDScene、曲面、参数曲线

## 场景模板

`templates/` 下有起步模板（位于 skill 根目录的 `templates/`）：

- `teaching_scene.py` — **教学视频场景**（含 AudioManager + 布局守卫，推荐起步用这个）
- `basic_scene.py` — 标准 2D 场景（纯 ManimCE，无音频）
- `camera_scene.py` — MovingCameraScene（zoom/pan）
- `threed_scene.py` — 3D 场景（曲面 + 旋转相机）

## 快速参考

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)
```

```bash
manim -pql scene.py MyScene    # 低清预览
manim -pqh scene.py MyScene    # 高清
manim --format gif scene.py    # GIF
```
