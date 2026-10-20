# ManimCE Basics: Scenes, Mobjects, Layout, Styling

A Scene is the canvas where all animations take place. Every Manim animation is defined within a Scene class.

## Basic Scene Structure

All animation code resides within the `construct()` method of a Scene subclass.

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)
```

## Scene Lifecycle Methods

### construct()
The main method where you define your animation. Called automatically when rendering.

### setup()
Called before `construct()`. Use for initialization that should happen before animation logic.

```python
class MyScene(Scene):
    def setup(self):
        self.camera.background_color = BLUE_E

    def construct(self):
        circle = Circle()
        self.play(Create(circle))
```

## Scene Methods

### Adding and Removing Objects

```python
# Add without animation (instant)
self.add(mobject)
self.add(mobject1, mobject2, mobject3)

# Remove without animation
self.remove(mobject)

# Clear all mobjects
self.clear()
```

### Playing Animations

```python
# Play a single animation
self.play(Create(circle))

# Play multiple animations simultaneously
self.play(Create(circle), FadeIn(square))

# With run_time
self.play(Create(circle), run_time=2)
```

### Waiting

```python
# Wait for 1 second (default)
self.wait()

# Wait for specific duration
self.wait(2)
```

## Scene Types

### Scene (Default)
Standard 2D scene for most animations.

### ThreeDScene
For 3D animations with camera orientation control.

```python
class My3DScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        sphere = Sphere()
        self.add(axes, sphere)
