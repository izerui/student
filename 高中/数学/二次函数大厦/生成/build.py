"""生成二次函数大厦 drawio，并用 draw.io 命令行导出高清 PDF（矢量、单页、按图裁切；不再导出 PNG）。
用法（在 数学/二次函数大厦/ 下）：
  python3 生成/build.py v2              → outputs/quadratic-tree-v2.drawio、.pdf
  python3 生成/build.py 任意路径.drawio   → 写到指定路径（不导出 PDF，调试用）"""
import json, math, re, subprocess, sys, html
from xml.sax.saxutils import escape
from data import NODES, E, EXT, TOOLS, ENTRIES, TITLE, SUBTITLE, SECTIONS, ENTRY_HOW, LAYERS, LAYER_NOTE, TOOL_SIGNALS, TOOL_LABEL, METHODS, METHOD_IGNORE, EDGE_USES
from texify import texify as TX

from pathlib import Path
HERE = Path(__file__).resolve().parent
ARG = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
VERSIONED = not ARG.endswith(".drawio")
OUT = str(HERE.parent / "outputs" / f"quadratic-tree-{ARG}.drawio") if VERSIONED else ARG
ST = {
 "start": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#6A1B9A;strokeWidth=2;fontFamily=PingFang SC;fontSize=13;fontColor=#4A148C;shadow=1;arcSize=12;",
 "green": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=2;fontFamily=PingFang SC;fontSize=13;fontColor=#1B5E20;fontStyle=1;shadow=1;arcSize=12;",
 "white": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#90A4AE;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#37474F;arcSize=10;",
 "orange": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE0B2;strokeColor=#E65100;strokeWidth=2.5;fontFamily=PingFang SC;fontSize=13;fontColor=#BF360C;fontStyle=1;shadow=1;arcSize=12;",
 "lorange": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FB8C00;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#BF360C;arcSize=10;",
 "tool": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1565C0;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#0D47A1;arcSize=10;align=left;spacingLeft=8;",
 "method": "rounded=1;whiteSpace=wrap;html=1;fillColor=#EFEBE9;strokeColor=#6D4C41;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#4E342E;arcSize=10;align=left;spacingLeft=8;",
 "entry": "rounded=1;arcSize=12;whiteSpace=wrap;html=1;dashed=1;dashPattern=6 4;fillColor=#E0F2F1;strokeColor=#00897B;strokeWidth=2;align=left;spacingLeft=10;spacingRight=6;fontFamily=PingFang SC;fontSize=11;fontColor=#00695C;",
 "panel": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#B0BEC5;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#37474F;align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;arcSize=4;",
 "title": "text;html=1;fontFamily=PingFang SC;fontSize=40;fontStyle=1;fontColor=#263238;align=left;verticalAlign=top;whiteSpace=wrap;",
 "grid": "text;html=1;fontFamily=PingFang SC;fontSize=28;fontStyle=1;fontColor=#B0BEC5;align=center;verticalAlign=middle;",
 "gridline": "line;strokeColor=#ECEFF1;strokeWidth=2;dashed=1;html=1;",
}
EDGE = ("html=1;whiteSpace=nowrap;rounded=1;curved=1;fontFamily=PingFang SC;labelBackgroundColor=#FFFFFF;"
        "endArrow=block;endSize=7;fontSize=11;")
E_MAIN = EDGE + "strokeColor=#263238;strokeWidth=3.5;fontColor=#263238;"
E_DER = EDGE + "strokeColor=#455A64;strokeWidth=2;fontColor=#263238;"
E_PRE = EDGE + "strokeColor=#B0BEC5;strokeWidth=1.5;fontColor=#607D8B;dashed=0;"
TYPE = {"start": "起点", "green": "结论", "white": "中间结果", "orange": "结论（有条件）", "lorange": "中间结果（有条件）"}

def vlen(s):
    return sum(1.0 if ord(ch) > 0x2E80 else 0.56 for ch in s)

def mvlen(s):
    return sum(1.0 if ord(ch) > 0x2E80 else 0.72 for ch in s)

def size(lines, fs=13, maxw=560, minw=230):
    w = max(mvlen(l) for l in lines) * fs * 1.08 + 40
    w = max(minw, min(maxw, w))
    per = (w - 40) / (fs * 1.08)
    rows = sum(max(1, math.ceil(mvlen(l) / per)) for l in lines)
    tall = sum(1 for l in lines if "/" in l or "√" in l)
    return int(w), int(rows * (fs + 8) + 30 + tall * 16)

gray = lambda s: f'<span style="font-size:11px;color:#607D8B;font-weight:normal;">{TX(s)}</span>'
code_span = lambda c: f'<span style="font-size:10px;color:#78909C;font-weight:normal;">{c}</span>'
tag = lambda t: f'<span style="background-color:#E65100;color:#FFFFFF;font-size:10px;font-weight:bold;">&nbsp;{TX(t)}&nbsp;</span>'
ext_tag = '<span style="background-color:#90A4AE;color:#FFFFFF;font-size:10px;">&nbsp;拓展&nbsp;</span>'

nodes = {}
for nid, typ, cond, title, lines, note in NODES:
    head = (tag(cond) + " " if cond else "") + (ext_tag + " " if nid in EXT else "") + code_span(nid)
    rest = [TX(l) for l in lines]
    if note:
        rest.append(f'<span style="font-size:11px;color:#8D6E63;">{TX(note)}</span>' if typ == "start" else gray(note))
    w, h = size([title] + lines + ([note] if note else []) + ([cond + nid] if cond else []))
    nodes[nid] = dict(type=typ, cond=cond, title=title, head=head + "<br>" + TX(title), rest=rest, nbody=len(lines), w=w, h=h)

