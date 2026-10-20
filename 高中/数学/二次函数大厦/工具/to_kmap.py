"""把 data.py 的二次函数大厦数据转成 knowledge-map-web 的 md 格式。
用法：python3 工具/to_kmap.py > 二次函数大厦-知识地图.md
"""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "生成"))
from data import NODES, E, SECTIONS, TOOLS, METHODS, ENTRIES, ENTRY_HOW, EDGE_USES, TOOL_LABEL, TOOL_SIGNALS, METHOD_IGNORE

# ── helpers ──

def stars(title):
    """Count ★ in title for importance."""
    c = title.count("★")
    return c if c else None

def clean_title(title):
    """Remove ★ prefix and strip."""
    return re.sub(r'^★+\s*', '', title).strip()

def extract_method(labels):
    """Extract first 【…】 method name from edge labels."""
    for l in labels:
        for m in re.findall(r'【(.+?)】', l):
            if m not in METHOD_IGNORE:
                return m
    return None

def method_class(method_name):
    """Map a specific method label to its method class name."""
    for name, labels, *_ in METHODS:
        if method_name == name:
            return name
        if method_name in labels:
            return name
        # fuzzy: remove trailing 法
        bare = re.sub(r'法$', '', method_name)
        if bare and bare in labels:
            return name
        if bare and bare == name:
            return name
    return method_name  # fallback

# ── build node index ──

node_map = {}  # id -> node tuple
for n in NODES:
    node_map[n[0]] = n

# ── build section (layer) index ──

node_layer = {}  # node id -> layer number
for i, (title, ids) in enumerate(SECTIONS):
    for nid in ids:
        node_layer[nid] = i

# ── build deps per node (from edges) ──

node_deps = {}  # target_id -> [(src, kind, labels, marker, main)]
for s, t, kind, labels, marker, main in E:
    if t not in node_deps:
        node_deps[t] = []
    node_deps[t].append((s, kind, labels, marker, main))

# ── build tools as nodes ──

TOOL_ID_MAP = {}  # ① -> T01
for i, (circle, name, formula, uses) in enumerate(TOOLS, 1):
    tid = f"T{i:02d}"
    TOOL_ID_MAP[circle] = tid

# ── method nodes collector ──

method_nodes = {}  # method class name -> set of node ids
for s, t, kind, labels, marker, main in E:
    m = extract_method(labels)
    if m:
        mc = method_class(m)
        if mc not in method_nodes:
            method_nodes[mc] = set()
        method_nodes[mc].add(s)
        method_nodes[mc].add(t)

# ── main chains ──

def build_main_chains():
    """Build a few clean main chains from main=True edges."""
    adj = {}  # src -> [tgt]
    for s, t, _, _, _, m in E:
        if m:
            adj.setdefault(s, []).append(t)

    # DFS from every main-edge source to find all maximal paths
    all_paths = []
    def dfs(node, path, visited):
        if node not in adj or all(n in visited for n in adj[node]):
            if len(path) > 1:
                all_paths.append(tuple(path))
            return
        for nxt in adj[node]:
            if nxt not in visited:
                path.append(nxt)
                visited.add(nxt)
                dfs(nxt, path, visited)
                path.pop()
                visited.discard(nxt)

    main_nodes = set()
    for s, t, _, _, _, m in E:
        if m:
            main_nodes.add(s)
            main_nodes.add(t)

    for n in main_nodes:
        if n in adj:
            dfs(n, [n], {n})

    # Sort by length descending, greedily pick paths covering new edges
    all_paths = list(set(all_paths))
    all_paths.sort(key=len, reverse=True)
    used_edges = set()
    chains = []
    for p in all_paths:
        new_edges = set()
        for i in range(len(p) - 1):
            e = (p[i], p[i + 1])
            if e not in used_edges:
                new_edges.add(e)
        if new_edges and len(p) >= 3:
            chains.append(list(p))
            used_edges |= new_edges
        if len(chains) >= 4:
            break

    # Cover remaining edges
    for s, t, _, _, _, m in E:
        if m and (s, t) not in used_edges:
            chains.append([s, t])
            used_edges.add((s, t))

    return chains

# ── region mapping ──

def node_region(ntype):
    if ntype == "start":
        return "起点"
    elif ntype in ("green", "white"):
        return "无条件"
    else:  # orange, lorange
        return "有条件"

def node_type_str(ntype):
    if ntype == "start":
        return "起点"
    elif ntype in ("green", "orange"):
        return "结论"
    else:  # white, lorange
        return "中间步"

# ── output ──

