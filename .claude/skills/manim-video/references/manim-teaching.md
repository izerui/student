# Educational Animation Design

Use this guide before choosing Manim objects and effects for a complete explanation. The goal is to turn an idea into visual evidence that the viewer can interpret.

## Start with the Learning Outcome

Define what the viewer should be able to recognize, predict, derive, or explain after the animation.

Useful planning questions:

- What does the audience already know?
- Where is the likely conceptual obstacle?
- Which relationship is difficult to perceive in static notation?
- What should the viewer be able to do with the idea afterward?
- Which final visual state would demonstrate that the explanation succeeded?

A topic is not yet a learning outcome. "Fourier series" names content; "see how adding frequencies reconstructs a signal" identifies an observable understanding.

## Design Visual Evidence

Build each important beat around three parts:

1. **Claim** - the idea being communicated.
2. **Evidence** - what the viewer can inspect on screen.
3. **Change** - the animation that reveals or connects the evidence.

Example:

| Part | Design |
|------|--------|
| Claim | Increasing the sample size stabilizes the estimate |
| Evidence | Several estimates converge toward a fixed reference value |
| Change | A tracker increases sample size while the estimates tighten |

The scene is working when the claim can be inferred from the picture instead of depending entirely on a caption or narration.

## Decide Whether Motion Helps

Animation is valuable when understanding depends on change over time:

- a construction is assembled from parts
- an algorithm advances through states
- one expression transforms into another
- a parameter continuously affects a graph or geometric object
- two approaches need a synchronized comparison
- a spatial relationship changes

A static composition is often stronger when the main task is inspecting a stable structure, comparing a dense set of labels, or studying a final summary.

Judgment standard: if the explanation naturally uses "first, then, therefore," motion can expose the sequence. If it mainly uses "this part corresponds to that part," a stable annotated view may carry more information.

Technique-oriented defaults such as using `Write` for text or `Create` for graphs apply after deciding that the object's appearance is itself meaningful. Use an already-complete static object when the viewer's task is to inspect the final structure rather than follow its construction.

## Choose a Representation

Select the representation that makes the target relationship directly visible.

| Learning need | Possible representation |
|---------------|-------------------------|
| Magnitude or proportion | length, area, angle, count, aligned bars |
| Change over time | moving point, trace, evolving graph, counter |
| Mapping or correspondence | shared color, connecting line, matched transform |
| Accumulation | growing region, stacked pieces, running total |
| Comparison | aligned states, common axes, synchronized motion |
| Hierarchy or flow | grouped regions, directed connections, staged reveal |
| Invariance | transform the object while preserving the unchanged feature |
| Uncertainty or distribution | repeated samples, density, spread, intervals |

Use notation when precision matters and geometry when spatial intuition matters. Many mathematical explanations benefit from showing both and keeping their states synchronized.

## Preserve Object Identity

Continuity helps the viewer understand what changed and what stayed the same.

- Transform an existing object when it represents the same concept in a new state.
- Use matching terms, positions, or colors to expose correspondence.
- Introduce a new object when the concept itself changes or when simultaneous comparison is important.
- Keep multiple views driven by the same `ValueTracker` or model state when they describe the same quantity.

Judgment standard: after a transition, the viewer should know where each important idea came from.

## Build Mathematical Explanations

### Equations

Treat an equation as a structure, not as a line of text.

- Isolate terms that need separate identity.
- Show why an operation is introduced before presenting its result.
- Preserve matching terms through `TransformMatchingTex` where appropriate.
- Pair symbolic steps with a graph, diagram, number-line action, or other evidence when that representation clarifies the reasoning.
- Keep previous information visible as context when the new step depends on it.

### Algorithms

Expose the state that drives each decision:

- current input or active item
- relevant invariant
- comparison or condition
- resulting state change
- progress toward completion

The viewer should see why the next action occurs, not only watch objects move.

### Data and Models

Use common scales and synchronized states for comparisons. When values change, show the reference point that makes the change meaningful. Labels should explain units and semantics rather than duplicate obvious visual facts.

### 3D

Use 3D when depth, orientation, occlusion, surfaces, or spatial transformation is part of the concept. Camera motion should reveal a relationship that a fixed view cannot show as clearly.