TOOL_SPAN = '<span style="background-color:#BBDEFB;color:#0D47A1;font-weight:bold;">{}</span><sup style="color:#0D47A1;font-weight:bold;font-size:10px;">{}</sup>'
METH_SPAN = '<span style="background-color:#EFEBE9;color:#4E342E;font-weight:bold;">{}</span>'
M_CLASS = {lb: name for name, labels, *_ in METHODS for lb in labels}      # 推导线上的方法名 → 方法类


# 借用的工具不能是推出节点之后的结论（防循环）
_kids = {}
for s_, t_, k_, *_ in E:
    if k_ == "derive":
        _kids.setdefault(s_, []).append(t_)
def _desc(n, seen=None):
    seen = set() if seen is None else seen
    for c in _kids.get(n, []):
        if c not in seen:
            seen.add(c); _desc(c, seen)
    return seen
for (s_, t_), rs in EDGE_USES.items():
    assert any(a == s_ and b == t_ for a, b, k, *_ in E if k == "derive"), f"没有这条推导线：{s_}→{t_}"
    for r in rs:
        assert r not in (s_, t_) and r not in _desc(t_), f"{s_}→{t_} 引用 {r} 会循环"
USE_NAME = lambda r: re.split(r"[（(：]", nodes[r]["title"].lstrip("★ "))[0].strip()
def use_line(s, t):
    rs = EDGE_USES.get((s, t))
    return ("⇐ 用到工具：" + "、".join(f"{USE_NAME(r)}〔{r} · A1〕" for r in rs)) if rs else None


def elabel(lines, mark, s=None, t=None):
    """推导线标注：方法（棕底）；直接引用工具的（蓝底，右上角是引用的节点或工具箱圈号）。"""
    parts = []
    if mark:
        parts.append(f'<span style="color:#E65100;font-weight:bold;">{TX(mark)}</span>')
    for l in lines:
        x = TX(l)
        for m, r in TOOL_LABEL.items():            # 工具一律写「」（参照不等式大厦），右上角是引用的节点或圈号
            x = x.replace(f"【{m}】", TOOL_SPAN.format(f"「{m}」", r)).replace(f"「{m}」", TOOL_SPAN.format(f"「{m}」", r)) if f"【{m}】" in x else x.replace(f"「{m}」", TOOL_SPAN.format(f"「{m}」", r))
        for m in M_CLASS:
            x = x.replace(f"【{m}】", METH_SPAN.format(f"【{m}】"))
        parts.append(x)
    u = use_line(s, t)
    if u:
        u = re.sub(r"〔([SRP]\d\d) · A1〕", lambda m: f"〔{m.group(1)} · {grid(m.group(1))}〕", u)
        parts.append(TOOL_SPAN.format(TX(u), ""))
    return "<br>".join(parts)

# ── 排版：每个分区单独用 dot 排成一个紧凑的块，块再按依赖顺序摆成几行（参照不等式大厦的分区块）──
LFS, LCAP = 13, 330          # 线上标注字号、最大宽度（超出则折行）
def lsize(allL):
    ws = [mvlen(l) * LFS * 1.08 for l in allL]
    lw = min(LCAP, max(ws)) + 20
    rows = sum(max(1, math.ceil(w / LCAP)) for w in ws)
    return int(lw), int(rows * (LFS + 7) + sum(12 for l in allL if "/" in l or "√" in l) + 8)
def all_lines(s, t, kind, lines, mark):
    return ([mark] if mark else []) + lines + ([use_line(s, t)] if use_line(s, t) else [])

SEC_OF = {nid: k for k, (_, ids) in enumerate(SECTIONS) for nid in ids}
# 跨分区的前提不画线，写进节点“⇐ 前提”（先加高度再排版）
dropped = set()
for i, (s_, t_, kind, lines, mark, main) in enumerate(E):
    if kind == "premise" and SEC_OF[s_] != SEC_OF[t_]:
        dropped.add(i)
        nodes[t_].setdefault("pre", []).append((s_, " ".join(lines).replace("【前提】", "")))
        nodes[t_]["h"] += 18

PAD, TT = 60, 70             # 块内边距、块标题高度
blocks = []
epath = {}
for k, (stitle, ids) in enumerate(SECTIONS):
    S = set(ids)
    g = ["digraph G {", "rankdir=TB; nodesep=0.7; ranksep=0.9; splines=true; newrank=true;",
         'node [shape=box, fixedsize=true, label=""]; edge [fontsize=13, fontname="Courier"];']
    for nid in ids:
        g.append(f'"{nid}" [width={nodes[nid]["w"]/72:.2f}, height={nodes[nid]["h"]/72:.2f}];')
    for i, (s_, t_, kind, lines, mark, main) in enumerate(E):
        if s_ in S and t_ in S and i not in dropped:
            lw_, lh_ = lsize(all_lines(s_, t_, kind, lines, mark))
            ph = "\\n".join("x" * int(lw_ / 7.8) for _ in range(max(1, round(lh_ / 15.6))))
            extra = "constraint=false, " if kind == "premise" else f"weight={8 if main else 2}, "
            g.append(f'"{s_}" -> "{t_}" [{extra}label="{ph}", id="e{i+1}"];')
    g.append("}")
    lay = json.loads(subprocess.run(["dot", "-Tjson0"], input="\n".join(g), capture_output=True, text=True, check=True).stdout)
    bw, bh = map(float, lay["bb"].split(",")[2:])
    pos = {}
    for o in lay["objects"]:
        if o["name"] in S:
            x, y = map(float, o["pos"].split(","))
            pos[o["name"]] = (x, bh - y)
    paths = {}
    for ed in lay.get("edges", []):
        if "pos" not in ed:
            continue
        pts = [tuple(map(float, tok.split(","))) for tok in ed["pos"].split() if not tok.startswith(("e,", "s,"))]
        lp = tuple(map(float, ed["lp"].split(","))) if ed.get("lp") else None
        paths[ed["id"]] = ([(x, bh - y) for x, y in pts], (lp[0], bh - lp[1]) if lp else None)
    blocks.append(dict(k=k, title=stitle, pos=pos, paths=paths, w=bw + 2 * PAD, h=bh + 2 * PAD + TT))

