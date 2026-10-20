# ManimCE Objects: Text, Math, Graphs, 3D

The `Text` class renders text using Pango/Cairo, supporting various fonts and styles.

## Basic Text

```python
from manim import *

class TextExample(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
```

## Text Parameters

```python
text = Text(
    "Hello World",
    font_size=48,           # Size (default: 48)
    color=BLUE,             # Text color
    font="Arial",           # Font family
    weight=BOLD,            # NORMAL, BOLD, etc.
    slant=ITALIC,           # NORMAL, ITALIC, OBLIQUE
    line_spacing=1.5,       # Space between lines
)
```

## Font Size

```python
# Using font_size parameter
small = Text("Small", font_size=24)
medium = Text("Medium", font_size=48)
large = Text("Large", font_size=72)

# Using scale after creation
text = Text("Hello").scale(2)
```

## Custom Fonts

```python
# Use any installed system font
text = Text("Custom Font", font="Comic Sans MS")
text = Text("Monospace", font="Courier New")
text = Text("Serif", font="Times New Roman")
```

## Text Styling with MarkupText

Use Pango markup for mixed styling within one Text object:

```python
class MarkupExample(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>',
            color=RED
        )
        self.play(Write(text))
```

### Available Markup Tags

```python
# Bold and italic
text = MarkupText('<b>Bold</b> and <i>Italic</i>')

# Colors using fgcolor
text = MarkupText('<span fgcolor="yellow">Yellow</span>')

# Subscripts and superscripts
text = MarkupText('H<sub>2</sub>O and x<sup>2</sup>')

# Font size
text = MarkupText('<big>Big</big> and <small>small</small>')

# Underline and strikethrough
text = MarkupText('<u>Underline</u> and <s>Strike</s>')

# Double underline with color
text = MarkupText('<span underline="double" underline_color="green">text</span>')

# Monospace
text = MarkupText('type <tt>help</tt> for help')
```

### Gradients in MarkupText

```python
# Global gradient
text = MarkupText("nice gradient", gradient=(BLUE, GREEN))

# Inline gradient
text = MarkupText(
    'nice <gradient from="RED" to="YELLOW">colored</gradient> text'
)
```

### Escaping Special Characters

```python
# Must escape these characters:
# > as &gt;
# < as &lt;
# & as &amp;
text = MarkupText("5 &gt; 3 and 2 &lt; 4")
```

## Multi-line Text

```python
# Using \n for line breaks
text = Text("Line 1\nLine 2\nLine 3")

# Using Paragraph for better control
from manim import Paragraph

para = Paragraph(
    "This is a longer text",
    "that spans multiple lines",
    "with automatic alignment",
    line_spacing=0.5
)
```

## Coloring Parts of Text

```python
class ColoredText(Scene):
    def construct(self):
        text = Text("Hello World")
        text[0:5].set_color(RED)    # "Hello" in red
        text[6:11].set_color(BLUE)  # "World" in blue
        self.play(Write(text))
```

## Text with Gradients

```python
text = Text("Gradient Text")
text.set_color_by_gradient(RED, YELLOW, GREEN)
```

## Accessing Characters

```python
text = Text("ABCDE")

# Individual characters
text[0]  # 'A'
text[1]  # 'B'

# Slices
text[0:3]  # 'ABC'
text[-1]   # 'E'

# Iterate
for char in text:
    char.set_color(random_color())
```

## Text Positioning

```python
# Standard positioning methods work
text = Text("Hello")
text.to_edge(UP)
text.to_corner(UL)
text.move_to(ORIGIN)
text.next_to(other_mobject, DOWN)
```

## Best Practices

1. **Use Text for regular text** - Simple and fast
2. **Use MarkupText for mixed styles** - When you need multiple colors/weights
3. **Use MathTex for math** - Text doesn't render LaTeX
4. **Install fonts system-wide** - Manim uses system fonts
5. **Keep font_size consistent** - Use the same size for related text


# LaTeX in Manim

Manim uses LaTeX to render mathematical expressions and formatted text.

## MathTex vs Tex

- **MathTex**: Automatically wraps content in math mode (`align*` environment)
- **Tex**: Raw LaTeX - you control the mode

