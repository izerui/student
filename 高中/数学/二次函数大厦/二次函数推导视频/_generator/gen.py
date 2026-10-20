"""由二次函数大厦 data.py 生成视频任务书。用法：python3 gen.py
结论、条件、推导步骤、题型入口全部取自 data.py；讲法（开场、画面、易错点、例题）取自 episodes.py。"""
import collections, re, sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]                                  # 数学/二次函数大厦/
sys.path.insert(0, str(ROOT / "生成"))
sys.path.insert(0, str(HERE))
from data import NODES, E, ENTRIES, TOOLS, EXT           # noqa: E402
from episodes import EP, EXAMPLES, GROUPS, FACTS, EXTRA_PRE, NOTES  # noqa: E402

OUT = HERE.parent
DRAWIO = ROOT / "outputs" / "quadratic-tree-v2.drawio"
N = {n[0]: dict(id=n[0], type=n[1], cond=n[2], title=n[3], lines=n[4], note=n[5]) for n in NODES}
GRID = {u.get("id"): u.get("坐标") for u in ET.parse(DRAWIO).getroot().iter("UserObject")}

XREF = re.compile(r"[（(]?同见不等式大厦[^）)；。]*[）)]?|〔[^〕]*〕")
clean = lambda s: re.sub(r"\s+", " ", XREF.sub("", s)).strip(" ，；")
title = lambda i: N[i]["title"].lstrip("★ ").strip()
code = lambda i: f"{i} · {GRID.get(i, '?')}"

# ── 校验分集 ──
home = {}
for e in EP:
    for i in e["nodes"]:
        assert i in N, i
        assert i not in home, f"{i} 重复分配"
        home[i] = e["id"]
assert set(home) == set(N), f"未分配：{set(N) - set(home)}"
used = [x for _, _, ids in GROUPS for x in ids]
assert sorted(used) == sorted(en[0] for en in ENTRIES), set(en[0] for en in ENTRIES) ^ set(used)
assert set(EXAMPLES) == set(used)
order = {e["id"]: k for k, e in enumerate(EP)}
late = [(s, t) for s, t, kind, *_ in E if order[home[s]] > order[home[t]]]


def statement(i):
    n = N[i]
    out = [clean(x) for x in n["lines"]]
    if n["cond"]:
        out.insert(0, f"条件：{n['cond']}")
    return [x for x in out if x]


def why(i):
    if N[i]["type"] == "start":
        note = clean(N[i]["note"] or "").replace("起点：", "")
        return f"这是课本的{'定理（直接承认，不证）' if '定理' in N[i]['title'] else '定义或约定'}，直接承认" + (f"（{note}）" if note and note not in ('定义', '课本定义') else "") + "。"
    parts = []
    for s, t, kind, ls, mark, main in E:
        if t == i and kind == "derive":
            parts.append(f"由“{title(s)}”：" + "；".join(clean(x) for x in ls if clean(x)))
    return "。".join(parts) + "。"


def base_block(i):
    return [f"- **{title(i)}**", *[f"  - {x}" for x in statement(i)], f"  - 由来（简短复习）：{why(i)}"]


METH = re.compile(r"【([^】]+)】")
RULES = ("本集默认使用的基本规则（片头一句话带过，用到时写出）：一个数大于另一个数 ⟺ 两数之差为正；等式两边同加、同乘同一个数仍相等；"
         "不等式两边同加同一个数方向不变，同乘（除）正数方向不变，同乘（除）负数方向反向；正×正=正，负×负=正，正×负=负；平方非负：x²≥0，等号 ⟺ x=0。")
VERTEX_FROM = [e["id"] for e in EP].index("E10")


def extra_pre(eid, have):
    """推导线以外要补的结论：E10 以后的集和题型串讲都复习顶点式；再加 EXTRA_PRE。"""
    k = [e["id"] for e in EP].index(eid) if eid.startswith("E") else len(EP)
    out = (["R01"] if k > VERTEX_FROM else []) + EXTRA_PRE.get(eid, [])
    return [x for x in out if x not in have]