# 块的摆放：地基在最上面居中；下面按依赖顺序每行几块，行内居中
ROWS = [[0], [3, 1, 2], [4, 5], [7, 6]]
GAPX, GAPY = 220, 640
roww = [sum(blocks[k]["w"] for k in r) + GAPX * (len(r) - 1) for r in ROWS]
W = max(roww)
yy = 260
row_top = []
for r, rw in zip(ROWS, roww):
    xx = 200 + (W - rw) / 2
    for k in r:
        b = blocks[k]
        b["x"], b["y"] = xx, yy
        xx += b["w"] + GAPX
    for k in r:
        blocks[k]["row"] = ROWS.index(r)
    row_top.append(yy)
    yy += max(blocks[k]["h"] for k in r) + GAPY
for b in blocks:
    ox, oy = b["x"] + PAD, b["y"] + PAD + TT
    for nid, (cx, cy) in b["pos"].items():
        n = nodes[nid]
        n["x"], n["y"] = ox + cx - n["w"] / 2, oy + cy - n["h"] / 2
    for eid, (pts, lp) in b["paths"].items():
        epath[eid] = ([(x + ox, y + oy) for x, y in pts], (lp[0] + ox, lp[1] + oy) if lp else None)
DX = DY = 0
MAXX = 200 + W + 200
MAXY = yy - GAPY + 200

# ── 网格坐标 ──
CW, RH = 800, 600
cols = math.ceil(MAXX / CW); rows = math.ceil(MAXY / RH)
L = lambda i: chr(ord("A") + i)
def grid(nid):
    n = nodes[nid]
    cx, cy = n["x"] + n["w"] / 2, n["y"] + n["h"] / 2
    return f"{L(int(cx // CW))}{int(cy // RH) + 1}"
ref = lambda nid: f"〔{nid} · {grid(nid)}〕"

# ── 左侧导航 ──
cells = []
uid = [0]
def cell(value, style, x, y, w, h, parent="1", attrs=None):
    uid[0] += 1
    cid = f"c{uid[0]}"
    cells.append((cid, value, style, x, y, w, h, parent, attrs))
    return cid

PW = 1800; PX = -PW - 260
py = 40
cell(escape(TITLE), ST["title"], PX, py, PW, 60, "bg"); py += 70
cell("<br>".join(escape(s) for s in SUBTITLE), "text;html=1;fontFamily=PingFang SC;fontSize=15;fontColor=#455A64;align=left;verticalAlign=top;whiteSpace=wrap;", PX, py, PW, 80, "bg"); py += 110

LEG = [("start", "【定义】【约定】【公理】【定理】", "紫色：起点，直接承认或定义"),
       ("green", "★ 结论", "绿色：结论，对所有二次函数、所有 x 都成立"),
       ("white", "中间结果", "白底：推导中间一步，不加条件"),
       ("orange", "★ 结论（有条件）", "橙色：要加条件才成立（开口方向、Δ、区间、参数），标题旁橙色标签写明条件"),
       ("tool", "「韦达」ᴾ²¹", "蓝底「」：套用的工具，右上角是引用的节点或工具箱圈号；左侧“工具”一栏（工具、方法的区别见“三层”）"),
       ("method", "【作差】", "棕底【】：方法，往哪走，一条线只走一步；左侧“方法”一栏按类写方向、依据、信号、易错点"),
       ("entry", "看到… / 反推…", "青绿虚线框：题型入口，做题从这里进")]
ly = py
cell('<b style="font-size:20px">图例</b>', ST["panel"], PX, ly, PW, 60 + 70 * len(LEG) + 62 * 6 + 10, "bg")
ly += 56
for typ, sample, desc in LEG:
    cell(escape(sample), ST[typ], PX + 30, ly, 300, 54, "bg")
    cell(TX(desc), "text;html=1;fontFamily=PingFang SC;fontSize=14;fontColor=#37474F;align=left;verticalAlign=middle;whiteSpace=wrap;", PX + 350, ly, PW - 380, 54, "bg")
    ly += 70