```

### MovingCameraScene
For animations that require camera movement (zoom, pan).

```python
class ZoomScene(MovingCameraScene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.play(self.camera.frame.animate.scale(0.5).move_to(circle))
```

## Multiple Scenes in One File

Render specific scene:
```bash
manim -pql file.py Scene1
```

Render all scenes:
```bash
manim -pql -a file.py
```


# Mobjects in Manim

Mobject (Mathematical Object) is the base class for all displayable objects in Manim.

## Mobject Hierarchy

```
Mobject (base class)
├── VMobject (Vectorized Mobject - most common)
│   ├── Circle, Square, Rectangle, Polygon
│   ├── Line, Arrow, Vector
│   ├── Text, MathTex, Tex
│   ├── Axes, NumberPlane
│   └── VGroup
├── ImageMobject (for images)
├── PMobject (point clouds)
└── Group (for non-VMobject collections)
```

## VMobject (Vectorized Mobject)

Most shapes you'll use are VMobjects - they're defined by Bézier curves.

```python
# Common VMobjects
circle = Circle()
square = Square()
rect = Rectangle(width=4, height=2)
triangle = Triangle()
polygon = Polygon(ORIGIN, RIGHT, UP)
line = Line(LEFT, RIGHT)
arrow = Arrow(LEFT, RIGHT)
```

## Creating Custom VMobjects

```python
class CustomShape(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define points using set_points_as_corners or set_points_smoothly
        self.set_points_as_corners([
            LEFT, UP, RIGHT, DOWN, LEFT
        ])
```

## Mobject Properties

### Position and Size

```python
mobject.get_center()      # Returns center point
mobject.width             # Width (preferred over get_width())
mobject.height            # Height (preferred over get_height())
mobject.get_top()         # Top edge center point
mobject.get_bottom()      # Bottom edge center point
mobject.get_left()        # Left edge center point
mobject.get_right()       # Right edge center point
```

> **Note:** ManimCE 0.21+ recommends `.width` and `.height` properties over
> `get_width()` / `get_height()` method calls. The methods still work but
> emit a DeprecationWarning.

### Bounding Box Corners

```python
mobject.get_corner(UL)    # Upper left corner
mobject.get_corner(UR)    # Upper right corner
mobject.get_corner(DL)    # Lower left corner
mobject.get_corner(DR)    # Lower right corner
```

## Submobjects

Mobjects can contain other mobjects as submobjects.

```python
# Access submobjects
group = VGroup(Circle(), Square())
group.submobjects      # List of child mobjects
group[0]               # First submobject (Circle)
group[1]               # Second submobject (Square)

# Iterate over submobjects
for mob in group:
    mob.set_color(RED)
```

## Copying Mobjects

```python
# Create a copy
circle_copy = circle.copy()

# Copy and position
circle_copy = circle.copy().shift(RIGHT * 2)
```

## Method Chaining

Most mobject methods return `self`, allowing method chaining:

```python
circle = Circle().set_color(RED).shift(LEFT).scale(2)
```

## Best Practices

1. **Use VMobject for custom shapes** - Better rendering and animation support
2. **Prefer VGroup over Group** - VGroup works better with most animations
3. **Use copy() when reusing** - Avoid unintended modifications to original
4. **Chain methods for readability** - But break into lines if too long


# Positioning in Manim

Methods for placing and moving mobjects in the scene.

## Coordinate System

Manim uses a coordinate system where:
- Origin (0, 0, 0) is at the center of the screen
- X-axis: LEFT (-) to RIGHT (+)
- Y-axis: DOWN (-) to UP (+)
- Z-axis: IN (-) to OUT (+) (for 3D)

### Direction Constants
```python
UP = np.array([0, 1, 0])
DOWN = np.array([0, -1, 0])
LEFT = np.array([-1, 0, 0])
RIGHT = np.array([1, 0, 0])
ORIGIN = np.array([0, 0, 0])

# Diagonals
UL = UP + LEFT      # Upper left
UR = UP + RIGHT     # Upper right
DL = DOWN + LEFT    # Lower left
DR = DOWN + RIGHT   # Lower right
```

## move_to

Move to an absolute position.

```python
from manim import *

class MoveToExample(Scene):
    def construct(self):
        circle = Circle()

        # Move to origin
        circle.move_to(ORIGIN)

        # Move to specific coordinates
        circle.move_to(RIGHT * 2 + UP * 1)

        # Move to another mobject's position
        square = Square().shift(LEFT * 2)
        circle.move_to(square)

        # Move to a specific point of another mobject
        circle.move_to(square.get_top())
```

## shift

Move relative to current position.

```python
class ShiftExample(Scene):
    def construct(self):
        circle = Circle()

        # Shift in one direction
        circle.shift(RIGHT)
        circle.shift(UP * 2)

        # Shift in multiple directions
        circle.shift(RIGHT * 2 + UP * 1)

        # Chain shifts
        circle.shift(LEFT).shift(DOWN)
```

## next_to

Position relative to another mobject.

```python
class NextToExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()

        # Place circle to the right of square
        circle.next_to(square, RIGHT)

        # With buffer (spacing)
        triangle.next_to(square, DOWN, buff=0.5)

        # Aligned to specific edge
        circle.next_to(square, RIGHT, aligned_edge=UP)
```

### buff Parameter
```python
# Default buffer
circle.next_to(square, RIGHT)  # Uses DEFAULT_MOBJECT_TO_MOBJECT_BUFFER

# Custom buffer
circle.next_to(square, RIGHT, buff=0)    # No gap
circle.next_to(square, RIGHT, buff=1)    # 1 unit gap
circle.next_to(square, RIGHT, buff=0.5)  # Half unit gap
```

## align_to

Align edges with another mobject.

```python
class AlignToExample(Scene):
    def construct(self):
        square = Square().shift(LEFT)
        circle = Circle().shift(RIGHT)

        # Align circle's left edge with square's left edge
        circle.align_to(square, LEFT)

        # Align tops
        circle.align_to(square, UP)

        # Align to a point
        circle.align_to(ORIGIN, DOWN)
```

## Edge Methods

Position at screen edges.

```python
class EdgeExample(Scene):
    def construct(self):
        # To screen edges
        text1 = Text("Top").to_edge(UP)
        text2 = Text("Bottom").to_edge(DOWN)
        text3 = Text("Left").to_edge(LEFT)
        text4 = Text("Right").to_edge(RIGHT)

        # With buffer
        text5 = Text("Buffered").to_edge(UP, buff=1)
```

## Corner Methods

Position at screen corners.

```python
class CornerExample(Scene):
    def construct(self):
        t1 = Text("UL").to_corner(UL)
        t2 = Text("UR").to_corner(UR)
        t3 = Text("DL").to_corner(DL)
        t4 = Text("DR").to_corner(DR)

        # With buffer
        t5 = Text("Buffered").to_corner(UL, buff=0.5)
```

## center

Center on screen or another mobject.

```python
mobject.center()           # Center on screen
mobject.center_on(other)   # Center on another mobject (custom helper)
```

## Getting Positions

```python
circle = Circle()

# Get various points
circle.get_center()        # Center point
circle.get_top()           # Top edge center
circle.get_bottom()        # Bottom edge center
circle.get_left()          # Left edge center
circle.get_right()         # Right edge center
circle.get_corner(UL)      # Upper left corner
circle.get_corner(DR)      # Lower right corner
circle.get_start()         # Start of path
circle.get_end()           # End of path
```

## Animated Positioning

```python
class AnimatedPosition(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # Animate movement
        self.play(square.animate.shift(RIGHT * 2))
        self.play(square.animate.move_to(UP * 2))
        self.play(square.animate.to_edge(LEFT))
```

## Best Practices

1. **Use next_to for relative positioning** - Maintains relationships
2. **Use move_to for absolute positioning** - Precise coordinates
3. **Use shift for relative adjustments** - Quick tweaks
4. **Use to_edge/to_corner for screen positioning** - Responsive layouts
5. **Adjust buff for visual spacing** - Don't let elements crowd

## Explanation Layout Guidance

1. **Lay out the meaningful final state first** - Arrange everything that must coexist at a key moment, verify that state, then animate its parts into place.
2. **Use stable spatial roles** - Keep recurring concepts in predictable regions unless moving them communicates a real change.
3. **Prefer relational positioning** - Use `next_to`, `align_to`, groups, and anchors when objects belong together; reserve absolute coordinates for deliberate composition.
4. **Protect the focus area** - Titles, labels, equations, and diagrams should support the current evidence rather than compete for the same visual region.
5. **Design for replacement and growth** - Leave room for the longest equation, final graph, or expanded diagram instead of fitting only the first state.
6. **Inspect actual frames** - Bounding boxes and coordinates are planning aids; the rendered image is the final test for clipping, crowding, and unintended overlap.


# Grouping Mobjects

Organize multiple mobjects into groups for collective manipulation.

## VGroup

VGroup (Vectorized Group) is for grouping VMobjects. Most commonly used.

```python
from manim import *

class VGroupExample(Scene):
    def construct(self):
        # Create a group
        group = VGroup(
            Circle(),
            Square(),
            Triangle()
        )

        # Operations apply to all members
        group.set_color(RED)
        group.shift(UP)

        self.add(group)
```

## Group

Group is for mixing different mobject types (VMobjects, ImageMobjects, etc.).

```python
class GroupExample(Scene):
    def construct(self):
        # Mix different types
        text = Text("Hello")
        group = Group(
            Circle(),
            text
        )
        self.add(group)
```

## Creating Groups

```python
# From individual mobjects
group = VGroup(circle, square, triangle)

# From a list
shapes = [Circle(), Square(), Triangle()]
group = VGroup(*shapes)

# Using list comprehension
group = VGroup(*[Circle() for _ in range(5)])

# Empty group, add later
group = VGroup()
group.add(Circle())
group.add(Square())
```

## arrange

Arrange mobjects in a line.

```python
class ArrangeExample(Scene):
    def construct(self):
        # Horizontal arrangement (default)
        row = VGroup(*[Circle().scale(0.3) for _ in range(5)])
        row.arrange(RIGHT, buff=0.5).shift(UP * 2)

        # Vertical arrangement
        column = VGroup(*[Square().scale(0.3) for _ in range(4)])
        column.arrange(DOWN, buff=0.5).shift(LEFT * 2)

        # With custom buffer
        spaced = VGroup(*[Triangle().scale(0.3) for _ in range(3)])
        spaced.arrange(RIGHT, buff=1).shift(DOWN * 2)

        self.add(row, column, spaced)
```

### Direction Options
```python
group.arrange(RIGHT)      # Left to right
group.arrange(LEFT)       # Right to left
group.arrange(UP)         # Bottom to top
group.arrange(DOWN)       # Top to bottom
```

## arrange_in_grid

Arrange in a grid pattern.

```python
class GridExample(Scene):
    def construct(self):
        # Auto grid
        grid = VGroup(*[Square().scale(0.3) for _ in range(20)])
        grid.arrange_in_grid()

        # Specify rows and columns
        grid = VGroup(*[Circle().scale(0.2) for _ in range(12)])
        grid.arrange_in_grid(rows=3, cols=4)

        # With spacing
        grid.arrange_in_grid(rows=3, cols=4, buff=0.5)

        self.add(grid)
```

## Accessing Group Members

```python
group = VGroup(Circle(), Square(), Triangle())

# By index
first = group[0]          # Circle
second = group[1]         # Square
last = group[-1]          # Triangle

# Slicing
first_two = group[0:2]    # VGroup with Circle and Square

# Iteration
for mob in group:
    mob.set_color(random_color())

# Length
num_items = len(group)
```

## Modifying Groups

```python
group = VGroup(Circle(), Square())

# Add mobjects
group.add(Triangle())
group.add(Star(), Pentagon())

# Remove mobjects
group.remove(circle)

# Insert at position
group.insert(0, new_mobject)

# Submobjects list
group.submobjects  # List of all children
```

## Group Transformations

```python
group = VGroup(Circle(), Square(), Triangle()).arrange(RIGHT)

# All transformations apply to entire group
group.shift(UP * 2)
group.scale(0.5)
group.rotate(PI / 4)
group.set_color(BLUE)

# But can target individuals
group[0].set_color(RED)  # Just the circle
```

## Nested Groups

```python
class NestedGroups(Scene):
    def construct(self):
        # Create sub-groups
        row1 = VGroup(*[Circle() for _ in range(3)]).arrange(RIGHT)
        row2 = VGroup(*[Square() for _ in range(3)]).arrange(RIGHT)
        row3 = VGroup(*[Triangle() for _ in range(3)]).arrange(RIGHT)

        # Group of groups
        all_rows = VGroup(row1, row2, row3).arrange(DOWN)

        self.add(all_rows)
```

## Useful Group Methods

```python
group = VGroup(Circle(), Square(), Triangle())

# Get bounding box info
group.get_center()
group.get_width()
group.get_height()

# Set position for whole group
group.move_to(ORIGIN)
group.to_edge(LEFT)

# Copy entire group
group_copy = group.copy()

# Match layout of another group
group1.match_height(group2)
group1.match_width(group2)
```

## Best Practices

1. **Use VGroup for VMobjects** - Better performance and compatibility
2. **Use arrange after creating** - Don't position individually then group
3. **Name your groups semantically** - `equation_parts` not `group1`
4. **Use nested groups for structure** - Rows within columns, etc.
5. **Copy groups when needed** - Avoid unintended modifications


# Geometric Shapes

Basic geometric primitives in Manim.

## Circle

```python
from manim import *

class CircleExample(Scene):
    def construct(self):
        # Default circle
        c1 = Circle()

        # With parameters
        c2 = Circle(
            radius=2,
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=4
        )

        self.add(c1, c2)
```

### Circle Methods

```python
circle = Circle()

# Get properties
circle.get_radius()
circle.get_center()

# Create from points
Circle.from_three_points(p1, p2, p3)

# Surround another mobject
triangle = Triangle()
circle = Circle().surround(triangle)  # Circle wraps around triangle
circle = Circle().surround(triangle, buffer_factor=1.5)  # With padding
circle = Circle().surround(triangle, stretch=True)  # Stretch to fit
```

## Ellipse

```python
class EllipseExample(Scene):
    def construct(self):
        ellipse = Ellipse(
            width=4,
            height=2,
            color=GREEN
        )
        self.add(ellipse)
```

## Square

```python
class SquareExample(Scene):
    def construct(self):
        # Default square
        s1 = Square()

        # With parameters
        s2 = Square(
            side_length=2,
            color=RED,
            fill_opacity=0.8
        )

        self.add(s1, s2)
```

## Rectangle

```python
class RectangleExample(Scene):
    def construct(self):
        rect = Rectangle(
            width=4,
            height=2,
            color=YELLOW,
            fill_opacity=0.5
        )
        self.add(rect)
```

### RoundedRectangle

```python
class RoundedRectExample(Scene):
    def construct(self):
        rounded = RoundedRectangle(
            width=4,
            height=2,
            corner_radius=0.5,
            color=BLUE,
            fill_opacity=0.8
        )
        self.add(rounded)
```

## Triangle

```python
class TriangleExample(Scene):
    def construct(self):
        # Equilateral triangle
        tri = Triangle(color=PURPLE)

        # Custom triangle (using Polygon)
        custom_tri = Polygon(
            ORIGIN, RIGHT * 2, UP * 3,
            color=GREEN
        )

        self.add(tri, custom_tri.shift(RIGHT * 3))
```

## Polygon

Create any polygon from vertices.

```python
class PolygonExample(Scene):
    def construct(self):
        # Pentagon
        pentagon = RegularPolygon(n=5, color=ORANGE)

        # Hexagon
        hexagon = RegularPolygon(n=6, color=TEAL)

        # Custom polygon
        custom = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [2, 1, 0],
            [0, 2, 0],
            [-2, 1, 0],
            color=PINK
        )

        VGroup(pentagon, hexagon, custom).arrange(RIGHT, buff=1)
        self.add(pentagon, hexagon, custom)
```

## RegularPolygon

```python
class RegularPolygonExamples(Scene):
    def construct(self):
        shapes = VGroup(
            RegularPolygon(n=3),   # Triangle
            RegularPolygon(n=4),   # Square
            RegularPolygon(n=5),   # Pentagon
            RegularPolygon(n=6),   # Hexagon
            RegularPolygon(n=8),   # Octagon
        ).arrange(RIGHT)
        self.add(shapes)
```

## Star

```python
class StarExample(Scene):
    def construct(self):
        star = Star(
            n=5,                    # Number of points
            outer_radius=2,
            inner_radius=1,         # Optional: auto-calculated if not specified
            density=2,              # How vertices connect (affects shape)
            color=YELLOW,
            fill_opacity=1
        )
        self.add(star)

        # Different densities create different star patterns
        star_d2 = Star(7, outer_radius=2, density=2, color=RED)
        star_d3 = Star(7, outer_radius=2, density=3, color=PURPLE)
```

## RegularPolygram

Star-like shapes with vertices connected by density.

```python
class PolygramExample(Scene):
    def construct(self):
        # Pentagram (5-pointed star pattern)
        pentagram = RegularPolygram(5, radius=2)
        self.add(pentagram)
```

## Annulus (Ring)

```python
class AnnulusExample(Scene):
    def construct(self):
        ring = Annulus(
            inner_radius=1,
            outer_radius=2,
            color=BLUE,
            fill_opacity=0.5
        )
        self.add(ring)
```

## Sector and Arc

```python
class SectorArcExample(Scene):
    def construct(self):
        # Sector (pie slice)
        sector = Sector(
            radius=2,
            angle=PI/2,
            start_angle=0,
            color=RED,
            fill_opacity=0.8
        ).shift(LEFT * 2)

        # Arc (just the curve)
        arc = Arc(
            radius=2,
            angle=PI/2,
            start_angle=PI,
            color=BLUE
        ).shift(RIGHT * 2)

        self.add(sector, arc)
```

## ArcBetweenPoints

```python
class ArcBetweenPointsExample(Scene):
    def construct(self):
        arc = ArcBetweenPoints(
            start=LEFT * 2,
            end=RIGHT * 2,
            angle=PI/2,  # Curvature
            color=GREEN
        )
        self.add(arc)
```

## Dot

```python
class DotExample(Scene):
    def construct(self):
        # Default dot
        d1 = Dot()

        # Customized
        d2 = Dot(
            point=RIGHT * 2,
            radius=0.2,
            color=YELLOW
        )

        self.add(d1, d2)
```

## Common Shape Operations

```python
shape = Square()

# Transform
shape.scale(2)
shape.rotate(PI/4)
shape.stretch(2, dim=0)  # Stretch horizontally

# Style
shape.set_fill(RED, opacity=0.5)
shape.set_stroke(WHITE, width=4)

# Position
shape.move_to(ORIGIN)
shape.shift(UP * 2)
shape.next_to(other, RIGHT)
```

## Angle and RightAngle

Mark angles between lines — essential for geometry problem explanations.

```python
class AngleExample(Scene):
    def construct(self):
        line1 = Line(LEFT, RIGHT)
        line2 = Line(LEFT, UP + RIGHT)

        angle = Angle(line1, line2, radius=0.5)
        label = MathTex(r"\theta", font_size=28).move_to(
            Angle(line1, line2, radius=0.7).point_from_proportion(0.5)
        )
        self.add(line1, line2, angle, label)
```

### Dynamic Angle with ValueTracker

```python
class MovingAngle(Scene):
    def construct(self):
        pivot = LEFT
        tracker = ValueTracker(60)

        base = Line(LEFT, RIGHT)
        arm = Line(LEFT, RIGHT)
        ref = arm.copy()
        arm.rotate(tracker.get_value() * DEGREES, about_point=pivot)

        angle = Angle(base, arm, radius=0.5)
        label = MathTex(r"\theta", font_size=28).move_to(
            Angle(base, arm, radius=0.7).point_from_proportion(0.5)
        )

        arm.add_updater(
            lambda m: m.become(ref.copy()).rotate(
                tracker.get_value() * DEGREES, about_point=pivot
            )
        )
        angle.add_updater(lambda m: m.become(Angle(base, arm, radius=0.5)))
        label.add_updater(
            lambda m: m.move_to(
                Angle(base, arm, radius=0.7).point_from_proportion(0.5)
            )
        )

        self.add(base, arm, angle, label)
        self.play(tracker.animate.set_value(120), run_time=2)
```

### RightAngle

```python
right = RightAngle(line1, line2, length=0.3)
```

### Related

- `ArcBetweenPoints(start, end, angle=PI/2)` — arc connecting two points
- `Angle(other_angle=True)` — use the reflex (larger) angle

## Best Practices

1. **Use RegularPolygon for regular shapes** - More precise than manual Polygon
2. **Set fill_opacity for visibility** - Default is often 0 (transparent)
3. **Use Dot for points** - Better than Circle with small radius
4. **Use RoundedRectangle for UI elements** - More polished look
5. **Combine shapes with VGroup** - For complex figures
6. **Use Angle for geometry** - Dynamic angle markers with ValueTracker for interactive derivations


# Lines and Arrows

Connect points and show relationships with lines and arrows.

## Line

Basic line between two points.

```python
from manim import *

class LineExample(Scene):
    def construct(self):
        # Line from two points
        line = Line(LEFT * 2, RIGHT * 2)

        # With styling
        styled_line = Line(
            UP * 2, DOWN * 2,
            color=BLUE,
            stroke_width=4
        )

        self.add(line, styled_line)
```

### Line Properties

```python
line = Line(LEFT, RIGHT)

# Get points
line.get_start()
line.get_end()
line.get_center()
line.get_length()
line.get_angle()

# Modify
line.put_start_and_end_on(new_start, new_end)
line.set_length(3)  # Keep direction, change length
```

## Arrow

Line with an arrowhead.

```python
class ArrowExample(Scene):
    def construct(self):
        # Basic arrow
        arrow = Arrow(LEFT * 2, RIGHT * 2)

        # Styled arrow
        styled = Arrow(
            start=UP,
            end=DOWN,
            color=RED,
            stroke_width=6,
            tip_length=0.4,
            max_tip_length_to_length_ratio=0.5
        )

        self.add(arrow, styled)
```

### Arrow Variations

```python
# Double-headed arrow
double = DoubleArrow(LEFT * 2, RIGHT * 2)

# Arrow with custom tip
arrow = Arrow(LEFT, RIGHT)
arrow.tip  # Access the tip mobject
```

## Vector

Arrow starting from origin (useful for physics/math).

```python
class VectorExample(Scene):
    def construct(self):
        # Vector from origin
        v1 = Vector([2, 1, 0], color=YELLOW)
        v2 = Vector([-1, 2, 0], color=GREEN)

        self.add(v1, v2)
```

## DashedLine

```python
class DashedLineExample(Scene):
    def construct(self):
        dashed = DashedLine(
            LEFT * 2, RIGHT * 2,
            dash_length=0.2,
            dashed_ratio=0.5,  # Ratio of dash to gap
            color=WHITE
        )
        self.add(dashed)
```

## TangentLine

Line tangent to a curve at a point.

```python
class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)

        # Tangent at specific point (t parameter 0-1 along curve)
        tangent = TangentLine(circle, alpha=0.25, length=3, color=YELLOW)

        self.add(circle, tangent)
```

## Brace

Curly brace for highlighting.

```python
class BraceExample(Scene):
    def construct(self):
        rect = Rectangle(width=4, height=1)

        # Brace under the rectangle
        brace = Brace(rect, DOWN)

        # With label
        brace_text = brace.get_text("Width")

        # Alternative: BraceLabel
        brace_label = BraceLabel(rect, "Width", DOWN)

        self.add(rect, brace, brace_text)
```

### Brace Directions

```python
brace_down = Brace(mobject, DOWN)
brace_up = Brace(mobject, UP)
brace_left = Brace(mobject, LEFT)
brace_right = Brace(mobject, RIGHT)
```

## CurvedArrow

Curved arrow between points.

```python
class CurvedArrowExample(Scene):
    def construct(self):
        curved = CurvedArrow(
            start_point=LEFT * 2,
            end_point=RIGHT * 2,
            angle=PI/2  # Curvature
        )
        self.add(curved)
```

## Elbow

Right-angle connector.

```python
class ElbowExample(Scene):
    def construct(self):
        elbow = Elbow(width=2, angle=PI/2)
        self.add(elbow)
```

## NumberLine Ticks

```python
class TicksExample(Scene):
    def construct(self):
        line = NumberLine(x_range=[-3, 3, 1])
        self.add(line)
```

## Connecting Mobjects

### Line Between Mobjects

```python
class ConnectMobjects(Scene):
    def construct(self):
        c1 = Circle().shift(LEFT * 2)
        c2 = Circle().shift(RIGHT * 2)

        # Line connecting centers
        line = Line(c1.get_center(), c2.get_center())

        # Arrow between edges
        arrow = Arrow(
            c1.get_right(),  # Right edge of c1
            c2.get_left(),   # Left edge of c2
            buff=0.1         # Small gap from edges
        )

        self.add(c1, c2, line, arrow)
```

### Dynamic Connections with Updaters

```python
class DynamicLine(Scene):
    def construct(self):
        dot1 = Dot(LEFT * 2)
        dot2 = Dot(RIGHT * 2)

        # Line that follows dots
        line = always_redraw(lambda: Line(
            dot1.get_center(),
            dot2.get_center(),
            color=YELLOW
        ))

        self.add(dot1, dot2, line)
        self.play(dot1.animate.shift(UP * 2), run_time=2)
```

## Best Practices

1. **Use Arrow for direction** - Clearer than plain lines
2. **Use Vector for physics/math** - Semantically meaningful
3. **Use Brace for labeling dimensions** - Professional look
4. **Use DashedLine for auxiliary lines** - Distinguishes from main content
5. **Use always_redraw for dynamic lines** - Updates with moving endpoints


# Colors in Manim

Manim provides predefined color constants and supports custom colors.

## Color Constants

### Primary Colors
```python
RED, GREEN, BLUE
YELLOW, ORANGE, PINK, PURPLE
WHITE, BLACK, GREY (or GRAY)
```

### Color Variants (Shades)
Most colors have variants from `_A` (lightest) to `_E` (darkest):
```python
BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E
RED_A, RED_B, RED_C, RED_D, RED_E
GREEN_A, GREEN_B, GREEN_C, GREEN_D, GREEN_E
GREY_A, GREY_B, GREY_C, GREY_D, GREY_E
```

### Common Named Colors
```python
TEAL, TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E
GOLD, GOLD_A, GOLD_B, GOLD_C, GOLD_D, GOLD_E
MAROON, MAROON_A, MAROON_B, MAROON_C, MAROON_D, MAROON_E
PURPLE, PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D, PURPLE_E
```

### Special Colors
```python
PURE_RED, PURE_GREEN, PURE_BLUE  # RGB primaries
LIGHT_GREY, DARK_GREY
LIGHTER_GREY, DARKER_GREY
LIGHT_BROWN, DARK_BROWN
```

## Using Colors

### Setting Color on Creation
```python
circle = Circle(color=RED)
square = Square(color=BLUE, fill_color=GREEN, fill_opacity=0.5)
text = Text("Hello", color=YELLOW)
```

### Setting Color After Creation
```python
circle = Circle()
circle.set_color(RED)
```

## Hex Colors

```python
# Use hex strings
circle = Circle(color="#FF5733")
square = Square(color="#2ECC71")

# RGB values (0-1 range)
from manim import rgb_to_color
custom = rgb_to_color([0.5, 0.2, 0.8])
```

## Fill vs Stroke Color

```python
square = Square()
square.set_fill(RED, opacity=0.8)      # Interior color
square.set_stroke(BLUE, width=4)       # Border color
```

### Combined Styling
```python
square = Square(
    color=BLUE,            # Sets both fill and stroke
    fill_opacity=0.5,      # Fill transparency
    stroke_width=4         # Border thickness
)
```

## Gradients

### Color Gradient on Mobject
```python
text = Text("GRADIENT")
text.set_color_by_gradient(RED, YELLOW, GREEN)
```

### Gradient Along Path
```python
line = Line(LEFT * 3, RIGHT * 3)
line.set_color_by_gradient(BLUE, GREEN, YELLOW)
```

## Color Interpolation

Create colors between two colors:

```python
from manim import interpolate_color

# Get color halfway between RED and BLUE
mid_color = interpolate_color(RED, BLUE, 0.5)

# Create a range of colors
colors = [interpolate_color(RED, BLUE, alpha) for alpha in np.linspace(0, 1, 10)]
```

## ManimColor Class

For advanced color manipulation, use ManimColor directly:

```python
from manim import ManimColor

# Create from various formats
color1 = ManimColor("#FF0000")           # From hex
color2 = ManimColor((0.0, 1.0, 0.5))     # From RGB floats (0-1)
color3 = ManimColor([255, 165, 0])       # From RGB ints (0-255)

# Color manipulation methods
lighter = color1.lighter()               # Lighter version
darker = color1.darker()                 # Darker version
inverted = color1.invert()               # Inverted color
with_alpha = color1.opacity(0.5)         # With 50% opacity

# Convert formats
hex_str = color1.to_hex()                # To hex string
rgb = color1.to_rgb()                    # To RGB float array
hsv = color1.to_hsv()                    # To HSV array

# Interpolation
mixed = color1.interpolate(color2, 0.5)  # Blend two colors
```

## Opacity

```python
# Set opacity (0 = transparent, 1 = opaque)
circle = Circle(fill_opacity=0.5, stroke_opacity=0.8)

# Modify opacity
circle.set_opacity(0.5)         # Both fill and stroke
circle.set_fill_opacity(0.7)    # Fill only
circle.set_stroke_opacity(0.3)  # Stroke only
```

## Color by Value

Color mobjects based on a value (useful for data visualization):

```python
class ColorByValue(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)]).arrange(RIGHT)

        for i, dot in enumerate(dots):
            # Color from blue (cold) to red (hot)
            dot.set_color(interpolate_color(BLUE, RED, i / 9))

        self.add(dots)