COMMON = """## 制作要求（每集通用）
### 每集独立完整（最重要）
- **验收标准**：一个没看过其他任何一集、也没见过总图的高中生，看完本集，能否知道**每一步为什么成立**。做不到就不算完成。
- 本集用到的每个结论，都按“本集先补齐的基础”在片中**写出公式、写出条件、用一两句话复习由来**，不能用“前面讲过”“上一集学过”代替。复习要短，时间主要给本集的新推导。
- 不要求接上一集、预告下一集；开场用“开场问题”直接进入。编号、坐标、系列顺序只是制作元数据，不进入讲解。
### 连贯、不跳步
- **一步只做一件事**：推导过程里每条线可能含多个【方法】，视频中每个【方法】单独成一步，写出中间式子；“展开得”“整理即得”这类说法必须把中间结果写出来。
- **每一步按“为什么想到 → 怎么做 → 得到什么”讲**：先说动机，再动手，最后指出得到的式子和目标差在哪里。
### 着重标注（统一规范）
- 条件（a≠0、a>0、Δ 的符号、区间、参数范围）用橙色框；**▼ 加条件的那一步停顿 1–2 秒**，说明为什么必须加，并给出去掉条件的反例（反例用叉号，不只靠颜色）。
- 区分“运算能不能做”和“结论成不成立”：例如 Δ<0 时方程没有实数根，是“没有实数满足”，不是“运算被禁止”；乘负数后不等号反向，是比较规则变了，不是不能乘。
- 等号成立条件、端点能否取到单独一行框出；关键变形（配方、代换、作差、换元）用高亮色；最终结论用粗框。
- 屏幕上同时保留的高亮不超过两处，讲完的标注及时淡出。
### 数形结合
- 图要简单到**学生能在草稿纸上自己画出来**（一般不超过三个对象），先出图、再从图里“读出”结论，最后把图和式子一一对应。
- 每个图讲完都说一句“以后遇到什么样的题，可以画这张图”。
### 解题导向与内容依据
- 片尾用一句话给出“以后看到什么 → 想到什么”（见本集的“解题思维导向”）。
- 用 manim-video 流程制作；本任务书是**内容依据**，讲法、画面由制作方按 skill 的制作指南设计。
- **结论、条件、取等写法以本任务书为准**，不得自行简化或改写条件（如把“Δ≥0”写成“Δ>0”，或省掉“a>0”“x∈ℝ”）。数值必须自己再算一遍。
- 同一字母在一集里只表示一个量：二次项系数用 a，题目里的参数改用 m、t、k 等。
- 叙述用高中生听得懂的说法，不用超纲术语。
"""