for t in ["灰底虚线框 = 分区：最上面是地基，沿箭头往下读；跨框的深色线是分区之间的推导，跨框的前提写在节点里“⇐ 前提”；紫色起点放在第一次用到它的分区",
          "连线：深色实线 = 推导，越粗越是主干；线上写【方法】和具体操作",
          "浅灰线 = 前提：引用别处已推出的结论，线上写【前提】",
          "▼ 加条件：从这一步起有使用条件，后面的结论都带着它",
          "〔编号 · 坐标〕：S 起点，R、P 是结论的编号（有没有条件看颜色和橙色标签，不看字母）；按图边字母（列）和数字（行）找格子",
          "★ 越多越重要；灰色“拓展”可先跳过；“同见不等式大厦〔编号〕”= 两张图重合的结论"]:
    cell(escape(t), "text;html=1;fontFamily=PingFang SC;fontSize=14;fontColor=#37474F;align=left;verticalAlign=middle;whiteSpace=wrap;", PX + 30, ly, PW - 60, 56, "bg")
    ly += 62
py = ly + 60

scope = ["条件层级（越往下限制越多）",
         "所有二次函数（a≠0）、所有实数 x —— 绿色、白色节点",
         "  └ 开口方向：a>0（或 a<0）—— 单调性、最值、远近规律、三个二次",
         "      └ 判别式：Δ>0、Δ=0、Δ<0；交点式、韦达要求 Δ≥0",
         "      └ 区间：x∈[m,n] —— 闭区间最值、区间上恒成立",
         "  └ 参数：系数含参数时先分 a=0（不是二次函数）与 a≠0",
         "a<0 的结论把 a>0 的结论“上下翻过来”即可：最小变最大、递增变递减"]
cell("<br>".join(("<b style='font-size:18px'>" + escape(s) + "</b>") if i == 0 else TX(s) for i, s in enumerate(scope)),
     ST["panel"] + "fontSize=14;", PX, py, PW, 200, "bg")
py += 240


# 三层说明
lay = ["<b style='font-size:20px'>三层：工具、方法、题型入口</b>"] + [f"<b>{escape(n)}</b>（{escape(q)}）：{TX(d)}　→ 图中：{escape(w)}" for n, q, d, w in LAYERS] + [TX(x) for x in LAYER_NOTE]
lh = 50 + 22 * sum(max(1, math.ceil(mvlen(re.sub(r'<[^>]+>', '', x)) * 14 * 1.08 / (PW - 40))) for x in lay)
cell("<br>".join(lay), ST["panel"] + "fontSize=14;", PX, py, PW, lh, "bg")
py += lh + 40
ENO = {en[0]: k + 1 for k, en in enumerate(ENTRIES)}                 # 入口编号
short = lambda see: re.split(r"[（：]", see)[0]
def wrap_rows(txt, w, fs=13):
    return max(1, math.ceil(mvlen(txt) * fs * 1.08 / (w - 24)))
def refs_txt(t):
    """把文字里的〔编号〕换成〔编号 · 坐标〕。"""
    return re.sub(r"〔([SRP]\d\d)〕", lambda m: f"〔{m.group(1)} · {grid(m.group(1))}〕", t)
def target(x):
    return f"入口{ENO[x[3:]]}" if x.startswith("入口:") else f"〔{x} · {grid(x)}〕"
BLOCK = "fontSize=13;verticalAlign=top;spacingTop=10;spacingLeft=12;spacingRight=8;absoluteArcSize=1;arcSize=18;"
bw = (PW - 30) // 2
def draw_blocks(title, color, style, blocks):
    """一栏：标题一行，下面每个工具（方法）一个独立小块，两列，哪列低放哪列。blocks = [(html 行, 估高用的纯文字行)]"""
    global py
    cell(f'<b style="font-size:20px">{title}</b>', f"text;html=1;fontFamily=PingFang SC;fontColor={color};align=left;whiteSpace=wrap;", PX, py, PW, 40, "bg")
    py += 50
    col = [py, py]
    for lines, rows in blocks:
        h = 30 + sum(wrap_rows(re.sub(r'<[^>]+>', '', x), bw, 12) * 19 for x in rows)
        c = col.index(min(col))
        cell("<br>".join(lines), style + BLOCK, PX + c * (bw + 30), col[c], bw, h, "bg")
        col[c] += h + 20
    py = max(col) + 50

# 工具：主图节点就是工具；这里放常用节点速查和借来的公式，每条一块
tb = []
sig = ["<b>常用节点速查：看到什么 → 想到哪个节点</b>"]; sr = list(sig)
for see, go in TOOL_SIGNALS:
    sig.append(f"▸ 看到{TX(see)} → {TX(refs_txt(go))}"); sr.append(f"▸ 看到{see} → {refs_txt(go)}")
tb.append((sig, sr))
for no, name, f, uses in TOOLS:
    tl = [f"<b>{no} {escape(name)}</b>", TX(f)]; tr = [f"{no} {name}", f]
    for where, how, xs in uses:
        x = f"▸ 用在 {where}：{how} " + "".join(target(t) for t in xs)
        tl.append(TX(x)); tr.append(x)
    tb.append((tl, tr))
draw_blocks("工具（能用什么）：主图每个节点都是工具；下面是常用节点速查和工具箱（借来的公式原文，按圈号查，不画线）", "#0D47A1", ST["tool"], tb)

# 方法：每类一块，写方向、依据、信号、易错点；用在哪里由推导线上的【…】自动统计
used = {name: [] for name, *_ in METHODS}
unknown = set()
for s_, t_, k_, ls_, *_ in E:
    if k_ != "derive":
        continue
    for m in re.findall(r"【(.+?)】", " ".join(ls_)):
        if m in TOOL_LABEL or m in METHOD_IGNORE:
            continue
        if m not in M_CLASS:
            unknown.add(m); continue
        if t_ not in used[M_CLASS[m]]:
            used[M_CLASS[m]].append(t_)