## Direct Attention

At each moment, establish a visual priority:

- current evidence
- supporting context
- structural background

Priority can come from position, scale, contrast, opacity, motion, camera framing, or a temporary annotation. Choose the least intrusive combination that makes the intended focus apparent.

When several elements move together, they should express one combined event. Sequence unrelated changes so the viewer can interpret each one.

## Explore Creative Alternatives

Creativity is useful when it improves the explanatory model, not when it only adds novelty.

Generate alternatives by changing one dimension at a time:

- Replace the conventional metaphor with a spatially clearer one.
- Combine symbolic and geometric views into synchronized representations.
- Begin with the result and deconstruct it when backward reasoning exposes dependencies.
- Exaggerate a parameter to make its effect perceptible, then return to the realistic range.
- Remove notation temporarily to test whether the underlying relationship is visually understandable.
- Change viewpoint, scale, or dimensionality when it reveals information hidden by the standard view.

Evaluate each alternative with one question: what can the viewer understand from this version that was difficult to see before?

## Completion Test

Before implementation, confirm:

- The intended audience and learning outcome are explicit.
- Every major claim has visible evidence.
- Motion represents construction, change, causality, comparison, or attention.
- Important concepts preserve identity across states.
- The final visual state supports the conclusion.
- Creative choices clarify the subject instead of becoming the subject.


# Storyboarding Manim Explanations

A storyboard connects the learning outcome to concrete scene states and animations. Write it before implementation when the task involves more than a small isolated scene.

## Choose a Narrative Shape

Use a structure that matches the reasoning rather than forcing every topic into the same sequence.

### Discovery

1. Present a question or observable pattern.
2. Build an intuitive model.
3. Introduce formal notation.
4. Reveal the relationship that resolves the question.
5. Apply or extend the idea.

### Problem and Insight

1. Establish the problem and success condition.
2. Show why the direct approach is insufficient.
3. Introduce the key observation.
4. Use it to construct the solution.
5. Verify the result.

### Derivation

1. Establish known quantities and the target.
2. Make the first justified transformation.
3. Preserve relevant terms while simplifying.
4. Expose the decisive step.
5. Interpret and check the result.

### Comparison

1. Establish a common task or scale.
2. Demonstrate each approach under comparable conditions.
3. Align the outcomes.
4. Highlight the meaningful differences.
5. State when each approach is appropriate.

### Build-Up

1. Introduce the first component and its role.
2. Add components as their dependencies become relevant.
3. Show the connections or data flow.
4. Demonstrate the assembled system.
5. Return to an overview that preserves the learned structure.

These are planning lenses, not fixed scene counts. Combine or shorten them according to the subject.

## Give Each Scene a Cognitive Job

A scene should have one clear responsibility, such as:

- establish the problem
- define a representation
- reveal a transformation
- compare alternatives
- demonstrate a consequence
- consolidate the result

Several small facts may share a scene when they support the same responsibility. Split the scene when the viewer must reset attention or adopt a different mental model.

## Plan Final States Before Entrances

For every important moment:

1. List the objects that must coexist.
2. Arrange and size the complete state.
3. Identify the current focus and supporting context.
4. Decide which objects are introduced, transformed, dimmed, archived, or removed.
5. Animate toward the already validated composition.

This keeps early choices from consuming space needed by later equations, labels, or diagrams.

## Map the Explanation into Visual Beats

A visual beat is a meaningful change in what the viewer can understand.

| Spoken or conceptual beat | Visual response |
|---------------------------|-----------------|
| Introduce an object | establish its form and label |
| State a condition | mark the affected region or term |
| Perform an operation | transform the relevant object |
| Compare states | align or synchronize them |
| Draw a conclusion | consolidate and emphasize the evidence |

A beat may use one animation or a small simultaneous group. Treat one relationship as a coherent beat, and give unrelated reasoning steps separate beats so each change remains interpretable.

## Synchronize Narration and Visuals

When narration is present:

- Map each important phrase to the visual evidence it explains.
- Start the corresponding visual change close enough to the phrase that the connection is obvious.
- Keep relevant context visible while the narration refers to it.
- Let the visual settle when the audience needs to read, compare, or infer.
- Use narration to explain causes and decisions rather than merely reading visible labels.

