# Animations in Manim

Animations interpolate mobjects between states over time. They are played using `self.play()`.

## The .animate Syntax

The most common way to animate is using the `.animate` property:

```python
# Move a square to the right
self.play(square.animate.shift(RIGHT))

# Scale up
self.play(circle.animate.scale(2))

# Change color
self.play(text.animate.set_color(RED))

# Chain multiple changes
self.play(square.animate.shift(RIGHT).rotate(PI/4).set_color(BLUE))
```

## Animation Parameters

### run_time
Controls animation duration in seconds (default: 1).

```python
self.play(Create(circle), run_time=2)  # 2 second animation
self.play(Create(circle), run_time=0.5)  # Half second
```

### rate_func
Controls the animation's timing curve (easing).

```python
from manim import smooth, linear, there_and_back

self.play(square.animate.shift(RIGHT), rate_func=smooth)
self.play(square.animate.shift(RIGHT), rate_func=linear)
self.play(square.animate.shift(RIGHT), rate_func=there_and_back)
```

## Playing Multiple Animations

### Simultaneously

```python
# All play at the same time
self.play(
    Create(circle),
    FadeIn(square),
    Write(text)
)
```

### Sequentially

```python
# One after another
self.play(Create(circle))
self.play(FadeIn(square))
self.play(Write(text))

# Or use Succession
self.play(Succession(
    Create(circle),
    FadeIn(square),
    Write(text)
))
```

## Common Animation Classes

### Creation Animations
```python
Create(mobject)           # Draw the mobject progressively
Write(text)               # Write text/equations
FadeIn(mobject)           # Fade in from transparent
DrawBorderThenFill(mob)   # Draw outline, then fill
GrowFromCenter(mobject)   # Grow from center point
```

### Removal Animations
```python
FadeOut(mobject)          # Fade to transparent
Uncreate(mobject)         # Reverse of Create
ShrinkToCenter(mobject)   # Shrink to center and disappear
```

### Transform Animations
```python
Transform(mob1, mob2)              # Morph mob1 into mob2
ReplacementTransform(mob1, mob2)   # Replace mob1 with mob2
TransformFromCopy(mob1, mob2)      # Keep mob1, create mob2
```

### Movement Animations
```python
MoveToTarget(mobject)     # Move to preset target
Rotate(mobject, angle)    # Rotate by angle
Circumscribe(mobject)     # Draw attention with circle
```

## Animation vs Instant Changes

```python
# Animated change (visible transition)
self.play(circle.animate.set_color(RED))

# Instant change (no animation)
circle.set_color(RED)
self.add(circle)
```

## Best Practices

1. **Use .animate for simple transformations** - Cleaner than explicit Animation classes
2. **Keep run_time reasonable** - 0.5-2 seconds for most animations
3. **Use rate_func for polish** - `smooth` is usually better than `linear`
4. **Group related animations** - Play simultaneously when conceptually related

The `0.5-2` second range above is a narrow starting point for simple, ordinary actions. The broader `0.5-3` second range in [timing.md](timing.md) covers general standalone animations. Use the rendered sequence to adjust either range when the viewer needs more or less time.

## Educational Guidance

1. **Choose motion from the relationship** - Use creation for establishment, transforms for continuity, movement for spatial change, and emphasis for an existing object.
2. **Preserve semantic identity** - When the viewer should understand that an object remains the same while changing, animate that object instead of replacing it with an unrelated copy.
3. **Group one idea at a time** - Simultaneous animations work when they express one causal or comparative relationship. Sequence them when each change needs separate interpretation.
4. **Let motion carry information** - An animation earns its place when removing it would make the construction, change, correspondence, or conclusion harder to understand.
5. **Select timing and easing intentionally** - Base `run_time` and `rate_func` on the distance traveled, information density, and tone of the explanation. See [timing.md](timing.md).

Semantic identity describes what the viewer should perceive; it does not prescribe one transform class. Choose `Transform`, `ReplacementTransform`, or `TransformFromCopy` according to the scene membership and reference behavior documented in [transform-animations.md](transform-animations.md).


# Transform Animations

Animations that morph one mobject into another.

## Transform

Morphs the source mobject into the shape of the target. The source mobject is modified.

```python
class TransformExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.play(Transform(square, circle))
        # Note: 'square' now looks like 'circle' but is still 'square'
```

**Important:** After Transform, the original variable still references the mobject, even though it looks like the target.

## ReplacementTransform

Morphs source into target and replaces the reference. More intuitive for most uses.

```python
class ReplacementTransformExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()

        self.play(Create(square))
        self.play(ReplacementTransform(square, circle))
        # 'square' is removed, 'circle' is now in the scene
        self.play(ReplacementTransform(circle, triangle))
        # 'circle' is removed, 'triangle' is now in the scene
```

## Transform vs ReplacementTransform

