"""对二次函数大厦做自动检查。用法：python3 工具/check.py outputs/quadratic-tree-v2.drawio
数据检查（读 生成/data.py）：每个非起点节点有推导线连入、从起点都能走到、橙色节点有 ▼ 或由橙色节点推出、
  连线和入口引用的编号都存在、每个节点都分到一个分区。
成图检查（读 drawio）：节点互相重叠、分区互不重叠、跨块推导线不穿过其他分区块、不压节点、线上标注不盖住自己的线且互不重叠、〔编号 · 坐标〕引用与节点坐标一致、
  PDF 是否为单页（同名 .pdf 存在时）。
检查通过只说明结构没有问题，不能证明数学内容正确。"""
import html, os, re, sys
import xml.etree.ElementTree as ET

f = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "生成"))
from data import NODES, E, ENTRIES, SECTIONS  # noqa: E402

problems = 0


def report(name, items):
    global problems
    problems += bool(items)
    print(("✗ " if items else "✓ ") + name + (f"：{items}" if items else ""))


# ── 数据 ──
ids = {n[0] for n in NODES}
typ = {n[0]: n[1] for n in NODES}
report("连线引用的编号都存在", [(s, t) for s, t, *_ in E if s not in ids or t not in ids])
report("入口引用的编号都存在", [(en[0], c) for en in ENTRIES for c in en[3] if c not in ids])
inn = {t for s, t, k, *_ in E if k == "derive"}
report("非起点节点都有推导线连入", sorted(i for i in ids if typ[i] != "start" and i not in inn))
seen = {i for i in ids if typ[i] == "start"}
grow = True
while grow:
    grow = False
    for s, t, k, *_ in E:
        if k == "derive" and s in seen and t not in seen:
            seen.add(t)
            grow = True
report("从起点都能走到", sorted(ids - seen))
cond = ("orange", "lorange")
report("橙色节点有 ▼ 或由橙色节点推出", sorted(
    i for i in ids if typ[i] in cond and not any(t == i and k == "derive" and (m or typ[s] in cond) for s, t, k, ls, m, mn in E)))
sec = [x for _, l in SECTIONS for x in l]
report("每个节点恰好分到一个分区", sorted((ids ^ set(sec)) | {x for x in sec if sec.count(x) > 1}))

# ── 成图 ──
root = ET.parse(f).getroot().find(".//root")
N, grid, labels = {}, {}, []
for el in root:
    if el.tag == "UserObject" and el.get("编号"):
        g = el.find("mxCell/mxGeometry")
        N[el.get("编号")] = tuple(float(g.get(k)) for k in ("x", "y", "width", "height"))
        grid[el.get("编号")] = el.get("坐标")
    lab = el.get("label") if el.tag == "UserObject" else el.get("value")
    if lab:
        labels.append(html.unescape(lab))
report("drawio 节点与数据一致", sorted(ids ^ set(N)))
ov = lambda a, b: a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]
keys = sorted(N)
report("节点互不重叠", [(a, b) for i, a in enumerate(keys) for b in keys[i + 1:] if ov(N[a], N[b])])
box = []
for k, (_, l) in enumerate(SECTIONS):          # 分区：本区节点占的范围
    l = [x for x in l if x in N]
    box.append((min(N[x][0] for x in l), min(N[x][1] for x in l),
                max(N[x][0] + N[x][2] for x in l) - min(N[x][0] for x in l), max(N[x][1] + N[x][3] for x in l) - min(N[x][1] for x in l)))
report("分区互不重叠", [(a + 1, b + 1) for a in range(len(box)) for b in range(a + 1, len(box)) if ov(box[a], box[b])])
blk = []                                         # 分区块框（背景层的虚线圆角框）
for el in root:
    st_ = el.get("style") or ""
    if el.tag == "mxCell" and "dashPattern=10 6" in st_ and "rounded=1" in st_:
        g = el.find("mxGeometry")
        blk.append(tuple(float(g.get(k)) for k in ("x", "y", "width", "height")))
inb = lambda px, py, b: b[0] < px < b[0] + b[2] and b[1] < py < b[1] + b[3]
thru = []
for el in root:
    if el.tag != "mxCell" or el.get("edge") != "1":
        continue
    s_, t_ = el.get("source"), el.get("target")
    way = [(float(q.get("x")), float(q.get("y"))) for q in el.iter("mxPoint") if q.get("as") is None]
    if not way or s_ not in N or t_ not in N:
        continue
    S, T = N[s_], N[t_]
    own = [b for b in blk if inb(S[0] + 1, S[1] + 1, b) or inb(T[0] + 1, T[1] + 1, b)]
    if len(own) < 2:                                # 同一块内的线不查
        continue
    poly = [(S[0] + S[2] / 2, S[1] + S[3])] + way + [(T[0] + T[2] / 2, T[1])]
    for (x1, y1), (x2, y2) in zip(poly, poly[1:]):
        if any(inb(x1 + (x2 - x1) * k / 30, y1 + (y2 - y1) * k / 30, b) for k in range(1, 30) for b in blk if b not in own):
            thru.append(f"{s_}→{t_}")
            break
