"""逐节点放大检查：只留节点导出 PNG，再把每个节点裁出来拼成几张总览图，查文字溢出、公式折行。
用法：python3 工具/tiles.py outputs/quadratic-tree-v2.drawio /tmp/tiles [R07,R12,...]
  不给编号时输出全部节点（每张 18 个），图片为 目录/tiles0.png、tiles1.png …"""
import os, subprocess, sys
import xml.etree.ElementTree as ET
from PIL import Image

src = sys.argv[1] if len(sys.argv) > 2 else sys.exit(__doc__)
out = sys.argv[2]
pick = sys.argv[3].split(",") if len(sys.argv) > 3 else None
os.makedirs(out, exist_ok=True)
t = ET.parse(src)
root = t.getroot().find(".//root")
for el in list(root):                      # 连线标注会撑大导出边界，只留节点，裁剪坐标才准
    if el.tag == "UserObject" or el.get("id") in ("0", "1"):
        continue
    root.remove(el)
nd, npng = os.path.join(out, "nodes.drawio"), os.path.join(out, "nodes.png")
t.write(nd, encoding="utf-8")
S = 0.6
subprocess.run(["drawio", "-x", "-f", "png", "-s", str(S), "-o", npng, nd], check=True, capture_output=True)
geo = {u.get("编号"): [float(u.find("mxCell/mxGeometry").get(k)) for k in ("x", "y", "width", "height")] for u in root.iter("UserObject")}
mnx = min(v[0] for v in geo.values()); mny = min(v[1] for v in geo.values())
mxx = max(v[0] + v[2] for v in geo.values()); mxy = max(v[1] + v[3] for v in geo.values())
im = Image.open(npng)
W, H = im.size
bx, by = (W - (mxx - mnx) * S) / 2, (H - (mxy - mny) * S) / 2      # 导出时四周留的边
crops = []
for i in (pick or sorted(geo)):
    x, y, w, h = geo[i]
    X, Y = (x - mnx) * S + bx, (y - mny) * S + by
    crops.append(im.crop((int(X) - 4, int(Y) - 4, int(X + w * S) + 4, int(Y + h * S) + 4)))
for b in range(0, len(crops), 18):
    part = crops[b:b + 18]
    cw, ch = max(c.size[0] for c in part), max(c.size[1] for c in part)
    sheet = Image.new("RGB", (cw * 3, ch * 6), "white")
    for k, c in enumerate(part):
        sheet.paste(c, ((k % 3) * cw, (k // 3) * ch))
    sheet.save(os.path.join(out, f"tiles{b // 18}.png"))
print(f"{len(crops)} 个节点 → {out}/tiles*.png")