```python
# Transform - source variable changes appearance
self.play(Transform(A, B))
# A is still in scene (but looks like B)
# B is NOT in scene

# ReplacementTransform - source is replaced by target
self.play(ReplacementTransform(A, B))
# A is removed from scene
# B is now in scene
```

## TransformFromCopy

Creates a copy of source and morphs it to target. Original remains unchanged.

```python
class TransformFromCopyExample(Scene):
    def construct(self):
        square = Square().shift(LEFT * 2)
        circle = Circle().shift(RIGHT * 2)

        self.add(square)
        self.play(TransformFromCopy(square, circle))
        # Both square and circle are now visible
```

## TransformMatchingShapes

Intelligently matches and transforms corresponding parts.

```python
class MatchingShapesExample(Scene):
    def construct(self):
        source = Text("ABC")
        target = Text("ABCD")

        self.play(Write(source))
        self.play(TransformMatchingShapes(source, target))
```

## TransformMatchingTex

Matches LaTeX parts by their TeX strings.

```python
class MatchingTexExample(Scene):
    def construct(self):
        eq1 = MathTex("a", "^2", "+", "b", "^2")
        eq2 = MathTex("a", "^2", "+", "2ab", "+", "b", "^2")

        self.play(Write(eq1))
        self.play(TransformMatchingTex(eq1, eq2))
```

## MoveToTarget

Pre-set a target state and animate to it.

```python
class MoveToTargetExample(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # Generate and modify target
        square.generate_target()
        square.target.shift(RIGHT * 2)
        square.target.set_color(RED)
        square.target.scale(2)

        self.play(MoveToTarget(square))
```

## Path Arc Transforms

Control the path of transformation with `path_arc`.

```python
class PathArcExample(Scene):
    def construct(self):
        dot1 = Dot(LEFT * 2)
        dot2 = Dot(RIGHT * 2)

        self.add(dot1)
        # Transform along an arc
        self.play(Transform(dot1, dot2, path_arc=PI/2))
```

## Chained Transformations

```python
class ChainedExample(Scene):
    def construct(self):
        shape = Square()
        self.play(Create(shape))

        # Chain of transformations
        for target in [Circle(), Triangle(), Star()]:
            self.play(Transform(shape, target))
            self.wait(0.5)
```

## The `.animate` Syntax

Chain method calls to build a target state and animate toward it in one step.
This is the modern ManimCE approach — prefer it over `ApplyMethod`.

```python
# Preferred: .animate chain
self.play(square.animate.shift(RIGHT * 2).scale(1.5).set_color(BLUE), run_time=1.5)

# Equivalent but verbose
square.generate_target()
square.target.shift(RIGHT * 2)
square.target.scale(1.5)
square.target.set_color(BLUE)
self.play(MoveToTarget(square), run_time=1.5)
```

`.animate` works with any mobject method that returns `self`. Multiple calls
chain naturally and execute as one interpolation.

```python
# Fade a conclusion to a corner while shrinking
self.play(
    conclusion.animate.scale(0.6).to_corner(UL, buff=0.4).set_opacity(0.7),
    run_time=0.8,
)
```

### `.animate` Interpolation Pitfall

`.animate` interpolates from the starting state to the ending state. When both
states are identical — such as a 180° rotation — no visible animation occurs.
Use the dedicated animation class instead.

```python
# Wrong — start and end states are the same, nothing visible happens
self.play(square.animate.rotate(PI))

# Right — Rotate tracks the actual rotation path
self.play(Rotate(square, angle=PI))
```

This also applies to any property change that loops back to its starting value
(e.g., full-circle color shift). If `.animate` produces unexpected stillness or
contraction, switch to the corresponding animation class (`Rotate`, `Homotopy`,
etc.).

## Choosing the Right Transform

| Situation | Use | Why |
|-----------|-----|-----|
| One object through a series of states | `Transform(a, b)` then `Transform(a, c)` | `a` keeps its identity — variable always refers to the same object |
| Replace one object with another | `ReplacementTransform(a, b)` | After the animation, `b` is in the scene and `a` is removed; subsequent code operates on `b` |
| Preserve the original and show a copy | `TransformFromCopy(a, b)` | Both `a` and `b` are visible after the animation |
| Morph matching parts of equations | `TransformMatchingTex(eq1, eq2)` | Matching TeX substrings animate into their new positions; unmatched parts fade in/out |
| Morph matching shapes in text/SVG | `TransformMatchingShapes(s1, s2)` | Same idea but matching by shape paths instead of TeX strings |

**Decision rule for equation derivations:** when a formula transforms step by
step and you need matching terms to visually connect, use `TransformMatchingTex`.
When the entire formula is replaced by something structurally different, use
`ReplacementTransform`. When you want the old formula to remain visible for
comparison, use `TransformFromCopy`.

## Best Practices

