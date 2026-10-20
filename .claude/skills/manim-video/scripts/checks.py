#!/usr/bin/env python3
"""ManimCE 工程检查合集。

由 manim_cli.py 调用，不需要直接运行。包含：
  - 结构与 API 检查（原 check.py）
  - LaTeX 预编译（原 preflight_tex.py）
  - 旁白产物校验（原 validate_audio.py）
  - cue 消费完整性（原 validate_cue_consumption.py）
"""

# ============================================================================
# 结构与 API 检查
# ============================================================================

"""
ManimCE 教学视频代码检查脚本。

验证 script.py 是否具备可运行的场景、音频契约和基本工程完整性。
不规定动画类型、布局方式或视觉风格。

使用方法:
    python scripts/check.py [script_file]
"""

import ast
import sys
import re
from pathlib import Path


class _FunctionNameOrderVisitor(ast.NodeVisitor):
    """Collect local definitions and loads without descending into nested scopes."""

    def __init__(self, root):
        self.root = root
        self.definitions = {}
        self.loads = []
        self.globals = set()
        for argument in (*root.args.posonlyargs, *root.args.args, *root.args.kwonlyargs):
            self.definitions[argument.arg] = 0
        if root.args.vararg:
            self.definitions[root.args.vararg.arg] = 0
        if root.args.kwarg:
            self.definitions[root.args.kwarg.arg] = 0

    def visit_FunctionDef(self, node):
        if node is self.root:
            for statement in node.body:
                self.visit(statement)
            return
        self.definitions.setdefault(node.name, node.lineno)

    def visit_AsyncFunctionDef(self, node):
        if node is self.root:
            for statement in node.body:
                self.visit(statement)
            return
        self.definitions.setdefault(node.name, node.lineno)

    def visit_ClassDef(self, node):
        self.definitions.setdefault(node.name, node.lineno)

    def visit_Lambda(self, node):
        return

    def visit_ListComp(self, node):
        return

    def visit_SetComp(self, node):
        return

    def visit_GeneratorExp(self, node):
        return

    def visit_DictComp(self, node):
        return

    def visit_Global(self, node):
        self.globals.update(node.names)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.definitions.setdefault(node.id, node.lineno)
        elif isinstance(node.ctx, ast.Load):
            self.loads.append((node.id, node.lineno))

    def visit_Import(self, node):
        for alias in node.names:
            self.definitions.setdefault(alias.asname or alias.name.split(".")[0], node.lineno)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            if alias.name != "*":
                self.definitions.setdefault(alias.asname or alias.name, node.lineno)

