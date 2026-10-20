"""生成恒等式大厦 drawio，并用 draw.io 命令行导出矢量 PDF（v4 起不再出 PNG）。
用法（在 数学/恒等式大厦/ 下）：
  python3 生成/build.py v3              → outputs/identity-tree-v3.drawio、.pdf
  python3 生成/build.py 任意路径.drawio   → 写到指定路径（不导出，调试用）
样式、节点格式、导航栏照不等式大厦 v35；排版用 graphviz dot，每棵树一个 cluster（= 分区背景框）。"""
import json, math, re, subprocess, sys
from xml.sax.saxutils import escape
from data import JIEFA, SECS, NODES, EDGES, TOOLS, FORMULAS, ENTRIES, TITLE, SUBTITLE, CIRC, METHODS, METHOD_OF, TOOL_LABELS, DIRECTION

import os
HERE = os.path.dirname(os.path.abspath(__file__))
ARG = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
VERSIONED = not ARG.endswith(".drawio")
OUT = os.path.join(HERE, "..", "outputs", f"identity-tree-{ARG}.drawio") if VERSIONED else ARG

# ── 样式（取自 inequality-tree-v35.drawio，与当前 v50 相同）──
NODE_ST = {
 "start":   "rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#6A1B9A;strokeWidth=2;fontFamily=PingFang SC;fontSize=13;fontColor=#4A148C;shadow=1;arcSize=12;spacingLeft=8;spacingRight=8;",
 "green":   "rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#2E7D32;strokeWidth=2;fontFamily=PingFang SC;fontSize=13;fontColor=#1B5E20;fontStyle=1;shadow=1;arcSize=12;spacingLeft=8;spacingRight=8;",
 "white":   "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#90A4AE;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#37474F;arcSize=10;spacingLeft=8;spacingRight=8;",
 "orange":  "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE0B2;strokeColor=#E65100;strokeWidth=2.5;fontFamily=PingFang SC;fontSize=13;fontColor=#BF360C;fontStyle=1;shadow=1;arcSize=12;spacingLeft=8;spacingRight=8;",
 "lorange": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#FB8C00;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#BF360C;arcSize=10;spacingLeft=8;spacingRight=8;",
}
ST = {
 "tool": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1565C0;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#0D47A1;arcSize=10;align=left;spacingLeft=8;",
 "entry": "rounded=1;arcSize=12;whiteSpace=wrap;html=1;dashed=1;dashPattern=6 4;fillColor=#E0F2F1;strokeColor=#00897B;strokeWidth=2;align=left;spacingLeft=10;spacingRight=6;fontFamily=PingFang SC;fontSize=11;fontColor=#00695C;",
 "panel": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#B0BEC5;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#37474F;align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;arcSize=4;",
 "method": "rounded=1;whiteSpace=wrap;html=1;fillColor=#EFEBE9;strokeColor=#8D6E63;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=12;fontColor=#3E2723;align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;arcSize=4;",
 "title": "text;html=1;fontFamily=PingFang SC;fontSize=40;fontStyle=1;fontColor=#263238;align=left;verticalAlign=top;whiteSpace=wrap;",
 "secbox": "rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=#F7F9FA;strokeColor=#B0BEC5;strokeWidth=2;dashed=1;dashPattern=8 6;",
 "secbar": "rounded=1;arcSize=50;whiteSpace=wrap;html=1;fontFamily=PingFang SC;fontSize=22;fontStyle=1;fillColor=#37474F;fontColor=#FFFFFF;strokeColor=none;align=left;spacingLeft=14;",
 "grid": "text;html=1;align=center;verticalAlign=middle;fontFamily=PingFang SC;fontStyle=1;fontSize=28;fontColor=#B0BEC5;",
 "gridline": "endArrow=none;html=1;strokeColor=#B0BEC5;strokeWidth=1;dashed=1;dashPattern=2 8;",
 "text": "text;html=1;align=left;verticalAlign=middle;fontFamily=PingFang SC;whiteSpace=wrap;fontSize=14;fontColor=#37474F;",
}
EDGE = ("html=1;rounded=1;curved=1;fontFamily=PingFang SC;labelBackgroundColor=#FFFFFF;fontColor=#263238;"
        "endArrow=block;")
E_MAIN = EDGE + "strokeColor=#263238;strokeWidth=4;fontStyle=1;endSize=8;"
E_DER = EDGE + "strokeColor=#455A64;strokeWidth=2.5;endSize=7;"
E_PRE = EDGE + "strokeColor=#90A4AE;strokeWidth=2;endSize=7;"
E_APPLY = EDGE + "strokeColor=#00897B;strokeWidth=2.5;endSize=7;fontColor=#00695C;"
E_DEFINE = EDGE + "strokeColor=#8E24AA;strokeWidth=2.5;endSize=7;fontColor=#6A1B9A;"
NODE_ST["problem"] = ("rounded=1;arcSize=18;whiteSpace=wrap;html=1;fillColor=#E0F2F1;strokeColor=#00897B;strokeWidth=2.5;"
                      "fontFamily=PingFang SC;fontSize=12;fontColor=#004D40;spacingLeft=8;spacingRight=8;")
TYPE = {"start": "起点", "green": "结论", "white": "中间结果", "orange": "结论（有条件）", "lorange": "中间结果（有条件）", "problem": "问题（看到什么）"}


# ── 公式：$…$ → \({…}\)；含分式的加上下边距（同 v35）──
def tex(s):
    parts = s.split("$")
    out = []
    for k, p in enumerate(parts):
        if k % 2 == 0:
            out.append(escape(p))
        else:
            m = r"\({" + escape(p) + r"}\)"
            if re.search(r"\\(dfrac|frac|displaystyle)", p):
                m = f'<span style="display:inline-block;margin:3px 0;">{m}</span>'
            out.append(m)
    return "".join(out)


# ── 估算显示宽度（单位：字号 em）──
def _brace(s, i):
    d = 0
    for j in range(i, len(s)):
        d += 1 if s[j] == "{" else (-1 if s[j] == "}" else 0)
        if d == 0:
            return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def _arg(s, i):
    while i < len(s) and s[i] == " ":
        i += 1
    if i < len(s) and s[i] == "{":
        return _brace(s, i)
    if i < len(s) and s[i] == "\\":
        m = re.match(r"\\[A-Za-z]+|\\.", s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i:i + 1], i + 1