assert not unknown, f"推导线上的方法没有归类：{unknown}"
mb = []
for name, labels, way, basis, signal, warn in METHODS:
    subs = [l for l in labels if l != name]
    head = f"【{name}】" + (f"（{'、'.join(subs)}）" if subs else "")
    mrows = [f"方向：{way}"] + ([f"依据：{basis}"] if basis else []) + [f"信号：{signal}"]
    if used[name]:
        mrows.append("用在：" + "、".join(f"{nodes[t]['title'].lstrip('★ ')}〔{t} · {grid(t)}〕" for t in used[name]))
    mrows.append(f"⚠ {warn}")
    mb.append(([f"<b style='font-size:15px'>{escape(head)}</b>"] + [TX(refs_txt(r)) for r in mrows], [head] + [refs_txt(r) for r in mrows]))
draw_blocks("方法（往哪走）：每类方法往哪走、凭什么、何时用", "#4E342E", ST["method"], mb)
cell('<b style="font-size:20px">题型入口（从哪进）：看到什么 → 反推到哪 → 先查什么 → 用哪个工具、走哪个方向 → 去这里查</b>', "text;html=1;fontFamily=PingFang SC;fontColor=#00695C;align=left;", PX, py, PW, 40, "bg")
py += 50
ew = (PW - 60) // 3
col_y = [py, py, py]
for i, (see, back, check, codes) in enumerate(ENTRIES):
    links = "<br>".join(f'<span style="color:#004D40;">▸ {TX(nodes[c]["title"].lstrip("★ "))} <b>{ref(c)}</b></span>' for c in codes)
    how = ENTRY_HOW.get(see, [])
    tools_txt = ""
    if how:
        tools_txt = ('<span style="color:#37474F;"><b>用哪个工具、走哪个方向：</b></span><br>'
                     + "<br>".join((f'<span style="color:#0D47A1;">{TOOL_SPAN.format(nodes[k]["title"].lstrip("★ "), k)} {TX(t)}</span>' if k in nodes
                                    else f'<span style="color:#4E342E;">{METH_SPAN.format("【" + k + "】")} {TX(t)}</span>') for k, t in how) + "<br>")
    v = (f"<b>入口{i + 1}　看到 {TX(see)}</b><br>反推：{TX(back)}<br>{TX(check)}<br>{tools_txt}"
         f'<span style="color:#00695C;font-weight:bold;">去这里查：</span><br>{links}')
    nrow = lambda x: max(1, math.ceil(mvlen(x) * 11 * 1.08 / (ew - 30)))
    h = 30 + 18 * (nrow("看到 " + see) + nrow("反推：" + back) + nrow(check) + (1 + sum(nrow("X " + t) for _, t in how) if how else 0) + 1 + len(codes))
    c = col_y.index(min(col_y))
    cell(v, ST["entry"], PX + c * (ew + 30), col_y[c], ew, h, "1")
    col_y[c] += h + 24
py = max(col_y) + 40



# 分区块：浅底虚线框，左上角深色标题
for b in blocks:
    cell("", f"rounded=1;arcSize=3;html=1;fillColor={'#F3F6F9' if b['k'] % 2 else '#FFFDF5'};strokeColor=#B0BEC5;strokeWidth=2;dashed=1;dashPattern=10 6;", b["x"], b["y"], b["w"], b["h"], "bg")
    cell(f"<b>{escape(b['title'])}</b>", "rounded=1;arcSize=20;html=1;fillColor=#37474F;strokeColor=none;fontColor=#FFFFFF;fontFamily=PingFang SC;fontSize=24;align=left;spacingLeft=14;", b["x"] + 16, b["y"] + 14, min(b["w"] - 32, mvlen(b["title"]) * 26 + 40), 46, "bg")
# 网格
for i in range(cols + 1):
    cell("", ST["gridline"], i * CW, 140, 1, rows * RH + 120, "bg")
for j in range(rows + 1):
    cell("", ST["gridline"], 0, 200 + j * RH - 60, cols * CW, 1, "bg")
for i in range(cols):
    cell(L(i), ST["grid"], i * CW + CW / 2 - 40, 150, 80, 50, "bg")
    cell(L(i), ST["grid"], i * CW + CW / 2 - 40, rows * RH + 210, 80, 50, "bg")
for j in range(rows):
    cell(str(j + 1), ST["grid"], -90, j * RH + RH / 2 - 25, 70, 50, "bg")
    cell(str(j + 1), ST["grid"], cols * CW + 20, j * RH + RH / 2 - 25, 70, 50, "bg")

# ── 写 XML ──
out = ['<mxfile host="build.py"><diagram id="quadratic" name="二次函数大厦"><mxGraphModel dx="2000" dy="1000" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" math="1" shadow="0"><root>',
       '<mxCell id="0"/>', '<mxCell id="bg" value="背景（锁定）" style="locked=1;" parent="0"/>', '<mxCell id="1" value="推导" parent="0"/>']
A = lambda s: escape(s, {'"': "&quot;"})
for cid, value, style, x, y, w, h, parent, attrs in cells:
    out.append(f'<mxCell id="{cid}" value="{A(value)}" style="{A(style)}" vertex="1" parent="{parent}"><mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')
for nid, n in nodes.items():
    for src, txt in n.get("pre", []):
        n["rest"].append(f'<span style="font-size:11px;color:#607D8B;font-weight:normal;">⇐ 前提：{TX(txt)}〔{src} · {grid(src)}〕</span>')
