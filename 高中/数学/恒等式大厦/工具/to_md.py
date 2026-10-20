"""把 data.py + steps.py 转换成 knowledge-map-web 的 md 格式。
用法：cd 数学/恒等式大厦 && python3 工具/to_md.py > 恒等式大厦-web-节点清单.md
"""
import sys, re, textwrap
sys.path.insert(0, "生成")
from data import SECS, NODES, EDGES, METHODS, TOOLS, TOOL_LABELS, DIRECTION, JIEFA, FORMULAS, METHOD_OF
from steps import STEPS

# ── 1. 区域（sections → regions）──
SEC_COLORS = {
    "base": "#795548",   # 棕：地基
    "alg":  "#1565C0",   # 蓝：代数
    "exp":  "#6A1B9A",   # 紫：指数对数
    "tri":  "#C62828",   # 红：三角
    "vec":  "#AD1457",   # 玫红：向量
    "cpx":  "#4527A0",   # 深紫：复数
    "seq":  "#00695C",   # 深青：数列
    "cnt":  "#E65100",   # 橙：计数
    "der":  "#2E7D32",   # 绿：导数
    "fun":  "#0277BD",   # 浅蓝：函数性质
    "geo":  "#BF360C",   # 深橙：解析几何
    "sp":   "#37474F",   # 深灰蓝：空间
    "prob": "#00838F",   # 青：概率统计
}
SEC_ANCHORS = {
    "base": 0.5,
    "alg": 0.15, "exp": 0.3, "tri": 0.45, "vec": 0.55, "cpx": 0.65,
    "seq": 0.2, "cnt": 0.8,
    "der": 0.35, "fun": 0.1,
    "geo": 0.75, "sp": 0.6,
    "prob": 0.9,
}

# ── 2. 计算楼层（依赖深度）──
# 建邻接表：谁依赖谁（derive 和 premise 都算）
node_map = {n["id"]: n for n in NODES}
# 来源 → 目标
deps_of = {}  # target → [source_ids]
for e in EDGES:
    deps_of.setdefault(e["t"], []).append(e["s"])

def compute_layers():
    """BFS 拓扑排序算层。"""
    layer = {}
    # 无来源的放 L=0
    for n in NODES:
        if n["id"] not in deps_of or all(s.startswith("Q") or node_map[s]["type"] == "problem" for s in deps_of.get(n["id"], [])):
            if n["type"] in ("start",) or n["id"].startswith("S"):
                layer[n["id"]] = 0
    # 先把所有 S 节点放 0 层
    for n in NODES:
        if n["id"].startswith("S"):
            layer[n["id"]] = 0

    changed = True
    while changed:
        changed = False
        for n in NODES:
            nid = n["id"]
            if nid in layer:
                continue
            sources = [s for s in deps_of.get(nid, []) if not s.startswith("Q")]
            if not sources:
                layer[nid] = 0
                changed = True
                continue
            if all(s in layer for s in sources):
                layer[nid] = max(layer[s] for s in sources) + 1
                changed = True

    # Q 节点：放在它来源的最高层 + 1
    for n in NODES:
        nid = n["id"]
        if nid not in layer:
            sources = [s for s in deps_of.get(nid, []) if s in layer]
            if sources:
                layer[nid] = max(layer[s] for s in sources) + 1
            else:
                layer[nid] = 0
    return layer

layers = compute_layers()
max_layer = max(layers.values())

# 给每层起名
LAYER_NAMES = {}
for L in range(max_layer + 1):
    nodes_at = [n for n in NODES if layers[n["id"]] == L]
    if L == 0:
        LAYER_NAMES[L] = "地基：公理、定义与起点"
    else:
        # 按最多的 section 命名
        from collections import Counter
        sec_cnt = Counter(n["sec"] for n in nodes_at if not n["id"].startswith("Q"))
        if sec_cnt:
            top_sec = sec_cnt.most_common(1)[0][0]
            LAYER_NAMES[L] = f"推导第 {L} 层"
        else:
            LAYER_NAMES[L] = f"第 {L} 层"

# ── 3. 映射节点类型 ──
def map_type(n):
    t = n["type"]
    if t == "start":
        return "起点"
    elif t == "problem":
        return "结论"  # Q 节点也算结论
    elif t == "green":
        return "结论"
    elif t in ("orange", "lorange"):
        return "结论"  # 有条件的结论
    elif t == "white":
        return "中间步"
    return "结论"

def map_importance(n):
    title = n.get("title", "")
    stars = title.count("★")
    return min(stars, 3) if stars else None