def write_ep(e, prev_id, next_id):
    S = set(e["nodes"])
    steps = [x for i in e["nodes"] for x in E if x[1] == i and x[2] == "derive"] + \
            [x for i in e["nodes"] for x in E if x[1] == i and x[2] == "premise"]
    pre = list(dict.fromkeys(s for s, t, *_ in steps if s not in S))
    pre += extra_pre(e["id"], set(pre) | S)
    meths = collections.Counter(m for s, t, kind, ls, *_ in steps if kind == "derive" for m in METH.findall(" ".join(ls)))
    tools = sorted({m for s, t, kind, ls, *_ in steps for m in re.findall(r"工具([①-⑦])", " ".join(ls))})
    entries = [en for en in ENTRIES if any(c in S for c in en[3])]
    stars = [title(i) for i in e["nodes"] if N[i]["type"] != "start"]
    ext = e.get("ext") or all(i in EXT for i in e["nodes"])
    L = [f"# {e['id']}｜{e['name']}", "",
         f"- 建议时长：{e['minutes']} 分钟；叙事模型：{e.get('model', '逐步构建')}（见 manim-video 的 story-models.md）",
         f"- 本集结论：{'；'.join(stars) if stars else '（本集为起点：定义、约定与公理）'}"]
    if any(i in EXT for i in e["nodes"]):
        L.append(f"- 拓展内容（可按需制作）：{'、'.join(title(i) for i in e['nodes'] if i in EXT)}")
    L += ["", "## 这一集要讲明白的一件事", e["goal"], "", "## 开场问题（不依赖其他集）", e["open"], ""]
    L += ["## 本集先补齐的基础（开场后简短复习：写出公式和条件，一两句话讲清由来；每条不超过约 20 秒，重点仍放在本集）"]
    if e["id"] != "E01":
        L.append(f"- {RULES}")
    if e["id"] in NOTES:
        L.append(f"- {NOTES[e['id']]}")
    for nm, tx in FACTS.get(e["id"], []):
        L.append(f"- **{nm}**：{tx}")
    for s in pre:
        L += base_block(s)
    if not pre and not FACTS.get(e["id"]):
        L.append("- 无（本集从定义出发）")
    L += ["", "## 推导过程（按顺序讲；每一步讲“为什么想到 → 怎么做 → 得到什么”）"]
    if not steps:
        L.append("- 本集都是起点（定义、约定、公理），逐条讲清含义、举例，不需要推导。")
    for k, (s, t, kind, ls, mark, main) in enumerate(steps, 1):
        nsub = len(METH.findall(" ".join(ls)))
        hint = f"；含 {nsub} 个小步骤，逐个展开" if nsub > 1 and kind == "derive" else ""
        L.append(f"{k}. **{title(s)} → {title(t)}**（{'推导' if kind == 'derive' else '提供前提'}{hint}）")
        if mark:
            L.append(f"   - {clean(mark)}（此处停顿，讲为什么要加条件，并给去掉条件的反例）")
        L += [f"   - {clean(x)}" for x in ls if clean(x)]
    L += ["", "## 本集各结论的完整内容（结论、条件、取等以此为准）"]
    for i in e["nodes"]:
        L += [f"#### {title(i)}"] + [f"- {x}" for x in statement(i)] + [""]
    if tools:
        L += ["## 用到的公式工具（片中写出公式即可）"] + [f"- {no} {nm}：{f}" for no, nm, f, *_ in TOOLS if no in tools] + [""]
    L += ["## 画面建议（数形结合：先出图，再从图中读出结论；图要学生能自己画、能套用）"] + [f"- {v}" for v in e["visual"]] + [""]
    L += ["## 着重标注（本集必须突出的地方）"] + [f"- {v}" for v in e["emph"]] + [""]
    L += ["## 解题思维导向（片尾一句话）", e["guide"], ""]
    L += ["## 易错点与边界（必须讲到）"] + [f"- {v}" for v in e["pitfalls"]] + [""]
    if meths:
        L += ["## 本集练到的方法", "、".join(f"{m}（{n} 次）" for m, n in meths.most_common()), ""]
    L += ["## 独立性自检（交付前逐条回答）",
          "- 没看过其他任何一集、也没见过总图的学生，能否说出本集每一步为什么成立？",
          "- “本集先补齐的基础”里的每个结论，片中是否都写出了公式、条件和理由？",
          "- 每个 ▼ 处，是否讲了为什么要加条件，并给出了去掉条件的反例？", "", COMMON]
    L += ["## 制作元数据（不进入讲解）",
          f"- 系列位置：二次函数推导视频 {e['id']}（共 {len(EP)} 集推导 + {len(GROUPS)} 集题型串讲 + 总览）；前一集 {prev_id or '无'}，后一集 {next_id or '无'}",
          "- 本集结论在总图 数学/二次函数大厦/outputs/quadratic-tree-v2.drawio 中的编号与坐标：" + "；".join(f"{title(i)}〔{code(i)}〕" for i in e["nodes"])]
    if pre:
        L.append("- 补齐的基础在系列中的出处：" + "；".join(f"{title(s)}（{s}，{home[s]}）" for s in pre))
    if entries:
        L.append("- 对应的题型入口：" + "、".join(en[0] for en in entries))
    xr = [f"{title(i)}：{N[i]['note']}" for i in e["nodes"] if N[i]["note"] and "同见" in N[i]["note"]]
    if xr:
        L.append("- 与不等式大厦的接口（不进入讲解）：" + "；".join(xr))
    return "\n".join(L) + "\n"