```python
from manim import *

class LaTeXComparison(Scene):
    def construct(self):
        # MathTex - auto math mode
        math = MathTex(r"E = mc^2")

        # Tex - need explicit math delimiters
        tex = Tex(r"$E = mc^2$")

        # Both render the same
        VGroup(math, tex).arrange(DOWN)
        self.add(math, tex)
```

## Basic MathTex

```python
class MathTexExample(Scene):
    def construct(self):
        # Simple equation
        eq1 = MathTex(r"x^2 + y^2 = z^2")

        # Fractions
        eq2 = MathTex(r"\frac{a}{b}")

        # Square roots
        eq3 = MathTex(r"\sqrt{2}")

        # Greek letters
        eq4 = MathTex(r"\alpha + \beta = \gamma")

        # Integrals
        eq5 = MathTex(r"\int_0^\infty e^{-x} dx")

        # Summations
        eq6 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2}")

        equations = VGroup(eq1, eq2, eq3, eq4, eq5, eq6).arrange_in_grid(2, 3)
        self.add(equations)
```

## Coloring Parts of Equations

### Using set_color_by_tex

```python
class ColoredEquation(Scene):
    def construct(self):
        eq = MathTex(r"e^{i\pi} + 1 = 0")
        eq.set_color_by_tex("e", RED)
        eq.set_color_by_tex(r"\pi", BLUE)
        eq.set_color_by_tex("i", GREEN)
        self.add(eq)
```

### Double-Brace `{{ }}` Syntax for TransformMatchingTex

Enclose parts of a formula with double braces to split it into matchable
substrings automatically. This is the simplest way to prepare equations for
`TransformMatchingTex`.

```python
class DoubleBraceExample(Scene):
    def construct(self):
        eq1 = MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")
        eq2 = MathTex(r"{{ a^2 }} = {{ c^2 }} - {{ b^2 }}")

        self.play(Write(eq1))
        self.play(TransformMatchingTex(eq1, eq2))
```

The rendered mobject splits into substrings `a^2`, `+`, `b^2`, `=`, `c^2`.
Matching substrings animate into their new positions; unmatched parts fade
in or out.

**Rules:**
- `{{` must appear at the start of the string or after whitespace to be
  treated as a group opener
- `{{` directly after non-whitespace LaTeX (e.g., `\frac{{{n}}}{k}`) is
  left untouched — ordinary nested braces are not affected
- To prevent a leading `{{` from splitting, insert a space: `{ { ... } }`

For derivation chains, this is usually more readable than multi-argument
`MathTex("a^2", "+", "b^2", "=", "c^2")` or `substrings_to_isolate`.

### Using substrings_to_isolate

For precise coloring, isolate substrings first:

```python
class IsolatedColoring(Scene):
    def construct(self):
        eq = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2}x^2 + \cdots",
            substrings_to_isolate=["x"]
        )
        eq.set_color_by_tex("x", YELLOW)
        self.add(eq)
```

### Using index_labels for debugging

```python
class DebugLabels(Scene):
    def construct(self):
        eq = MathTex(r"\frac{a}{b}")
        # Add index labels to see which index is which part
        self.add(index_labels(eq[0]))
        self.add(eq)
```

### Direct indexing

```python
eq = MathTex(r"a + b = c")
eq[0][0].set_color(RED)   # 'a'
eq[0][2].set_color(BLUE)  # 'b'
eq[0][4].set_color(GREEN) # 'c'
```

## Multi-part Equations

Split equations into parts for individual control:

```python
class MultiPartEquation(Scene):
    def construct(self):
        eq = MathTex("a", "^2", "+", "b", "^2", "=", "c", "^2")

        eq[0].set_color(RED)    # a
        eq[3].set_color(BLUE)   # b
        eq[6].set_color(GREEN)  # c

        self.play(Write(eq))
```

## Text with Math (Tex)

```python
class MixedContent(Scene):
    def construct(self):
        # Mix text and math
        tex = Tex(r"The area is $A = \pi r^2$")
        self.play(Write(tex))
```

## Custom LaTeX Packages

```python
class CustomPackage(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{mathrsfs}")

        eq = Tex(
            r"$\mathscr{L}$",
            tex_template=template
        )
        self.add(eq)
```

## Equation Alignment