1. **Prefer `.animate` for property changes** — shifting, scaling, coloring, rotating
2. **Use ReplacementTransform when the old object is no longer needed** — cleaner variable flow
3. **Use TransformMatchingTex for equation derivations** — aligns matching terms automatically
4. **Use TransformFromCopy to preserve the original** — when you need both visible for comparison
5. **Set path_arc for visual interest** — curved paths look more dynamic

Use `path_arc` when the route helps distinguish crossing objects, communicate direction, or reveal a meaningful spatial path. A direct transform is clearer when only the source and destination states matter.


# Creation Animations

Animations that introduce mobjects to the scene.

## Create

Draws a VMobject progressively along its path.

```python
from manim import *

class CreateExample(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
```

Best for: Geometric shapes, lines, arrows.

## Write

Simulates handwriting. Best for text and equations.

```python
class WriteExample(Scene):
    def construct(self):
        text = Text("Hello World")
        equation = MathTex(r"E = mc^2")

        self.play(Write(text))
        self.wait()
        self.play(Write(equation))
```

Write automatically sets appropriate timing based on text length.

## DrawBorderThenFill

Draws the outline first, then fills in the shape.

```python
class DrawBorderExample(Scene):
    def construct(self):
        square = Square(fill_opacity=0.8, color=BLUE)
        self.play(DrawBorderThenFill(square))
```

Best for: Shapes with fills where you want to emphasize the outline first.

## FadeIn / FadeOut

Simple opacity transitions.

```python
class FadeExample(Scene):
    def construct(self):
        circle = Circle()

        # Fade in
        self.play(FadeIn(circle))
        self.wait()

        # Fade out
        self.play(FadeOut(circle))
```

### Directional Fades

```python
# Fade in from a direction
self.play(FadeIn(square, shift=UP))      # Fade in while moving up
self.play(FadeIn(square, shift=LEFT))    # Fade in from right

# Fade out to a direction
self.play(FadeOut(square, shift=DOWN))   # Fade out while moving down
```

### Scale Fades

```python
self.play(FadeIn(circle, scale=0.5))   # Fade in while growing
self.play(FadeOut(circle, scale=2))    # Fade out while shrinking
```

## GrowFromCenter / ShrinkToCenter

```python
class GrowExample(Scene):
    def construct(self):
        circle = Circle()

        self.play(GrowFromCenter(circle))
        self.wait()
        self.play(ShrinkToCenter(circle))
```

## GrowFromPoint

Grow from a specific point.

```python
self.play(GrowFromPoint(circle, ORIGIN))
self.play(GrowFromPoint(circle, LEFT * 3))
```

## GrowFromEdge

Grow from a specific edge.

```python
self.play(GrowFromEdge(square, LEFT))   # Grow from left edge
self.play(GrowFromEdge(square, DOWN))   # Grow from bottom edge
```

## SpinInFromNothing

Object spins in while growing.

```python
self.play(SpinInFromNothing(circle))
```

## Uncreate

Reverse of Create - erases the mobject.

```python
self.play(Create(circle))
self.wait()
self.play(Uncreate(circle))  # Erases in reverse
```

## AddTextLetterByLetter

Types text one character at a time.

```python
class TypingExample(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(AddTextLetterByLetter(text, time_per_char=0.1))
```

Note: Only works with `Text`, not `MathTex`.

## Best Practices

1. **Use Write for text** - Looks more natural than Create
2. **Use Create for shapes** - Clean progressive drawing
3. **Use FadeIn for quick introductions** - When drawing isn't important
4. **Match removal to creation** - If you Create, use Uncreate; if FadeIn, use FadeOut

Choose the entrance from what the viewer needs to learn. `Write` and `Create` expose construction, while `FadeIn` presents an object as an already-complete fact. Matching entrance and removal supports visual symmetry when reversal is meaningful; a transform or different exit is clearer when the object changes role or hands information to the next state.


# Text Animations

Animations specifically designed for text and equations.

## Write

The most common text animation. Simulates handwriting.

```python
from manim import *

class WriteExample(Scene):
    def construct(self):
        text = Text("Hello World")
        equation = MathTex(r"E = mc^2")

        self.play(Write(text))
        self.wait()
        self.play(Write(equation))
```

### Write Parameters

```python
self.play(Write(
    text,
    run_time=2,           # Override auto-calculated time
    rate_func=linear,     # Timing curve
    reverse=False,        # Write backwards if True
))
```

Write automatically adjusts `run_time` based on text length.

## AddTextLetterByLetter

Types text one character at a time.

```python
class LetterByLetterExample(Scene):
    def construct(self):
        text = Text("Typing effect")

        self.play(AddTextLetterByLetter(
            text,
            time_per_char=0.1  # Speed of typing
        ))
```

**Note:** Only works with `Text`, not `MathTex`.

## RemoveTextLetterByLetter

Reverse of AddTextLetterByLetter - removes character by character.

