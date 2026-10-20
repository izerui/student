# 内容指南

从头到尾读完。这是一套完整流程，适用于任何需要讲明白的内容。

---

## 输入材料处理

- **参考材料是参考，不是讲稿**：输入可能附带标准答案、解题步骤、知识要点或文档。学习者看视频时不会同时看原文，所以视频必须**自身完整**——该有的推导要有，该写的公式要写。但你不是在念材料，而是用自己的教学语言重新组织，在完整呈现内容的同时叠加材料给不了的东西：方法识别、决策理由、易错拦截、举一反三。
- **不要逐句复述**：不要按参考材料的原文顺序朗读或改写。像一个真正吃透了这个内容的老师那样，把完整过程和背后的道理一起讲明白。
- **图片输入**：如果用户提供了图片（截图、照片等），先用 Read 工具查看。图中文字识别后作为输入材料；图中的**图形**（几何图、函数图、装置图、流程图）要用 ManimCE 重新绘制，不要用 `ImageMobject` 直接贴原图。
- **来源有错时**：完成独立复核后按正确结论继续生成，并把来源错误、纠正依据和最终结论写入 `source-correction.json`。来源错误本身不中断生成。

---

## 内容分析

拿到输入后，在思考中完成以下分析，结论写进 `storyboard.md`。

### 独立核实

先独立核对输入内容的关键结论。涉及计算的自己重算一遍，涉及事实的自己核对一遍，涉及推理的自己走一遍。

### 教学分析六问

- **核心问题**：这份内容要讲明白的**一件事**是什么？
- **方法/机制**：为什么是这个方法、这个机制？触发条件是什么？还有没有别的路径？
- **关键转折**：哪一步是整个讲解的灵魂？最容易卡在哪里？
- **推进链**：每步的 `前状态 → 操作 → 后状态`，形成可检查的链条
- **易错点**：哪里容易算错、漏条件、套错方法、理解偏差？
- **拓展价值**：这个方法/概念还能迁移到哪里？

**先形成可检查的推进链，再进入分镜和旁白。不要先写旁白，再倒推内容。**

### 识别内容的形状

问一个问题：**这份内容里，什么在变？**

| 内容里在变的东西 | 对应的叙事模型（见 `story-models.md`） |
|---|---|
| 一个问题被逐步解决 | 问题求解七拍 |
| 一个事物随时间演进 | 过程演化 |
| 一个系统的各部分依次登场协作 | 系统穿行 |
| 两个或多个方案的优劣 | 同条件对照 |
| 一个结构被一层层搭起来 | 逐步构建 |
| 从一堆现象里归纳出规律 | 观察到规律 |
| 一次操作引发一连串反馈 | 操作与反馈 |

读一到两个匹配的模型即可，**不要机械套用**——模型是骨架，不是模具。内容不匹配任何模型时自己组织结构，但必须能回答「观众跟着什么线索往前走」。

### 找到主角

任何能讲明白的内容都有一个**主角**——一个贯穿全片、观众能一直追踪的对象。

主角可以是任何东西——一个几何图形、一条曲线、一个数据集、一台设备、一个流程节点、一个符号、一个角色、一个容器里的量。由内容决定。

**主角由内容决定，载体由主角推出来。** 不要反过来——先定"我要做个 3D 动画"再去找内容往里塞，一定做不好。

判据：观众能不能在片子的任意时刻指着画面说「这个东西刚才还是那样，现在变成这样了」。指不出来，说明还没找到主角。

### 防罗列退化

**内容是「一组并列项」时（公式清单、性质列表、题型分类、易错点、步骤集合），把「罗列」改成「由来」**——不展示 N 个并列结果，而展示它们怎么从一个共同来源分化出来：

- 公式清单 → 从前一画面的对象上抽出符号，各项移到骨架对应位置长成
- 性质列表 → 从定义出发，每条性质都是「对定义做一次操作」的结果
- 分类体系 → 从一个母体分裂出 N 支，分裂依据可见
- 易错点 → 照错误做法走一遍，看结果偏出去，再走对的
- 步骤集合 → 让前一步的结果驱动后一步的动作，不是编号依次出现

这类内容没有现成的运动对象，是最容易退回「依次淡入」的地方。

---

## 视觉设计

### 讲解载体优先级

自上而下取用，每降一级写一句降级理由：

1. 真实情境与实物
2. 三维结构
3. 二维图形演绎
4. 结构图 / 流程图 / 网络图
5. 动态数据图表
6. 平面坐标系上的函数图像

