"""读取《数学大厦-节点清单.md》，给 工具/check.py 用。
网页由 skill knowledge-map-web 的 tools/build.mjs 从同一份 md 生成（解析规则见它的 lib/md.js）；这里按同样的格式读，只做数学大厦自己的检查。

清单两级：
- `### 编号 名称　〔学段〕`：分组（一类知识）。写短名、区域、标志、是什么、要点、从哪来、依赖、后来发展到、用在哪、例子、往上通向、注释；
  没有拆的分组本身就是一张卡片，它的“依赖”写成“⇐推出 编号（怎么推的）；⇐用到 编号（…）”。
- `#### 编号 名称`：分组里的知识点（卡片），写标志、是什么、从哪来、要点、例子；“从哪来”里编号后面紧跟的全角括号写这一步怎么推的。
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID = r"\d\.\d{1,2}(?:\.\d{1,2})?"
ids_in = lambda t: re.findall(r"(?<![\d.])(%s)(?![\d])(?!\.\d)" % ID, t)
key = lambda i: tuple(int(x) for x in i.split("."))
layer_of = lambda i: int(i.split(".")[0])
KINDS = ("推出", "用到", "推广", "特例", "前提", "对照")


def parse_deps(src, self_id):
    """“依赖”或“从哪来”→ [{id, kind, how}]。分号分段；段里有“⇐推出/用到…”就用它，否则算“对照”；
    编号后面紧跟的全角括号是“怎么推的”。"""
    deps = []
    for seg in re.split(r"[；;]", src):
        kind = next((k for k in KINDS if "⇐" + k in seg), "对照")
        for m in re.finditer(r"(?<![\d.])(%s)(?![\d])(?!\.\d)" % ID, seg):
            r = m.group(1)
            if r == self_id or r in [d["id"] for d in deps]:
                continue
            how = re.match(r"\s*（([^）]*)）", seg[m.end():])
            deps.append({"id": r, "kind": kind, **({"how": how.group(1)} if how else {})})
    return deps


def fields(block):
    """“- 字段：内容”；列表字段下面缩进的“  - 条目”接到内容后面（用“；”连起来，便于检查和搜索）"""
    f, cur = {}, None
    for ln in block.split("\n"):
        m = re.match(r"^- ([^：:\s]{1,8})[：:]\s*(.*)$", ln)
        if m:
            cur = m.group(1)
            f[cur] = m.group(2).strip()
            continue
        s = re.match(r"^\s{2,}[-*] (.*)$", ln)
        if s and cur:
            f[cur] = "；".join(x for x in (f[cur], s.group(1).strip()) if x)
    return f


def load():
    text = open(os.path.join(ROOT, "数学大厦-节点清单.md"), encoding="utf-8").read()
    rooms, points = {}, {}
    for blk in re.split(r"^### ", text, flags=re.M)[1:]:
        blk = re.split(r"^(?:---|## )", blk, flags=re.M)[0]
        head, *subs = re.split(r"^#### ", blk, flags=re.M)
        m = re.match(r"(%s) (.+?)　(〔.*?〕)" % ID, head.split("\n")[0])
        rid = m.group(1)
        rooms[rid] = {"id": rid, "full": m.group(2), "stage": m.group(3).strip("〔〕"), "f": fields(head),
                      "layer": layer_of(rid), "points": [], "text": head}
        for sub in subs:
            pm = re.match(r"(%s) (.+)" % ID, sub.split("\n")[0])
            pid = pm.group(1)
            points[pid] = {"id": pid, "name": pm.group(2).strip(), "room": rid, "f": fields(sub),
                           "layer": layer_of(pid), "text": sub}
            rooms[rid]["points"].append(pid)
    # 图上的卡片：知识点，加上没有拆的分组
    nodes = {**{r: rooms[r] for r in rooms if not rooms[r]["points"]}, **points}
    deps = {n: parse_deps(nodes[n]["f"].get("依赖", nodes[n]["f"].get("从哪来", "")), n) for n in nodes}
    ups = {r: ids_in(rooms[r]["f"].get("往上通向", "")) for r in rooms}
    return {"text": text, "rooms": rooms, "points": points, "nodes": nodes, "deps": deps, "ups": ups}