```python
class AlignedEquations(Scene):
    def construct(self):
        eqs = MathTex(
            r"a &= b + c \\",
            r"d &= e + f + g \\",
            r"h &= i"
        )
        self.add(eqs)
```

## Common LaTeX Symbols

```python
# Greek letters
MathTex(r"\alpha \beta \gamma \delta \epsilon")
MathTex(r"\Gamma \Delta \Theta \Lambda \Pi")

# Operators
MathTex(r"\times \div \pm \mp \cdot")

# Relations
MathTex(r"\leq \geq \neq \approx \equiv")

# Arrows
MathTex(r"\rightarrow \leftarrow \Rightarrow \Leftrightarrow")

# Sets
MathTex(r"\in \notin \subset \supset \cup \cap")

# Calculus
MathTex(r"\int \iint \oint \partial \nabla")
```

## Font Size

```python
# Using font_size parameter
eq = MathTex(r"E = mc^2", font_size=72)

# Using scale
eq = MathTex(r"E = mc^2").scale(2)
```

## Best Practices

1. **Use raw strings** - Always use `r"..."` for LaTeX
2. **Use MathTex for pure math** - Simpler than adding `$...$`
3. **Use Tex for mixed content** - When combining text and math
4. **Split for animation control** - Separate parts you'll animate differently
5. **Use substrings_to_isolate** - For reliable coloring of repeated elements

## Project Conventions

### Chinese Text Never Goes Into MathTex

LaTeX rejects CJK characters without a CJK-aware template. Verified failing on
ManimCE 0.21.0: `MathTex(r"\text{旋度}")` raises a Unicode character error.

Descriptive labels — Chinese or English — belong in `Text()`. `MathTex` carries
only mathematical notation. Combine them with `VGroup` or `next_to`.

```python
label = Text("旋度", font=CJK_FONT)
formula = MathTex(R"\nabla\times\vec{F}")
VGroup(label, formula).arrange(RIGHT, buff=0.3)
```

The runtime's `SafeMathTex` raises early on this mistake so it surfaces before
rendering rather than during LaTeX compilation.

### Raw Strings for Every Formula

Write formula literals as raw strings so Python passes each backslash through
unchanged. Commands such as `\vec`, `\frac`, `\theta`, and `\nabla` begin with
sequences an ordinary Python string may interpret as control characters.

```python
MathTex(R"\frac{a}{b}")
MathTex(R"\vec{v}")
MathTex(r"\theta = \frac{\pi}{3}")
MathTex("\\frac{a}{b}")
```

When LaTeX fails, read the first compiler error and inspect the exact string
passed in. Check Python escaping, brace balance, and the text/math boundary.
Do not replace valid mathematical operators merely because a later internal
LaTeX macro appears in the error message.

### Coloring Uses tex_to_color_map

ManimCE's `MathTex` has no `t2c` parameter — that name belongs to `Text`.

```python
MathTex(R"E = mc^2", tex_to_color_map={"E": BLUE, "m": GREEN})
Text("旋度", font=CJK_FONT, t2c={"旋": YELLOW})
```

### No Markdown Delimiters

`$...$` and `$$...$$` belong to Markdown and web text. They render literally
inside `Text()` and are redundant inside `MathTex()`.

### tex_to_color_map 不能用于上下标内的符号

`tex_to_color_map` 在匹配时向 TeX 源码注入 dvisvgm 标记。当目标子串
出现在上下标位置（如 `^\infty`）时，注入的标记破坏 LaTeX 语法导致编译
失败。对这类符号改用 `set_color_by_tex`（构造后调用，不会注入标记）。

```python
# 错 — \infty 在 ^{} 内，tex_to_color_map 注入标记后 LaTeX 报错
eq = MathTex(r"\int_0^\infty e^{-x} dx = 1",
             tex_to_color_map={r"\infty": YELLOW})

# 对 — 构造后用 set_color_by_tex
eq = MathTex(r"\int_0^\infty e^{-x} dx = 1")
eq.set_color_by_tex(r"\infty", YELLOW)
```

### Brace.get_text() 不能传中文

`Brace.get_text()` 内部走 `Tex()` 渲染，中文字符会导致 LaTeX Unicode
错误。中文标签用 `Text(font=CJK_FONT)` 创建后手动 `next_to(brace)` 定位。