```python
class RemoveLetterByLetter(Scene):
    def construct(self):
        text = Text("Disappearing text")
        self.add(text)

        self.play(RemoveTextLetterByLetter(
            text,
            time_per_char=0.05
        ))
```

## TypeWithCursor

Types text with a visible cursor.

```python
class TypeWithCursorExample(Scene):
    def construct(self):
        text = Text("Typing with cursor")

        # Create cursor
        cursor = Rectangle(
            color=GREY_A,
            fill_color=GREY_A,
            fill_opacity=1.0,
            height=1.1,
            width=0.1,
        )

        self.play(TypeWithCursor(text, cursor))

        # Optional: blink cursor after typing
        self.play(Blink(cursor, blinks=3))
```

### Cursor Customization

```python
# Line cursor
cursor = Line(UP * 0.5, DOWN * 0.5, color=WHITE, stroke_width=2)

# Block cursor
cursor = Rectangle(width=0.5, height=1, fill_opacity=0.8, color=WHITE)

# Custom cursor position
self.play(TypeWithCursor(
    text,
    cursor,
    buff=0.05,           # Space between text and cursor
    keep_cursor_y=True,  # Keep cursor at consistent height
    leave_cursor_on=True # Show cursor after animation
))
```

## Blink (for cursors)

```python
class BlinkExample(Scene):
    def construct(self):
        cursor = Rectangle(height=1, width=0.1, fill_opacity=1)
        self.add(cursor)

        self.play(Blink(cursor, blinks=5, time_on=0.3, time_off=0.3))
```

## Word by Word Animation

Using LaggedStart for word-by-word appearance:

```python
class WordByWord(Scene):
    def construct(self):
        # Split into individual Text objects
        words = VGroup(
            Text("Hello"),
            Text("World"),
            Text("!")
        ).arrange(RIGHT, buff=0.3)

        self.play(LaggedStart(
            *[Write(word) for word in words],
            lag_ratio=0.5
        ))
```

## Equation Transformations

Animate between equations:

```python
class EquationTransform(Scene):
    def construct(self):
        eq1 = MathTex(r"a^2 + b^2 = c^2")
        eq2 = MathTex(r"c = \sqrt{a^2 + b^2}")

        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
```

## Highlighting Text

```python
class HighlightText(Scene):
    def construct(self):
        text = Text("Important message")
        self.add(text)

        # Circumscribe (draw around)
        self.play(Circumscribe(text, color=YELLOW))

        # Indicate (pulse)
        self.play(Indicate(text, color=RED))

        # Flash
        self.play(Flash(text.get_center(), color=WHITE))
```

## Replacing Text

```python
class ReplaceText(Scene):
    def construct(self):
        text1 = Text("Before")
        text2 = Text("After")

        self.play(Write(text1))
        self.wait()

        # Transform text
        self.play(Transform(text1, text2))

        # Or replacement transform
        self.play(ReplacementTransform(text1, text2))
```

## Colored Text Animation

```python
class ColoredTextAnimation(Scene):
    def construct(self):
        text = Text("Colorful")
        self.play(Write(text))

        # Animate color change per letter
        self.play(LaggedStart(
            *[char.animate.set_color(random_bright_color()) for char in text],
            lag_ratio=0.1
        ))
```

## Best Practices

1. **Use Write for most text** - Natural and smooth
2. **Use AddTextLetterByLetter for "typing" effect** - Terminal/code aesthetics
3. **Use TypeWithCursor for interactive feel** - Good for tutorials
4. **Use TransformMatchingTex for equations** - Smooth mathematical transitions
5. **Adjust time_per_char for pacing** - 0.05-0.1 is usually good
6. **Only use Text (not MathTex) for letter-by-letter** - API limitation

The text effects above are defaults for moments when appearance order supports the explanation. Add or fade in text as a complete unit when the audience should read or compare it immediately; use `Write` or letter-by-letter effects when gradual construction carries meaning.


# Animation Groups

Control how multiple animations play together.

## AnimationGroup

Play multiple animations with controlled timing.

```python
from manim import *

class AnimationGroupExample(Scene):
    def construct(self):
        circles = VGroup(*[Circle() for _ in range(5)]).arrange(RIGHT)

        # All animations play simultaneously (lag_ratio=0)
        self.play(AnimationGroup(
            *[Create(c) for c in circles],
            lag_ratio=0
        ))
```

### lag_ratio Parameter

Controls the delay between animation starts:
- `lag_ratio=0`: All start simultaneously
- `lag_ratio=0.5`: Each starts when previous is 50% complete
- `lag_ratio=1`: Each starts when previous finishes (sequential)

```python
class LagRatioDemo(Scene):
    def construct(self):
        squares = VGroup(*[Square() for _ in range(4)]).arrange(RIGHT)

        # Staggered start - each begins when previous is 25% done
        self.play(AnimationGroup(
            *[FadeIn(s) for s in squares],
            lag_ratio=0.25,
            run_time=2
        ))
```