Exact timing depends on speech rate, information density, and animation distance. Review synchronization in the rendered video instead of relying only on accumulated `run_time` values.

## Plan Pacing by Cognitive Load

Estimate time from the work the viewer must do:

- notice a visual change
- read new text or notation
- connect it with prior information
- inspect a comparison
- predict or understand the next step

Important structural changes deserve more time than familiar arithmetic or repeated operations. Consecutive movements that complete the same thought can flow without a pause; a new idea may need a stable observation state.

Use contrast in tempo to clarify importance. Variation should follow the explanation's structure rather than a preset rhythm.

## Connect Scenes

Choose a transition according to conceptual continuity:

- **Carry forward** an object when it remains the subject of the next scene.
- **Transform across the boundary** when the next scene reframes the same concept.
- **Move or reframe the camera** when the explanation changes scale or viewpoint.
- **Use a clean cut** when the conceptual context resets and continuity would imply a false relationship.
- **Clear selected context** when only part of the previous state remains relevant.

The transition is successful when the viewer understands whether the next scene continues, reframes, or replaces the previous idea.

## Storyboard Template

```markdown
# Title

## Audience and outcome
- Audience:
- Prior knowledge:
- Learning outcome:
- Likely obstacle:

## Visual language
- Concept-to-color assignments:
- Recurring spatial anchors:
- Primary representations:

## Scene: [name]
- Cognitive job:
- Starting state:
- Final state:
- Visual evidence:
- Context retained from previous scene:

### Beats
1. Concept or narration:
   - Visual change:
   - Manim technique:
   - Why this technique communicates the relationship:
2. ...

### Transition
- What persists:
- What changes:
- Why the next scene follows:
```

## Storyboard Review

Before coding, confirm:

- The opening creates a concrete question, need, or observable state.
- Every scene advances the explanation.
- Each important statement maps to visible evidence.
- Layouts account for their complete final states.
- Repeated concepts retain recognizable identity.
- Timing reflects reading and reasoning demands.
- The conclusion is supported by what the viewer has seen.

<!-- Stage Ownership section moved to content-types.md (解题讲解) -->

# Narration Sync (Project AudioManager)

The `teaching_runtime` module ships an `AudioManager` built on ManimCE's `Scene.add_sound()` and
`Scene.time`. It is project-specific, not part of ManimCE.

See the "Storyboarding" section earlier in this file for how to decide which phrase earns
a visual beat. This section covers the API contract only.

## Per-Segment Contract

```python
duration = audio.start("scene_solve")   # adds the wav, returns its length in seconds
audio.wait_for_cue("write_curl")        # holds until the cue timestamp
self.play(Write(line1), run_time=1.0)
audio.end(duration)                     # pads so visuals cover the whole narration
```

- `start(scene_id) -> float` returns `durationSec` from `durations.json` and calls `add_sound`.
- `wait_for_cue(cue_id)` waits until the cue's `timeSec` offset within the current segment.
- `end(expected_duration)` waits out the remaining time plus a 0.2s safety margin.
- `wait_until(seconds)` waits to an absolute offset within the current segment.

## Never Pass a Literal Zero to end()

`audio.end(0)` ends the visual timeline while narration is still playing. The
muxer then truncates the tail with `-shortest`, silently losing the end of the
explanation. Always pass the value returned by `start()`.

```python
# Wrong — the tail of this segment gets cut
duration = audio.start("scene_solve")
self.play(Write(line1))
audio.end(0)

# Right
duration = audio.start("scene_solve")
self.play(Write(line1))
audio.end(duration)
```

## One Segment at a Time

Do not call `start()` again before the previous segment's `end()`. Overlapping
segments stack audio tracks and desynchronize every later cue.

## Cue Offsets Are Segment-Relative

All cue offsets are measured from the segment's own start, not from the start
of the video. `AudioManager` records `scene.time` at `start()` and subtracts it
on every wait. Do not convert cue times to absolute video timestamps.


# Updaters and Dynamic Animations

Updaters allow mobjects to automatically update based on other values or mobjects.

## Basic Updaters

Add a function that runs every frame.