```python
# 错 — get_text 走 LaTeX，中文报错
brace_label = brace.get_text("底边 = 4")

# 对 — 用 Text + next_to
brace_label = Text("底边 = 4", font=CJK_FONT, font_size=24).next_to(brace, DOWN, buff=0.1)
```

### MovingCameraScene 必须先 save_state 才能 Restore

`Restore(self.camera.frame)` 要求目标对象此前调用过 `save_state()`。
MovingCameraScene 的 camera.frame 不会自动保存初始状态。

```python
# 必须在变换前显式保存
self.camera.frame.save_state()
self.play(self.camera.frame.animate.scale(0.5).move_to(target))
# 之后才能恢复
self.play(Restore(self.camera.frame))
```


# Coordinate Systems

Create axes, grids, and number lines for mathematical visualizations.

## Axes

Basic 2D coordinate axes.

```python
from manim import *

class AxesExample(Scene):
    def construct(self):
        # Default axes
        axes = Axes()
        self.add(axes)
```

### Customizing Axes

```python
class CustomAxes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],      # [min, max, step]
            y_range=[-3, 3, 1],
            x_length=10,              # Physical length on screen
            y_length=6,
            axis_config={
                "color": BLUE,
                "include_tip": True,
                "include_numbers": True,
            },
            x_axis_config={
                "numbers_to_include": [-4, -2, 0, 2, 4],
            },
            y_axis_config={
                "numbers_to_include": [-2, 0, 2],
            },
        )
        self.add(axes)
```

### Adding Labels

```python
class AxesLabels(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5], y_range=[-3, 3])

        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Custom labels
        x_label = axes.get_x_axis_label(MathTex(r"\theta"))
        y_label = axes.get_y_axis_label(MathTex(r"f(\theta)"))

        self.add(axes, x_label, y_label)
```

## NumberPlane

Grid with axes - shows coordinate lines.

```python
class NumberPlaneExample(Scene):
    def construct(self):
        # Default plane
        plane = NumberPlane()
        self.add(plane)
```

### Customizing NumberPlane

```python
class CustomPlane(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            axis_config={
                "color": WHITE,
            },
        )
        self.add(plane)
```

## ComplexPlane

For visualizing complex numbers.

```python
class ComplexPlaneExample(Scene):
    def construct(self):
        plane = ComplexPlane()

        # Plot complex number
        z = complex(2, 1)  # 2 + i
        dot = Dot(plane.n2p(z), color=YELLOW)
        label = MathTex("2+i").next_to(dot, UR)

        self.add(plane, dot, label)
```

## NumberLine

Single axis line.

```python
class NumberLineExample(Scene):
    def construct(self):
        line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_numbers=True,
            include_tip=True,
        )
        self.add(line)
```

## Coordinate Conversions

```python
class CoordinateConversion(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5], y_range=[-3, 3])

        # Convert coordinates to screen position
        point = axes.c2p(2, 1)  # coords_to_point: (2, 1) -> screen position

        # Convert screen position to coordinates
        coords = axes.p2c(point)  # point_to_coords: screen -> (x, y)

        dot = Dot(point, color=RED)
        self.add(axes, dot)
```

### Shorthand Methods

```python
axes = Axes()

# c2p = coords_to_point
axes.c2p(x, y)

# p2c = point_to_coords
axes.p2c(point)

# i2gp = input_to_graph_point (for graphs)
axes.i2gp(x, graph)

# For NumberPlane/ComplexPlane
plane.n2p(complex_number)  # number_to_point
plane.p2n(point)           # point_to_number
```

## ThreeDAxes

For 3D visualizations.

```python
class ThreeDAxesExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=6,
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)
```

## Plotting Points

```python
class PlotPoints(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5], y_range=[-3, 3])

        points = [(1, 2), (-2, 1), (3, -1), (0, 2)]
        dots = VGroup(*[
            Dot(axes.c2p(x, y), color=YELLOW)
            for x, y in points
        ])

        self.add(axes, dots)
```

## Best Practices

1. **Set appropriate ranges** - Don't include unnecessary empty space
2. **Match x_length/y_length to range ratio** - Prevents distortion
3. **Use NumberPlane for transformations** - Grid shows distortion clearly
4. **Use c2p for all coordinate work** - Don't manually convert
5. **Include numbers sparingly** - Too many numbers clutter the display