def emit():
    lines = []
    def w(s=""):
        lines.append(s)

    w("# 二次函数大厦 · 知识地图")
    w()
    w("> 从函数定义和二次函数定义出发，推出图像、性质、三个二次、根的分布与综合应用。共 %d 个知识节点。" % len(NODES))
    w()
    w("---")
    w()

    # ── 页面设置 ──
    w("## 页面设置")
    w()
    w("- 标题：二次函数大厦")
    w("- 编号写法：[SRPT]\\d{2}")
    w("- 保存键：quadratic-tree-learned")
    w()
    w("| 区域 | 颜色 | 位置 | 说明 |")
    w("|---|---|---|---|")
    w("| 起点 | #7B1FA2 | 0.5 | 公理、定义、借来的公式 |")
    w("| 无条件 | #2E7D32 | 0.3 | 对任意二次函数成立 |")
    w("| 有条件 | #EF6C00 | 0.7 | 需要特定条件（a>0、Δ≥0、区间等） |")
    w()
    w("---")
    w()

    # ── 主干链（手工指定，自动提取太碎） ──
    w("## 主干链")
    w()
    w("1. **从定义到顶点式**")
    w("   【定义】二次函数 S02 → a[x² + (b/a)x] + c R44 → a[(x + b/2a)² − b²/(4a²)] + c R45 → 顶点式 R01")
    w("2. **从方程到求根公式**")
    w("   一元二次方程的解法 R33 → x² + (b/a)x + c/a = 0 R39 → x² + (b/a)x = −c/a R40 → (x + b/2a)² = Δ/(4a²) R41 → 求根公式与判别式 R34 → 韦达定理 P21 → 交点式 P01")
    w("3. **从顶点式到最值**")
    w("   顶点式 R01 → 最值 P03 → 恒成立 P08")
    w("4. **从图像到性质**")
    w("   【约定】点在图像上 S03 → y = x² 的图像 R30 → y = ax² 的图像 R31 → 平移 R32 → 顶点式 R01 → 作差 R43 → 作差恒等式 R18 → 单调性 P02 → 闭区间上的最值 P05 → 含参最值 P06")
    w("5. **从零点到不等式**")
    w("   【定义】零点 S07 → 零点⟺根⟺交点 R08 → 三个二次的关系 P07 → 解一元二次不等式 R09")
    w()
    w("---")
    w()

    # ── 楼层与节点 ──
    for layer_idx, (sec_title, sec_ids) in enumerate(SECTIONS):
        # Extract section name from title (remove ① etc.)
        sec_name = re.sub(r'^[①②③④⑤⑥⑦⑧]\s*', '', sec_title)
        w(f"## 第 {layer_idx} 层　{sec_name}")
        w()

        for nid in sec_ids:
            n = node_map.get(nid)
            if not n:
                continue
            nid, ntype, cond, title, content_lines, note = n

            imp = stars(title)
            name = clean_title(title)
            region = node_region(ntype)
            ttype = node_type_str(ntype)

            w(f"### {nid} {name}")

            # one (标志)
            if content_lines:
                # Use first content line as one if it looks like a formula
                w(f"- 标志：{content_lines[0]}")
            elif name and ntype in ("white", "lorange"):
                # Intermediate nodes: title IS the formula
                w(f"- 标志：{title}")

            w(f"- 区域：{region}")
            w(f"- 类型：{ttype}")

            if imp:
                w(f"- 重要度：{imp}")

            # Tags from title
            tag_match = re.match(r'【(.+?)】', name)
            if tag_match:
                w(f"- 标签：【{tag_match.group(1)}】")

            # Conditions
            if cond:
                w(f"- 条件：{cond}")

            # What (description)
            if len(content_lines) > 1:
                what = "；".join(content_lines[1:])
                w(f"- 是什么：{what}")
            elif content_lines:
                # Only one line, used as 标志; repeat as what
                w(f"- 是什么：{content_lines[0]}")
            elif ntype in ("white", "lorange"):
                w(f"- 是什么：推导过程的中间步骤")
            else:
                # Fallback: use title as what
                w(f"- 是什么：{name}")

            # Notes
            if note:
                w(f"- 注释：{note}")

            # Dependencies
            deps = node_deps.get(nid, [])
            if deps:
                w("- 依赖：")
                for src, kind, labels, marker, main in deps:
                    kind_str = "推出" if kind == "derive" else "前提"
                    w(f"  - 来源：{src}")
                    w(f"    种类：{kind_str}")

                    # Extract method
                    meth = extract_method(labels)
                    if meth:
                        mc = method_class(meth)
                        w(f"    方法：{meth}")

                    # Steps from labels
                    step_lines = []
                    for l in labels:
                        # Remove leading 【前提】etc for cleaner steps
                        step_lines.append(l)
                    if marker:
                        step_lines.append(marker)

                    if step_lines:
                        w("    步骤：")
                        for j, sl in enumerate(step_lines, 1):
                            w(f"      {j}. {sl}")

                    # EDGE_USES
                    key = (src, nid)
                    if key in EDGE_USES:
                        tools_used = EDGE_USES[key]
                        tool_names = []
                        for tu in tools_used:
                            tn = node_map.get(tu)
                            if tn:
                                tool_names.append(f"{clean_title(tn[3])}（{tu}）")
                            else:
                                tool_names.append(tu)
                        w(f"    条件：借用工具 {', '.join(tool_names)}")

            w()

        # Add tool nodes in layer 0
        if layer_idx == 0:
            w()
            w("### 借来的公式（工具箱）")
            w()
            for i, (circle, name, formula, uses) in enumerate(TOOLS, 1):
                tid = f"T{i:02d}"
                w(f"### {tid} {name}")
                w(f"- 标志：{formula}")
                w(f"- 区域：起点")
                w(f"- 类型：起点")
                w(f"- 标签：【公式】")

                use_strs = []
                for where, how, codes in uses:
                    use_strs.append(f"{where}：{how}")
                if use_strs:
                    w(f"- 是什么：{'; '.join(use_strs)}")

                w()

    w("---")
    w()

    # ── 思想方法 ──
    w("## 思想方法")
    w()
    for name, labels, direction, basis, signal, pitfall in METHODS:
        w(f"### {name}")
        w(f"- 说明：{direction.split('→')[0].strip() if '→' in direction else direction[:20]}")
        w(f"- 方向：{direction}")
        if basis:
            w(f"- 依据：{basis}")
        if signal:
            w(f"- 信号：{signal}")

        # Collect nodes that use this method
        mnodes = method_nodes.get(name, set())
        if mnodes:
            w(f"- 出现在：{'、'.join(sorted(mnodes))}")

        if labels:
            w(f"- 标签：{'；'.join(labels)}")

        if pitfall:
            w(f"- 易错：")
            w(f"  - {pitfall}")

        w()

    return "\n".join(lines)


if __name__ == "__main__":
    print(emit())
