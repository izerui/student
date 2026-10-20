"""对生成的恒等式大厦做自动检查。用法：python3 工具/check.py outputs/identity-tree-v3.drawio
检查项：节点重叠、节点是否在分区框内、分区框互相重叠、〔编号·坐标〕引用是否存在且与节点坐标一致、
每个节点是否有“⇒ 用于”、题型入口个数、PDF 是否单页（同名 .pdf 存在时；旧版 .png 仍检查是否截空）。"""
import html, re, sys, os
import xml.etree.ElementTree as ET

f = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
root = ET.parse(f).getroot().find(".//root")
N, lab, boxes = {}, {}, []
for el in root:
    if el.tag == "UserObject" and el.get("编号"):
        g = el.find("mxCell/mxGeometry")
        N[el.get("编号")] = tuple(float(g.get(k)) for k in ("x", "y", "width", "height"))
        lab[el.get("编号")] = html.unescape(el.get("label"))
    if el.tag == "mxCell" and "dashPattern=8 6" in (el.get("style") or ""):
        g = el.find("mxGeometry")
        boxes.append(tuple(float(g.get(k)) for k in ("x", "y", "width", "height")))
ov = lambda a, b: a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]
inside = lambda v, s: s[0] <= v[0] and s[1] <= v[1] and v[0] + v[2] <= s[0] + s[2] and v[1] + v[3] <= s[1] + s[3]
ids = list(N)
problems = 0
def report(name, items):
    global problems
    problems += bool(items)
    print(("✗ " if items else "✓ ") + name + (f"：{items}" if items else ""))
report("节点重叠", [(a, b) for i, a in enumerate(ids) for b in ids[i + 1:] if ov(N[a], N[b])])
report("超出分区框的节点", [k for k, v in N.items() if not any(inside(v, s) for s in boxes)])
report("分区框互相重叠", [(i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes)) if ov(boxes[i], boxes[j])])
text = html.unescape(open(f, encoding="utf-8").read())
refs = set(re.findall(r"〔([SRPQ]\d{2,3}) · ([A-Z]\d+)〕", text)) | set(re.findall(r"([SRPQ]\d{2,3})〔([A-Z]\d+)〕", text))
coord = {el.get("编号"): el.get("坐标") for el in root if el.tag == "UserObject" and el.get("编号")}
report("指向不存在节点的引用", sorted({a for a, b in refs if a not in N}))
report("坐标与节点不一致的引用", sorted({(a, b, coord[a]) for a, b in refs if a in coord and coord[a] != b}))
report("缺“⇒ 用于”的工具节点", [k for k, v in lab.items() if "⇒ 用于" not in v and not k.startswith("Q")])
qids = [k for k in N if k.startswith("Q")]
report("问题目录里缺的问题节点", [q for q in qids if not re.search(q + r"〔[A-Z]\d+〕", text)])
print(f"  节点 {len(N)}（问题节点 {len(qids)}），坐标引用 {len(refs)}")
pdf = f[:-7] + ".pdf"
if os.path.exists(pdf):
    import subprocess
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    w_, h_ = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
    report("PDF 不是单页", [pages] if pages != 1 else [])
    print(f"  PDF {w_:.0f}×{h_:.0f} pt，{pages} 页")
png = f[:-7] + ".png"
if os.path.exists(png) and not os.path.exists(pdf):
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(png).convert("L"); w, h = im.size
    blank = im.crop((int(w * 0.8), 0, w, h)).getextrema()[0] > 240
    report("PNG 右侧被截空", ["是"] if blank else [])
    blank_b = im.crop((0, int(h * 0.9), w, h)).getextrema()[0] > 240
    report("PNG 底部被截空", ["是"] if blank_b else [])
    print(f"  PNG {w}×{h}")
sys.exit(1 if problems else 0)