def write_group(gid, name, ids, prev_id, next_id):
    EN = {en[0]: en for en in ENTRIES}
    codes = list(dict.fromkeys(c for x in ids for c in EN[x][3]))
    codes += extra_pre(gid, set(codes))
    L = [f"# {gid}｜题型串讲：{name}", "",
         "- 建议时长：每个题型 1.5–3 分钟，整集 6–10 分钟；叙事模型：问题求解七拍（见 manim-video 的 story-models.md）",
         "- 讲法：每个题型按“看到什么 → 反推到哪 → 先查什么 → 例题演示”的顺序；用到的结论先按“本集先补齐的基础”写出公式、条件和理由。", "",
         "## 本集先补齐的基础（用到时写出公式和条件，一两句话讲清由来）", f"- {RULES}"]
    if gid in NOTES:
        L.append(f"- {NOTES[gid]}")
    L += [f"- **{nm}**：{tx}" for nm, tx in FACTS.get(gid, [])]
    for c in codes:
        L += base_block(c)
    L += ["", "## 题型（按顺序讲）"]
    for k, x in enumerate(ids, 1):
        see, back, check, cs = EN[x]
        q, sol, ans = EXAMPLES[x]
        L += [f"### {k}. 看到：{see}", f"- 反推：{clean(back)}", f"- {clean(check)}",
              "- 用到的结论：" + "、".join(title(c) for c in cs),
              f"- 例题：{q}"] + [f"  - {s}" for s in sol] + [f"  - 答案：{ans}", ""]
    L += ["## 着重标注", "- 每个题型的“先查”用橙色框，讲到时停顿；按“先查”漏掉会错的地方，用反例或叉号标出。",
          "- 例题的每个数值都写出计算过程，答案用粗框。", "",
          "## 解题思维导向（片尾一句话）", "看到题目先问：它在问函数、方程还是不等式？参数在哪里？再从对应的入口反推到结论。", "",
          COMMON,
          "## 制作元数据（不进入讲解）",
          f"- 系列位置：二次函数推导视频 {gid}；前一集 {prev_id or '无'}，后一集 {next_id or '无'}",
          "- 涉及的结论与所在推导片：" + "；".join(f"{title(c)}（{c}〔{GRID.get(c, '?')}〕，{home[c]}）" for c in codes)]
    return "\n".join(L) + "\n"


def fname(e):
    return f"{e['id']}-{e['slug']}.md"


ids_all = [e["id"] for e in EP] + [g[0] for g in GROUPS]
files = {}
for k, e in enumerate(EP):
    files[fname(e)] = write_ep(e, ids_all[k - 1] if k else None, ids_all[k + 1])
for k, (gid, name, ids) in enumerate(GROUPS):
    j = len(EP) + k
    files[f"{gid}-{name}.md"] = write_group(gid, name, ids, ids_all[j - 1], ids_all[j + 1] if j + 1 < len(ids_all) else None)

# 总览
rows = []
for e in EP:
    nd = [i for i in e["nodes"] if N[i]["type"] != "start"]
    nderive = sum(1 for s, t, kind, *_ in E if t in e["nodes"])
    rows.append(f"| [{e['id']}]({fname(e)}) | {e['name']} | {len(e['nodes'])} | {nderive} | {'是' if e.get('ext') else ('部分' if any(i in EXT for i in e['nodes']) else '')} |")
for gid, name, ids in GROUPS:
    rows.append(f"| [{gid}]({gid}-{name}.md) | 题型串讲：{name} | {len(ids)} 个题型 | — | |")
ov = ["# 二次函数推导视频：任务总览", "",
      "依据：`数学/二次函数大厦/outputs/quadratic-tree-v2.drawio`。每集一份任务书，交给视频 agent（manim-video）制作；任务书由 `_generator/gen.py` 从大厦数据 `数学/二次函数大厦/生成/data.py` 生成，改图后重跑即可同步。", "",
      "## 系列结构",
      "- **[E00 总览片](E00-总览-二次函数大厦怎么读.md)**（建议最后做）：讲清怎么读这张图。",
      f"- **E01–E{len(EP):02d} 推导片**：按推导顺序排列，前面的集是后面的前提；标“拓展”的内容可按需制作。",
      f"- **T01–T{len(GROUPS):02d} 题型串讲**：看到题目 → 反推到大厦的哪条路径。建议在对应推导片完成后制作。", "",
      "## 分集清单", "", "| 集 | 标题 | 节点数 | 连线数 | 拓展 |", "|---|---|---|---|---|", *rows, "",
      "## 覆盖核对",
      f"- 图中 {len(N)} 个节点（含 {sum(1 for n in N.values() if n['type'] == 'start')} 个起点）全部分配到推导片，各出现一次；{len(ENTRIES)} 个题型入口全部分配到题型串讲，每个配一道已验算的例题。",
      f"- 连线共 {len(E)} 条（推导 {sum(1 for x in E if x[2] == 'derive')}、前提 {sum(1 for x in E if x[2] == 'premise')}），每条都在其终点所在的那一集讲。",
      "- 跨集引用的结论在每集“本集先补齐的基础”里写出公式、条件和由来。",
      "- 顺序检查：" + ("所有连线的起点都在终点之前或同一集。" if not late else "以下连线的起点在后面的集，制作时作为已知结论引用：" + "；".join(f"{s}→{t}" for s, t in late)), "",
      COMMON]