class CodeChecker:
    """代码结构检查器。"""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.errors = []
        self.warnings = []
        self.tree = None
        self.source = ""
        self.scene_classes = set()
        self.all_calls = set()
        self.all_methods = set()

    def parse(self):
        if not self.file_path.exists():
            self.errors.append(f"文件不存在: {self.file_path}")
            return False
        try:
            self.source = self.file_path.read_text(encoding='utf-8')
            self.tree = ast.parse(self.source)
            return True
        except SyntaxError as e:
            self.errors.append(f"语法错误: {e}")
            return False

    def analyze(self):
        if not self.tree:
            return
        scene_bases = {"Scene", "ThreeDScene", "MovingCameraScene"}
        for node in ast.iter_child_nodes(self.tree):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    if (isinstance(base, ast.Name) and base.id in scene_bases) or \
                       (isinstance(base, ast.Attribute) and base.attr in scene_bases):
                        self.scene_classes.add(node.name)
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        self.all_methods.add(item.name)
                        for sub in ast.walk(item):
                            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute):
                                self.all_calls.add(sub.func.attr)

    def check_scene_class(self):
        """通用问题：场景必须继承 Scene 基类。"""
        if not self.scene_classes:
            self.errors.append("未找到继承自 Scene 的类")

    def check_scene_structure(self):
        """通用问题：场景必须包含实际动画调用。"""
        has_scene_action = bool({'play', 'add', 'add_sound'} & self.all_calls)
        if not has_scene_action:
            self.errors.append(
                "场景没有发现 add()、play() 或 add_sound() 调用\n"
                "  请确认 construct() 包含实际的 ManimCE 场景逻辑"
            )

    def check_audio_usage(self):
        """通用问题：使用 AudioManager 时 start/end 必须配对。"""
        has_audio_manager = 'AudioManager(' in self.source
        has_start = 'start' in self.all_calls
        has_end = 'end' in self.all_calls

        if not has_audio_manager:
            self.warnings.append(
                "未使用 AudioManager\n"
                "  如果有音频需要同步，请使用 AudioManager"
            )
            return

        if has_start and not has_end:
            self.errors.append(
                "调用了 audio.start() 但未调用 audio.end()\n"
                "  每个 start() 必须有对应的 end() 防止音频重叠"
            )

    def check_audio_manager_definition(self):
        """调用 AudioManager 前必须先导入或定义它。

        通用问题：调用 AudioManager 时必须有其定义或导入。
        """
        if self.tree is None:
            return

        uses_audio_manager = any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "AudioManager"
            for node in ast.walk(self.tree)
        )
        if not uses_audio_manager:
            return

        defined_names = {
            node.name
            for node in ast.iter_child_nodes(self.tree)
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
        }
        imported_names = {
            alias.asname or alias.name
            for node in ast.walk(self.tree)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
            if alias.name != "*"
        }
        if "AudioManager" not in defined_names and "AudioManager" not in imported_names:
            self.errors.append(
                "调用了 AudioManager(...)，但脚本中没有 AudioManager 定义或导入\n"
                "  在文件顶部加上: from teaching_runtime import AudioManager"
            )

    def check_audio_timing_contract(self):
        """Require scene narration to hold until the duration returned by start().

        通用问题：旁白时长必须传给 end() 以保证音画覆盖。
        """
        if self.tree is None:
            return

        for class_node in ast.iter_child_nodes(self.tree):
            if not isinstance(class_node, ast.ClassDef) or class_node.name not in self.scene_classes:
                continue
            audio_receivers = set()
            for node in ast.walk(class_node):
                if (
                    isinstance(node, ast.Assign)
                    and isinstance(node.value, ast.Call)
                    and isinstance(node.value.func, ast.Name)
                    and node.value.func.id == "AudioManager"
                ):
                    audio_receivers.update(
                        self._attribute_path(target)
                        for target in node.targets
                        if isinstance(target, (ast.Name, ast.Attribute))
                    )
            for function in class_node.body:
                if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                assignments = {
                    id(node.value): self._attribute_path(node.targets[0])
                    for node in ast.walk(function)
                    if isinstance(node, ast.Assign)
                    and len(node.targets) == 1
                    and isinstance(node.targets[0], (ast.Name, ast.Attribute))
                    and isinstance(node.value, ast.Call)
                }
                active_starts = {}
                calls = sorted(
                    (node for node in ast.walk(function) if isinstance(node, ast.Call)),
                    key=lambda node: (node.lineno, node.col_offset),
                )
                for node in calls:
                    if (
                        not isinstance(node.func, ast.Attribute)
                        or self._attribute_path(node.func.value) not in audio_receivers
                    ):
                        continue
                    receiver = self._attribute_path(node.func.value)
                    if node.func.attr == "start":
                        if receiver in active_starts:
                            start_line = active_starts[receiver]
                            self.errors.append(
                                f"第 {node.lineno} 行: 开始下一段旁白前，未结束第 {start_line} 行启动的旁白\n"
                                "  每段使用 duration = audio.start(scene_id)，完成本段画面后调用 audio.end(duration)"
                            )
                        duration_name = assignments.get(id(node))
                        if not duration_name:
                            self.errors.append(
                                f"第 {node.lineno} 行: audio.start() 的返回时长未保存\n"
                                "  使用 duration = audio.start(scene_id)，并在本段末尾调用 audio.end(duration)"
                            )
                        active_starts[receiver] = node.lineno
                        continue
                    if node.func.attr != "end":
                        continue
                    duration_arg = node.args[0] if node.args else next(
                        (
                            keyword.value
                            for keyword in node.keywords
                            if keyword.arg in {"expected", "expected_duration", "duration"}
                        ),
                        None,
                    )
                    invalid = duration_arg is None or isinstance(duration_arg, ast.Constant)
                    if invalid:
                        self.errors.append(
                            f"第 {node.lineno} 行: audio.end() 必须接收当前场景的完整旁白时长\n"
                            "  使用 duration = audio.start(scene_id)，并在场景末尾调用 audio.end(duration)"
                        )
                    active_starts.pop(receiver, None)
                for receiver, start_line in active_starts.items():
                    self.errors.append(
                        f"第 {start_line} 行: {receiver}.start() 启动的旁白在当前方法结束前没有对应 end()\n"
                        "  在本段画面完成后调用 audio.end(duration)，再进入下一段"
                    )

    def check_tex_inputs(self):
        """Reject text and malformed literal input before invoking LaTeX.

        通用问题（非引擎怪癖）：LaTeX 不接受未配置 CJK 支持的汉字；大括号不配对必然编译失败。
        """
        if self.tree is None:
            return

        tex_calls = {"Tex", "MathTex", "SafeMathTex"}
        # 保持与原实现一致的转义写法，避免源文件编码差异影响匹配范围。
        cjk_pattern = re.compile("[\\u3400-\\u4dbf\\u4e00-\\u9fff]")
        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Call):
                continue
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else None
            )
            if name not in tex_calls:
                continue

            for arg in node.args:
                try:
                    value = ast.literal_eval(arg)
                except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
                    continue
                if not isinstance(value, str):
                    continue
                if cjk_pattern.search(value):
                    self.errors.append(
                        f"第 {arg.lineno} 行: {name}() 参数包含中文字符\n"
                        "  中文使用 Text(..., font=CJK_FONT)，公式使用 MathTex(...)，再用 VGroup 排列"
                    )
                if self._has_unbalanced_tex_braces(value):
                    self.errors.append(
                        f"第 {arg.lineno} 行: {name}() 的 LaTeX 大括号不匹配\n"
                        f"  公式片段: {value[:120]}"
                    )

    @staticmethod
    def _has_unbalanced_tex_braces(value):
        depth = 0
        index = 0
        while index < len(value):
            character = value[index]
            if character == "\\":
                slash_count = 1
                while index + slash_count < len(value) and value[index + slash_count] == "\\":
                    slash_count += 1
                next_index = index + slash_count
                if slash_count % 2 == 1 and next_index < len(value) and value[next_index] in "{}":
                    index = next_index + 1
                    continue
                index = next_index
                continue
            if character == "{":
                depth += 1
            elif character == "}":
                depth -= 1
                if depth < 0:
                    return True
            index += 1
        return depth != 0

    def check_audio_api_misuse(self):
        """Reject calling AudioManager methods on the Scene.

        wait_for_cue 是 teaching_runtime 的 AudioManager 方法，不属于 Scene。
        """
        if self.tree is None:
            return

        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr == "wait_for_cue" and isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                self.errors.append(
                    f"第 {node.lineno} 行: wait_for_cue() 属于 AudioManager，不属于 Scene\n"
                    "  保存 audio = AudioManager(self)，然后调用 audio.wait_for_cue(...)"
                )

    # ManimGL → ManimCE 迁移期专用拦截。
    # 引擎怪癖类规则：仅在 ManimCE 环境有效。当仓库中不再出现 ManimGL 写法后可以移除。
    # 名称到替代写法的映射，值为 (替代写法, 补充说明)。
    _GL_NAME_REPLACEMENTS = {
        "ShowCreation": ("Create", "ManimCE 的绘制动画是 Create"),
        "TexText": ("Tex", "ManimCE 的 Tex 就是文本模式；数学公式用 MathTex"),
    }
    _GL_METHOD_REPLACEMENTS = {
        "set_backstroke": ("set_stroke", "ManimCE 没有 set_backstroke"),
        "fix_in_frame": ("add_fixed_in_frame_mobjects", "ManimCE 由 Scene 登记固定对象"),
    }

    def check_manimgl_leftovers(self):
        """Reject ManimGL-only names that silently mean something else in ManimCE."""
        if self.tree is None:
            return

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] == "manimlib":
                self.errors.append(
                    f"第 {node.lineno} 行: 使用了 ManimGL 的 from manimlib import\n"
                    "  改为 from manim import *"
                )
                continue

            if not isinstance(node, ast.Call):
                continue

            if isinstance(node.func, ast.Name) and node.func.id in self._GL_NAME_REPLACEMENTS:
                replacement, note = self._GL_NAME_REPLACEMENTS[node.func.id]
                self.errors.append(
                    f"第 {node.lineno} 行: {node.func.id}() 属于 ManimGL\n"
                    f"  改用 {replacement}()；{note}"
                )

            if isinstance(node.func, ast.Attribute) and node.func.attr in self._GL_METHOD_REPLACEMENTS:
                replacement, note = self._GL_METHOD_REPLACEMENTS[node.func.attr]
                self.errors.append(
                    f"第 {node.lineno} 行: {node.func.attr}() 属于 ManimGL\n"
                    f"  改用 {replacement}()；{note}"
                )

            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else None
            )
            if name in {"Tex", "MathTex", "SafeMathTex"}:
                for keyword in node.keywords:
                    if keyword.arg == "t2c":
                        self.errors.append(
                            f"第 {node.lineno} 行: {name}() 不支持 t2c 参数\n"
                            "  ManimCE 使用 tex_to_color_map={...}；Text() 才用 t2c"
                        )

    @staticmethod
    def _attribute_path(node):
        parts = []
        while isinstance(node, ast.Attribute):
            parts.append(node.attr)
            node = node.value
        if isinstance(node, ast.Name):
            parts.append(node.id)
        return ".".join(reversed(parts))

    def check_markdown_math_in_text(self):
        """Markdown math delimiters render literally in ManimCE Text.

        通用问题：Markdown 公式分隔符在 ManimCE Text 中会原样显示。
        """
        if not self.tree:
            return
        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Call):
                continue
            name = node.func.id if isinstance(node.func, ast.Name) else None
            if name != "Text":
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str) and "$" in arg.value:
                    self.errors.append(
                        f"第 {arg.lineno} 行: Text() 包含 Markdown 公式分隔符 '$'\n"
                        "  $...$ 只适用于 Markdown/网页文本；请将公式拆为 MathTex，中文保留在 Text()"
                    )

    def check_latex_string_escaping(self):
        """Reject LaTeX commands that Python will consume as string escapes.

        通用问题：非 raw 字符串中的反斜杠会被 Python 解释为控制字符。
        """
        if not self.tree or not self.source:
            return

        math_calls = {"Tex", "MathTex"}
        literal_prefix = re.compile(r"^\s*([rubfRUBF]*)(?:'''|\"\"\"|'|\")")
        backslash_runs = re.compile(r"\\+")

        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Call):
                continue
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else None
            )
            if name not in math_calls:
                continue

            for arg in node.args:
                for literal in ast.walk(arg):
                    if not isinstance(literal, (ast.Constant, ast.JoinedStr)):
                        continue
                    if isinstance(literal, ast.Constant) and not isinstance(literal.value, str):
                        continue
                    segment = ast.get_source_segment(self.source, literal)
                    if not segment:
                        continue
                    prefix_match = literal_prefix.match(segment)
                    if not prefix_match or "r" in prefix_match.group(1).lower():
                        continue
                    if not any(len(match.group(0)) % 2 == 1 for match in backslash_runs.finditer(segment)):
                        continue

                    self.errors.append(
                        f"第 {literal.lineno} 行: {name}() 中的 LaTeX 命令使用了非 raw Python 字符串\n"
                        "  反斜杠可能被 Python 解释为制表符、换页符或其他控制字符；"
                        f"改用 {name}(R\"\\vec{{a}}\")，或将每个反斜杠写成双反斜杠"
                    )

    def check_use_before_assignment(self):
        """Reject local names read before their first assignment in a scene method.

        通用问题：局部对象在定义前引用会导致运行时 NameError。
        """
        if self.tree is None:
            return
        reported = set()
        for class_node in ast.iter_child_nodes(self.tree):
            if not isinstance(class_node, ast.ClassDef) or class_node.name not in self.scene_classes:
                continue
            for function in class_node.body:
                if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                visitor = _FunctionNameOrderVisitor(function)
                visitor.visit(function)
                for name, load_line in visitor.loads:
                    definition_line = visitor.definitions.get(name)
                    key = (function.name, name)
                    if (
                        name not in visitor.globals
                        and definition_line is not None
                        and definition_line > load_line
                        and key not in reported
                    ):
                        reported.add(key)
                        self.errors.append(
                            f"第 {load_line} 行: 局部对象 {name!r} 在第 {definition_line} 行定义前已被引用\n"
                            "  先创建对象，再把它加入 VGroup、列表或阶段清理集合"
                        )

    def check_construct_flow(self):
        """起步模板的占位 construct 必须替换为实际场景代码。"""
        if self.tree is None:
            return
        for node in ast.iter_child_nodes(self.tree):
            if not isinstance(node, ast.ClassDef) or node.name not in self.scene_classes:
                continue
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == 'construct':
                    body_src = ast.get_source_segment(self.source, item)
                    if body_src and 'pass' == body_src.strip().split('\n')[-1].strip():
                        self.errors.append(
                            f"{node.name}.construct() 以 pass 结尾\n"
                            "  起步模板的示例 construct 需要替换为实际场景代码"
                        )

    def check_layout_guard(self):
        """construct 必须启用布局守卫。

        背景是可选的（想要黑板底就调 add_background，不要就不调），
        但守卫不可省：越界、重叠和「有旁白却画面不动」全靠它发现。
        不开守卫，`layout` 命令就拿不到任何报告，等于跳过了渲染前唯一的硬闸门。
        """
        if self.tree is None:
            return
        for node in ast.iter_child_nodes(self.tree):
            if not isinstance(node, ast.ClassDef) or node.name not in self.scene_classes:
                continue
            for item in node.body:
                if not isinstance(item, ast.FunctionDef) or item.name != 'construct':
                    continue
                has_guard = any(
                    isinstance(call, ast.Call)
                    and isinstance(call.func, ast.Name)
                    and call.func.id == "enable_layout_guard"
                    for call in ast.walk(item)
                )
                if not has_guard:
                    self.errors.append(
                        f"{node.name}.construct() 没有调用 enable_layout_guard(self)\n"
                        "  在 construct 开头调用 enable_layout_guard(self)，否则越界、重叠和旁白静止都检测不到"
                    )

    # 在黑板底（最亮区 RGB 60,102,83）上按 WCAG 相对亮度实测的对比度。
    # 低于 4.0 的原色在小字号下发灰，运行时的语义色板是照同一口径挑的。
    _LOW_CONTRAST_COLORS = {
        "GREY": 1.84, "GRAY": 1.84, "DARK_GREY": 1.84, "DARK_GRAY": 1.84,
        "LIGHT_GREY": 2.6, "LIGHT_GRAY": 2.6,
        "RED": 2.18, "DARK_BLUE": 1.9, "PURPLE": 2.2, "DARK_BROWN": 1.6,
        "GREEN": 3.04, "BLUE": 3.22, "TEAL": 3.46, "MAROON": 2.7,
    }
    _PALETTE_HINT = "INK/ACCENT/CORRECT/SECOND/DATA/WRONG/MUTED"

    def check_board_contrast(self):
        """绿色黑板上用低对比原色，小字号会发灰看不清。

        运行时导出了一组按同一口径验过对比度的语义色，按语义取用即可，
        不必自己配色——五条成片曾出现 16 个互不相同的十六进制色值。
        """
        if self.tree is None:
            return

        hits = {}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Name) and node.id in self._LOW_CONTRAST_COLORS:
                hits.setdefault(node.id, []).append(node.lineno)
        if not hits:
            return

        parts = []
        for name in sorted(hits, key=lambda n: self._LOW_CONTRAST_COLORS[n]):
            lines = sorted(set(hits[name]))
            shown = ", ".join(str(n) for n in lines[:6])
            more = f" 等 {len(lines)} 处" if len(lines) > 6 else ""
            parts.append(f"    {name}（对比度 {self._LOW_CONTRAST_COLORS[name]:.2f}）第 {shown} 行{more}")
        self.warnings.append(
            "在黑板底上使用了低对比原色，小字号会发灰：\n"
            + "\n".join(parts)
            + f"\n  改用 teaching_runtime 的语义色：{self._PALETTE_HINT}"
        )

    def check_indicate_usage(self):
        """Indicate 会把整个家族染成同色，容器里的浅色文字会被填充色吞掉。"""
        if self.tree is None:
            return

        # 已经自己封装了 pulse 的，说明作者知道这件事，内部用 Indicate 是实现细节
        if "pulse" in self.all_methods or re.search(r"^\s*def\s+_?pulse\b", self.source, re.M):
            return

        lines = sorted({
            node.lineno for node in ast.walk(self.tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "Indicate"
        })
        if not lines:
            return
        shown = ", ".join(str(n) for n in lines[:6])
        more = f" 等 {len(lines)} 处" if len(lines) > 6 else ""
        self.warnings.append(
            f"第 {shown} 行{more}使用了 Indicate。\n"
            "  目标若是含文字的容器（如 VGroup(圆, 标签)），Indicate 会把整个家族染成同一个颜色，\n"
            "  文字和填充融成一片、强调反而把字盖掉；目标是纯文本或纯图形时无妨。\n"
            "  前者改用 teaching_runtime 的 pulse()：只染外壳、文字转深色保持可读，整体放大后弹回"
        )

    def run(self):
        print(f"🔍 检查文件: {self.file_path}")
        print("=" * 50)

        if not self.parse():
            return self.report()

        self.analyze()
        self.check_scene_class()
        self.check_scene_structure()
        self.check_audio_usage()
        self.check_audio_manager_definition()
        self.check_audio_timing_contract()
        self.check_tex_inputs()
        self.check_audio_api_misuse()
        self.check_manimgl_leftovers()
        self.check_markdown_math_in_text()
        self.check_latex_string_escaping()
        self.check_use_before_assignment()
        self.check_construct_flow()
        self.check_layout_guard()
        self.check_board_contrast()
        self.check_indicate_usage()

        return self.report()

    def report(self):
        success = len(self.errors) == 0

        if self.errors:
            print("\n❌ 错误 (必须修复):")
            for i, error in enumerate(self.errors, 1):
                print(f"\n  {i}. {error}")

        if self.warnings:
            print("\n⚠️  警告 (建议修复):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"\n  {i}. {warning}")

        if success and not self.warnings:
            print("\n✅ 所有检查通过！可以开始渲染。")
        elif success:
            print("\n✅ 必要检查通过，但有警告建议处理。")

        print("\n" + "=" * 50)

        if success:
            print("🎬 下一步: 运行渲染命令")
        else:
            print("⛔ 检查失败，请修复错误后重试。")

        return success


def main_check_structure():
    if len(sys.argv) > 1:
        script_file = sys.argv[1]
    else:
        script_file = "script.py"

    checker = CodeChecker(Path(script_file))
    success = checker.run()
    sys.exit(0 if success else 1)



# ============================================================================
# LaTeX 预编译
# ============================================================================

"""Compile static ManimCE TeX expressions without rendering a scene."""

# pyright: reportMissingImports=false
import ast
import sys
from pathlib import Path

# manim 只在 LaTeX 预编译时需要，延迟到函数内 import（避免结构检查时也要求装 manim）
manim = None  # type: ignore
MathTex = None  # type: ignore
Tex = None  # type: ignore

TEX_CALLS = {"Tex", "MathTex", "SafeMathTex"}
PREFLIGHT_KEYWORDS = {"substrings_to_isolate", "tex_to_color_map"}


def call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def safe_value(node, constants):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in constants:
            return constants[node.id]
        if node.id.isupper() and hasattr(manim, node.id):
            return getattr(manim, node.id)
        raise ValueError(f"unsupported name: {node.id}")
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = safe_value(node.left, constants)
        right = safe_value(node.right, constants)
        if isinstance(left, str) and isinstance(right, str):
            return left + right
        raise ValueError("only string concatenation is supported")
    if isinstance(node, ast.List):
        return [safe_value(item, constants) for item in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(safe_value(item, constants) for item in node.elts)
    if isinstance(node, ast.Dict):
        return {
            safe_value(key, constants): safe_value(value, constants)
            for key, value in zip(node.keys, node.values)
            if key is not None
        }
    if isinstance(node, ast.Subscript):
        container = safe_value(node.value, constants)
        key = safe_value(node.slice, constants)
        return container[key]
    raise ValueError(f"unsupported expression: {type(node).__name__}")


def collect_constants(tree):
    constants = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        try:
            constants[node.targets[0].id] = safe_value(node.value, constants)
        except (ValueError, TypeError, KeyError, IndexError):
            continue
    return constants


def literal_strings(call, constants):
    values = []
    for argument in call.args:
        try:
            value = safe_value(argument, constants)
        except (ValueError, TypeError, KeyError, IndexError):
            return None
        if not isinstance(value, str):
            return None
        values.append(value)
    return values or None


def preflight_keywords(call, constants):
    values = {}
    for keyword in call.keywords:
        if keyword.arg not in PREFLIGHT_KEYWORDS:
            continue
        try:
            values[keyword.arg] = safe_value(keyword.value, constants)
        except (ValueError, TypeError, KeyError, IndexError):
            continue
    return values


def collect_expressions(tree):
    expressions = []
    seen = set()
    constants = collect_constants(tree)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = call_name(node.func)
        if name not in TEX_CALLS:
            continue
        values = literal_strings(node, constants)
        if values is None:
            continue
        keywords = preflight_keywords(node, constants)
        key = (name, repr(values), repr(keywords))
        if key in seen:
            continue
        seen.add(key)
        expressions.append((node.lineno, name, values, keywords))
    return expressions


def compile_expressions(expressions):
    failures = []
    for line, name, values, keywords in expressions:
        # ManimCE 中 Tex 是文本模式、MathTex 是数学模式，与 ManimGL 相反。
        # SafeMathTex 是 teaching_runtime 对 MathTex 的中文保护子类，按 MathTex 编译。
        constructor = Tex if name == "Tex" else MathTex
        try:
            constructor(*values, **keywords)
        except Exception as error:
            message = str(error).strip().splitlines()[-1] if str(error).strip() else type(error).__name__
            failures.append((line, name, values, keywords, message))
    return failures


def main_preflight_tex():
    global manim, MathTex, Tex
    import manim as _manim  # noqa: F811
    from manim import MathTex as _MathTex, Tex as _Tex  # noqa: F811
    manim = _manim
    MathTex = _MathTex
    Tex = _Tex

    script_path = Path(sys.argv[1] if len(sys.argv) > 1 else "script.py")
    try:
        source = script_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (OSError, SyntaxError) as error:
        print(f"TeX preflight could not read {script_path}: {error}", file=sys.stderr)
        return 1

    expressions = collect_expressions(tree)
    failures = compile_expressions(expressions)
    if failures:
        print(f"TeX preflight found {len(failures)} invalid expression(s):", file=sys.stderr)
        for line, name, values, keywords, message in failures:
            preview = " | ".join(values).replace("\n", " ")[:160]
            keyword_names = ", ".join(sorted(keywords)) or "none"
            print(
                f"  line {line}: {name}({preview!r}, keywords={keyword_names}) -> {message}",
                file=sys.stderr,
            )
        return 1

    print(f"TeX preflight compiled {len(expressions)} static expression(s)")
    return 0



# ============================================================================
# 旁白产物校验
# ============================================================================

"""校验 scripts/narrate.mjs 产出的旁白资产（durations.json + public/audio）。"""

import json
import subprocess
import sys
from pathlib import Path


def probe_duration(path: Path) -> float | None:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    try:
        return float(result.stdout.strip())
    except ValueError:
        return None


def main_validate_audio() -> int:
    workspace = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    manifest_path = workspace / "durations.json"
    if not manifest_path.is_file():
        print(f"错误：未找到 {manifest_path}，请先运行 node scripts/narrate.mjs <slug>")
        return 1

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"错误：durations.json 无法读取：{error}")
        return 1

    if not isinstance(manifest, dict) or not manifest:
        print("错误：durations.json 为空或格式错误")
        return 1

    errors: list[str] = []
    total = 0.0
    for scene_id, entry in manifest.items():
        if not isinstance(entry, dict):
            errors.append(f"{scene_id}: 条目不是对象")
            continue
        relative = entry.get("file")
        expected = entry.get("durationSec")
        if not isinstance(relative, str) or not relative:
            errors.append(f"{scene_id}: 缺少 file")
            continue
        if not isinstance(expected, (int, float)) or expected <= 0:
            errors.append(f"{scene_id}: durationSec 无效")
            continue

        audio_path = workspace / "public" / relative
        if not audio_path.is_file():
            errors.append(f"{scene_id}: 音频不存在 {audio_path}")
            continue
        actual = probe_duration(audio_path)
        if actual is None or actual <= 0:
            errors.append(f"{scene_id}: 音频无法探测时长")
            continue

        start = entry.get("speechStartSec", 0)
        end = entry.get("speechEndSec", actual)
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            errors.append(f"{scene_id}: speech 区间无效")
        elif not 0 <= start <= end <= actual + 0.1:
            errors.append(f"{scene_id}: speech 区间越界")
        if abs(actual - float(expected)) > 0.2:
            errors.append(f"{scene_id}: 时长不一致 manifest={expected} actual={actual:.3f}")

        cue_points = entry.get("cuePoints")
        if not isinstance(cue_points, list) or len(cue_points) == 0:
            errors.append(f"{scene_id}: 缺少 cuePoints（每段旁白至少需要一个语义同步点）")
        else:
            cue_ids = [c.get("id") for c in cue_points if isinstance(c, dict)]
            if len(cue_ids) != len(set(cue_ids)):
                errors.append(f"{scene_id}: cuePoints 中存在重复 id")

        total += actual
        cue_count = len(cue_points) if isinstance(cue_points, list) else 0
        print(f"  {scene_id}: {audio_path.name} {actual:.3f}s cues={cue_count}")

    if errors:
        print("\n验证失败：")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"\n验证通过：{len(manifest)} 段旁白，总时长 {total:.3f}s")
    return 0



# ============================================================================
# cue 消费完整性
# ============================================================================

"""Cross-validate cue consumption between script.py and durations.json.

Checks two directions:
1. Every cuePoint declared in durations.json is consumed by a wait_for_cue() call
   in the corresponding scene of script.py (no wasted cues).
2. Every wait_for_cue() call in script.py references a cue id that exists in
   durations.json for that scene (no phantom cues).

Cue ids are per-scene: audio.start("scene_id") sets the current scene,
audio.wait_for_cue("cue_id") references a cue within that scene.
"""

import ast
import json
import re
import sys
from pathlib import Path


def extract_cue_usage(script_path: Path) -> dict[str, list[str]]:
    """Parse script.py and extract {scene_id: [cue_id, ...]} from audio manager calls."""
    source = script_path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError:
        print(f"警告：无法解析 {script_path}，跳过 AST 分析")
        return _extract_cue_usage_regex(source)

    usage: dict[str, list[str]] = {}

    def ordered_calls(function: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.Call]:
        calls: list[ast.Call] = []
        pending = list(function.body)
        while pending:
            node = pending.pop()
            if isinstance(node, ast.Call):
                calls.append(node)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
                continue
            pending.extend(ast.iter_child_nodes(node))
        return sorted(calls, key=lambda node: (node.lineno, node.col_offset))

    def literal_arg(call: ast.Call) -> str | None:
        if not call.args:
            return None
        value = call.args[0]
        return value.value if isinstance(value, ast.Constant) and isinstance(value.value, str) else None

    def self_method_name(call: ast.Call, methods: dict[str, ast.FunctionDef | ast.AsyncFunctionDef]) -> str | None:
        func = call.func
        if (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "self"
            and func.attr in methods
        ):
            return func.attr
        return None

    def process_function(
        function: ast.FunctionDef | ast.AsyncFunctionDef,
        current_scene: str | None,
        methods: dict[str, ast.FunctionDef | ast.AsyncFunctionDef],
        stack: set[str],
    ) -> str | None:
        for call in ordered_calls(function):
            method_name = _method_name(call.func)
            if method_name == "start":
                scene_id = literal_arg(call)
                if scene_id is not None:
                    current_scene = scene_id
                    usage.setdefault(current_scene, [])
                continue
            if method_name == "wait_for_cue":
                cue_id = literal_arg(call)
                if cue_id is not None and current_scene is not None:
                    usage.setdefault(current_scene, []).append(cue_id)
                continue

            helper_name = self_method_name(call, methods)
            if helper_name is None or helper_name in stack:
                continue
            current_scene = process_function(
                methods[helper_name],
                current_scene,
                methods,
                stack | {helper_name},
            )
        return current_scene

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            process_function(node, None, {}, {node.name})
        elif isinstance(node, ast.ClassDef):
            methods = {
                item.name: item
                for item in node.body
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
            }
            construct = methods.get("construct")
            if construct is not None:
                process_function(construct, None, methods, {"construct"})

    return usage


def _method_name(node: ast.expr) -> str | None:
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


_START_RE = re.compile(r"""\.start\(\s*["']([^"']+)["']\s*\)""")
_CUE_RE = re.compile(r"""\.wait_for_cue\(\s*["']([^"']+)["']\s*\)""")


def _extract_cue_usage_regex(source: str) -> dict[str, list[str]]:
    """Fallback regex extraction when AST parsing fails."""
    usage: dict[str, list[str]] = {}
    current_scene: str | None = None
    for line in source.splitlines():
        m = _START_RE.search(line)
        if m:
            scene_id: str = m.group(1)
            current_scene = scene_id
            usage.setdefault(scene_id, [])
        m2 = _CUE_RE.search(line)
        if m2 and current_scene is not None:
            usage.setdefault(current_scene, []).append(m2.group(1))
    return usage


def load_declared_cues(durations_path: Path) -> dict[str, set[str]]:
    """Extract {scene_id: {cue_id, ...}} from durations.json."""
    try:
        manifest = json.loads(durations_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"无法读取或解析 {durations_path}: {error}") from error
    if not isinstance(manifest, dict):
        raise ValueError(f"{durations_path} 顶层必须是 JSON object")
    declared: dict[str, set[str]] = {}
    for scene_id, entry in manifest.items():
        if not isinstance(entry, dict):
            continue
        cue_points = entry.get("cuePoints")
        if not isinstance(cue_points, list):
            continue
        declared[scene_id] = {
            c["id"] for c in cue_points if isinstance(c, dict) and isinstance(c.get("id"), str)
        }
    return declared


def main_validate_cues() -> int:
    if len(sys.argv) < 2:
        print("用法: validate_cue_consumption.py <workspace> [script.py]")
        return 1

    workspace = Path(sys.argv[1]).resolve()
    script_name = sys.argv[2] if len(sys.argv) > 2 else "script.py"
    script_path = workspace / script_name
    durations_path = workspace / "durations.json"

    if not script_path.is_file():
        print(f"错误：脚本不存在 {script_path}")
        return 1
    if not durations_path.is_file():
        print("跳过 cue 消费检查：durations.json 尚未生成")
        return 0

    try:
        declared = load_declared_cues(durations_path)
    except ValueError as error:
        print(f"错误：{error}")
        return 1
    consumed = extract_cue_usage(script_path)

    errors: list[str] = []
    all_scenes = sorted(set(declared.keys()) | set(consumed.keys()))

    for scene_id in all_scenes:
        scene_declared = declared.get(scene_id, set())
        scene_consumed = consumed.get(scene_id, [])
        consumed_set = set(scene_consumed)

        wasted = scene_declared - consumed_set
        phantom = consumed_set - scene_declared

        if wasted:
            errors.append(
                f"{scene_id}: durations.json 声明了 cue {sorted(wasted)} "
                f"但 script.py 未调用 wait_for_cue()"
            )
        if phantom:
            errors.append(
                f"{scene_id}: script.py 调用了 wait_for_cue({sorted(phantom)}) "
                f"但 durations.json 中无对应 cuePoint"
            )

        duplicates = [cid for cid in scene_consumed if scene_consumed.count(cid) > 1]
        if duplicates:
            errors.append(
                f"{scene_id}: script.py 重复调用了 wait_for_cue({sorted(set(duplicates))})"
            )

    if errors:
        print("Cue 消费检查失败：")
        for error in errors:
            print(f"  - {error}")
        return 1

    total_cues = sum(len(v) for v in declared.values())
    total_consumed = sum(len(v) for v in consumed.values())
    print(f"Cue 消费检查通过：{len(all_scenes)} 个场景，{total_cues} 个声明，{total_consumed} 个消费")
    return 0




# ============================================================================
# 统一 CLI 入口
# ============================================================================

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if not args:
        print("用法: python checks.py [--preflight-tex|--validate-audio|--validate-cues] <参数…>")
        raise SystemExit(1)

    if args[0] == "--preflight-tex":
        sys.argv = [sys.argv[0]] + args[1:]
        raise SystemExit(main_preflight_tex())
    elif args[0] == "--validate-audio":
        sys.argv = [sys.argv[0]] + args[1:]
        raise SystemExit(main_validate_audio())
    elif args[0] == "--validate-cues":
        sys.argv = [sys.argv[0]] + args[1:]
        raise SystemExit(main_validate_cues())
    else:
        # 默认：结构与 API 检查（兼容旧调用方式：python checks.py script.py）
        main_check_structure()