以坐标系函数图像为主载体时，必须说明更高优先级的载体为什么不适用。**不默认从 3D 开始，也不把一维过程随手铺成二维折线图**：升维必须显示新增的关系，降维必须服务精确比较。

### 视觉模型发现（推荐，写进 `visual-research.md`）

视觉设计选择空间大时（没有现成的推导链可以直接搬上画面），推荐做这一步。

从要讲的核心主张反向拆出：知识里的角色是谁、关键关系是什么、真实机制怎么运作、成立前提是什么、什么量保持不变。

然后提出 **3 个机制明显不同的视觉候选**。候选差异必须来自**认知路径**，不能靠换色换材质冒充新方案。

每个候选说明：现实中的对象如何映射到可见主体、知识关系变成什么动作、模型保留与省略什么、如何形成连贯的视觉世界、表示接力怎么走、实现代价多大。

比较后选**能让观众从对象变化中复述关键关系**的那个。

### plan.md（推荐）

视觉设计复杂时推荐写 plan.md，在 storyboard 之前完成：

- 学习目标：观众最终应建立什么理解
- 现实锚点：从什么真实对象、现象、数据、历史问题或工程任务进入，又怎样回到现实验证
- 发现链：观众在哪里观察、预测、比较、产生疑问、看到结果、完成迁移
- 选定模型比其他候选更强的理由、依据和边界
- 贯穿全片的视觉世界与运动语法：核心主体、变换词汇、状态接力、动态节奏
- 每个核心主张对应的动态视觉证据：具体对象、初始状态、动作、结果状态、观众应自行得出的推断
- 旁白如何通过问题、预测、观察提示和揭示推动发现

### design-reviewer 复核（推荐）

视觉设计选择空间大、容易走偏时，推荐在写 storyboard 之前派 `design-reviewer` 做一次独立复核。提供主题、原始内容、两份草案和拟定的分镜。让它独立检查：现实锚点是否参与推理、候选是否真正结构同构、视觉世界是否清晰专属、机制和边界是否可靠、讲解是否能推动发现、是否遗漏了更强的经典构造。

吸收有效反馈；保留原方案时在 `visual-research.md` 记录理由。

### 把关系变成动作

列出内容里的关键关系，逐条翻译成**可见的动作**：

| 关系 | 动作 |
|---|---|
| A 导致 B | A 变形/移动后 B 随之改变（同一状态驱动，不是各演各的） |
| A 和 B 对应 | 颜色、位置或轨迹上的一一对应，同时高亮 |
| A 由 B 和 C 组成 | B、C 合并成 A；或 A 分裂成 B、C |
| A 比 B 大/好 | 同一坐标下并排，差异用长度、面积或位置直接可见 |
| A 在条件 X 下成立 | 把 X 推到边界，看 A 怎么失效 |
| A 是 B 的特例 | 从 B 连续变形到 A，参数可见地收紧 |
| A 分成 N 类 | 从一个母体分裂出 N 支，分裂依据可见 |

翻译不出来的关系，说明你还没真正理解它——回去想清楚再往下走。

---

## 片子结构

### 结构最低要求

不管内容是什么、用什么叙事模型，这四条必须满足：

1. **有一个进入点**——从具体的东西开始（一个现象、一个问题、一个数字、一个场景），不要从抽象定义开始。
2. **有连续的推进**——每个场景的结果是下个场景的输入。场景之间不能是平行的几块，必须有交接。
3. **有一个最强时刻**——全片最重要的理解，对应最强的视觉表达。
4. **有一个回收**——结尾回到开头提出的问题或现象，让人看到它被解决了。

### 开场

**每条视频都必须有开场。** 开场的职责是在 5–10 秒内让观众知道「这条视频要讲什么、值不值得看下去」。

#### 形式由内容决定

开场没有固定形式，由内容自己决定最自然的打开方式。判据：观众看完开场后，能不能用一句话说出「这个视频要讲什么」。说不出来就没起到作用。

#### 旁白

开场旁白**简短直接**，不寒暄、不铺垫。一到两句话说清楚这条视频要讲什么。不要写「带你深入了解 XX」这种空话。

#### 过渡到主线

开场结束后过渡到主线，退出和进入要重叠或无缝衔接，**画面上不能出现只剩空白板的时刻**。

#### 实现

开场是独立的 segment（有自己的 `audio.start` / `audio.end`），不要和主线的第一段旁白合并。

### 主线讲解

这是全片的核心，占大部分时长。节奏和分段由内容决定：简单内容两三段讲完，复杂内容拆成多个阶段。

**主线推进的通用要求**：