# Graphing Functions

Plot mathematical functions and curves.

## Plotting Functions on Axes

```python
from manim import *

class BasicPlot(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 8])

        # Plot a function
        graph = axes.plot(lambda x: x**2, color=BLUE)

        self.add(axes, graph)
```

## plot() Parameters

```python
class PlotParameters(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5], y_range=[-2, 2])

        graph = axes.plot(
            lambda x: np.sin(x),
            x_range=[-PI, PI],    # Limit domain
            color=YELLOW,
            stroke_width=4,
        )

        self.add(axes, graph)
```

## Multiple Functions

```python
class MultiplePlots(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 10])

        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        quad_graph = axes.plot(lambda x: x**2, color=GREEN)

        self.add(axes, sin_graph, cos_graph, quad_graph)
```

## Adding Labels to Graphs

```python
class GraphLabels(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 10])
        graph = axes.plot(lambda x: x**2, color=BLUE)

        # Add label to graph
        label = axes.get_graph_label(
            graph,
            label=MathTex("y = x^2"),
            x_val=2,
            direction=UR
        )

        self.add(axes, graph, label)
```

## Parametric Curves

Plot curves defined by parametric equations.

```python
class ParametricExample(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-3, 3])

        # Circle: x = cos(t), y = sin(t)
        curve = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2 * PI],
            color=YELLOW
        )

        self.add(axes, curve)
```

### Parametric Curve Examples

```python
# Lissajous curve
curve = axes.plot_parametric_curve(
    lambda t: np.array([np.sin(3*t), np.sin(2*t), 0]),
    t_range=[0, 2*PI],
)

# Spiral
curve = axes.plot_parametric_curve(
    lambda t: np.array([t*np.cos(t), t*np.sin(t), 0]),
    t_range=[0, 4*PI],
)

# Heart curve
curve = axes.plot_parametric_curve(
    lambda t: np.array([
        16 * np.sin(t)**3,
        13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t),
        0
    ]) / 10,
    t_range=[0, 2*PI],
)
```

## ParametricFunction (standalone)

Create parametric curves without axes:

```python
class StandaloneParametric(Scene):
    def construct(self):
        curve = ParametricFunction(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=BLUE
        )
        self.add(curve)
```

## Area Under Curve

```python
class AreaUnderCurve(Scene):
    def construct(self):
        axes = Axes(x_range=[-1, 5], y_range=[-1, 10])
        graph = axes.plot(lambda x: x**2, x_range=[0, 3], color=BLUE)

        # Shade area under curve
        area = axes.get_area(
            graph,
            x_range=[0, 2],
            color=BLUE,
            opacity=0.5
        )

        self.add(axes, graph, area)
```

## Riemann Rectangles

```python
class RiemannRectangles(Scene):
    def construct(self):
        axes = Axes(x_range=[-1, 5], y_range=[-1, 10])
        graph = axes.plot(lambda x: x**2, color=BLUE)

        rects = axes.get_riemann_rectangles(
            graph,
            x_range=[0, 3],
            dx=0.5,
            color=YELLOW,
            stroke_width=1
        )

        self.add(axes, graph, rects)
```

## Animated Graphing

```python
class AnimatedGraph(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
        self.add(axes)

        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        # Animate the graph being drawn
        self.play(Create(graph), run_time=3)
```

## Moving Point on Graph

```python
class MovingPointOnGraph(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        # Point that follows graph
        x_tracker = ValueTracker(-3)

        dot = always_redraw(lambda: Dot(
            axes.i2gp(x_tracker.get_value(), graph),
            color=YELLOW
        ))

        self.add(axes, graph, dot)
        self.play(x_tracker.animate.set_value(3), run_time=4)
```

## 3D Surface Plots

```python
class SurfacePlot(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        surface = axes.plot_surface(
            lambda u, v: np.sin(u) * np.cos(v),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            colorscale=[BLUE, GREEN, YELLOW],
        )

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes, surface)
```

## Best Practices

1. **Set x_range on plot for discontinuities** - Avoid graphing undefined regions
2. **Use get_graph_label for clarity** - Label functions on the graph
3. **Match graph color to concept** - Consistent color coding
4. **Use i2gp for points on graphs** - Automatically handles conversion
5. **Animate graph creation** - More engaging than static display