## LaggedStart

Convenience class with default `lag_ratio=0.05` (5% overlap).

```python
class LaggedStartExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)]).arrange(RIGHT)

        # Rapid staggered animation
        self.play(LaggedStart(
            *[GrowFromCenter(d) for d in dots],
            lag_ratio=0.1
        ))
```

### Common LaggedStart Patterns

```python
# Staggered fade in
self.play(LaggedStart(*[FadeIn(m) for m in mobjects], lag_ratio=0.2))

# Wave effect
self.play(LaggedStart(
    *[m.animate.shift(UP * 0.5) for m in mobjects],
    lag_ratio=0.1
))

# Staggered color change
self.play(LaggedStart(
    *[m.animate.set_color(RED) for m in mobjects],
    lag_ratio=0.15
))
```

## Succession

Play animations one after another (equivalent to `lag_ratio=1`).

```python
class SuccessionExample(Scene):
    def construct(self):
        circle = Circle().shift(LEFT * 2)
        square = Square()
        triangle = Triangle().shift(RIGHT * 2)

        # Animations play in sequence
        self.play(Succession(
            Create(circle),
            Create(square),
            Create(triangle)
        ))
```

### Succession vs Multiple play() Calls

```python
# These are equivalent:

# Using Succession
self.play(Succession(
    Create(circle),
    Create(square)
))

# Using separate play calls
self.play(Create(circle))
self.play(Create(square))
```

Succession is useful when you want to treat sequential animations as a single unit.

## Combining Group Types

```python
class CombinedExample(Scene):
    def construct(self):
        group1 = VGroup(*[Circle() for _ in range(3)]).arrange(RIGHT).shift(UP)
        group2 = VGroup(*[Square() for _ in range(3)]).arrange(RIGHT).shift(DOWN)

        # First group appears with stagger, then second group
        self.play(Succession(
            LaggedStart(*[Create(c) for c in group1], lag_ratio=0.2),
            LaggedStart(*[Create(s) for s in group2], lag_ratio=0.2)
        ))
```

## LaggedStartMap

Apply an animation to all submobjects of a mobject with staggered timing.

```python
class LaggedStartMapExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot(radius=0.16) for _ in range(35)]).arrange_in_grid(rows=5, cols=7)

        # Apply FadeIn to all dots with stagger
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.1))
        self.wait(0.5)

        # Change color with stagger using LaggedStart
        self.play(LaggedStart(
            *[dot.animate.set_color(YELLOW) for dot in dots],
            lag_ratio=0.05
        ))
```

LaggedStartMap is cleaner for applying the same animation to each submobject. For property changes, use LaggedStart with `.animate`.

## AnimationGroup with run_time

The total `run_time` is distributed among animations based on `lag_ratio`.

```python
self.play(AnimationGroup(
    *[Create(c) for c in circles],
    lag_ratio=0.5,
    run_time=4  # Total duration is 4 seconds
))
```

## Practical Examples

### Text Appearing Word by Word

```python
class WordByWord(Scene):
    def construct(self):
        words = VGroup(
            Text("Hello"),
            Text("World"),
            Text("!")
        ).arrange(RIGHT)

        self.play(LaggedStart(
            *[Write(w) for w in words],
            lag_ratio=0.5
        ))
```

### Grid Animation

```python
class GridAnimation(Scene):
    def construct(self):
        grid = VGroup(*[
            Square().scale(0.3)
            for _ in range(25)
        ]).arrange_in_grid(5, 5)

        # Diagonal wave effect
        self.play(LaggedStart(
            *[GrowFromCenter(s) for s in grid],
            lag_ratio=0.05
        ))
```

## Best Practices

1. **Use LaggedStart for visual polish** - Staggered animations look more dynamic
2. **Keep lag_ratio small (0.05-0.2)** - Too high feels slow
3. **Use Succession for distinct steps** - When animations are conceptually separate
4. **Adjust run_time with lag_ratio** - More items may need longer total time

Use staggered timing when it reveals order, grouping, propagation, or repeated structure, or when it reduces the load of many simultaneous entrances. Treat the suggested `lag_ratio` as a starting range: each item may need more separation when it carries information that must be read independently.


# Animation Timing

Control the speed and feel of animations with timing parameters.

## run_time

Controls how long an animation takes in seconds.

```python
from manim import *

class RunTimeExample(Scene):
    def construct(self):
        circle = Circle()

        # Default (1 second)
        self.play(Create(circle))

        # Longer animation
        self.play(circle.animate.shift(RIGHT), run_time=3)

        # Quick animation
        self.play(circle.animate.set_color(RED), run_time=0.5)
```

## Rate Functions

Rate functions control how the animation progresses over time (easing).

### Using Rate Functions

```python
self.play(
    circle.animate.shift(RIGHT),
    rate_func=smooth
)
```

### Common Rate Functions