files["00-总览与制作说明.md"] = "\n".join(ov) + "\n"

E00 = f"""# E00｜总览：二次函数大厦怎么读

- 建议时长：5–6 分钟；叙事模型：全景导览（见 manim-video 的 story-models.md）；建议在推导片完成后制作
- 本集结论：无新结论，讲清“怎么读这张图”

## 这一集要讲明白的一件事
二次函数的知识是一座从定义往上盖的楼：先有函数和二次函数的定义，再有图像、方程、表达式、性质，最后是三个二次、根的分布和综合应用；每一层都由下面一层推出来，加条件的地方都有标记。

## 开场问题（不依赖其他集）
二次函数有顶点式、判别式、韦达定理、根的分布、恒成立……这么多结论，它们是各自独立的，还是能从同一个起点一步步推出来？

## 讲解内容（按顺序）
1. 地基：函数的定义、二次函数的定义（a≠0）、“点在图像上 ⟺ 坐标满足解析式”、实数运算规则、平方非负、区间。
2. 一条主线：y=x² → y=ax² → 平移得顶点式；解方程 → 求根公式与判别式 → 韦达定理。
3. 配方是枢纽：一般式配方得顶点式；由顶点式作差，得到一个恒等式 f(x₁)−f(x₂)=a(x₁−x₂)(x₁+x₂−2h)，对称、单调、比较大小都从它推出。
4. 三个二次：函数的零点、方程的实根、图像与 x 轴的交点是同一组数；开口向上且 Δ>0 时“两根之外为正、之间为负”，同时回答方程和不等式。
5. 条件怎么标：绿色、白色对所有二次函数都成立；橙色要加条件（开口方向、Δ 的符号、区间、参数范围），从哪一步开始加条件就在哪条线上标 ▼。
6. 正推与反推：顺着箭头是“由因导果”；做题时从题型入口“看到什么 → 反推到哪 → 先查什么”往回找。

## 画面建议
- 用总图的缩略图做底，按“地基 → 图像与方程 → 方程的延伸 → 三种表达式 → 图像与性质 → 三个二次 → 根的分布 → 综合”八个分区逐层点亮。
- 在缩略图上走一条完整路径示范：二次函数定义 → 配方得顶点式 → 作差恒等式 → 单调性 → 闭区间最值 → 含参最值；▼ 处停顿说明加了什么条件。
- 再示范一次反推：从“恒成立”入口出发，反推到闭区间最值，再追回地基。

## 着重标注
- 颜色含义（紫色起点、绿色结论、白色中间结果、橙色有条件、蓝色公式与工具、青绿虚线题型入口）用图例框固定在角落。
- ▼ 的含义单独讲一次。

## 解题思维导向（片尾一句话）
遇到二次函数的题，先找它在楼里的哪一层，再顺着箭头往下找依据。

## 易错点与边界（必须讲到）
- 橙色结论离开条件就不成立：例如“最小值 −Δ/(4a)”只在 a>0、x 取全体实数时成立。

{COMMON}
## 制作元数据（不进入讲解）
- 依据：数学/二次函数大厦/outputs/quadratic-tree-v2.drawio；本片可以出现总图缩略图，这是唯一允许提到“总图”的一集。
"""
files["E00-总览-二次函数大厦怎么读.md"] = E00

for f, txt in files.items():
    (OUT / f).write_text(txt)
print(f"写出 {len(files)} 个文件到 {OUT}；顺序问题 {len(late)} 处")