```python
from manim import *

class UpdaterExample(Scene):
    def construct(self):
        dot = Dot()
        label = Text("Follow me").next_to(dot, UP)

        # Label always follows the dot
        label.add_updater(lambda m: m.next_to(dot, UP))

        self.add(dot, label)
        self.play(dot.animate.shift(RIGHT * 3), run_time=2)
        self.play(dot.animate.shift(DOWN * 2), run_time=2)
```

## Updater Syntax

```python
# Lambda function
mobject.add_updater(lambda m: m.move_to(target.get_center()))

# Named function
def follow_target(mob):
    mob.next_to(target, RIGHT)

mobject.add_updater(follow_target)

# With dt (delta time) parameter
def time_based_update(mob, dt):
    mob.rotate(dt * PI)  # Rotate based on time elapsed

mobject.add_updater(time_based_update)
```

## ValueTracker

A mobject that holds a numeric value. Perfect for animating parameters.

```python
class ValueTrackerExample(Scene):
    def construct(self):
        # Create tracker
        tracker = ValueTracker(0)

        # Create number display
        number = DecimalNumber(0, num_decimal_places=2)
        number.add_updater(lambda m: m.set_value(tracker.get_value()))

        # Create circle that grows with tracker
        circle = Circle()
        circle.add_updater(lambda m: m.set_width(tracker.get_value()))

        self.add(number, circle)

        # Animate the tracker
        self.play(tracker.animate.set_value(4), run_time=3)
        self.play(tracker.animate.set_value(1), run_time=2)
```

### ValueTracker Operations

```python
tracker = ValueTracker(5)

# Get and set value
current = tracker.get_value()
tracker.set_value(10)

# Increment
tracker.increment_value(2.5)

# Arithmetic operators (direct manipulation, no animation)
tracker += 1
tracker -= 2
tracker *= 3
tracker /= 2

# Animate changes
self.play(tracker.animate.set_value(100))
self.play(tracker.animate.increment_value(-50))
```

## DecimalNumber with ValueTracker

Display a changing number:

```python
class NumberDisplay(Scene):
    def construct(self):
        tracker = ValueTracker(0)

        number = DecimalNumber(
            0,
            num_decimal_places=2,
            include_sign=True,
            font_size=72
        )
        number.add_updater(lambda m: m.set_value(tracker.get_value()))
        number.add_updater(lambda m: m.move_to(ORIGIN))

        self.add(number)
        self.play(tracker.animate.set_value(100), run_time=3)
```

## always_redraw

Recreate a mobject every frame based on current values.

```python
class AlwaysRedrawExample(Scene):
    def construct(self):
        tracker = ValueTracker(1)

        # Line that always connects two points based on tracker
        line = always_redraw(
            lambda: Line(
                LEFT * 2,
                RIGHT * 2 * tracker.get_value()
            )
        )

        self.add(line)
        self.play(tracker.animate.set_value(2), run_time=2)
        self.play(tracker.animate.set_value(0.5), run_time=2)
```

## `Mobject.always` — Convenient Updaters (ManimCE 0.20+)

For simple "keep this property in sync" updaters, `.always` is shorter and
clearer than a lambda:

```python
dot = Dot()
label = Text("here")

# Preferred (0.20+)
label.always.next_to(dot, UP)

# Equivalent older form
label.add_updater(lambda m: m.next_to(dot, UP))
```

`.always` wraps any mobject method into an updater in one line. Use it for
positional following, alignment, and simple property mirroring. For updaters
that need `dt`, conditional logic, or multiple statements, use
`add_updater(func)`.

```python
# .always works with any method
brace.always.next_to(group, DOWN)
arrow.always.put_start_and_end_on(a.get_center(), b.get_center())
```

## Common Updater Patterns

### Following Another Mobject
```python
# Preferred
follower.always.next_to(leader, RIGHT)

# Or with lambda when you need custom logic
follower.add_updater(lambda m: m.move_to(leader.get_center() + UP * 0.5))
```

### Pointing at Another Mobject
```python
arrow = Arrow(ORIGIN, RIGHT)
arrow.add_updater(lambda m: m.put_start_and_end_on(
    start.get_center(),
    end.get_center()
))
```

### Rotating Continuously
```python
mobject.add_updater(lambda m, dt: m.rotate(dt * PI))
```

