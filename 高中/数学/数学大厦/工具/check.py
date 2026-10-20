"""检查《数学大厦-节点清单.md》是否自洽（数学大厦自己的规则；通用的结构检查由 skill knowledge-map-web 的 tools/build.mjs 做）。
用法（在数学大厦目录下）：python3 工具/check.py
检查项：
1. 每个分组写了短名、区域、标志、是什么、从哪来、例子；每个知识点写了标志、是什么、从哪来；没拆的分组写了“依赖”；
2. 依赖引用的都是图上的卡片（拆过的分组要写到具体知识点），且不能依赖更高的楼层；整张图没有环；
3. “往上通向”只能指向更高位置；
4. 主干链（清单开头）每一步都有清单里的依赖或“往上通向”支撑；
5. 思想方法引用的都是图上的卡片；
6. 每条依赖都在括号里写明“怎么推的”。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from checklist import load, ids_in, key, layer_of

C = load()
text, rooms, points, nodes, deps, ups = C["text"], C["rooms"], C["points"], C["nodes"], C["deps"], C["ups"]
problems = []
dep_ids = {n: {d["id"] for d in ds} for n, ds in deps.items()}

# 1. 字段齐全
for r, room in rooms.items():
    for k in ("短名", "区域", "标志", "是什么", "从哪来", "例子"):
        if not room["f"].get(k):
            problems.append(f"分组 {r} 缺少“{k}”")
    if not room["points"] and "依赖" not in room["f"]:
        problems.append(f"分组 {r} 没拆成知识点，要写“依赖”")
for p, pt in points.items():
    for k in ("标志", "是什么", "从哪来"):
        if not pt["f"].get(k):
            problems.append(f"知识点 {p} 缺少“{k}”")
    if not p.startswith(pt["room"] + "."):
        problems.append(f"知识点 {p} 的编号和所在分组 {pt['room']} 对不上")

# 2. 依赖存在、不往高层指、无环
for n in nodes:
    for r in dep_ids[n]:
        if r in rooms and rooms[r]["points"]:
            problems.append(f"{n} 引用了已拆成知识点的分组 {r}，请写到具体知识点")
        elif r not in nodes:
            problems.append(f"{n} 的依赖引用了不存在的 {r}")
        elif layer_of(r) > layer_of(n):
            problems.append(f"{n}（第 {layer_of(n)} 层）依赖了更高楼层的 {r}（应写进“往上通向”）")
state = {}
def dfs(x, path):
    state[x] = 1
    for y in [n for n in nodes if x in dep_ids[n]]:
        if state.get(y) == 1:
            problems.append("依赖成环：" + " → ".join(path + [x, y]))
        elif not state.get(y):
            dfs(y, path + [x])
    state[x] = 2
for n in nodes:
    if not state.get(n):
        dfs(n, [])

# 3. 往上通向
for r, targets in ups.items():
    for t in targets:
        if t not in rooms and t not in points:
            problems.append(f"{r} 的“往上通向”指向不存在的 {t}")
        elif key(t) <= key(r):
            problems.append(f"{r} 的“往上通向”指向 {t}，方向不对")

# 4. 主干链
chain = text[text.index("## 主干链"):text.index("## 第 0 层")]
for line in chain.splitlines():
    toks = re.findall(r"(→|⇢|/)|(?<![\d.])(\d\.\d{1,2}(?:\.\d{1,2})?)(?![\d])(?!\.\d)", line)
    prev, op, base = None, None, None
    for arrow, nid in toks:
        if arrow:
            op = arrow
            continue
        if nid not in nodes:
            problems.append(f"主干链里的 {nid} 不是图上的卡片")
        if op == "/":
            src, op = base, "→"
        else:
            src, base = prev, prev
        if src and op:
            ok = (src in dep_ids.get(nid, set())) if op == "→" else (nid in ups.get(src, []) or nid in ups.get(src.rsplit(".", 1)[0], []))
            if not ok:
                problems.append(f"主干链 {src} {op} {nid} 在清单里没有依据")
        prev, op = nid, None

# 5. 思想方法
sec = text[text.index("## 思想方法"):text.index("## 节点总数")]
for name, where in re.findall(r"- \*\*(.+?)\*\*：.*?｜出现在：(.*)", sec):
    for r in ids_in(where):
        if r not in nodes:
            problems.append(f"思想方法“{name}”引用的 {r} 不是图上的卡片")

# 6. 怎么推的
for n in nodes:
    for d in deps[n]:
        if not d.get("how"):
            problems.append(f"{n} 的依赖 {d['id']} 没在括号里写“怎么推的”")

print(f"分组 {len(rooms)} 个，其中 {sum(1 for r in rooms.values() if r['points'])} 个拆成 {len(points)} 个知识点；图上卡片 {len(nodes)} 张")
if problems:
    print(f"发现 {len(problems)} 个问题：")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("全部检查通过")