`Create` is especially useful when the drawing direction, domain progression, or buildup is part of the explanation. Add or fade in the completed graph when construction order carries no information and the viewer needs to inspect the full shape immediately.


# 3D Graphics in Manim

Create 3D visualizations with ThreeDScene.

## ThreeDScene Basics

```python
from manim import *

class Basic3D(ThreeDScene):
    def construct(self):
        # Set camera angle
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Add 3D axes
        axes = ThreeDAxes()
        self.add(axes)
```

## Camera Orientation

```python
class CameraOrientation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        # phi: angle from z-axis (0 = top view, 90 = side view)
        # theta: rotation around z-axis
        # gamma: roll angle

        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=-45 * DEGREES,
            gamma=0
        )

        self.add(axes)
```

### Animated Camera Movement

```python
class AnimatedCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=0)

        # Animate camera movement
        self.move_camera(phi=45*DEGREES, theta=90*DEGREES, run_time=3)
```

### Continuous Camera Rotation

```python
class RotatingCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=0)

        # Start ambient rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
```

## 3D Primitives

### Sphere

```python
class SphereExample(ThreeDScene):
    def construct(self):
        sphere = Sphere(radius=1, resolution=(20, 20))
        sphere.set_color(BLUE)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(sphere)
```

### Cube / Prism

```python
class CubeExample(ThreeDScene):
    def construct(self):
        cube = Cube(side_length=2, fill_opacity=0.8)
        cube.set_color(RED)

        # Rectangular prism
        prism = Prism(dimensions=[3, 1, 2])

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(cube)
```

### Cylinder / Cone

```python
class CylinderCone(ThreeDScene):
    def construct(self):
        cylinder = Cylinder(radius=1, height=2, fill_opacity=0.8)
        cone = Cone(base_radius=1, height=2, fill_opacity=0.8)

        cylinder.shift(LEFT * 2)
        cone.shift(RIGHT * 2)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(cylinder, cone)
```

### Torus

```python
class TorusExample(ThreeDScene):
    def construct(self):
        torus = Torus(major_radius=2, minor_radius=0.5)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(torus)
```

## 3D Axes

```python
class ThreeDAxesExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=6,
        )

        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("z")

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes, x_label, y_label, z_label)
```

## Surface Plots

```python
class SurfacePlot(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-2, 2])

        # Function z = f(x, y)
        surface = axes.plot_surface(
            lambda u, v: np.sin(u) * np.cos(v),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            colorscale=[BLUE, GREEN, YELLOW, RED],
        )

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes, surface)
```

### Surface Class (standalone)

```python
class SurfaceExample(ThreeDScene):
    def construct(self):
        def param_func(u, v):
            x = u
            y = v
            z = np.sin(np.sqrt(u**2 + v**2))
            return np.array([x, y, z])

        surface = Surface(
            param_func,
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_opacity=0.8,
        )
        surface.set_color_by_gradient(BLUE, GREEN)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(surface)
```

## 3D Parametric Curves

```python
class ParametricCurve3D(ThreeDScene):
    def construct(self):
        # Helix
        curve = ParametricFunction(
            lambda t: np.array([
                np.cos(t),
                np.sin(t),
                t * 0.2
            ]),
            t_range=[-4*PI, 4*PI],
            color=YELLOW
        )
        curve.set_shade_in_3d(True)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(ThreeDAxes(), curve)
```

## Shading in 3D

```python
class Shading3D(ThreeDScene):
    def construct(self):
        sphere = Sphere()

        # Enable shading for realistic lighting
        sphere.set_shade_in_3d(True)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(sphere)
```

## Arrow3D and Line3D

```python
class Vectors3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        arrow = Arrow3D(ORIGIN, [2, 1, 2], color=RED)
        line = Line3D(ORIGIN, [-2, 1, 1], color=BLUE)

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.add(axes, arrow, line)
```

## Best Practices

1. **Always set camera orientation** - Default view may not show 3D well
2. **Use set_shade_in_3d for realism** - Adds depth perception
3. **Use ambient camera rotation sparingly** - Can be disorienting
4. **Match resolution to detail needed** - Higher res = slower render
5. **Use colorscale for surfaces** - Shows elevation/value changes