- 从现实中的对象、现象、数据或问题进入；现实锚点**参与推理**，不是开场装饰。
- 核心关系由对象的运动、形变、切分、组合、分解、展开、对齐、替换、投影、轨迹或视角变化来呈现；每段变化完成 `前状态 → 动作 → 后状态`，让观众能自行得出结论。
- 旁白通过提问、预测、观察提示和揭示组织发现；画面负责解释并提供证据。**屏幕文字不复述旁白**，不把定理和长段说明当作场景主体。
- 事实、公式、数据、机制和图形关系准确；画面与旁白使用同一套变量、坐标和状态来源。
- 表达维度由内容的**内在自由度**决定，不由视觉复杂度决定。

### 收束

- 把已累积的上下文、全部正式步骤或结论重新编排成紧凑的全览。
- 围绕方法本质、易错点和拓展补充。
- 定格完整全貌，用颜色或编号标记因果关系，让人整体回顾。
- 总结不从头复述过程——画面保留全览，旁白提炼方法、转折和易错点。
- **最后必须落到明确的结束画面**：全览讲完后，把画面收拢到最终结论（或结束卡），配一句收束旁白，静止停留 3–5 秒。这是一个独立的状态，不是总结的最后一条要点——观众要能明确感到「这条视频讲完了」。

### 变换过程的呈现

- **不要直接替换公式或状态**——变换前后短暂并列，让人看到「从什么」变成「什么」。
- 公式间有推导关系时，让对应项保持身份并连续变换（`TransformMatchingTex`、`TransformFromCopy`）。
- 推导中的关键跳转要给足解释；常规算术可以简洁带过。
- 静音和停顿服务于观察，不用动画机械填满空白。

---

## 画布管理

根据内容的推进方式选一种模式，或混合使用。

### 连续画布模式

整个讲解在**同一块板上**完成，从起点到终点在一个连续画面中推进。适合推导密集、有连续变换链的内容。**旁白分段只影响音频文件切分，画面始终在同一块板上连续推进。**

#### Stage Ownership

每个可见对象归属且仅归属一个角色：

- `context_anchor`——缩小的上下文锚点，始终可见。可以是题干条件、核心命题、定义、核心问题或目标——任何需要全程保持可见的上下文。
- `current_stage`——当前阶段的全部对象。
- `conclusion_chain`——正式结论，跨阶段累积保留。
- `temporary_marks`——临时高亮、箭头、括号，阶段结束前清理。

```python
self.context_anchor = VGroup()
self.current_stage = VGroup()
self.conclusion_chain = VGroup()
self.temporary_marks = VGroup()
```

**阶段切换**：对 `current_stage` 整体退出，不要逐个对象记忆。正式结论在退出前移到 `conclusion_chain`：

```python
self.current_stage.remove(conclusion)
self.conclusion_chain.add(conclusion)
self.conclusion_chain.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
self.conclusion_chain.next_to(self.context_anchor, DOWN, buff=0.3, aligned_edge=LEFT)
self.play(
    FadeOut(self.current_stage),
    conclusion.animate.move_to(self.conclusion_chain[-1]),
)
self.current_stage = next_stage
```

**"整体退出"不等于"全部消失"。** 每个阶段的正式结论必须在退出前移到留痕区，保持**可读大小**。只有试算草稿、临时标记才真正消失。

临时标记在创建时注册，阶段切换前统一清理：

```python
focus_box = SurroundingRectangle(expression, color=YELLOW)
self.temporary_marks.add(focus_box)
self.play(Create(focus_box))

# 阶段切换前
self.play(FadeOut(self.temporary_marks))
self.temporary_marks = VGroup()
```

#### 移入 conclusion_chain 的三个必要步骤

1. **先从 `current_stage` 移除，再加入 `conclusion_chain`**——不移除就 FadeOut，结论会一起消失：

```python
# 错 — conclusion 仍在 current_stage 里，FadeOut 会连它一起消掉
self.conclusion_chain.add(conclusion)
self.play(FadeOut(self.current_stage))

# 对 — 先移除再重新归属
self.current_stage.remove(conclusion)
self.conclusion_chain.add(conclusion)
self.play(FadeOut(self.current_stage))
```

2. **阶段仍须完成切换**——移走结论后，剩余的 `current_stage` 仍要 FadeOut。

3. **新结论不能和已有 `conclusion_chain` 成员重叠**——每次加入后重排：

```python
self.conclusion_chain.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
self.conclusion_chain.to_edge(LEFT, buff=0.6).shift(UP * 0.5)
```

#### 阶段内局部 FadeOut 不等于切换