### Matching Properties
```python
# Match color
follower.add_updater(lambda m: m.set_color(leader.get_color()))

# Match position with offset
follower.add_updater(lambda m: m.move_to(leader.get_center() + UP))
```

## Removing Updaters

```python
# Remove specific updater
mobject.remove_updater(updater_function)

# Remove all updaters
mobject.clear_updaters()

# Suspend temporarily
mobject.suspend_updating()
mobject.resume_updating()
```

## Updaters with Animations

Updaters continue running during animations:

```python
class UpdaterDuringAnimation(Scene):
    def construct(self):
        dot = Dot()
        trail = TracedPath(dot.get_center, stroke_color=YELLOW)

        self.add(dot, trail)
        self.play(dot.animate.shift(RIGHT * 3 + UP * 2), run_time=3)
```

## TracedPath

Built-in updater for drawing paths:

```python
class TracedPathExample(Scene):
    def construct(self):
        dot = Dot()
        path = TracedPath(dot.get_center, stroke_width=2, stroke_color=BLUE)

        self.add(dot, path)
        self.play(
            dot.animate.shift(RIGHT * 2),
            dot.animate.shift(UP * 2),
            run_time=3
        )
```

## Best Practices

1. **Use ValueTracker for animated parameters** - Clean and controllable
2. **Use always_redraw for complex shapes** - When updaters get complicated
3. **Clear updaters when done** - Prevent performance issues
4. **Keep updater functions simple** - Complex logic can slow rendering
5. **Use dt for time-based animations** - Frame-rate independent


# Production Review

Code correctness is necessary, but the rendered animation is the product. Review still frames, motion, and the complete sequence before treating a video as finished.

## Before Coding

Confirm:

- the target resolution, aspect ratio, frame rate, and output format
- the audience and learning outcome
- the storyboard's key visual states
- the meaning of recurring colors and spatial anchors
- the availability of fonts, LaTeX packages, images, audio, and other assets
- which scenes require camera, updater, graphing, or 3D rules

Resolve uncertain APIs with the relevant rule file or the installed ManimCE version before building around them.

## Implement in Reviewable Units

Keep scenes or major sections independently renderable while developing. Separate content construction from repeated style constants and helper functions when doing so makes the visual logic easier to inspect.

For each unit:

1. Build the complete key state.
2. Render a representative frame.
3. Correct layout and readability.
4. Add the animation path.
5. Render the motion at draft quality.
6. Integrate it into the full sequence.

## Draft Render Loop

Use low or medium quality for iteration:

```bash
manim -ql scene.py SceneName
manim -qm scene.py SceneName
manim -qm -s scene.py SceneName
```

Use a higher-quality render after the content, layout, and timing have stabilized:

```bash
manim -qh scene.py SceneName
```

Choose custom resolution and frame rate when required by the delivery target. See [cli.md](cli.md) and [config.md](config.md).

## Review Key Frames

Inspect states that carry meaning:

- the first usable visual
- the most information-dense composition
- each important transformation's start and end
- graph extrema or significant parameter states
- the main comparison
- the final conclusion

For each frame, check:

- Is the intended focus apparent?
- Can text, notation, labels, and thin lines be read at delivery size?
- Are related objects visually associated?
- Are any objects clipped, crowded, or unintentionally overlapping?
- Does supporting context remain visible without competing with the focus?
- Does the frame itself contain the evidence required by the explanation?

## Review Motion

Watch the animation at normal speed and with audio when present.

Check:

- whether the viewer can track object identity through transformations
- whether simultaneous motion represents one coherent event
- whether important states remain visible long enough to inspect
- whether pauses provide useful observation time
- whether camera movement reveals information and settles before detailed reading
- whether narration and visual changes refer to the same idea at the same time
- whether scene transitions communicate continuation or reset correctly

Scrubbing and isolated previews help diagnose problems, but a full-speed watch reveals pacing and attention issues that individual frames cannot.

## Revise by Visual State

When a frame fails, repair the complete composition that owns that moment:

1. Identify the intended focus and evidence.
2. List everything visible at that time.
3. Rebalance position, scale, contrast, and context together.
4. Recheck the paths entering and leaving the state.
5. Render the same frame and surrounding motion again.