```python
# Smooth start and end (default for most animations)
smooth

# Constant speed
linear

# Start slow, end fast
rush_into

# Start fast, end slow
rush_from

# Go there and back
there_and_back

# Go there and back with pause
there_and_back_with_pause

# Double smooth (extra smooth)
double_smooth

# Stay put (useful for delays in AnimationGroup)
lingering
```

### Ease Functions (CSS-like)

```python
# Ease in (start slow)
ease_in_sine
ease_in_quad
ease_in_cubic
ease_in_expo
ease_in_circ
ease_in_back    # Slight overshoot at start

# Ease out (end slow)
ease_out_sine
ease_out_quad
ease_out_cubic
ease_out_expo
ease_out_circ
ease_out_back   # Slight overshoot at end
ease_out_bounce # Bouncy ending

# Ease in-out (slow at both ends)
ease_in_out_sine
ease_in_out_quad
ease_in_out_cubic
ease_in_out_expo
ease_in_out_circ
ease_in_out_back
```

## Visual Comparison

```python
class RateFuncComparison(Scene):
    def construct(self):
        funcs = [linear, smooth, rush_into, rush_from, there_and_back]
        names = ["linear", "smooth", "rush_into", "rush_from", "there_and_back"]

        dots = VGroup()
        labels = VGroup()

        for i, (func, name) in enumerate(zip(funcs, names)):
            dot = Dot().shift(LEFT * 4 + DOWN * i)
            label = Text(name, font_size=24).next_to(dot, LEFT)
            dots.add(dot)
            labels.add(label)

        self.add(dots, labels)

        self.play(*[
            dot.animate(rate_func=func).shift(RIGHT * 8)
            for dot, func in zip(dots, funcs)
        ], run_time=3)
```

## Combining run_time and rate_func

```python
self.play(
    square.animate.shift(RIGHT * 3),
    run_time=2,
    rate_func=ease_out_bounce
)
```

## there_and_back

Animation goes forward then reverses.

```python
class ThereAndBackExample(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # Moves right then back to start
        self.play(
            square.animate.shift(RIGHT * 2),
            rate_func=there_and_back,
            run_time=2
        )
```

## Custom Rate Functions

Create your own rate function (takes t from 0 to 1, returns progress 0 to 1):

```python
def my_rate_func(t):
    # Quadratic ease
    return t ** 2

self.play(
    circle.animate.shift(RIGHT),
    rate_func=my_rate_func
)
```

## wait() Timing

```python
# Wait for default time (1 second)
self.wait()

# Wait for specific duration
self.wait(2)    # 2 seconds
self.wait(0.5)  # Half second
```

## Animation Speed Multiplier

Using `run_time` on AnimationGroup affects all children:

```python
self.play(AnimationGroup(
    Create(circle),
    Create(square),
    lag_ratio=0.5
), run_time=3)  # Total duration is 3 seconds
```

## Best Practices

1. **Use smooth for most animations** - Looks natural
2. **Use linear for constant motion** - Mechanical/precise movement
3. **Use ease_out_bounce for playful effects** - Attention-grabbing
4. **Keep run_time between 0.5-3 seconds** - Maintain viewer attention
5. **Use there_and_back for emphasis** - Show something temporarily
6. **Match rate_func to content** - Smooth for elegant, bouncy for fun

The `0.5-3` second range is the general starting range for standalone actions; the `0.5-2` second guidance in [animations.md](animations.md) is its narrower quick-reference range for simple actions. Neither is a delivery constraint. Longer transformations and shorter micro-actions are appropriate when their distance, complexity, synchronization, or repetition calls for them.

## Explanatory Timing Guidance

1. **Time for comprehension** - Allow enough time to notice the change, read new information, and connect it to the previous state.
2. **Match duration to information density** - A subtle highlight can be brief; a new equation, unfamiliar diagram, or important transformation usually needs more time.
3. **Use pauses as observation time** - Add `wait()` when the viewer needs to inspect or infer something. Continue directly when the next motion completes the same thought.
4. **Synchronize semantic beats** - When narration or music is present, align the relevant visual change with the phrase or beat that gives it meaning.
5. **Match easing to physical and conceptual behavior** - Use `linear` for constant rates, smooth easing for state changes, and expressive easing only when it supports the subject's tone.
6. **Vary tempo by explanatory importance** - Slow down around decisions and structural insights; compress familiar or repetitive operations.
7. **Review the whole sequence at normal speed** - Timing that feels acceptable one animation at a time may become rushed, repetitive, or inert in context.


# ManimCE 动画与标注工具速查

题目讲解视频的全部可用动画类和标注工具。按教学场景分组，每组按使用频率排序。

## 一、动画类