for nid, n in nodes.items():
    if n["nbody"] >= 2:   # 多行：徽标与标题居中，公式和说明左对齐
        n["w"] += 16; n["x"] -= 8
        bw = n["w"] - 4
        n["label"] = (f'<div style="width:{bw}px;padding:0 8px;box-sizing:border-box;"><div style="text-align:center;">{n["head"]}</div>'
                      f'<div style="text-align:left;">' + "<br>".join(n["rest"]) + "</div></div>")
        n["style"] = ST[n["type"]] + "spacingLeft=0;spacingRight=0;"
    else:                 # 短节点：整体居中
        n["label"] = "<br>".join([n["head"]] + n["rest"])
        n["style"] = ST[n["type"]]
for nid, n in nodes.items():
    scope_txt = n["cond"] or "所有二次函数、所有 x"
    out.append(f'<UserObject id="{nid}" label="{A(n["label"])}" 编号="{nid}" 类型="{TYPE[n["type"]]}" 适用范围="{A(scope_txt)}" 坐标="{grid(nid)}">'
               f'<mxCell style="{A(n["style"])}" vertex="1" parent="1"><mxGeometry x="{n["x"]:.0f}" y="{n["y"]:.0f}" width="{n["w"]}" height="{n["h"]}" as="geometry"/></mxCell></UserObject>')
order = sorted(range(len(E)), key=lambda i: 0 if E[i][2] == "premise" else 1)
# 跨块推导线：每个行间空隙里分车道，标注放在横段上，互不重叠
cross_plan = {}
gaps = {}
for i, (s_, t_, kind, lines, mark, main) in enumerate(E):
    if i in dropped or f"e{i+1}" in epath:
        continue
    rs, rt = blocks[SEC_OF[s_]]["row"], blocks[SEC_OF[t_]]["row"]
    a_, b_ = nodes[s_], nodes[t_]
    sx, tx = a_["x"] + a_["w"] / 2, b_["x"] + b_["w"] / 2
    sy = a_["y"] if rs == rt else a_["y"] + a_["h"]
    lw_, lh_ = lsize(all_lines(s_, t_, kind, lines, mark))
    pre = []
    sb = blocks[SEC_OF[s_]]
    mates = [nodes[x] for x in SECTIONS[SEC_OF[s_]][1] if x != s_ and x in nodes]
    inside = lambda px, py: any(m["x"] - 6 < px < m["x"] + m["w"] + 6 and m["y"] - 6 < py < m["y"] + m["h"] + 6 for m in mates)
    bottom = a_["y"] + a_["h"]
    blk_bot, blk_top = sb["y"] + sb["h"], sb["y"]
    down_clear = not any(inside(sx, y) for y in range(int(bottom) + 8, int(blk_bot), 12))
    up_clear = not any(inside(sx, y) for y in range(int(blk_top), int(a_["y"]) - 8, 12))
    k_ = sum(len(g) for g in gaps.values())
    right = tx > sb["x"] + sb["w"] / 2
    bx = (sb["x"] + sb["w"] + GAPX / 2 if right else sb["x"] - GAPX / 2) + 14 * (k_ % 7 - 3)
    if rs == rt and up_clear:                  # 同一行、上方畅通：从上沿出（原走法）
        pass
    elif rs != rt and down_clear and rt - rs < 2:
        pass
    else:                                      # 先下到本层节点下方的空隙，横着出块，进块间走廊
        yg = bottom + 28
        while any(inside(x, yg) for x in range(int(min(sx, bx)), int(max(sx, bx)), 12)) and yg < blk_bot:
            yg += 14
        sy = bottom
        pre = [(sx, yg), (bx, yg)]
    if rt - rs >= 2:                           # 跨两行以上：在源行下方空隙横走到中间各块之间的走廊，再往下
        mids = [b for b in blocks if rs < b["row"] < rt]
        spans = sorted((b["x"] - 60, b["x"] + b["w"] + 60) for b in mids)
        free = [spans[0][0] - 60] + [(spans[k][1] + spans[k + 1][0]) / 2 for k in range(len(spans) - 1) if spans[k][1] < spans[k + 1][0]] + [spans[-1][1] + 60]
        hx0 = pre[-1][0] if pre else sx
        cx = min(free, key=lambda v: abs(v - hx0) + abs(v - tx))
        gy1 = row_top[rs + 1] - GAPY / 2 + 40 * (len([1 for g in gaps.values() for d in g if d["pre"]]) % 5 - 2)
        pre = pre + [(hx0, gy1), (cx, gy1)]
    tb = blocks[SEC_OF[t_]]
    tmates = [nodes[x] for x in SECTIONS[SEC_OF[t_]][1] if x != t_ and x in nodes]
    tin = lambda px, py: any(m["x"] - 6 < px < m["x"] + m["w"] + 6 and m["y"] - 6 < py < m["y"] + m["h"] + 6 for m in tmates)
    post = []
    if any(tin(tx, y) for y in range(int(tb["y"]), int(b_["y"]) - 8, 12)):   # 目标正上方被本块节点挡住：沿块旁走廊下来，再从目标上方空隙横着进
        tright = (pre[-1][0] if pre else sx) > tb["x"] + tb["w"] / 2
        ex = (tb["x"] + tb["w"] + GAPX / 2 if tright else tb["x"] - GAPX / 2) + 14 * (k_ % 7 - 3)
        yt = b_["y"] - 28
        while any(tin(x, yt) for x in range(int(min(ex, tx)), int(max(ex, tx)), 12)) and yt > tb["y"]:
            yt -= 14
        post = [(ex, yt), (tx, yt)]
    gaps.setdefault(rt, []).append(dict(i=i, sx=sx, tx=tx, sy=sy, ty=b_["y"], lw=lw_, lh=lh_, same=rs == rt, pre=pre, post=post))