This produces more stable results than adjusting one overlapping object without considering the rest of the composition.

## Technical Checks

Before final rendering:

- Every referenced asset and font resolves in the target environment.
- LaTeX expressions compile from a clean cache.
- Dynamic objects use valid updaters and remove them when no longer needed.
- Output dimensions and frame rate match the target.
- All selected scenes render without exceptions.
- Transparent output, audio, or plugins are configured when required.

## Final Review

Confirm the delivered file:

- opens and contains the expected video stream
- uses the intended resolution, aspect ratio, duration, and format
- has no blank frames, accidental flashes, clipped content, or unfinished states
- remains understandable at normal playback speed
- preserves audio synchronization when audio is included
- ends on a complete and interpretable state

The final standard is not the number of animations or visual effects. It is whether the viewer can follow the intended reasoning from the rendered result.


# 内容特征到动画技术的通用映射

面对任意输入内容时，先识别内容的**抽象特征**（不是具体学科或题目），再选择合适的 ManimCE 技术。这张表覆盖了引擎能做到的核心表达方式。

## 特征识别 → 技术选择

| 内容特征 | 核心动画手段 | 关键约束 |
|---|---|---|
| **连续变化**（某个量随参数平滑改变） | `ValueTracker` + `always_redraw` / updater | 变化必须在画面上逐帧可见，不能只展示起止两个定格 |
| **公式推导**（一个表达式变换成另一个） | `TransformMatchingTex` + `{{ }}` 拆分 | 对应项保持身份并连续变换，不要整块替换；变换前后短暂并列 |
| **几何关系**（对象之间有位置/角度/长度约束） | 用 ManimCE 几何原语精确构造 | 几何位置必须忠实于数学关系，不能为了避开重叠而拆散有关系的对象 |
| **函数图像**（输入-输出映射可视化） | `Axes` + `.plot()` / `FunctionGraph` | 坐标轴必须有标注；函数变化用 `ValueTracker` 驱动参数连续变 |
| **空间结构**（三维对象或立体关系） | `ThreeDScene` + `Surface` / 3D 原语 | 旋转相机要有教学意义（换视角是为了看到新的关系），不是装饰 |
| **分步过程**（一步一步推进的序列） | `Succession` / `LaggedStart` + cue 同步 | 每步的前状态、操作、后状态都要可见；步骤之间有视觉连接 |
| **对比/比较**（两个方案或状态的差异） | 并排放置 + 颜色区分 + 同步变化 | 比较对象必须在同一坐标系/同一基准下，差异用长度/面积/位置直接可见 |
| **面积/体积关系** | 几何图形 + `fill_opacity` + 面积标注 | 图形必须贴在对应的边/面上（几何位置关系是内容本身） |
| **向量/方向** | `Arrow` / `Vector` + `.get_end()` 精确定位 | 向量的起点、方向、长度必须与数学定义一致 |
| **数据展示**（数值集合的可视化） | `BarChart` / `Axes` + 数据驱动 | 保留单位、基线、刻度含义；数据变化用同一图元连续变化 |
| **集合关系**（交集/并集/包含） | `Union` / `Intersection` / `Difference` + 颜色填充 | 运算结果必须正确；用半透明叠加让关系可见 |
| **流程/网络** | `DiGraph` / 手动节点+边 | 按数据流/控制流顺序让图"长出来"，不要一次性铺开再高亮 |
| **周期/循环** | `always_rotate` / 参数曲线 + 循环动画 | 周期性必须能从画面看出"绕回来了" |
| **拆分/组合** | `VGroup` 操作 + `Transform` | 拆分时各部分保持身份（颜色/标签不变）；组合时来源可追溯 |
| **极限/逼近** | `ValueTracker` + updater，参数趋向目标值 | 逼近过程必须连续可见，不能跳到结果 |
| **场/梯度** | `ArrowVectorField` / `StreamLines` | 箭头方向和长度必须与函数一致；场的对称性等特征要从画面可见 |
| **分类/分支** | 从母体分裂出 N 支 + 颜色/位置区分 | 分类依据必须可见（不是直接出现 N 个并列结果） |

## 选择原则