### 创建与书写 (animation.creation)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `Write` | 模拟手写文字或手绘图形 | `self.play(Write(formula))` |
| `Create` | 沿路径逐步绘制 VMobject | `self.play(Create(circle))` |
| `DrawBorderThenFill` | 先画边框再填充 | `self.play(DrawBorderThenFill(rect))` |
| `AddTextLetterByLetter` | 逐字显示文本 | `self.play(AddTextLetterByLetter(text))` |
| `TypeWithCursor` | 带光标的打字效果 | `self.play(TypeWithCursor(text))` |
| `Uncreate` | Create 的逆过程 | `self.play(Uncreate(shape))` |
| `Unwrite` | Write 的逆过程（模拟擦除） | `self.play(Unwrite(formula))` |
| `ShowIncreasingSubsets` | 逐个显示子对象（保留已显示的） | `self.play(ShowIncreasingSubsets(group))` |
| `ShowSubmobjectsOneByOne` | 逐个显示子对象（移除前一个） | `self.play(ShowSubmobjectsOneByOne(group))` |
| `SpiralIn` | 子对象沿螺旋轨迹飞入 | `self.play(SpiralIn(group))` |
| `RemoveTextLetterByLetter` | 逐字移除文本 | `self.play(RemoveTextLetterByLetter(text))` |

### 出场与退场 (animation.fading + animation.growing)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `FadeIn` | 淡入，可带方向 | `self.play(FadeIn(obj, shift=UP))` |
| `FadeOut` | 淡出，可带方向 | `self.play(FadeOut(obj, shift=DOWN))` |
| `GrowFromCenter` | 从中心放大出场 | `self.play(GrowFromCenter(obj))` |
| `GrowFromEdge` | 从边缘生长出场 | `self.play(GrowFromEdge(obj, LEFT))` |
| `GrowFromPoint` | 从指定点生长出场 | `self.play(GrowFromPoint(obj, ORIGIN))` |
| `GrowArrow` | 箭头从起点向终点生长 | `self.play(GrowArrow(arrow))` |
| `SpinInFromNothing` | 旋转放大出场 | `self.play(SpinInFromNothing(obj))` |
| `ShrinkToCenter` | 缩小到中心消失 | `self.play(ShrinkToCenter(obj))` |

### 变换 (animation.transform)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `Transform` | 将源变形为目标形状（源变量保持引用） | `self.play(Transform(a, b))` |
| `ReplacementTransform` | 替换变换（源移除，目标加入场景） | `self.play(ReplacementTransform(a, b))` |
| `TransformFromCopy` | 保留原件，复制品变换为目标 | `self.play(TransformFromCopy(a, b))` |
| `FadeTransform` | 淡入淡出式变换 | `self.play(FadeTransform(a, b))` |
| `FadeTransformPieces` | 子对象级别的淡入淡出变换 | `self.play(FadeTransformPieces(a, b))` |
| `MoveToTarget` | 变换到预设的 target 状态 | `obj.generate_target(); obj.target.shift(RIGHT); self.play(MoveToTarget(obj))` |
| `ApplyMatrix` | 应用矩阵变换 | `self.play(ApplyMatrix([[1,1],[0,1]], obj))` |
| `Restore` | 恢复到上次保存的状态 | `obj.save_state(); ...; self.play(Restore(obj))` |
| `ClockwiseTransform` | 沿顺时针弧线变换 | `self.play(ClockwiseTransform(a, b))` |
| `CounterclockwiseTransform` | 沿逆时针弧线变换 | `self.play(CounterclockwiseTransform(a, b))` |
| `ScaleInPlace` | 原地缩放 | `self.play(ScaleInPlace(obj, 2))` |
| `FadeToColor` | 颜色渐变 | `self.play(FadeToColor(obj, RED))` |
| `CyclicReplace` / `Swap` | 多个对象循环换位 | `self.play(CyclicReplace(a, b, c))` |
| `.animate` 链式语法 | 链式调用任意方法 | `self.play(obj.animate.shift(RIGHT).scale(1.5).set_color(BLUE))` |

### 公式匹配变换 (animation.transform_matching_parts)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `TransformMatchingTex` | 按 TeX 子串匹配变换公式 | `self.play(TransformMatchingTex(eq1, eq2))` |
| `TransformMatchingShapes` | 按形状路径匹配变换 | `self.play(TransformMatchingShapes(text1, text2))` |

配合 `{{ }}` 双大括号语法效果最佳：`MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")`

### 焦点强调 (animation.indication)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `Indicate` | 临时放大并变色以引起注意 | `self.play(Indicate(formula, color=YELLOW))` |
| `Circumscribe` | 绘制临时环绕线 | `self.play(Circumscribe(formula, color=YELLOW))` |
| `Flash` | 从一点向外发射线条 | `self.play(Flash(point, color=YELLOW))` |
| `FocusOn` | 聚光灯收缩到一个位置 | `self.play(FocusOn(obj))` |
| `Wiggle` | 左右摇晃 | `self.play(Wiggle(obj))` |
| `ApplyWave` | 波浪扭曲效果 | `self.play(ApplyWave(obj))` |
| `ShowPassingFlash` | 沿 VMobject 路径的闪光滑过 | `self.play(ShowPassingFlash(line.copy()))` |