for rt, items in gaps.items():
    lo, hi = row_top[rt] - GAPY + 50, row_top[rt] - 50       # 空隙的上下界
    items.sort(key=lambda d: abs(d["tx"] - d["sx"]))
    step = min(34, (hi - lo) / max(1, len(items) - 1))
    placed = []
    for k, it in enumerate(items):                            # 每条线一条车道（横段高度不同）
        gy = lo + k * step
        hx = it["pre"][-1][0] if it["pre"] else it["sx"]       # 横段起点（有走廊时从走廊出发）
        ex_ = it["post"][0][0] if it["post"] else it["tx"]
        x0, x1 = sorted((hx, ex_))
        w_, h_ = it["lw"] + 40, it["lh"] * 1.35 + 10           # 标注实际渲染比估算大，放宽
        cands = sorted({x0 + f * (x1 - x0) for f in [q / 20 for q in range(1, 20)]} | {(x0 + x1) / 2},
                       key=lambda v: abs(v - (x0 + x1) / 2))
        def hit(px):
            r = (px - w_ / 2, gy - h_ / 2, w_, h_)
            return sum(max(0, min(r[0] + r[2], q[0] + q[2]) - max(r[0], q[0])) * max(0, min(r[1] + r[3], q[1] + q[3]) - max(r[1], q[1])) for q in placed)
        px = min(cands, key=lambda v: (hit(v) > 0, hit(v), abs(v - (x0 + x1) / 2)))
        placed.append((px - w_ / 2, gy - h_ / 2, w_, h_))
        path = [(it["sx"], it["sy"])] + it["pre"] + [(hx, gy), (ex_, gy)] + it["post"] + [(it["tx"], it["ty"])]
        seg = [abs(path[q][0] - path[q + 1][0]) + abs(path[q][1] - path[q + 1][1]) for q in range(len(path) - 1)]
        before = sum(seg[:len(it["pre"]) + 1]) + abs(px - hx)          # 标注之前走过的长度
        cross_plan[it["i"]] = (gy, before / max(1, sum(seg)) * 2 - 1, it["pre"], it["post"])