1. **先识别特征，再选技术**——不要反过来。"我想用 ThreeDScene" 不是理由；"这个关系在二维投影中会丢失信息" 才是。

2. **一个场景可以组合多个特征**——连续变化 + 几何关系 + 公式推导可以同时出现。用 `ValueTracker` 驱动几何图形变化，同时用 `always_redraw` 更新公式里的数值。

3. **降维有代价**——三维关系投影到二维会丢失信息。如果降维后观众无法从画面重建原始关系，就不该降。同样，一维过程不必强行铺成二维图表。

4. **几何位置是内容**——当内容说"A 在 B 上面"、"C 和 D 相切"、"面积等于某个正方形"，画面中的位置关系就是教学内容本身。为了布局好看或避免重叠而破坏位置关系，等于讲错了。正确做法是缩小整体、分阶段展示或调整全局布局。

5. **共享状态驱动**——如果多个对象反映同一个变量的变化（比如函数图像和面积值），它们必须由同一个 `ValueTracker` 驱动，不能各演各的。否则观众看到的是两个不相关的动画，而不是"同一件事的两个视角"。

6. **标注跟随对象**——标签、数值、箭头的生命周期跟它标注的对象绑定。对象移动时标注一起动，对象消失时标注一起走。

## ManimCE 最佳用法速查

通用编码原则见 `production-guide.md`。以下是 ManimCE 各能力的最优使用方式：

| 想实现的效果 | 最佳 API 选择 | 要点 |
|---|---|---|
| 公式逐项变换 | `TransformMatchingTex` + `{{ }}` 拆分 | 对应项保持身份连续变换，观众看到"从什么变成什么" |
| 参数连续驱动 | `ValueTracker` + `always_redraw` / updater | 一个 tracker 驱动多个对象，画面逐帧变化 |
| 坐标系完整标注 | `Axes(axis_config={"include_numbers": True})` | 刻度、单位、轴名让图表自解释 |
| 多组数据同基准对比 | 共用一个 `Axes`，统一 `x_range`/`y_range` | 相同坐标系下差异才有意义 |
| 对象运动留痕 | `TracedPath` | 挂载前确保对象已在正确初始位置 |
| 3D 场景中的文字 | `add_fixed_in_frame_mobjects(text)` | 覆盖层固定在屏幕，内容层参与 3D 变换 |
| 镜头推近/拉远 | `MovingCameraScene` + `camera.frame.save_state()` | 先保存再变换，`Restore()` 平滑回位 |
| 精确边缘对齐 | `.align_to(ref, DOWN/UP/LEFT/RIGHT)` | `move_to()` 只管中心，边缘对齐需要显式指定 |
| 向量场可视化 | `ArrowVectorField` + `StreamLines` | 箭头显示方向和大小，流线显示运动轨迹 |
| 集合运算 | `Intersection` / `Union` / `Difference` | 半透明填充让运算结果直观可见 |
| 数据变化动画 | `BarChart` + `change_bar_values()` | 柱子连续变高，不是换一张图 |

## 布局守卫的智能跳过

守卫自动跳过以下类型的"重叠"（它们是正常的，不需要调整）：

| 跳过的情况 | 原因 |
|---|---|
| `Dot`/`ParametricFunction`/`FunctionGraph` 与 `Axes`/`NumberLine` | 数据点和曲线天然在坐标系上 |
| 图表数据元素之间 | 多条曲线或多个数据点可以交叉 |
| 小字号标签（`font_size≤24`）与坐标系 | 数据标注自然位于图内 |
| 装饰类型（`SurroundingRectangle`、`Brace`、`Cross`、`Underline`、`RightAngle`、`Angle`） | 它们本来就该贴在目标上 |
| 有填充的几何图形之间（`Polygon`、`Circle`、`Rectangle` 等 `fill_opacity>0`） | 几何嵌套（如三角形在矩形内）是教学内容 |
| 只含 `VectorizedPoint` 的空容器 | `always_redraw` 的占位符 |

同一对象在同一位置只报一次（去重机制），`always_redraw` 每帧重建不会产生重复。

如果守卫报告了你认为正确的重叠（比如几何关系要求对象必须贴合），可以用 `--skip-gates` 跳过闸门渲染。