Shading and camera movement are depth cues, not goals by themselves. Use them when they make orientation, curvature, occlusion, or spatial relationships easier to judge; use a simpler view when surface realism competes with labels or exact geometry.


# Camera Control

Control what the viewer sees with camera manipulation.

## MovingCameraScene

For 2D scenes with camera movement (zoom, pan).

```python
from manim import *

class CameraExample(MovingCameraScene):
    def construct(self):
        circle = Circle()
        square = Square().shift(RIGHT * 3)
        self.add(circle, square)

        # Access camera frame
        # self.camera.frame is the viewable area
```

## Zooming

### Zoom In/Out by Scaling Frame

```python
class ZoomExample(MovingCameraScene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(100)])
        dots.arrange_in_grid(10, 10, buff=0.3)
        self.add(dots)

        # Zoom in (make frame smaller)
        self.play(self.camera.frame.animate.scale(0.5))
        self.wait()

        # Zoom out (make frame larger)
        self.play(self.camera.frame.animate.scale(4))
```

### Zoom to Specific Width

```python
class ZoomToWidth(MovingCameraScene):
    def construct(self):
        text = Text("Focus on me!")
        self.add(text)

        # Zoom to fit text with padding
        self.play(
            self.camera.frame.animate.set(width=text.width * 1.5)
        )
```

## Panning

### Move Camera to Location

```python
class PanExample(MovingCameraScene):
    def construct(self):
        c1 = Circle().shift(LEFT * 3)
        c2 = Circle().shift(RIGHT * 3)
        self.add(c1, c2)

        # Pan to first circle
        self.play(self.camera.frame.animate.move_to(c1))
        self.wait()

        # Pan to second circle
        self.play(self.camera.frame.animate.move_to(c2))
```

### Combined Zoom and Pan

```python
class ZoomAndPan(MovingCameraScene):
    def construct(self):
        square = Square().shift(LEFT * 2)
        triangle = Triangle().shift(RIGHT * 2)
        self.add(square, triangle)

        # Zoom in and pan simultaneously
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(square)
        )
        self.wait()

        # Move to triangle (still zoomed)
        self.play(self.camera.frame.animate.move_to(triangle))
```

## Save and Restore Camera State

```python
class SaveRestoreCamera(MovingCameraScene):
    def construct(self):
        circle = Circle()
        self.add(circle)

        # Save current state
        self.camera.frame.save_state()

        # Make changes
        self.play(self.camera.frame.animate.scale(0.3).move_to(circle))
        self.wait()

        # Restore to saved state
        self.play(Restore(self.camera.frame))
```

## auto_zoom

Automatically zoom to fit mobjects.

```python
class AutoZoomExample(MovingCameraScene):
    def construct(self):
        squares = VGroup(*[
            Square().shift(RIGHT * i + UP * j)
            for i in range(-2, 3) for j in range(-2, 3)
        ])
        self.add(squares)

        # Zoom to fit specific mobject
        self.play(self.camera.auto_zoom(squares[0]))
        self.wait()

        # Zoom to fit all with margin
        self.play(self.camera.auto_zoom(squares, margin=1))
```

## 3D Camera (ThreeDScene)

```python
class ThreeDCameraExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere()
        self.add(axes, sphere)

        # Set initial camera orientation
        self.set_camera_orientation(
            phi=75 * DEGREES,    # Angle from z-axis
            theta=-45 * DEGREES  # Angle around z-axis
        )
```

### Animated Camera Rotation

```python
class RotatingCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES, theta=0)

        # Continuous rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
```

### Move 3D Camera

```python
class Move3DCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Animate camera movement
        self.move_camera(
            phi=45 * DEGREES,
            theta=45 * DEGREES,
            run_time=3
        )
```

## Camera Background

```python
class CameraBackground(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BLUE_E

        circle = Circle()
        self.add(circle)
```

## Best Practices

1. **Use MovingCameraScene for zoom/pan** - Regular Scene camera is static
2. **Save state before complex movements** - Easy to restore
3. **Use auto_zoom for dynamic content** - Automatically fits content
4. **Keep camera movements smooth** - Don't make viewers dizzy
5. **Use 3D camera rotation sparingly** - Can be disorienting