阶段内为教学效果 FadeOut 个别元素不算阶段切换。阶段切换是 `current_stage` 整体退场的那个点：

```python
# 阶段内教学效果——不算切换
self.play(FadeOut(old_derivation))
self.play(FadeIn(answer_block))

# 真正的阶段切换——必须在下一阶段开始前完成
self.current_stage.remove(answer_block)
self.conclusion_chain.add(answer_block)
self.play(FadeOut(self.current_stage))
self.current_stage = VGroup()
```

#### 上下文锚点生命周期

完整上下文是展示态，不是永久覆盖。推进开始前缩小为锚点：

```python
self.context_anchor = full_context
self.play(self.context_anchor.animate.scale(0.55).to_edge(UP, buff=0.3))
```

锚点的位置由内容的空间结构决定，放在不干扰主要推进区域的地方。展示时**逐条件/逐要素显示**，不要一次性出画面。

#### 左右分区

当内容需要同时展示上下文和推导时，可以采用左右分区：

```python
from manim import config

LEFT_X_MIN = -config.frame_width / 2 + 1.6
LEFT_X_MAX = 0
RIGHT_X_MIN = 0
RIGHT_X_MAX = config.frame_width / 2 - 1.6

def fit_in_right_workspace(stage, margin=1.6, min_scale=0.6):
    top = config.frame_height / 2 - margin
    bottom = -config.frame_height / 2 + margin
    max_width = RIGHT_X_MAX - RIGHT_X_MIN
    max_height = top - bottom
    scale_factor = min(max_width / stage.width, max_height / stage.height, 1.0)
    if scale_factor < min_scale:
        raise ValueError("stage too small to read; split it instead")
    if scale_factor < 1.0:
        stage.scale(scale_factor)
    stage.move_to([(RIGHT_X_MIN + RIGHT_X_MAX) / 2, (top + bottom) / 2, 0])
    return stage
```

#### 总结是重新编排，不是另起一页

```python
self.play(FadeOut(self.current_stage), FadeOut(self.temporary_marks))
summary = VGroup(
    self.context_anchor, *self.conclusion_chain, final_answer, takeaway
).arrange(DOWN, buff=0.3)
max_w = config.frame_width - 3.2
max_h = config.frame_height - 3.2
sf = min(max_w / summary.width, max_h / summary.height, 1.0)
if sf < 0.65:
    raise ValueError("summary too small; split into two cue-driven states")
if sf < 1.0:
    summary.scale(sf)
summary.move_to(ORIGIN)
self.current_stage = summary
```

#### 先排版再用 cue 逐步显示

```python
stage = VGroup(line1, line2, conclusion).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
self.current_stage = stage

audio.wait_for_cue("show_line1")
self.play(Write(line1))
audio.wait_for_cue("show_line2")
self.play(TransformMatchingTex(line1.copy(), line2))
audio.wait_for_cue("show_conclusion")
self.play(FadeIn(conclusion))
```

### 多场景画布模式

每个场景有自己的画面，场景间通过交接保持连贯。适合多阶段、多角度、需要不同视觉载体的内容。

#### 场景间交接规范

- 全片共享一个清晰专属的**视觉世界**：主体身份、变换词汇、状态接力、空间规则、色彩语义保持一致。
- 转场表达前后关系：能连续就连续（同一对象从旧状态变换到新状态），淡入淡出仅作兜底。
- 每个场景的结果是下个场景的输入——场景之间不能是平行的几块。

#### 场景完成度约束

每个场景都要同时满足：

- 旁白完成「提问 → 引导观察 → 揭示 → 命名」完整一拍
- 写得出多步可追踪的状态变化，并有对应实现代码
- 有明确的状态交接（这个场景的结果成为下个场景的输入）

达不到就与相邻场景合并——那个场景是在凑数。

**实测反例**：10 个场景那条片旁白 486 字、8 个场景那条 537 字——多出来的场景没带来更多内容，只是把同样的内容摊薄成「标题加要点加一次淡入」。

---

## 特定内容形态的额外要求

### 数据密集型内容

- 保留单位、方向、尺度、基线或归一化的含义，不要为了好看而截断坐标轴。
- 数据的来源和口径要交代，没有来源就不做数量声明。
- 不要用「炫」的图表类型掩盖数据本身很单薄的事实——数据少就直接展示数据，不要堆装饰。
- 数据在变时，让**同一个图元**连续变化，不要每帧重画一张新图。

### 流程与系统型内容

