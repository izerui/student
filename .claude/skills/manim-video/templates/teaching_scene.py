"""教学视频场景模板 —— 含 AudioManager + 布局守卫。

使用方法：
  1. 写 segments.json（分段旁白 + cue）
  2. node scripts/narrate.mjs <slug>
  3. 基于本模板编写场景代码
  4. python3 scripts/manim_cli.py check  <slug>
  5. python3 scripts/manim_cli.py layout <slug>
  6. python3 scripts/manim_cli.py render <slug> -q draft
  7. python3 scripts/manim_cli.py stills <slug> 3 8 15
  8. python3 scripts/manim_cli.py render <slug> -q final
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
        add_background(self)        # 可选：默认黑板纹理，可传 image= 或 color=
        enable_layout_guard(self)   # 必需：越界/重叠/静止检测
        audio = AudioManager(self)

        # —— 第 1 段旁白 ——
        d = audio.start("s1")
        audio.wait_for_cue("c1")

        title = Text("标题", font=CJK_FONT, font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)

        audio.end(d)

        # —— 第 2 段旁白 ——
        # d = audio.start("s2")
        # audio.wait_for_cue("c2")
        # self.play(...)
        # audio.end(d)