# ── 4. 清洁标题 ──
def clean_title(title):
    """去掉开头的 ★ 和【标签】"""
    t = re.sub(r'^[★\s]+', '', title)
    t = re.sub(r'^【[^】]+】\s*', '', t)
    return t.strip()

def extract_tags(n):
    """从标题提取标签"""
    title = n.get("title", "")
    tags = re.findall(r'【([^】]+)】', title)
    if n.get("ext"):
        tags.append("拓展")
    return tags

# ── 5. 条件 ──
def get_conditions(n):
    cond = n.get("cond")
    if not cond:
        return []
    # 条件可能含多个，用"；"分隔
    return [c.strip() for c in cond.replace("〔", "").replace("〕", "").split("；") if c.strip()]

# ── 6. 节点内容 ──
def get_what(n):
    """合并 lines 为 what 描述"""
    lines = n.get("lines", [])
    parts = []
    for l in lines:
        if l.startswith("✗"):
            continue  # counterexamples handled separately
        parts.append(l)
    return "；".join(parts) if parts else None

def get_counterexamples(n):
    lines = n.get("lines", [])
    return [l[2:].strip() if l.startswith("✗ ") else l[1:].strip() for l in lines if l.startswith("✗")]

def get_notes(n):
    notes = n.get("notes", [])
    cleaned = []
    for note in notes:
        # 去掉前缀标记
        note = re.sub(r'^(⚡ 第一反应：|⋯ |用于：|起点：|枢纽：)', '', note).strip()
        if note:
            cleaned.append(note)
    return cleaned

def get_one(n):
    """取第一行公式作为标志"""
    lines = n.get("lines", [])
    if lines and not lines[0].startswith("✗"):
        return lines[0]
    return None

# ── 7. 推导过程（deps 的 how）──
def get_derive_edges(target_id):
    """获取指向 target 的 derive 边"""
    return [e for e in EDGES if e["t"] == target_id and e["kind"] == "derive"]

def get_premise_edges(target_id):
    """获取指向 target 的 premise 边"""
    return [e for e in EDGES if e["t"] == target_id and e["kind"] == "premise"]

def format_steps(edge):
    """把边的推导步骤格式化成行列表（每行一步）"""
    s, t = edge["s"], edge["t"]
    key = (s, t)

    # 优先用 steps.py 的内容
    if key in STEPS:
        lines = list(STEPS[key])
    else:
        lines = list(edge.get("lines", []))

    return lines if lines else None

# ── 已确认的方法误标：按边显式指定核心方法，覆盖启发式推断 ──
METHOD_OVERRIDE = {
    ("R03", "P01"): "配凑",       # 配方是配凑的教科书范例
    ("S16", "P65"): "回到定义",   # 核心是定义斜率
    ("S09", "P51"): "回到定义",   # 核心是套用等差/等比定义
    ("S19", "R47"): "分类讨论",   # 核心是分解互斥事件
    ("S21", "R41"): "展开分解",   # 核心是分解坐标
    ("S16", "P68"): "回到定义",   # 从定义出发写标准方程
    ("R03", "P68"): "配凑",       # 一般方程配方化标准
    ("S08", "R55"): "回到定义",   # 回到导数定义
    ("S04", "P83"): "回到定义",   # 回到弧度定义（实际边是 S04→P83）
    ("R15", "R16"): "数形结合",   # 两角差余弦由数量积坐标推出
    ("S05", "P49"): "数形结合",   # 向量模的平方
    ("P20", "P21"): "补形",       # 正弦定理由面积法推出
    ("R46", "P77"): "补形",       # 外接球补成长方体（实际边是 R46→P77）
    ("S18", "P76"): "补形",       # 台体 = 大锥 − 小锥
    ("R05", "R31"): "作差相消",   # 立方差展开后累加相消（不是归纳）
    ("R29", "R32"): "归纳",       # 立方和用归纳法
    ("R26", "R27"): "归纳",       # 棣莫弗用归纳法
    ("R45", "P64"): "代换",       # 正弦型函数由平移伸缩（代换）得到
    ("P69", "P96"): "代换",       # 直线系由代入组合方程得到
    # P05→P90：步骤是累乘，映射到作差相消，按实际动作走
    # P21→P86：步骤是正弦定理+作比，映射到作差相消，按实际动作走
}