### 旋转 (animation.rotation)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `Rotate` | 旋转指定角度（**优先用这个而非 .animate.rotate**） | `self.play(Rotate(obj, angle=PI/2))` |
| `Rotating` | 持续旋转（适合 updater 场景） | `self.play(Rotating(obj, radians=TAU, run_time=2))` |

> `.animate.rotate(PI)` 因起止状态相同不产生视觉效果，始终用 `Rotate` 类。

### 沿路径运动 (animation.movement)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `MoveAlongPath` | 沿另一个 VMobject 的路径移动 | `self.play(MoveAlongPath(dot, curve))` |
| `Homotopy` | 自定义点映射的连续变形 | `self.play(Homotopy(lambda x,y,z,t: ..., obj))` |

### 编排控制 (animation.composition)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `AnimationGroup` | 同时播放一组动画 | `self.play(AnimationGroup(FadeIn(a), Create(b)))` |
| `LaggedStart` | 依次启动，每个延迟 `lag_ratio` | `self.play(LaggedStart(*[FadeIn(m) for m in group], lag_ratio=0.2))` |
| `LaggedStartMap` | LaggedStart + map 简写 | `self.play(LaggedStartMap(FadeIn, group, lag_ratio=0.15))` |
| `Succession` | 依次播放（上一个结束后下一个开始） | `self.play(Succession(FadeIn(a), FadeIn(b), FadeIn(c)))` |
| `ChangeSpeed` | 修改动画的速度曲线 | `self.play(ChangeSpeed(Create(obj), speedinfo={0.5: 0.2}))` |

### 数值动画 (animation.numbers)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `ChangeDecimalToValue` | 将 DecimalNumber 线性插值到目标值 | `self.play(ChangeDecimalToValue(num, 100))` |
| `ChangingDecimal` | 用自定义函数驱动 DecimalNumber | `self.play(ChangingDecimal(num, lambda t: t**2))` |

### 更新器动画 (animation.updaters)

| 动画 | 描述 | 典型用法 |
|------|------|---------|
| `UpdateFromFunc` | 每帧执行 `func(mobject)` | `self.play(UpdateFromFunc(dot, lambda m: m.move_to(...)))` |
| `UpdateFromAlphaFunc` | 带插值参数 alpha 的更新 | `self.play(UpdateFromAlphaFunc(obj, lambda m, a: m.set_opacity(a)))` |

### 其他

| 动画 | 描述 |
|------|------|
| `Broadcast` | 从 mobject 向外广播扩散效果 |
| `Wait` | 无操作等待 |
| `Add` | 静态添加到场景（无动画效果） |


## 三、常用 rate_func（缓动函数）

传给动画的 `rate_func` 参数控制动画节奏：

| 缓动 | 效果 | 适用场景 |
|------|------|---------|
| `smooth` | 慢→快→慢（默认） | 大多数动画 |
| `linear` | 匀速 | 持续旋转、匀速滑动 |
| `rush_into` | 慢→快 | 入场加速 |
| `rush_from` | 快→慢 | 停下减速 |
| `there_and_back` | 去→回 | 临时强调后恢复 |
| `there_and_back_with_pause` | 去→停→回 | 强调后停顿再恢复 |
| `ease_in_sine` / `ease_out_sine` | 正弦缓入/缓出 | 自然运动 |
| `ease_in_out_bounce` | 弹跳效果 | 活泼的入场 |
| `double_smooth` | 双段平滑 | 两阶段变化 |
| `lingering` | 结尾停留更久 | 让观众看清结果 |


# 补充：文字动画

## AddTextWordByWord

逐词显示文本（相比 AddTextLetterByLetter 更自然）。

```python
text = Text("这是一段逐词出现的文字", font=CJK_FONT, font_size=36)
self.play(AddTextWordByWord(text), run_time=3)
```

## UntypeWithCursor

TypeWithCursor 的反向——带光标逐字删除。

```python
text = Text("将被删除的文字", font=CJK_FONT)
self.add(text)
self.play(UntypeWithCursor(text), run_time=2)
```

## ApplyFunction

对 Mobject 应用任意变换函数。

```python
circle = Circle()
# 函数接收 mobject，返回变换后的 mobject
self.play(ApplyFunction(lambda m: m.scale(2).set_color(RED).shift(UP), circle))
```

## MaintainPositionRelativeTo

在另一个对象做动画时，让当前对象保持相对位置不变。

```python
dot = Dot()
label = Text("标签", font=CJK_FONT).next_to(dot, UP)
self.play(
    dot.animate.shift(RIGHT * 3),
    MaintainPositionRelativeTo(label, dot),
    run_time=2,
)
```