report("跨块推导线不穿过其他分区块", sorted(set(thru)))
press = []                                       # 跨块推导线（从目标上沿进入的）不压到起点、终点以外的节点
for el in root:
    if el.tag != "mxCell" or el.get("edge") != "1" or "entryY=0" not in (el.get("style") or ""):
        continue
    s_, t_ = el.get("source"), el.get("target")
    if s_ not in N or t_ not in N:
        continue
    S, T = N[s_], N[t_]
    m = re.search(r"exitX=([\d.]+);exitY=([\d.]+)", el.get("style"))
    src = (S[0] + S[2] * float(m.group(1)), S[1] + S[3] * float(m.group(2))) if m else (S[0] + S[2] / 2, S[1] + S[3])
    poly = [src] + [(float(q.get("x")), float(q.get("y"))) for q in el.iter("mxPoint") if q.get("as") is None] + [(T[0] + T[2] / 2, T[1])]
    for (x1, y1), (x2, y2) in zip(poly, poly[1:]):
        if any(n not in (s_, t_) and b[0] + 2 < x1 + (x2 - x1) * k / 60 < b[0] + b[2] - 2 and b[1] + 2 < y1 + (y2 - y1) * k / 60 < b[1] + b[3] - 2
               for k in range(1, 60) for n, b in N.items()):
            press.append(f"{s_}→{t_}")
            break
report("跨块推导线不压节点", sorted(set(press)))
LB = {}                                          # 线上标注：独立文字块 e{n}L
for el in root:
    i_ = el.get("id") or ""
    if el.tag == "mxCell" and i_.endswith("L") and i_[:-1].startswith("e") and el.get("vertex") == "1":
        g = el.find("mxGeometry")
        LB[i_[:-1]] = tuple(float(g.get(k)) for k in ("x", "y", "width", "height"))
own = []
for el in root:
    if el.tag != "mxCell" or el.get("edge") != "1" or el.get("id") not in LB:
        continue
    s_, t_ = el.get("source"), el.get("target")
    if s_ not in N or t_ not in N:
        continue
    S, T, st_ = N[s_], N[t_], el.get("style") or ""
    m = re.search(r"exitX=([\d.]+);exitY=([\d.]+)", st_)
    src = (S[0] + S[2] * float(m.group(1)), S[1] + S[3] * float(m.group(2))) if m else (S[0] + S[2] / 2, S[1] + S[3] / 2)
    poly = [src] + [(float(q.get("x")), float(q.get("y"))) for q in el.iter("mxPoint") if q.get("as") is None] + [(T[0] + T[2] / 2, T[1] + (0 if "entryY=0" in st_ else T[3] / 2))]
    x, y, w, h = LB[el.get("id")]
    if any(x < a + (c - a) * k / 20 < x + w and y < b + (d - b) * k / 20 < y + h for (a, b), (c, d) in zip(poly, poly[1:]) for k in range(21)):
        own.append(f"{s_}→{t_}")
report("线上标注不盖住自己的线", sorted(own))
lk = sorted(LB)
report("线上标注互不重叠、不压节点", [(a, b) for i, a in enumerate(lk) for b in lk[i + 1:] if ov(LB[a], LB[b])] + [a for a in lk if any(ov(LB[a], N[n]) for n in N)])
bad = []
for lab in labels:
    for c, gpos in re.findall(r"〔([SJRP]\d\d) · ([A-Z]+\d+)〕", lab):
        if c not in grid:
            bad.append(f"{c} 不存在")
        elif grid[c] != gpos:
            bad.append(f"{c} 写作 {gpos}，实际 {grid[c]}")
report("〔编号 · 坐标〕引用一致", sorted(set(bad)))
pdf = f[:-len(".drawio")] + ".pdf"
if os.path.exists(pdf):
    import subprocess
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    pages = re.search(r"Pages:\s+(\d+)", info)
    report("PDF 为单页（整图不被分页）", [] if pages and pages.group(1) == "1" else [f"{pdf} 页数 {pages.group(1) if pages else '?'}"])
print("全部通过" if not problems else f"{problems} 项有问题")