def get_method_for_edge(edge):
    """从 edge 的 lines 或 STEPS 提取方法名"""
    s, t = edge["s"], edge["t"]
    key = (s, t)

    # 优先用显式指定
    if key in METHOD_OVERRIDE:
        return METHOD_OVERRIDE[key]

    lines = STEPS.get(key, edge.get("lines", []))
    # 从最后一行提取【方法】
    for line in reversed(lines):
        m = re.search(r'【([^】]+)】', line)
        if m:
            action = m.group(1)
            # 看 METHOD_OF 里有没有
            if action in METHOD_OF:
                return METHOD_OF[action][1]  # 方法名
    # 从 DIRECTION 看
    if t in DIRECTION:
        return DIRECTION[t][0]
    return None

# ── 8. 区域名映射 ──
SEC_NAMES = {}
for k, v in SECS.items():
    # 取 | 后面的说明的第一段
    name = re.sub(r'^[①②③④⑤⑥⑦⑧⑨]', '', v.split("：")[0]).strip()
    if name.endswith("a") or name.endswith("b") or name.endswith("c"):
        name = name[:-1].strip()
    SEC_NAMES[k] = name

# 手动修正
SEC_NAMES["base"] = "地基"
SEC_NAMES["alg"] = "代数"
SEC_NAMES["exp"] = "指数与对数"
SEC_NAMES["tri"] = "三角"
SEC_NAMES["vec"] = "向量"
SEC_NAMES["cpx"] = "复数"
SEC_NAMES["seq"] = "数列"
SEC_NAMES["cnt"] = "计数"
SEC_NAMES["der"] = "导数"
SEC_NAMES["fun"] = "函数性质"
SEC_NAMES["geo"] = "解析几何"
SEC_NAMES["sp"] = "空间"
SEC_NAMES["prob"] = "概率统计"