```

## Random Colors

```python
from manim import random_color, random_bright_color

circle = Circle(color=random_color())
square = Square(color=random_bright_color())
```

## Color Lists for Animations

```python
class ColorCycle(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)

        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        for color in colors:
            self.play(circle.animate.set_color(color), run_time=0.5)
```

## Best Practices

1. **Use color variants for depth** - `BLUE_E` for shadows, `BLUE_A` for highlights
2. **Maintain color consistency** - Use the same colors for related concepts
3. **Use opacity for layering** - Semi-transparent fills show overlapping
4. **Consider colorblind accessibility** - Avoid red-green only distinctions
5. **Use gradients sparingly** - They can be distracting

## Visual Explanation Guidance

1. **Assign color a role** - Use color to identify concepts, distinguish states, encode values, or direct attention. A viewer should be able to explain what a recurring color means.
2. **Keep meanings stable** - Preserve a concept's color while its shape, position, or notation changes so color supports object identity.
3. **Build a clear attention hierarchy** - Give the current evidence the strongest contrast and reduce the presence of context without making it unreadable.
4. **Use more than hue alone** - Pair color with labels, position, shape, stroke, or motion when the distinction is important, especially for colorblind accessibility.
5. **Check contrast in rendered frames** - Judge text, thin strokes, grids, and transparent fills against the actual background and output size.
6. **Use gradients when they encode continuity** - Gradients are effective for magnitude, direction, temperature, or progression; a flat color is usually clearer when no continuous value is present.

Examples using `random_color()` demonstrate the API rather than a production palette strategy. Use randomness when variability itself is part of the subject; use stable semantic assignments when viewers need to track concepts across time.


# Styling Mobjects

Control the visual appearance of mobjects with fill, stroke, and opacity settings.

## Fill Properties

Fill controls the interior of shapes.

```python
from manim import *