lane = {}
labels_out = []
placed_lab = []
still_cover = []
for i in order:
    s, t, kind, lines, mark, main = E[i]
    if i in dropped:
        continue
    st = E_PRE if kind == "premise" else (E_MAIN if main else E_DER)
    cross = f"e{i+1}" not in epath
    if cross:   # 跨分区块的推导线：曲线，从节点下沿（同一行时从上沿）出，经目标所在行上方的空隙，再从上沿进入目标
        rs, rt = blocks[SEC_OF[s]]["row"], blocks[SEC_OF[t]]["row"]
        gy, lx, pre, post = cross_plan[i]
        a_, b_ = nodes[s], nodes[t]
        sx, tx = a_["x"] + a_["w"] / 2, b_["x"] + b_["w"] / 2
        st += "curved=1;entryX=0.5;entryY=0;" + ("exitX=0.5;exitY=0;" if (rs == rt and not pre) else "exitX=0.5;exitY=1;")
        hx = pre[-1][0] if pre else sx
        pts, lp = pre + [(hx, gy), ((post[0][0] if post else tx), gy)] + post, None
    else:
        pts, lp = epath[f"e{i+1}"]
    pts = [(x + DX, y + DY) for x, y in pts]
    way = pts if cross else (pts[3:-3:3] if len(pts) > 7 else pts[1:-1][::3])
    poly = pts[::3] if pts else []
    geo = ""
    if way:
        geo += '<Array as="points">' + "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in way) + "</Array>"
    if lp and len(poly) >= 2:
        seg = [math.dist(poly[k], poly[k + 1]) for k in range(len(poly) - 1)]
        half, acc, mx, my = sum(seg) / 2, 0, poly[0][0], poly[0][1]
        for k, d_ in enumerate(seg):
            if acc + d_ >= half and d_ > 0:
                r = (half - acc) / d_
                mx = poly[k][0] + r * (poly[k + 1][0] - poly[k][0]); my = poly[k][1] + r * (poly[k + 1][1] - poly[k][1])
                break
            acc += d_
        geo += f'<mxPoint x="{lp[0] + DX - mx:.0f}" y="{lp[1] + DY - my:.0f}" as="offset"/>'
    allL = ([mark] if mark else []) + lines + ([use_line(s, t)] if use_line(s, t) else [])
    lw, lh = lsize(allL)
    ox = oy = 0.0
    m_ = re.search(r'x="(-?[\d.]+)" y="(-?[\d.]+)" as="offset"', geo)
    if m_:
        ox, oy = float(m_.group(1)), float(m_.group(2))
        geo = geo[:m_.start()].rsplit("<mxPoint", 1)[0] + geo[m_.end():].split("/>", 1)[1]
    out.append(f'<mxCell id="e{i+1}" value="" style="{A(st)}" edge="1" parent="1" source="{s}" target="{t}"><mxGeometry relative="1" as="geometry">{geo}</mxGeometry></mxCell>')
    fc = "#607D8B" if kind == "premise" else "#263238"
    lst = f"text;html=1;whiteSpace=wrap;align=center;verticalAlign=middle;fillColor=#FFFFFF;strokeColor=none;fontFamily=PingFang SC;fontSize=13;fontColor={fc};"
    # 标签改成独立文字块，等所有连线画完再画（白底盖住从下面穿过的线）：按连线路径算出绝对位置
    a_, b_ = nodes[s], nodes[t]
    if cross:
        up_ = blocks[SEC_OF[s]]["row"] == blocks[SEC_OF[t]]["row"] and not cross_plan[i][2]
        src = (a_["x"] + a_["w"] / 2, a_["y"] if up_ else a_["y"] + a_["h"])
        path = [src] + way + [(b_["x"] + b_["w"] / 2, b_["y"])]
        frac = (cross_plan[i][1] + 1) / 2
    else:
        path, frac = ([(a_["x"] + a_["w"] / 2, a_["y"] + a_["h"] / 2)] + way + [(b_["x"] + b_["w"] / 2, b_["y"] + b_["h"] / 2)]), 0.5   # draw.io 按途经点画线
    seg = [math.dist(path[k], path[k + 1]) for k in range(len(path) - 1)]
    want, acc, cx, cy = sum(seg) * frac, 0, path[0][0], path[0][1]
    for k, d_ in enumerate(seg):
        if acc + d_ >= want and d_ > 0:
            r = (want - acc) / d_
            cx = path[k][0] + r * (path[k + 1][0] - path[k][0]); cy = path[k][1] + r * (path[k + 1][1] - path[k][1])
            break
        acc += d_
    if lp and not cross:
        cx, cy = lp[0] + DX, lp[1] + DY
    else:
        cx, cy = cx + ox, cy + oy
    # 标签不盖住自己的线：线从标签框里穿过时，竖向段把标签挪到线的左/右，横向段挪到线的上/下（选不压节点、挪得最少的一侧）
    def _cover(cx_, cy_):
        x0, y0, x1, y1 = cx_ - lw / 2 - 4, cy_ - lh / 2 - 4, cx_ + lw / 2 + 4, cy_ + lh / 2 + 4
        hits = []
        for (px1, py1), (px2, py2) in zip(path, path[1:]):
            for q in range(21):
                px, py = px1 + (px2 - px1) * q / 20, py1 + (py2 - py1) * q / 20
                if x0 < px < x1 and y0 < py < y1:
                    hits.append((px, py, abs(px2 - px1) < abs(py2 - py1)))
        return hits
    def _on_node(cx_, cy_):
        return any(n_["x"] < cx_ + lw / 2 and cx_ - lw / 2 < n_["x"] + n_["w"] and n_["y"] < cy_ + lh / 2 and cy_ - lh / 2 < n_["y"] + n_["h"] for n_ in nodes.values())
    hits = _cover(cx, cy)
    if hits:
        vert = sum(1 for h_ in hits if h_[2]) >= len(hits) / 2
        lx_ = sum(h_[0] for h_ in hits) / len(hits); ly_ = sum(h_[1] for h_ in hits) / len(hits)
        cands = []
        for d_ in (12, 40, 80, 140):
            for dy_ in (0, -lh * 0.6, lh * 0.6):
                cands += [(lx_ + lw / 2 + d_, cy + dy_), (lx_ - lw / 2 - d_, cy + dy_)]
            for dx_ in (0, -lw * 0.5, lw * 0.5):
                cands += [(cx + dx_, ly_ - lh / 2 - d_ * 0.6), (cx + dx_, ly_ + lh / 2 + d_ * 0.6)]
        def _on_lab(cx_, cy_):
            return any(q[0] < cx_ + lw / 2 + 4 and cx_ - lw / 2 - 4 < q[0] + q[2] and q[1] < cy_ + lh / 2 + 4 and cy_ - lh / 2 - 4 < q[1] + q[3] for q in placed_lab)
        ok = [c for c in cands if not _cover(*c) and not _on_node(*c) and not _on_lab(*c)]
        if ok:
            cx, cy = min(ok, key=lambda c: abs(c[0] - cx) + abs(c[1] - cy))
    if _cover(cx, cy):
        still_cover.append(f"{s}→{t}")
    placed_lab.append((cx - lw / 2, cy - lh / 2, lw, lh))
    labels_out.append(f'<mxCell id="e{i+1}L" value="{A(elabel(lines, mark, s, t))}" style="{A(lst)}opacity=100;" vertex="1" parent="1"><mxGeometry x="{cx - lw / 2:.0f}" y="{cy - lh / 2:.0f}" width="{lw}" height="{lh}" as="geometry"/></mxCell>')
out += labels_out
out.append("</root></mxGraphModel></diagram></mxfile>")
open(OUT, "w").write("\n".join(out))
print("标签仍盖住自己的线：", still_cover)
print("dropped premise", len(dropped), "nodes", len(nodes), "edges", len(E), "grid", cols, "x", rows, "methods", sum(len(v) > 0 for v in used.values()))
if VERSIONED:   # 版本输出时同时导出高清 PDF（矢量，单页，裁到图的大小）
    pdf = OUT[:-len(".drawio")] + ".pdf"
    subprocess.run(["drawio", "-x", "-f", "pdf", "--crop", "-o", pdf, OUT], check=True, capture_output=True)
    print("PDF:", pdf)