# ── 输出 md ──
def output():
    out = []
    def w(s=""):
        out.append(s)

    w("# 恒等式大厦 · 拓扑图")
    w()
    # 只保留 S/R/P 节点（恒等式、公式、定理、公理），不含 Q 节点（题型入口）
    SRP_IDS = {n["id"] for n in NODES if not n["id"].startswith("Q")}
    srp_nodes = [n for n in NODES if n["id"] in SRP_IDS]
    w(f"> 从 23 个起点出发，不跳步推出高中全部恒等式与公式。S 起点（公理与定义）→ R 结论 → P 带条件结论，共 {len(srp_nodes)} 个知识节点。")
    w()
    w("---")
    w()

    # ── 页面设置 ──
    w("## 页面设置")
    w()
    w("- 标题：恒等式大厦")
    w("- 编号写法：[SRPQ]\\d{2,3}")
    w("- 保存键：identity-tree-learned")
    w()
    w("| 区域 | 颜色 | 位置 | 说明 |")
    w("|---|---|---|---|")
    for k in ["base", "alg", "exp", "tri", "vec", "cpx", "seq", "cnt", "der", "fun", "geo", "sp", "prob"]:
        w(f"| {SEC_NAMES[k]} | {SEC_COLORS[k]} | {SEC_ANCHORS[k]} | {SECS[k][:50]} |")
    w()
    w("---")
    w()

    # ── 主干链 ──
    w("## 主干链")
    w()
    # 从 EDGES 里找 main=True 的链
    main_edges = [(e["s"], e["t"]) for e in EDGES if e.get("main")]
    if main_edges:
        # 建主干图
        from collections import defaultdict
        main_next = defaultdict(list)
        main_prev = defaultdict(list)
        main_nodes_set = set()
        for s, t in main_edges:
            main_next[s].append(t)
            main_prev[t].append(s)
            main_nodes_set.add(s)
            main_nodes_set.add(t)
        # 找起点（没有 prev 的）
        starts = [n for n in main_nodes_set if n not in main_prev]
        # 按 section 分链
        chains_by_sec = {}
        for sec_key in SECS:
            sec_nodes = [n for n in main_nodes_set if node_map.get(n, {}).get("sec") == sec_key]
            if sec_nodes:
                chains_by_sec[sec_key] = sec_nodes

        # 每条主干链必须沿实际 derive 边连续，不能用分号拼接不相邻的路线
        w("1. **代数主干**")
        w("   运算律 S01 → 多项式乘法 R01 → 完全平方 R03 → 配方 P01 → 求根公式 P02 → 韦达定理 P03")
        w("2. **三角主干（勾股）**")
        w("   单位圆 S04 → 勾股恒等式 R13")
        w("3. **三角主干（和角）**")
        w("   数量积 S05 → 坐标式 R15 → 两角差余弦 R16 → 和角公式 R17 → 倍角 R18 → 降幂 R19")
        w("4. **向量到余弦定理**")
        w("   数量积 S05 → 向量模的平方 P49 → 余弦定理 P22")
        w("5. **等差数列**")
        w("   等差定义 S09 → 等差通项 P26 → 下标性质 P27 → 等差求和 P28")
        w("6. **等比数列**")
        w("   等比定义 S09 → 等比通项 P29 → 等比求和 P31")
    w()
    w("---")
    w()

    # ── 按楼层输出节点（只输出 S/R/P）──
    for L in range(max_layer + 1):
        nodes_at = [n for n in NODES if layers[n["id"]] == L and n["id"] in SRP_IDS]
        if not nodes_at:
            continue

        w(f"## 第 {L} 层　{LAYER_NAMES[L]}")
        w()

        for n in nodes_at:
            nid = n["id"]
            title = clean_title(n["title"])
            w(f"### {nid} {title}")

            # 标志（one）
            one = get_one(n)
            if one:
                w(f"- 标志：{one}")

            # 区域
            w(f"- 区域：{SEC_NAMES[n['sec']]}")

            # 类型
            ntype = map_type(n)
            w(f"- 类型：{ntype}")

            # 重要度
            imp = map_importance(n)
            if imp:
                w(f"- 重要度：{imp}")

            # 标签
            tags = extract_tags(n)
            if tags:
                w(f"- 标签：{'；'.join(tags)}")

            # 条件
            conds = get_conditions(n)
            if conds:
                w(f"- 条件：{'；'.join(conds)}")

            # 是什么（what）- 全部正文行
            lines = n.get("lines", [])
            non_err_lines = [l for l in lines if not l.startswith("✗")]
            if non_err_lines:
                if len(non_err_lines) == 1:
                    # 只有一行：标志和 what 都用它
                    w(f"- 是什么：{non_err_lines[0]}")
                else:
                    # 第一行已作标志，其余作 what
                    rest = non_err_lines[1:]
                    w(f"- 是什么：{'；'.join(rest)}")
            else:
                # 没有正文行，用标题当 what
                w(f"- 是什么：{title}")

            # 反例
            cex = get_counterexamples(n)
            if cex:
                w(f"- 反例：")
                for c in cex:
                    w(f"  - {c}")

            # 注释
            notes = get_notes(n)
            if notes:
                w(f"- 注释：")
                for note in notes:
                    w(f"  - {note}")

            # 依赖（derive edges）——只保留来源也是 S/R/P 的
            derives = [e for e in get_derive_edges(nid) if e["s"] in SRP_IDS]
            premises = [e for e in get_premise_edges(nid) if e["s"] in SRP_IDS]

            if derives or premises:
                w(f"- 依赖：")
                for e in derives:
                    src_name = clean_title(node_map[e["s"]]["title"]) if e["s"] in node_map else e["s"]
                    w(f"  - 来源：{e['s']}")
                    w(f"    种类：推出")

                    method = get_method_for_edge(e)
                    if method:
                        w(f"    方法：{method}")

                    # 条件
                    if e.get("mark"):
                        w(f"    条件：{e['mark']}")

                    # 步骤
                    steps_list = format_steps(e)
                    if steps_list:
                        w(f"    步骤：")
                        for i, step in enumerate(steps_list, 1):
                            w(f"      {i}. {step}")

                for e in premises:
                    w(f"  - 来源：{e['s']}")
                    w(f"    种类：前提")
                    if e.get("mark"):
                        w(f"    条件：{e['mark']}")
                    if e.get("lines"):
                        w(f"    步骤：")
                        for i, step in enumerate(e["lines"], 1):
                            w(f"      {i}. {step}")

            w()

    # ── 思想方法 ──
    w("## 思想方法")
    w()
    for m in METHODS:
        mid, short, full_name, direction, basis, signal, examples, pitfalls, action_names = m
        w(f"### {short}")
        w(f"- 说明：{full_name}")
        w(f"- 方向：{direction}")
        w(f"- 依据：{basis}")
        w(f"- 信号：{signal}")

        # 找出用到这个方法的节点（只看 S/R/P）
        method_nodes = []
        for n in NODES:
            nid = n["id"]
            if nid not in SRP_IDS:
                continue
            for e in EDGES:
                if e["t"] == nid and e["kind"] == "derive" and e["s"] in SRP_IDS:
                    em = get_method_for_edge(e)
                    if em == short:
                        method_nodes.append(nid)
                        break
        if method_nodes:
            w(f"- 出现在：{'、'.join(sorted(set(method_nodes)))}")

        if action_names:
            w(f"- 标签：{'；'.join(action_names)}")

        w(f"- 例子：")
        w(f"  - {examples}")

        if pitfalls:
            w(f"- 易错：")
            w(f"  - {pitfalls}")

        w()

    return "\n".join(out)


if __name__ == "__main__":
    print(output())