class FillExample(Scene):
    def construct(self):
        # Set fill on creation
        circle = Circle(fill_color=BLUE, fill_opacity=0.8)

        # Set fill after creation
        square = Square()
        square.set_fill(RED, opacity=0.5)

        self.add(circle, square)
```

### Fill Methods
```python
mobject.set_fill(color=RED)                    # Color only
mobject.set_fill(RED, opacity=0.5)             # Color and opacity
mobject.set_fill(opacity=0.5)                  # Opacity only
mobject.set_fill_color(RED)                    # Color only (alternative)
mobject.set_fill_opacity(0.5)                  # Opacity only (alternative)
```

## Stroke Properties

Stroke controls the outline/border of shapes.

```python
class StrokeExample(Scene):
    def construct(self):
        # Set stroke on creation
        circle = Circle(stroke_color=BLUE, stroke_width=4)

        # Set stroke after creation
        square = Square()
        square.set_stroke(RED, width=8)

        self.add(circle, square)
```

### Stroke Methods
```python
mobject.set_stroke(color=RED)                  # Color only
mobject.set_stroke(RED, width=4)               # Color and width
mobject.set_stroke(width=4)                    # Width only
mobject.set_stroke(opacity=0.5)                # Opacity only
mobject.set_stroke_color(RED)                  # Color only (alternative)
mobject.set_stroke_width(4)                    # Width only (alternative)
mobject.set_stroke_opacity(0.5)                # Opacity only (alternative)
```

### Stroke Width Reference
```python
# Common stroke widths
DEFAULT_STROKE_WIDTH = 4
thin = 1
normal = 4
thick = 8
very_thick = 12
```

## Combined Styling

```python
class CombinedStyling(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(YELLOW, width=6)
        self.add(square)
```

### Method Chaining
```python
square = Square().set_fill(RED, 0.5).set_stroke(WHITE, 4)
```

## The set_style Method

Set multiple style properties at once:

```python
square = Square()
square.set_style(
    fill_color=BLUE,
    fill_opacity=0.5,
    stroke_color=WHITE,
    stroke_width=4,
    stroke_opacity=1
)
```

## Opacity

Control transparency of mobjects:

```python
# Overall opacity
mobject.set_opacity(0.5)  # Affects both fill and stroke

# Separate opacities
mobject.set_fill_opacity(0.8)
mobject.set_stroke_opacity(0.3)

# Fade effect
mobject.fade(0.5)  # 0.5 = 50% faded (opposite of opacity)
```

## Background Rectangle

Add a background behind text or other mobjects:

```python
class BackgroundExample(Scene):
    def construct(self):
        text = Text("Important!")
        bg = BackgroundRectangle(text, fill_opacity=0.8, buff=0.1)
        group = VGroup(bg, text)
        self.add(group)
```

## Applying Style to Submobjects

```python
# Apply to all submobjects (family=True, default)
group.set_fill(RED, opacity=0.5, family=True)

# Apply only to parent, not submobjects
group.set_fill(RED, opacity=0.5, family=False)
```

## Style Based on Position

```python
class GradientFill(Scene):
    def construct(self):
        squares = VGroup(*[Square() for _ in range(5)]).arrange(RIGHT)

        for i, sq in enumerate(squares):
            opacity = (i + 1) / 5
            sq.set_fill(BLUE, opacity=opacity)

        self.add(squares)
```

## Copying Style

```python
# Copy style from another mobject
source = Circle().set_fill(RED, 0.5).set_stroke(WHITE, 4)
target = Square()
target.match_style(source)  # Now has same fill and stroke
```

## Best Practices

1. **Use fill_opacity for shapes** - Fully opaque fills can hide other elements
2. **Consistent stroke width** - Pick a width and stick with it
3. **Contrast fill and stroke** - Different colors help definition
4. **Use BackgroundRectangle for readability** - Behind text on busy backgrounds
5. **Chain methods for concise code** - But break lines if too long


# Configuration

Configure Manim's behavior through files and code.

## Configuration Hierarchy

Manim reads configuration from (in order of precedence):
1. Command-line arguments (highest priority)
2. User's `manim.cfg` in current directory
3. User's global config
4. Default values (lowest priority)

## manim.cfg File

Create a `manim.cfg` file in your project directory:

```ini
[CLI]
# Preview after rendering
preview = True

# Default quality
quality = medium_quality

# Output format
format = mp4

# Frame rate
frame_rate = 30

[output]
# Custom output directory
media_dir = ./media

# Save last frame as PNG
save_last_frame = False

[renderer]
# Background color
background_color = BLACK

[style]
# Default font
font = Arial
```

## Common Configuration Options

### CLI Section

```ini
[CLI]
# Quality presets: low_quality, medium_quality, high_quality, production_quality, fourk_quality
quality = medium_quality

# Preview video after rendering
preview = True

# Frame rate
frame_rate = 30

# Output format: mp4, gif, mov, webm, png
format = mp4

# Transparent background
transparent = False

# Progress bar: display, leave, none
progress_bar = display
```

### Rendering Section

```ini
[renderer]
# Background color (hex or color name)
background_color = #1e1e1e

# Renderer type: cairo, opengl
renderer = cairo
```

### Resolution

```ini
[CLI]
# Frame dimensions
pixel_width = 1920
pixel_height = 1080
```

## Programmatic Configuration

Access and modify config in your Python code:

```python
# Access config values
config.pixel_width  # e.g., 1920
config.frame_rate  # e.g., 30
config.background_color  # e.g., BLACK

# Modify config (before creating scenes)
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60
config.background_color = BLUE_E
```

### In Scene

```python
class MyScene(Scene):
    def construct(self):
        # Access frame dimensions
        width = config.frame_width
        height = config.frame_height

        # Create rectangle matching frame size
        frame_rect = Rectangle(
            width=width,
            height=height,
            stroke_color=WHITE
        )
        self.add(frame_rect)
```

## Background Color

### In Config File

```ini
[renderer]
background_color = BLACK
# Or hex color
background_color = #1a1a2e
```

### In Code

```python
class DarkBackground(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        # ... rest of scene
```

## Output Directory Structure

Default media directory structure:
```
media/
├── videos/
│   └── scene_file/
│       ├── 480p15/       # Low quality
│       ├── 720p30/       # Medium quality
│       ├── 1080p60/      # High quality
│       └── 2160p60/      # 4K quality
├── images/
│   └── scene_file/
│       └── SceneName.png
└── Tex/                  # LaTeX cache
```

### Custom Output Directory

```ini
[output]
media_dir = ./output
```

Or via CLI:
```bash
manim --media_dir ./output file.py Scene
```

## Tex Configuration

For LaTeX rendering:

```ini
[tex]
# Custom preamble
preamble = \usepackage{amsmath}\usepackage{amssymb}

# Tex compiler
tex_compiler = latex
```

## Caching

```ini
[CLI]
# Disable caching (useful for debugging)
disable_caching = True

# Max cached files
max_files_cached = 100
```

## Viewing Current Config

```bash
# Show all config values
manim cfg show

# Show specific section
manim cfg show CLI

# Write current config to file
manim cfg write
```

## Project-Specific Config

Create `manim.cfg` in your project root:

```ini
[CLI]
quality = high_quality
preview = True
frame_rate = 60

[renderer]
background_color = #0d1117

[output]
media_dir = ./renders
```

## Plugins

Manim has an extensible plugin system:

```bash
# List installed plugins
manim plugins -l

# Install a plugin
pip install manim-pluginname
```

Enable plugins in `manim.cfg`:

```ini
[CLI]
plugins = manim-pluginname
# For multiple plugins:
plugins = plugin1,plugin2
```

## Best Practices

1. **Use manim.cfg for project defaults** - Consistent settings across team
2. **Keep quality low during development** - Faster iteration
3. **Set background_color in config** - Not in every scene
4. **Use custom media_dir** - Keep renders organized
5. **Commit manim.cfg to version control** - Share settings with collaborators


# Manim CLI

The `manim` command-line interface for rendering scenes.

## Basic Usage

```bash
# Render a scene
manim file.py SceneName

# With preview (opens video after rendering)
manim -p file.py SceneName

# Preview with low quality (fast)
manim -pql file.py SceneName
```

## Quality Flags

Quality presets for different use cases:

```bash
# Low Quality: 854x480, 15fps (fast for testing)
manim -ql file.py SceneName

# Medium Quality: 1280x720, 30fps
manim -qm file.py SceneName

# High Quality: 1920x1080, 60fps
manim -qh file.py SceneName

# 2K Quality: 2560x1440, 60fps
manim -qp file.py SceneName

# 4K Quality: 3840x2160, 60fps
manim -qk file.py SceneName
```

### Common Combinations

```bash
# Preview + Low Quality (development workflow)
manim -pql file.py SceneName

# Preview + High Quality (final check)
manim -pqh file.py SceneName
```

## Preview Flag

```bash
# -p: Open video after rendering
manim -p file.py SceneName

# Without -p: Render only (no auto-open)
manim file.py SceneName
```

## Rendering Multiple Scenes

```bash
# Render all scenes in file
manim -a file.py

# Render specific scenes
manim file.py Scene1 Scene2 Scene3
```

## Output Options

### Save Last Frame Only

```bash
# -s: Save only the last frame as PNG
manim -s file.py SceneName

# With quality
manim -sql file.py SceneName
```

### Output Format

```bash
# GIF output
manim --format gif file.py SceneName

# PNG sequence
manim --format png file.py SceneName

# WebM (default is MP4)
manim --format webm file.py SceneName
```

### Custom Output Directory

```bash
manim -o custom_name file.py SceneName
manim --media_dir /path/to/output file.py SceneName
```

## Frame Control

```bash
# Start from specific animation number
manim -n 5 file.py SceneName

# Render frames from animation 3 to 7
manim -n 3,7 file.py SceneName
```

## Resolution and FPS

```bash
# Custom resolution
manim -r 1920,1080 file.py SceneName

# Custom frame rate
manim --fps 24 file.py SceneName

# Both
manim -r 1280,720 --fps 30 file.py SceneName
```

## Transparency

```bash
# Render with transparent background
manim -t file.py SceneName
```

## Renderer Selection

```bash
# Cairo renderer (default, 2D)
manim --renderer cairo file.py SceneName

# OpenGL renderer (3D, faster preview)
manim --renderer opengl file.py SceneName
```

## Other Useful Flags

```bash
# Verbose output
manim -v DEBUG file.py SceneName

# Quiet mode
manim -v WARNING file.py SceneName

# Show progress bar
manim --progress_bar display file.py SceneName

# Disable caching
manim --disable_caching file.py SceneName

# Write to movie even if no animations
manim --write_to_movie file.py SceneName
```

## Help

```bash
# Show all options
manim --help

# Show render command options
manim render --help
```

## Other Commands

```bash
# Check installation and dependencies
manim checkhealth

# Initialize new project
manim init

# Show config values
manim cfg show

# Write current config to file
manim cfg write

# List installed plugins
manim plugins -l
```

## Jupyter Notebook Support

Use the `%%manim` cell magic in Jupyter notebooks:

```python
%%manim -qm -v WARNING MyScene
class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
```

Flags work the same as CLI (`-qm`, `-ql`, etc.).

## Typical Development Workflow

```bash
# 1. Develop with fast preview
manim -pql scene.py MyScene

# 2. Check at medium quality
manim -pqm scene.py MyScene

# 3. Final render at high quality
manim -qh scene.py MyScene

# 4. Create GIF for sharing
manim --format gif -qm scene.py MyScene
```

## Best Practices

1. **Use -pql for development** - Fast iteration cycle
2. **Use -qh for final output** - Good quality, reasonable render time
3. **Use -s for thumbnails** - Quick last-frame capture
4. **Use -a sparingly** - Renders everything, can be slow
5. **Use --format gif for demos** - Easy to share and embed


# 补充：特殊 Scene 类型

## ZoomedScene

带局部放大镜效果的场景——对讲解公式细节、几何图形局部特征非常有用。

```python
class MyZoomedScene(ZoomedScene):
    def __init__(self, **kwargs):
        super().__init__(
            zoom_factor=0.3,           # 放大区域占画面的比例
            zoomed_display_height=3,   # 放大后显示区域的高度
            zoomed_display_width=3,
            zoomed_camera_frame_starting_position=ORIGIN,
            **kwargs,
        )

    def construct(self):
        # 设置放大对象
        formula = MathTex(r"\int_0^1 f(x) dx")
        self.add(formula)

        # 激活放大镜
        self.activate_zooming()
        self.play(
            self.zoomed_camera.frame.animate.move_to(formula[0][1]),  # 移到积分号
            run_time=2,
        )
```

## VectorScene

专门用于向量相关教学的场景，自带坐标平面和向量操作。

```python
class MyVectorScene(VectorScene):
    def construct(self):
        self.add_plane()
        v1 = self.add_vector([2, 1])
        v2 = self.add_vector([1, 2], color=RED)
        self.vector_to_coords(v1)  # 自动标注坐标
```

## LinearTransformationScene

线性变换教学的专用场景——自动显示网格变形。

```python
class MyLinearTransform(LinearTransformationScene):
    def construct(self):
        matrix = [[2, 1], [0, 1]]  # 剪切变换
        self.apply_matrix(matrix)
        self.wait()
```

# 补充：常用函数

## always_rotate / always_shift

让一个对象持续旋转或平移，不需要手写 updater。

```python
circle = Circle()
always_rotate(circle, rate=PI/4)  # 每秒旋转 π/4
self.add(circle)
self.wait(4)  # 旋转 4 秒

dot = Dot()
always_shift(dot, direction=RIGHT, rate=0.5)  # 每秒右移 0.5
self.add(dot)
self.wait(3)
```

## color_gradient

生成颜色渐变序列。

```python
colors = color_gradient([RED, YELLOW, BLUE], 10)  # 10 个渐变色
dots = VGroup(*[Dot(color=c) for c in colors]).arrange(RIGHT)
```

## squish_rate_func

把一个 rate_func 压缩到 [a, b] 区间内执行，区间外保持首尾值。

```python
# 只在中间 50% 的时间做动画（开头和结尾静止）
self.play(
    FadeIn(obj),
    rate_func=squish_rate_func(smooth, 0.25, 0.75),
)
```

## register_font

注册自定义字体文件（OTF/TTF），注册后 Text() 可使用。

```python
register_font("/path/to/MyFont.otf")
text = Text("自定义字体", font="MyFont")
```

## tempconfig

临时修改 ManimCE 配置，离开上下文自动恢复。

```python
with tempconfig({"background_color": WHITE}):
    # 这个场景里背景是白色
    self.play(Create(Circle()))
# 出了 with 自动恢复原背景色
```