def mw(t):
    w, i = 0.0, 0
    while i < len(t):
        c = t[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", t[i:])
            cmd = m.group(1); i += len(m.group(0))
            if cmd in ("dfrac", "frac", "tfrac"):
                a, i = _arg(t, i); b, i = _arg(t, i)
                w += max(mw(a), mw(b)) * (1 if cmd == "dfrac" else 0.75) + 0.3
            elif cmd == "sqrt":
                if i < len(t) and t[i] == "[":
                    j = t.index("]", i); w += 0.4; i = j + 1
                a, i = _arg(t, i); w += mw(a) + 0.8
            elif cmd in ("vec", "overline", "overrightarrow", "bar", "mathbb", "boldsymbol"):
                a, i = _arg(t, i); w += mw(a)
            elif cmd in ("left", "right", "displaystyle", ",", " ", "!", ";"):
                if cmd in ("left", "right") and i < len(t):
                    i += 1 if t[i] != "\\" else len(re.match(r"\\[A-Za-z]+|\\.", t[i:]).group(0))
                    w += 0.45
            elif cmd in ("sin", "cos", "tan", "log", "ln", "lg", "lim"):
                w += 0.5 * len(cmd) + 0.2
            elif cmd in ("sum",):
                w += 1.3
            elif cmd in ("cdots", "ldots"):
                w += 1.2
            else:
                w += 0.75
        elif c in "^_":
            a, i = _arg(t, i + 1)
            if t[i - len(a) - 2:i].startswith(c + "{") or len(a) > 1:
                pass
            w += 0.7 * mw(a)
        elif c in "{}":
            i += 1
        elif c in "+-=<>":
            w += 0.95; i += 1
        elif c in "()[]|,.;:'":
            w += 0.35; i += 1
        elif ord(c) > 0x2E80:
            w += 1.0; i += 1
        else:
            w += 0.6; i += 1
    return w


def vw(s):
    """一行（含 $…$）的显示宽度，em；同时返回其中最宽的一个公式（不可断行）。"""
    parts = s.split("$")
    tot, mx = 0.0, 0.0
    for k, p in enumerate(parts):
        if k % 2:
            x = mw(p) * 1.15; tot += x + 0.2; mx = max(mx, x)
        else:
            x = sum(1.0 if ord(ch) > 0x2E80 else 0.56 for ch in p); tot += x
    return tot, mx


def tall(s):
    """含竖排分式等的行要额外加高（px）。"""
    if re.search(r"\\frac\{\\frac|dfrac\{\\frac|\\dfrac\{[^}]*\\frac", s):
        return 30
    if "\\displaystyle" in s:
        return 22
    return 18 if re.search(r"\\(dfrac|frac)", s) else 0


def box(lines, fs, minw=220, maxw=620, pad=40):
    ws = [vw(l) for l in lines]
    need = max(mx for _, mx in ws) * fs * 1.05 + pad
    w = max(minw, min(maxw, max(t for t, _ in ws) * fs * 1.05 + pad), need)
    per = (w - pad) / (fs * 1.05)
    rows = sum(max(1, math.ceil(t / per)) for t, _ in ws)
    h = rows * (fs + 9) + sum(tall(l) for l in lines)
    return int(w), int(h)


# ── 节点 ──
code_span = lambda c: f'<span style="font-size:10px;color:#78909C;font-weight:normal;">{c}</span>'
tag = lambda t: f'<span style="background-color:#E65100;color:#FFFFFF;font-size:10px;font-weight:bold;">&nbsp;{tex(t)}&nbsp;</span>'
jiefa_tag = '<span style="background-color:#6D4C41;color:#FFFFFF;font-size:10px;">&nbsp;解法&nbsp;</span>'
ext_tag = '<span style="background-color:#90A4AE;color:#FFFFFF;font-size:10px;">&nbsp;拓展&nbsp;</span>'
# 应用线：线上只留【怎么用】，例子写进问题节点（每个工具一行）
_NB = {n["id"]: n for n in NODES}
# 推导线的【方法】统一成方法箱的 13 种：【短名】或【短名·原名】（原名保留，内容不删）
def _relabel(t):
    def f(m):
        old = m.group(1)
        if old in TOOL_LABELS:                     # 只是套用工具：不加【】
            tool, code = TOOL_LABELS[old]
            return f"由 {tool}〔{code}〕："
        if old not in METHOD_OF:
            return m.group(0)
        return m.group(0)                          # 线上写具体动作，不加类别名；类别到方法栏查
    return re.sub(r"【(.+?)】", f, t)
def tool_name(nid):
    t = re.sub(r"^[★\s]+", "", _NB[nid]["title"])
    return re.sub(r"^【.+?】", "", t).strip()
try:
    from steps import STEPS              # 推导线一步一行的写法（照不等式大厦 v48）；data.py 里的原文不动
except ImportError:
    STEPS = {}
for e in EDGES:
    if e["kind"] == "derive" and (e["s"], e["t"]) in STEPS:
        e["lines"] = list(STEPS[(e["s"], e["t"])])
    elif e["kind"] == "derive":
        e["lines"] = [_relabel(l) for l in e["lines"]]
    elif e["kind"] == "premise":
        # 【前提】= 这一步用到的工具（公式、定理、公理、定义）；其余是“另一路”推导，方法名照样统一
        e["lines"] = [(f"「{tool_name(e['s'])}」" + l[len("【前提】"):].strip()) if l.startswith("【前提】") else _relabel(l)
                      for l in e["lines"]]
for e in EDGES:
    if e["kind"] != "apply":
        continue
    m = re.match(r"(【.+?】)(.*)", e["lines"][0])
    how, ex = (m.group(1), m.group(2).strip()) if m else (e["lines"][0], "")
    e["lines"] = [how]
    if ex:
        q = _NB[e["t"]]
        q.setdefault("examples", []).append(f"例〔{e['s']}〕{how}：{ex}")
for n in NODES:
    if n.get("examples"):
        n["lines"] = n["lines"] + n["examples"]
for n in NODES:
    if n["type"] == "problem" and n["id"] in DIRECTION:
        short, d = DIRECTION[n["id"]]
        ls = [("工具：" + l[3:]) if l.startswith("路径：") else l for l in n["lines"]]
        k = next((i for i, l in enumerate(ls) if l.startswith("工具：")), 0)
        n["lines"] = ls[:k] + [f"方向：【{short}】{d}"] + ls[k:]
SECN = {}
nodes = {}
DOWN = {}
for e in EDGES:
    DOWN.setdefault(e["s"], [])
    if e["t"] not in DOWN[e["s"]]:
        DOWN[e["s"]].append(e["t"])
ENT_OF = {}
for k, (_, _, _, codes) in enumerate(ENTRIES):
    for c in codes:
        ENT_OF.setdefault(c, []).append(CIRC[k])
for n in NODES:
    man = [x[3:] for x in n["notes"] if x.startswith("用于：")]
    n["notes"] = [x for x in n["notes"] if not x.startswith("用于：")]
    n["uses"] = (DOWN.get(n["id"], []), man, ENT_OF.get(n["id"], []))
def uses_text(n, g):
    down, man, ent = n["uses"]
    parts = []
    if down:
        parts.append("、".join(f"{t}〔{g(t)}〕" for t in down))
    parts += man
    return "⇒ 用于：" + "；".join(parts) if parts else ""
SEC_OF = {n["id"]: n["sec"] for n in NODES}
PRIMARY, _seen = set(), set()
for i, e in enumerate(EDGES):                 # 每个问题节点只画第一条应用线（主工具）
    if e["kind"] == "apply" and e["t"] not in _seen:
        PRIMARY.add(i); _seen.add(e["t"])
TRUNK = {}                                    # (源城, 目标城) → 跨城推导、前提线
for i, e in enumerate(EDGES):
    if e["kind"] in ("derive", "premise") and SEC_OF[e["s"]] != SEC_OF[e["t"]]:
        TRUNK.setdefault((SEC_OF[e["s"]], SEC_OF[e["t"]]), []).append(i)
        txt = " ".join(([e["mark"]] if e["mark"] else []) + e["lines"])
        _NB[e["t"]].setdefault("pre", []).append((e["s"], e["kind"], txt))
def pre_text(kind, txt, refstr):
    if kind == "derive":
        return "⇐ 来路（跨区）：" + txt + refstr
    return ("⇐ 工具 " + txt if txt.startswith("「") else "⇐ 另一路：" + txt) + refstr
for n in NODES:
    fs = 13 if n["type"] in ("start", "green", "orange") else 12
    meas = [n["title"]] + n["lines"] + [x for x in n["notes"]] + [uses_text(n, lambda t: "A0")] \
        + [pre_text(k, t, f"〔{src} · A0〕") for src, k, t in n.get("pre", [])]
    w, h = box(meas + ([n["cond"] + "　" + n["id"]] if n["cond"] else []), fs)
    h += 34 + (16 if n["cond"] else 0)
    n.update(w=w, h=h, fs=fs)
    nodes[n["id"]] = n
    SECN.setdefault(n["sec"], []).append(n["id"])


def elabel_lines(e):
    return ([e["mark"]] if e["mark"] else []) + e["lines"]


# ── dot 排版：每座城单独排，再按“地基 → 主城 → 卫星城”分层拼接 ──
CROSS = lambda e: nodes[e["s"]]["sec"] != nodes[e["t"]]["sec"]
ROWS = [["base"], ["seq", "alg", "cnt"], ["der", "exp", "tri"], ["fun", "vec", "cpx", "prob"], ["geo", "sp"]]
UNDER = {"base": ("alg",), "fun": ("exp",), "vec": ("tri",), "cpx": ("tri",), "prob": ("cnt",), "geo": ("vec",), "sp": ("vec",)}   # 摆在哪座城的正上方 / 正下方；其余各层从左顺排
INVIS = {"cpx": [("R26", "S11")]}
GAP = 440
PADX, PADTOP, PADB = 50, 110, 50


def ph_label(L):
    cw = max(vw(l)[0] for l in L) * 11 * 1.05 + 20
    lh = len(L) * 17 + sum(tall(l) for l in L) + 12
    return "\\n".join("x" * max(1, int(cw / 6.6)) for _ in range(max(1, math.ceil(lh / 14))))


epath = {}
local = {}
for sk in SECS:
    ids = SECN[sk]
    dot = ["digraph G {", "rankdir=TB; nodesep=0.8; ranksep=1.0; splines=true;",
           'node [shape=box, fixedsize=true, label=""]; edge [fontsize=11, fontname="Courier"];']
    tools = list(ids)
    for nid in tools:
        n = nodes[nid]
        dot.append(f'"{nid}" [width={n["w"]/72:.2f}, height={n["h"]/72:.2f}];')
    for i, e in enumerate(EDGES):
        if (e["kind"] != "apply" or i in PRIMARY) and nodes[e["s"]]["sec"] == sk and nodes[e["t"]]["sec"] == sk:
            extra = "weight=1, " if e["kind"] in ("premise", "apply", "define") else f"weight={8 if e['main'] else 2}, "
            dot.append(f'"{e["s"]}" -> "{e["t"]}" [{extra}label="{ph_label(elabel_lines(e))}", id="e{i}"];')
    for a_, b_ in INVIS.get(sk, []):
        dot.append(f'"{a_}" -> "{b_}" [style=invis, weight=1];')
    dot.append("}")
    res = subprocess.run(["dot", "-Tjson0"], input="\n".join(dot), capture_output=True, text=True)
    if res.returncode:
        sys.exit(res.stderr)
    lay = json.loads(res.stdout)
    W, H = map(float, lay["bb"].split(",")[2:4])
    # 问题节点：排成城下方的“出口带”，尽量放在所用工具的正下方
    qs = []                                     # v3 第二版：问题节点由 dot 排在主工具旁边
    qpos = {}
    if qs:
        tx = {o["name"]: float(o["pos"].split(",")[0]) for o in lay["objects"] if o["name"] in nodes}
        want = []
        for q in qs:
            src = [e["s"] for e in EDGES if e["t"] == q and e["kind"] == "apply" and e["s"] in tx]
            want.append((sum(tx[t] for t in src) / len(src) if src else W / 2, q))
        want.sort()
        Wlim = max(W, 3200)
        rows_q, ends = [], []
        for cx, q in want:
            w = nodes[q]["w"]
            for r, end in enumerate(ends):
                xx = max(cx - w / 2, end + 60, 0)
                if xx + w <= Wlim:
                    rows_q[r].append((q, xx)); ends[r] = xx + w; break
            else:
                xx = max(cx - w / 2, 0)
                rows_q.append([(q, xx)]); ends.append(xx + w)
        y0 = H + 260                                    # 留出应用线标签的空间
        for row in rows_q:
            rh = max(nodes[q]["h"] for q, _ in row)
            for q, xx in row:
                qpos[q] = (xx, y0)
            y0 += rh + 120
        W = max(W, max(ends))
        Hq = y0 - H
    else:
        Hq = 0
    local[sk] = (W + 2 * PADX, H + Hq + PADTOP + PADB, H, lay, qpos)

# 每层先排横向位置：第二层（主城）顺排；地基、卫星城摆到所依附城市的正上方 / 正下方，再消除重叠
pos = {}
for row in ROWS:
    if all(sk not in UNDER for sk in row):
        x = 0
        for sk in row:
            pos[sk] = x; x += local[sk][0] + GAP
def place_row(row):
    want = []
    for sk in row:
        refs = UNDER[sk]
        cx = sum(pos[r] + local[r][0] / 2 for r in refs) / len(refs)
        want.append([sk, cx - local[sk][0] / 2])
    if len(set(UNDER[sk] for sk in row)) < len(row):          # 同挂在一座城下的几座卫星城：并排居中
        groups = {}
        for w in want:
            groups.setdefault(UNDER[w[0]], []).append(w)
        for refs, ws in groups.items():
            tot = sum(local[w[0]][0] for w in ws) + GAP * (len(ws) - 1)
            cx = sum(pos[r] + local[r][0] / 2 for r in refs) / len(refs)
            xx = cx - tot / 2
            for w in ws:
                w[1] = xx; xx += local[w[0]][0] + GAP
    want.sort(key=lambda w: w[1])
    for k in range(1, len(want)):
        prev = want[k - 1]
        want[k][1] = max(want[k][1], prev[1] + local[prev[0]][0] + GAP)
    for sk, xx in want:
        pos[sk] = xx
for row in ROWS:
    if any(sk in UNDER for sk in row):
        place_row(row)
SEC_ROW = {sk: r for r, row in enumerate(ROWS) for sk in row}
ROWTOP, ROWBOT = [], []
y = 0
for row in ROWS:
    ROWTOP.append(y); ROWBOT.append(y + max(local[sk][1] for sk in row)); y = ROWBOT[-1] + GAP
minx = min(pos.values())
DX, DY = 200 - minx, 300
clusters = {}
for sk in SECS:
    W, Hc, H, lay, qpos = local[sk]
    cx0, cy0 = pos[sk] + DX, ROWTOP[SEC_ROW[sk]] + DY
    ox, oy = cx0 + PADX, cy0 + PADTOP
    for o in lay["objects"]:
        if o["name"] in nodes:
            px, py_ = map(float, o["pos"].split(","))
            n = nodes[o["name"]]
            n["x"] = ox + px - n["w"] / 2
            n["y"] = oy + (H - py_) - n["h"] / 2
    for ed in lay.get("edges", []):
        if "pos" not in ed or not ed.get("id"):
            continue
        pts = []
        for tok in ed["pos"].split():
            if tok.startswith(("e,", "s,")):
                continue
            qx, qy = map(float, tok.split(","))
            pts.append((ox + qx, oy + H - qy))
        lp = ed.get("lp")
        lp = tuple(map(float, lp.split(","))) if lp else None
        epath[ed["id"]] = (pts, (ox + lp[0], oy + H - lp[1]) if lp else None)
    for q, (qx, qy) in qpos.items():
        nodes[q]["x"] = ox + qx
        nodes[q]["y"] = oy + qy
    clusters[sk] = (cx0, cy0, W, Hc)
ROWTOP = [t + DY for t in ROWTOP]; ROWBOT = [b + DY for b in ROWBOT]
MAXX = max(a + w for a, b, w, h in clusters.values()) + 200
MAXY = max(b + h for a, b, w, h in clusters.values()) + 200

# 不单独画的线：跨城推导、前提（并入城际干道）；非主工具的应用线（写在问题节点的路径里）
dropped = {i for idxs in TRUNK.values() for i in idxs} | {i for i, e in enumerate(EDGES) if e["kind"] == "apply" and i not in PRIMARY}

# ── 网格坐标 ──
NC = 14
CW = MAXX / NC
RH = CW
NR = math.ceil(MAXY / RH)
COLS = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
def grid(nid):
    n = nodes[nid]
    cx, cy = n["x"] + n["w"] / 2, n["y"] + n["h"] / 2
    return f"{COLS[int(cx // CW)]}{int(cy // RH) + 1}"
ref = lambda nid: f"〔{nid} · {grid(nid)}〕"
fill_refs = lambda html: re.sub(r"〔([SRPQ]\d{2,3})〕", lambda m: ref(m.group(1)), html)

cells = []
uid = [0]
def cell(value, style, x, y, w, h, parent="1"):
    uid[0] += 1
    cells.append((f"bg{uid[0]}", value, style, x, y, w, h, parent))

# 分区背景框与标题条
for sk, (x, y, w, h) in clusters.items():
    cell("", ST["secbox"], x, y, w, h, "bg")
    tw = min(w - 24, vw(SECS[sk])[0] * 22 * 1.02 + 60)
    cell("▍" + tex(SECS[sk]), ST["secbar"], x + 12, y + 10, tw, 40, "bg")

# 网格
for i in range(NC + 1):
    cell("", ST["gridline"], i * CW, -120, 1, NR * RH + 240, "bg")
for j in range(NR + 1):
    cell("", ST["gridline"], 0, j * RH, NC * CW, 1, "bg")
for i in range(NC):
    for yy in (-170, NR * RH + 60):
        cell(COLS[i], ST["grid"], i * CW, yy, CW, 80, "bg")
for j in range(NR):
    for xx in (-110, NC * CW + 20):
        cell(str(j + 1), ST["grid"], xx, j * RH + RH / 2 - 40, 90, 80, "bg")

# ── 左侧导航 ──
PW = 1900; PX = -PW - 300
py = -120
cell(escape(TITLE), ST["title"], PX, py, PW, 60, "bg"); py += 70
cell("<br>".join(tex(s) for s in SUBTITLE), "text;html=1;fontFamily=PingFang SC;fontSize=16;fontColor=#455A64;align=left;verticalAlign=top;whiteSpace=wrap;", PX, py, PW, 80, "bg")
py += 110

LEG = [("start", "【定义】【公理】【原理】", "紫色：起点，直接承认（定义、公理、课本给出）"),
       ("green", "★ 结论", "绿色：对所有取值都成立的恒等式，不需要任何条件"),
       ("white", "中间结果", "白底：推导中的一步，不需要条件"),
       ("orange", "★ 结论（有条件）", "橙色：要加条件才成立；标题上方橙色标签写明条件类别和内容"),
       ("lorange", "中间结果（有条件）", "淡橙：有条件的中间一步"),
       ("problem", "看到：……（问题）", "青绿：问题节点（应用层）——看到什么 → 解题路径 ①②③ → 注意")]
lines2 = ["三层：工具箱（能用什么）、方法（往哪走）、题型入口（从哪进），分工见“方法”一栏开头的表",
          "两层：推导层（深灰，公式怎么来的）与应用层（青绿，看到什么、用哪个工具、怎么用）同样重要；drawio 里用“标签（tags）”可只显示推导层或应用层",
          "连线：深色实线 = 推导，越粗越是主干；线上一步一行：【动作】+ 这一步的式子（变形前 ⇒ 变形后），理由放括号；用到的工具写「工具名」；动作属于哪一类方法，到“方法”栏查",
          "青绿线 = 应用：工具 → 问题，线上写【怎么用】+ 例子；紫色线 = 【定义】：起点建立在哪个更底层的起点之上",
          "⚡ 第一反应：工具节点里写“看到什么信号，就想到它”",
          "浅灰线 = 工具：这一步用到的已有公式、定理，线上写「工具名」和怎么用；跨区的写进节点“⇐ 工具「工具名」”",
          "▼ 加条件：从这一步起要带上条件，后面的结论都带着它；“★ 跨树”= 跨分区的推导",
          "✗ = 去掉条件的反例；“⋯ 同源 / 互逆 / 配合”写在节点里，不画成推导线",
          "⇒ 用于：本图下游〔坐标〕、其他大厦和章节的用途、问题节点（正推之后用在哪里）",
          "〔编号 · 坐标〕：S 起点、R 不加条件、P 加条件；按图边字母（列）和数字（行）找格子",
          "棕色“解法”= 写不成一个公式、由几种方法配合工具组成的流程（如因式分解的几种手法）",
          "★ 越多越重要；灰色“拓展”可先跳过；“同见不等式大厦 / 二次函数大厦 编号”= 两张图重合的结论"]
COND = [("〔定义域〕不满足时某一边没有意义",
         ["分式：分母 $\\ne 0$", "对数：真数 $>0$，底数 $>0$ 且 $\\ne 1$", "正切：$\\cos\\alpha\\ne 0$",
          "下标与组合数：$n\\ge 2$、$0\\le k\\le n$", "根式：被开方数 $\\ge 0$", "分数指数幂：底数 $>0$", "整数指数：底数 $\\ne 0$", "约分：约掉的因式 $\\ne 0$", "实根：$\\Delta\\ge 0$", "求导：函数在该点可导", "奇偶性：定义域关于原点对称", "斜率：$x_1\\ne x_2$", "圆：$D^2+E^2-4F>0$", "法向量：$\\vec n\\ne\\vec 0$", "条件概率：$P(A)>0$", "无穷递缩等比：$|q|<1$", "反三角：$|a|\\le 1$"]),
        ("〔结构前提〕两边都有意义，但只对某种结构成立",
         ["等差数列", "等比数列", "差比数列（等差×等比）", "同一三角形的边与对角", "基底不共线", "实系数方程", "关系式对每个 $x$ 成立（对称、周期）", "圆锥曲线的标准位置", "台体、长方体补形", "独立重复、不放回抽取", "完备事件组", "反函数：一一对应", "复利、按相同百分比变化"]),
        ("〔符号分支〕两边都有意义，但符号或角要按范围选定",
         ["半角 ±", "已知一值求其余的 ±", "$\\sqrt{a^2}=|a|$", "辅助角 $\\varphi$", "复数辐角", "二面角锐钝看图", "已知值求角：两组解"])]
ch = 70 + sum(56 + 34 * math.ceil(len(it) / 3) for _, it in COND) + 40
lh_ = 60 + 70 * len(LEG) + 56 * len(lines2) + 20
cell('<b style="font-size:20px">图例与条件</b>', ST["panel"], PX, py, PW, lh_ + ch, "bg")
ly = py + 56
for typ, sample, desc in LEG:
    cell(escape(sample), NODE_ST[typ], PX + 30, ly, 320, 54, "bg")
    cell(escape(desc), ST["text"], PX + 370, ly, PW - 400, 54, "bg")
    ly += 70
for t in lines2:
    cell(escape(t), ST["text"], PX + 30, ly, PW - 60, 50, "bg"); ly += 56
py += lh_
cell('<b style="font-size:17px">三类条件（各自独立，互不包含、互不推出）</b>', ST["text"], PX + 30, py, PW - 60, 40, "bg")
cy = py + 56
for head, items in COND:
    cell(f'<b style="color:#E65100;">{escape(head)}</b>', ST["text"] + "fontSize=15;", PX + 30, cy, PW - 60, 40, "bg"); cy += 46
    iw = (PW - 100) / 3
    for k, it in enumerate(items):
        cell("▸ " + tex(it), ST["text"], PX + 50 + (k % 3) * iw, cy + (k // 3) * 34, iw - 10, 30, "bg")
    cy += 34 * math.ceil(len(items) / 3) + 10
cell(escape("反例：〔定义域〕说明哪一边没有意义；〔结构前提〕〔符号分支〕给“两边有意义但不相等”的数值"), ST["text"] + "fontColor=#B71C1C;", PX + 30, cy, PW - 60, 30, "bg")
py += ch + 50

cell('<b style="font-size:22px">工具箱：能用什么——公式、定理、公理、定义，都能写成一个公式，拿来直接用</b><br><span style="font-size:13px;">每个公式：名称 · 公式 · 条件 · ⚡ 第一反应 · ▸ 用在哪里 · ⋯ 配合（内容取自对应节点）；最后一组是常用数值</span>', "text;html=1;fontFamily=PingFang SC;fontColor=#0D47A1;align=left;verticalAlign=top;", PX, py, PW, 56, "bg")
py += 66
CARD = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1565C0;strokeWidth=1.5;fontFamily=PingFang SC;"
        "fontSize=13;fontColor=#0D47A1;arcSize=8;align=center;verticalAlign=middle;spacingLeft=10;spacingRight=10;")
FRAME = "rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=#F1F8FE;strokeColor=#64B5F6;strokeWidth=2;"
cw2 = (PW - 90) // 2
frame_top = py
col_y = [py + 30, py + 30]
def usage_lines(nid):
    """公式卡里的用法：▸ 用在 什么问题：怎么用〔编号 · 坐标〕"""
    out_, seen = [], {}
    for e in EDGES:
        if e["s"] != nid or e["kind"] == "define":
            continue
        t = nodes[e["t"]]
        name = re.sub(r"^[★\s]+", "", t["title"]).replace("看到：", "")
        how = re.sub(r"^「[^」]*」", "", " ".join(e["lines"])).strip()
        if e["t"] in seen:
            out_[seen[e["t"]]][1].append(how); continue
        seen[e["t"]] = len(out_)
        out_.append([name, [how], e["t"]])
    res = [f"▸ 用在 {name}：{'；'.join(h for h in hows if h)}〔{t}〕" for name, hows, t in out_]
    down, man, ent = nodes[nid]["uses"]
    res += [f"▸ 用在 {m}" for m in man]
    return res


def card_html(nid, f):
    n = nodes[nid]
    name = re.sub(r"^[★\s]+", "", n["title"])
    rows = [f'<b style="font-size:14px;">{nid}〔{grid(nid)}〕 {tex(name)}</b>', tex(f.replace("\\frac", "\\dfrac"))]
    meas = [nid + name, f]
    if n["cond"]:
        rows.append(f'<span style="font-size:11px;color:#E65100;">条件：{tex(n["cond"])}</span>'); meas.append(n["cond"])
    for t in n["notes"]:
        if t.startswith("⚡"):
            rows.append(f'<span style="font-size:11px;color:#00695C;font-weight:bold;">{tex(t)}</span>'); meas.append(t)
    for ul in usage_lines(nid):
        rows.append(f'<span style="font-size:10px;color:#1565C0;">{fill_refs(tex(ul))}</span>'); meas.append(ul)
    for t in n["notes"]:
        if t.startswith("⋯ 配合"):
            rows.append(f'<span style="font-size:10px;color:#607D8B;">{fill_refs(tex(t))}</span>'); meas.append(t)
    per = (cw2 - 30) / (12 * 1.05)
    hgt = 26 + sum(max(1, math.ceil(vw(m)[0] / per)) * 20 for m in meas) + (16 if "\\frac" in f else 0)
    return "<br>".join(rows), hgt
for title, items in FORMULAS:
    cards = [card_html(i, f) for i, f in items]
    gh = 40 + sum(hh + 14 for _, hh in cards)
    c = col_y.index(min(col_y))
    x0 = PX + 30 + c * (cw2 + 30)
    yy = col_y[c]
    cell(f'<b style="font-size:16px;color:#0D47A1;">▍{escape(title)}</b>', ST["text"], x0, yy, cw2, 32, "bg")
    yy += 40
    for html_, hh in cards:
        cell(html_, CARD, x0, yy, cw2, hh, "bg")
        yy += hh + 14
    col_y[c] = yy + 16
n_before_frame = len(cells) - sum(len(it) + 1 for _, it in FORMULAS)
# 常用数值：工具箱的最后一组
py = max(col_y) + 10
cell('<b style="font-size:16px;color:#0D47A1;">▍常用数值：直接查表，不画线</b>', ST["text"], PX + 30, py, PW - 60, 32, "bg")
py += 40
col_y = [py, py]
n_num = 0
for no, name, ls in TOOLS:
    h = 44 + sum(21 + (9 if "\\frac" in l else 0) for l in ls)
    c = col_y.index(min(col_y))
    cell(f"<b>{no} {tex(name)}</b><br>" + "<br>".join(tex(l) for l in ls), ST["tool"] + "verticalAlign=top;spacingTop=8;",
         PX + 30 + c * (cw2 + 30), col_y[c], cw2, h, "bg")
    col_y[c] += h + 20
    n_num += 1
frame_h = max(col_y) - frame_top + 10
cells.insert(n_before_frame, ("bgframe", "", FRAME, PX, frame_top, PW, frame_h, "bg"))
py = frame_top + frame_h + 50
# ── 方法（往哪走）：一整块，开头是三层分工表；每类写 方向、依据、信号、范例、⚠ 陷阱（照不等式大厦 v47）──
meth = {m[0]: [] for m in METHODS}
for e in EDGES:
    if e["kind"] != "derive":
        continue
    for m in re.findall(r"【(.+?)】", " ".join(e["lines"])):
        no = METHOD_OF.get(m, (None,))[0]
        if no and e["t"] not in meth[no]:
            meth[no].append(e["t"])
cell('<b style="font-size:22px">方法：往哪走——运算逻辑、变换方式，本身不是公式；每类一块：方向、依据、信号、范例、陷阱</b>', "text;html=1;fontFamily=PingFang SC;fontColor=#4E342E;align=left;verticalAlign=top;", PX, py, PW, 40, "bg")
py += 50
TH = 'style="border:1px solid #A1887F;padding:4px 8px;background:#EFEBE9;"'
TD = 'style="border:1px solid #A1887F;padding:4px 8px;"'
LAYERS = [("工具", "能用什么", "公理、定义、定理、公式——一定能写成一个公式，拿来直接用", "主图每个节点（本图推出的）；工具箱；线上「工具名」、节点里“⇐ 工具”"),
          ("方法", "往哪走", "运算逻辑、变换方式，本身不是公式：把眼前的问题转化成什么", "推导线上的【】；本栏"),
          ("题型入口", "从哪进", "看到什么题，用哪个方法定方向、用哪些工具", "问题节点（方向、工具两行）；题型入口一栏")]
table = (f'<table style="border-collapse:collapse;font-size:14px;"><tr><th {TH}>层</th><th {TH}>回答</th><th {TH}>是什么</th><th {TH}>在图中</th></tr>'
         + "".join(f'<tr><td {TD}><b>{a}</b></td><td {TD}>{b}</td><td {TD}>{escape(c)}</td><td {TD}>{escape(d)}</td></tr>' for a, b, c, d in LAYERS) + "</table>")
intro = [table, "",
         "先用<b>方法</b>找方向，再用熟悉的<b>工具</b>完成每一步：方法决定能不能想到，工具决定能不能算对。",
         "题型入口按题型查（这道题走哪个方向、用哪些工具），本栏按方法查（这个方法用在哪些推导、哪些题），是同一张表的两种查法。",
         "推导线一步一行：【动作】+ 这一步的式子（如【移项】【错位相减】【开平方】），用到的工具写「工具名」；每类方法下列出它包含的动作。"]
# 方法框：开头一块写三层分工表，下面每类方法一个独立小块（两栏）
m_frame_top = py
n_before_mframe = len(cells)
ih = 40 + 6 * 34 + sum(max(1, math.ceil(vw(t)[0] / ((PW - 120) / 14.0))) * 22 for t in intro[1:])
cell("<br>".join(intro), "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#A1887F;strokeWidth=1.5;fontFamily=PingFang SC;fontSize=14;fontColor=#3E2723;arcSize=6;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;",
     PX + 30, py + 20, PW - 60, ih, "bg")
py += 20 + ih + 20
MCARD = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#EFEBE9;strokeColor=#6D4C41;strokeWidth=1.5;fontFamily=PingFang SC;"
         "fontSize=13;fontColor=#3E2723;arcSize=8;align=left;verticalAlign=top;spacingLeft=12;spacingRight=10;spacingTop=8;")
mw2 = (PW - 90) // 2
col_y = [py, py]
for no, short, name, direc, basis, signal, chain, trap, olds in METHODS:
    qs = sorted((q for q, v in DIRECTION.items() if v[0] == short), key=lambda q: int(q[1:]))
    rows = [f'<b style="font-size:16px;color:#4E342E;">【{escape(short)}】</b> <span style="font-size:12px;color:#8D6E63;">{escape(name.replace(short, "", 1))}</span>',
            f'<span style="font-size:12px;color:#6D4C41;"><b>线上动作</b>：{escape("、".join("【" + o + "】" for o in olds))}</span>',
            f'<b style="color:#BF360C;">方向</b>：{tex(direc)}',
            f'<b>依据</b>：{fill_refs(tex(basis))}',
            f'<b>信号</b>：{tex(signal)}',
            f'<b>范例</b>：{tex(chain.replace(chr(92) + "frac", chr(92) + "dfrac"))}',
            '<span style="font-size:12px;color:#00695C;"><b>题型入口里</b>：' + ("、".join(f"{q}〔{grid(q)}〕" for q in qs) or "—") + "</span>",
            f'<span style="color:#B71C1C;">⚠ {tex(trap)}</span>',
            f'<span style="font-size:10px;color:#607D8B;">推导线 {len(meth[no])} 处：' + "、".join(f"{t}〔{grid(t)}〕" for t in meth[no]) + "</span>"]
    meas = [short + name, "线上动作：" + "、".join("【" + o + "】" for o in olds), "方向：" + direc, "依据：" + basis, "信号：" + signal, "范例：" + chain,
            "题型入口里：" + "、".join(q + "〔A1〕" for q in qs), "⚠ " + trap, "推导线：" + "、".join(t + "〔A1〕" for t in meth[no])]
    per = (mw2 - 30) / 12.0
    hgt = 26 + sum(max(1, math.ceil(vw(m)[0] / per)) * 19 for m in meas) + (16 if "frac" in chain else 0)
    c = col_y.index(min(col_y))
    cell("<br>".join(rows), MCARD, PX + 30 + c * (mw2 + 30), col_y[c], mw2, hgt, "bg")
    col_y[c] += hgt + 16
cells.insert(n_before_mframe, ("bgmframe", "", "rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=#FBF8F6;strokeColor=#A1887F;strokeWidth=2;", PX, m_frame_top, PW, max(col_y) - m_frame_top + 10, "bg"))
py = max(col_y) + 60

cell('<b style="font-size:22px">题型入口：从哪进——看到什么题，走哪个方向、用哪些工具</b><br><span style="font-size:13px;">看到什么 → 【方向（方法）】 → 先查 → 去图里的问题节点〔编号 · 坐标〕；节点里写“方向”和“工具”两行</span>', "text;html=1;fontFamily=PingFang SC;fontColor=#00695C;align=left;verticalAlign=top;", PX, py, PW, 56, "bg")
py += 66
ew = (PW - 30) // 2
col_y = [py, py]
CITY_NAME = {sk: SECS[sk].split("：")[0] for sk in SECS}
QORDER = ["alg", "exp", "tri", "vec", "cpx", "seq", "cnt", "der", "fun", "geo", "sp", "prob"]
for sk in QORDER:
    qs = sorted((n for n in NODES if n["type"] == "problem" and n["sec"] == sk), key=lambda n: int(n["id"][1:]))
    if not qs:
        continue
    rows, meas = [], []
    for q in qs:
        see = q["title"].replace("看到：", "")
        note = next((l[3:] for l in q["lines"] if l.startswith("注意：")), "")
        mshort = DIRECTION.get(q["id"], ("", ""))[0]
        txt = f"▸ {see}" + (f" → 【{mshort}】" if mshort else "") + (f" → 先查：{note}" if note else "")
        rows.append(f'{tex(txt)} → <b style="color:#004D40;">{q["id"]}{escape("〔" + grid(q["id"]) + "〕")}</b>')
        meas.append(txt + q["id"] + "〔A1〕")
    per = (ew - 30) / (11 * 1.05)
    h = 46 + sum(max(1, math.ceil(vw(m)[0] / per)) * 18 + (8 if re.search(r"\\(d?frac)", m) else 0) for m in meas)
    c = col_y.index(min(col_y))
    cell(f'<b>▍{escape(CITY_NAME[sk])}</b><br>' + "<br>".join(rows), ST["entry"] + "verticalAlign=top;spacingTop=8;",
         PX + c * (ew + 30), col_y[c], ew, h, "bg")
    col_y[c] += h + 20
py = max(col_y) + 40


# ── 写 XML ──
A = lambda s: escape(s, {'"': "&quot;"})
out = ['<mxfile host="build.py"><diagram id="identity" name="恒等式大厦"><mxGraphModel dx="2000" dy="1000" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" math="1" shadow="0"><root>',
       '<mxCell id="0"/>', '<mxCell id="bg" value="背景（锁定）" style="locked=1;" parent="0"/>', '<mxCell id="1" value="推导与应用" parent="0"/>']
for cid, value, style, x, y, w, h, parent in cells:
    out.append(f'<mxCell id="{cid}" value="{A(value)}" style="{A(style)}" vertex="1" parent="{parent}"><mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')


def note_html(t):
    if t.startswith("⚡"):
        return f'<span style="font-size:11px;color:#00695C;font-weight:bold;">{fill_refs(tex(t))}</span>'
    color = "#1565C0" if t.startswith("同见") else "#607D8B"
    return f'<span style="font-size:10px;color:{color};font-weight:normal;">{fill_refs(tex(t))}</span>'



GUT = {}


def gutter(sk, left):
    x0, y0, w, h = clusters[sk]
    return x0 - GAP / 2 if left else x0 + w + GAP / 2


def row_gutters(r):
    xs = []
    for sk in ROWS[r]:
        xs += [gutter(sk, True), gutter(sk, False)]
    return xs


GUT = {}
def stagger(key):
    k = GUT.get(key, 0); GUT[key] = k + 1
    return ((k + 1) // 2) * 16 * (1 if k % 2 else -1)


def cross_route(i, e):
    return route(nodes[e["s"]], nodes[e["t"]])


def route(sn, tn):
    """跨城走线：进城旁竖向空隙 → 层间横向空隙 → 目标城旁竖向空隙 → 从侧面进入目标。"""
    ss, ts = sn["sec"], tn["sec"]
    rs, rt = SEC_ROW[ss], SEC_ROW[ts]
    sc, tc = clusters[ss], clusters[ts]
    scx, tcx = sn["x"] + sn["w"] / 2, tn["x"] + tn["w"] / 2
    sy, ty = sn["y"] + sn["h"] / 2, tn["y"] + tn["h"] / 2
    if rs == rt:
        s_left = tcx < scx
        t_left = scx < tcx
    else:
        s_left = tcx < scx if abs(tcx - scx) > sc[2] / 2 else scx < sc[0] + sc[2] / 2
        t_left = tcx < tc[0] + tc[2] / 2
    gs = gutter(ss, s_left); gt = gutter(ts, t_left)
    gs += stagger(("g", round(gs))); gt_off = gt + (stagger(("g", round(gt))) if abs(gt - gs) > 40 else 0)
    gt = gt_off
    pts = [(gs, sy)]
    if rs == rt:
        if abs(gs - gt) < 60:
            gt = gs
            pts.append((gs, ty))
        else:
            yc = ROWBOT[rs] + GAP / 2 + stagger(("c", rs, "b"))
            pts += [(gs, yc), (gt, yc), (gt, ty)]
    else:
        step = 1 if rt > rs else -1
        cur = gs
        r = rs
        while r != rt:
            nxt = r + step
            yc = (ROWTOP[nxt] - GAP / 2 if step > 0 else ROWTOP[r] - GAP / 2) + stagger(("c", min(r, nxt)))
            pts.append((cur, yc))
            if nxt == rt:
                pts += [(gt, yc), (gt, ty)]
            else:
                gm = min(row_gutters(nxt), key=lambda g: abs(g - gt))
                pts.append((gm, yc)); cur = gm
            r = nxt
    ex = sn["x"] if s_left else sn["x"] + sn["w"]
    en = tn["x"] if t_left else tn["x"] + tn["w"]
    path = [(ex, sy)] + pts + [(en, ty)]
    clean = [path[0]]
    for q in path[1:]:
        if math.dist(q, clean[-1]) > 1:
            clean.append(q)
    path = clean
    seg = [math.dist(path[j], path[j + 1]) for j in range(len(path) - 1)]
    half, acc = sum(seg) / 2, 0
    mx_, my_ = path[0]
    for j, d_ in enumerate(seg):
        if acc + d_ >= half and d_ > 0:
            r_ = (half - acc) / d_
            mx_ = path[j][0] + r_ * (path[j + 1][0] - path[j][0]); my_ = path[j][1] + r_ * (path[j + 1][1] - path[j][1])
            break
        acc += d_
    # 标签放在最后一段竖向空隙的中部；太短就放在横向空隙中部
    a_, b_ = path[-3], path[-2]
    if abs(a_[0] - b_[0]) < 1 and abs(a_[1] - b_[1]) > 180:
        lx, ly = a_[0], (a_[1] + b_[1]) / 2
    else:
        hs = max(((path[j], path[j + 1]) for j in range(len(path) - 1) if abs(path[j][1] - path[j + 1][1]) < 1),
                 key=lambda q: abs(q[0][0] - q[1][0]), default=(path[0], path[-1]))
        lx, ly = (hs[0][0] + hs[1][0]) / 2, hs[0][1]
    geo = ('<Array as="points">' + "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in path[1:-1]) + "</Array>"
           f'<mxPoint x="{lx - mx_:.0f}" y="{ly - my_:.0f}" as="offset"/>')
    route.last_path = path
    return geo, (f"exitX={0 if s_left else 1};exitY=0.5;exitDx=0;exitDy=0;"
                 f"entryX={0 if t_left else 1};entryY=0.5;entryDx=0;entryDy=0;")


def emit_edge(i):
    e = EDGES[i]
    st = {"premise": E_PRE, "apply": E_APPLY, "define": E_DEFINE}.get(e["kind"]) or (E_MAIN if e["main"] else E_DER)
    pts, lp = epath.get(f"e{i}", ([], None))
    geo = ""
    xrel = ""
    if CROSS(e):
        geo, extra_st = cross_route(i, e)
        st = st.replace("curved=1;", "curved=1;edgeStyle=orthogonalEdgeStyle;") + extra_st
    else:
        way = pts[3:-3:3] if len(pts) > 7 else pts[1:-1][::3]
        if way:
            geo += '<Array as="points">' + "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in way) + "</Array>"
        poly = pts[::3]
        if lp and len(poly) >= 2:
            seg = [math.dist(poly[k], poly[k + 1]) for k in range(len(poly) - 1)]
            half, acc, mx_, my_ = sum(seg) / 2, 0, poly[0][0], poly[0][1]
            for k, d_ in enumerate(seg):
                if acc + d_ >= half and d_ > 0:
                    r = (half - acc) / d_
                    mx_ = poly[k][0] + r * (poly[k + 1][0] - poly[k][0]); my_ = poly[k][1] + r * (poly[k + 1][1] - poly[k][1])
                    break
                acc += d_
            geo += f'<mxPoint x="{lp[0] - mx_:.0f}" y="{lp[1] - my_:.0f}" as="offset"/>'
    L = elabel_lines(e)
    parts = []
    if e["kind"] == "derive" and CROSS(e):
        parts.append('<span style="color:#6A1B9A;font-weight:bold;">★ 跨树</span>')
    if e["mark"]:
        parts.append(f'<span style="color:#E65100;font-weight:bold;">{tex(e["mark"])}</span>')
    parts += [fill_refs(tex(l)) for l in e["lines"]]
    if e["kind"] == "apply":
        parts = []          # “怎么用 + 例子”已写进问题节点，线上不重复
    if e["kind"] == "premise":
        st += "fontColor=#607D8B;"
    kind_cn = {"premise": "前提", "apply": "应用", "define": "定义"}.get(e["kind"], "推导")
    layer = "1"
    tagv = "应用层" if e["kind"] == "apply" else "推导层"
    return (f'<UserObject id="e{i}" label="{A("<br>".join(parts))}" 类型="{kind_cn}" tags="{tagv}">'
               f'<mxCell style="{A(st)}" edge="1" parent="{layer}" source="{e["s"]}" target="{e["t"]}"><mxGeometry{xrel} relative="1" as="geometry">{geo}</mxGeometry></mxCell></UserObject>')

E_TRUNK = ("html=1;rounded=1;curved=1;edgeStyle=orthogonalEdgeStyle;strokeColor=#546E7A;strokeWidth=5;opacity=80;"
           "endArrow=block;endSize=10;fontFamily=PingFang SC;fontSize=12;fontStyle=1;fontColor=#37474F;labelBackgroundColor=#FFFFFF;")
CITY = {sk: SECS[sk].split("：")[0] for sk in SECS}
for k, ((ss, ts), idxs) in enumerate(TRUNK.items()):
    sc, tc = clusters[ss], clusters[ts]
    sn = dict(x=sc[0], y=sc[1], w=sc[2], h=sc[3], sec=ss)
    tn = dict(x=tc[0], y=tc[1], w=tc[2], h=tc[3], sec=ts)
    geo, _ = route(sn, tn)
    p0, p1 = route.last_path[0], route.last_path[-1]
    rel = [f"{EDGES[i]['s']}→{EDGES[i]['t']}" + ("" if EDGES[i]["kind"] == "derive" else "（工具）") for i in idxs]
    lab = [f"{CITY[ss]} → {CITY[ts]}"] + ["、".join(rel[j:j + 3]) for j in range(0, len(rel), 3)]
    out.append(f'<mxCell id="tr{k}" value="{A("<br>".join(escape(x) for x in lab))}" style="{A(E_TRUNK)}" edge="1" parent="1">'
               f'<mxGeometry relative="1" as="geometry"><mxPoint x="{p0[0]:.0f}" y="{p0[1]:.0f}" as="sourcePoint"/>'
               f'<mxPoint x="{p1[0]:.0f}" y="{p1[1]:.0f}" as="targetPoint"/>{geo}</mxGeometry></mxCell>')
live = [i for i in range(len(EDGES)) if i not in dropped]
for i in [i for i in live if CROSS(EDGES[i]) or EDGES[i]["kind"] == "apply"]:
    out.append(emit_edge(i))
for nid, n in nodes.items():
    head = (tag(n["cond"]) + " " if n["cond"] else "") + (ext_tag + " " if n["ext"] else "") + (jiefa_tag + " " if nid in JIEFA else "") + code_span(nid)
    body = []
    for l in n["lines"]:
        if l.startswith("✗"):
            body.append(f'<span style="font-size:11px;color:#B71C1C;font-weight:normal;">{tex(l)}</span>')
        else:
            body.append(fill_refs(tex(l)))
    body += [note_html(t) for t in n["notes"]]
    ut = uses_text(n, grid)
    if ut:
        body.append(f'<span style="font-size:10px;color:#00695C;font-weight:normal;">{tex(ut)}</span>')
    for src, k, txt in n.get("pre", []):
        col = "#37474F" if k == "derive" else "#607D8B"
        body.append(f'<span style="font-size:10px;color:{col};font-weight:normal;">{fill_refs(tex(pre_text(k, txt, ref(src))))}</span>')
    align = "left" if len(body) >= 2 else "center"
    label = f'<div style="text-align:center">{head}<br>{tex(n["title"])}</div><div style="text-align:{align}">' + "<br>".join(body) + "</div>"
    cond = n["cond"] or "无条件"
    out.append(f'<UserObject id="{nid}" label="{A(label)}" 编号="{nid}" 类型="{TYPE[n["type"]]}" 条件="{A(cond)}" 分区="{A(SECS[n["sec"]].split("：")[0])}" 坐标="{grid(nid)}" tags="{"应用层" if n["type"] == "problem" else "推导层"}">'
               f'<mxCell style="{A(NODE_ST[n["type"]])}" vertex="1" parent="1"><mxGeometry x="{n["x"]:.0f}" y="{n["y"]:.0f}" width="{n["w"]}" height="{n["h"]}" as="geometry"/></mxCell></UserObject>')

for i in sorted([i for i in live if not CROSS(EDGES[i]) and EDGES[i]["kind"] != "apply"], key=lambda i: 0 if EDGES[i]["kind"] == "premise" else (1 if not EDGES[i]["main"] else 2)):
    out.append(emit_edge(i))
out.append("</root></mxGraphModel></diagram></mxfile>")
open(OUT, "w").write("\n".join(out))
print("nodes", len(nodes), "edges", len(EDGES), "dropped premise", len(dropped), "grid", NC, "x", NR,
      "canvas", int(MAXX), "x", int(MAXY), "methods", len(meth))
if VERSIONED:
    DRAWIO = "/Applications/draw.io.app/Contents/MacOS/draw.io"
    pdf = OUT[:-7] + ".pdf"
    if os.path.exists(DRAWIO):
        subprocess.run([DRAWIO, "-x", "-f", "pdf", "--crop", "-o", pdf, OUT], capture_output=True)
        print("已导出", os.path.relpath(pdf))
    print("已写出", os.path.relpath(OUT))