- 节点和连线的语义要固定：同一种颜色、形状在全片表示同一类东西。
- 不要一次性铺开整张图再逐个高亮——那是静态图加聚光灯。让图**长出来**，按数据或控制流的实际顺序。
- 有反馈回路时，把回路真正走一遍，让人看见"绕回来"这件事。

### 推导密集型内容

- 在上下文旁边或下方的空白区域逐步写出公式和变换，视线自然跟住。
- 每步得出关键结论后用框线或高亮标记，然后缩小移到画面边缘保持可读。
- 还有空间就继续往下写——**只有写不下时才擦掉草稿腾空间**。
- 新内容出现在离上一步最近的空白位置，不要从画面的不同角落冒出来。
- 推导结束时框出最终结论。

---

## 质量守卫

### 三个自检

对每个核心场景执行：

- **静音测试**：关掉旁白，画面本身能不能让人看懂主要关系？
- **定格测试**：随便停在一秒，能不能指着某个对象说「它正在变成……」？
- **讲义测试**：如果把这个场景印成一张纸，它比一段文字多提供了什么？

任一条不过，回到视觉设计阶段重做这个场景——不要用更多元素、更长旁白或更好的配色来补偿。

### 篇幅自查

按中文讲解约 5.3 字/秒估算。**这是自查信号，不是及格线。**

某段明显偏短时问自己：是这一拍确实只需要一句话，还是漏了提问、漏了引导观察、漏了解释为什么？是后者就补，是前者就留着。

内容确实不够时**优先加深已有场景的讲解层次**（多一个中间步骤、多一次对照、多一句为什么），而不是新增场景或拉长句子。注水（复述画面文字、空泛感叹、为长而长）不算篇幅。

**取舍要双向做**：既删注水，也补缺口。TTS 是付费且耗时的，合成前一次性写足，不要合成之后再为补内容整批重跑。

---

## 常用工具速查

按教学场景分类。完整目录见 `manim-animations.md`。

**动画**

| 场景 | 推荐 |
|---|---|
| 板书书写 | `Write`、`Create`、`DrawBorderThenFill`、`AddTextLetterByLetter` |
| 公式推导变换 | `TransformMatchingTex`、`ReplacementTransform`、`Transform`、`TransformFromCopy`、`FadeTransform` |
| 焦点强调 | `Indicate`、`Circumscribe`、`Flash`、`FocusOn`、`Wiggle`、`ShowPassingFlash` |
| 出入场 | `FadeIn`、`FadeOut`、`GrowFromCenter`、`GrowFromEdge`、`ShrinkToCenter` |
| 旋转与路径 | `Rotate`、`MoveAlongPath`、`Homotopy` |
| 编排控制 | `AnimationGroup`、`LaggedStart`、`Succession`、`ChangeSpeed` |
| 数值动态 | `ChangeDecimalToValue`、`UpdateFromFunc`、`UpdateFromAlphaFunc` |

**对象**

| 类别 | 可用 |
|---|---|
| 文字 | `Text`（中文必须 `font=CJK_FONT`）、`MarkupText`、`Paragraph` |
| 公式 | `MathTex`（数学模式，支持 `{{ }}` 拆分和 `tex_to_color_map`）、`Tex`（文本模式） |
| 基础图形 | `Circle`、`Square`、`Rectangle`、`Polygon`、`Triangle`、`Dot`、`Ellipse` |
| 线与箭头 | `Line`、`DashedLine`、`Arrow`、`DoubleArrow`、`CurvedArrow`、`Vector` |
| 标注 | `SurroundingRectangle`、`Brace`、`BraceLabel`、`Underline`、`Cross` |
| 几何标注 | `Angle`、`RightAngle`、`Arc` |
| 函数与坐标 | `Axes`、`NumberPlane`、`NumberLine`、`FunctionGraph`、`ParametricFunction` |
| 表格与矩阵 | `Table`、`MathTable`、`Matrix`、`BarChart` |
| 3D | `ThreeDAxes`、`Surface`、`ThreeDScene` |

**接口**

| 接口 | 用途 |
|---|---|
| `.animate` | 链式属性动画：`mob.animate.shift(RIGHT).scale(1.5)` |
| `always_redraw` | 每帧重建：`line = always_redraw(lambda: Line(a, b))` |
| `ValueTracker` | 数值驱动 + updater |
| `tex_to_color_map` | 公式着色：`MathTex(..., tex_to_color_map={"x": RED})` |
| `{{ }}` | 公式拆分：`MathTex(r"{{ a^2 }} + {{ b^2 }}")` |
| `MovingCameraScene` | 相机控制基类，支持 zoom/pan |