# 补充：函数图像与隐函数

## FunctionGraph

`FunctionGraph` 是画一元函数最常用的类，自动跨越 Axes 的 x 范围。

```python
# 在 Axes 上画函数
axes = Axes(x_range=[-3, 3], y_range=[-1, 5])
graph = axes.plot(lambda x: x**2, color=BLUE)  # 推荐：用 axes.plot
self.play(Create(axes), Create(graph))

# 独立使用（不需要坐标轴时）
func = FunctionGraph(lambda x: np.sin(x), x_range=[-PI, PI], color=YELLOW)
self.play(Create(func))

# 常用参数
graph = axes.plot(
    lambda x: x**2,
    color=BLUE,
    x_range=[-2, 2],        # 限制绘制范围
    use_smoothing=True,      # 平滑曲线（默认 True）
)

# 多条函数对比
f1 = axes.plot(lambda x: x**2, color=BLUE)
f2 = axes.plot(lambda x: x**3, color=RED)
self.play(Create(f1), Create(f2))

# 函数间面积
area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)
self.play(FadeIn(area))
```

## ImplicitFunction

隐函数图像，适合画圆锥曲线、等高线等不能写成 y=f(x) 的图形。

```python
# 椭圆 x²/4 + y²/1 = 1
ellipse = ImplicitFunction(
    lambda x, y: x**2/4 + y**2 - 1,
    color=YELLOW,
)
self.play(Create(ellipse))

# 双曲线
hyperbola = ImplicitFunction(
    lambda x, y: x**2 - y**2 - 1,
    x_range=[-4, 4], y_range=[-3, 3],
    color=RED,
)
```

## PolarPlane

极坐标系，适合螺线、玫瑰曲线等极坐标图形。

```python
polar = PolarPlane(radius_max=3)
curve = polar.plot_polar_graph(
    lambda theta: 1 + np.cos(theta),  # 心形线
    color=RED,
)
self.play(Create(polar), Create(curve))
```

## Variable

在画面上显示 "label = value" 并能动态更新。

```python
var = Variable(2, Text("x", font=CJK_FONT), num_decimal_places=1)
self.play(Write(var))
# 动态更新
tracker = var.tracker  # 内部 ValueTracker
self.play(tracker.animate.set_value(5), run_time=2)
```

# 补充：向量场与流线

## ArrowVectorField

用箭头阵列表示向量场，适合物理力场、梯度场、电磁场等。

```python
field = ArrowVectorField(
    lambda pos: np.array([pos[1], -pos[0], 0]),  # 旋转场
    x_range=[-3, 3], y_range=[-3, 3],
)
self.play(Create(field))
```

## StreamLines

用流线表示向量场的流动方向，比箭头更直观。

```python
stream = StreamLines(
    lambda pos: np.array([pos[1], -pos[0], 0]),
    stroke_width=2, max_anchors_per_line=30,
)
self.play(stream.create())  # 注意：用 .create() 而不是 Create()
```

# 补充：布尔运算

`Union`、`Intersection`、`Difference`、`Exclusion` 对 VMobject 做集合运算。

```python
circle1 = Circle(radius=1.5).shift(LEFT * 0.8)
circle2 = Circle(radius=1.5).shift(RIGHT * 0.8)

# 并集
union = Union(circle1, circle2, color=BLUE, fill_opacity=0.3)
# 交集
inter = Intersection(circle1, circle2, color=RED, fill_opacity=0.3)
# 差集
diff = Difference(circle1, circle2, color=GREEN, fill_opacity=0.3)
# 对称差
excl = Exclusion(circle1, circle2, color=YELLOW, fill_opacity=0.3)
```

# 补充：SVG 导入

```python
# 导入 SVG 文件
svg = SVGMobject("path/to/icon.svg")
svg.set_height(2)
svg.set_color(WHITE)
self.play(DrawBorderThenFill(svg))

# 访问子路径
svg[0].set_color(RED)    # 第一个子路径
svg[1].set_color(BLUE)   # 第二个子路径
```

# 补充：有向图

```python
from manim import DiGraph

vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
graph = DiGraph(vertices, edges, layout="circular")
self.play(Create(graph))

# 添加标签
labels = graph.add_labels()
```
