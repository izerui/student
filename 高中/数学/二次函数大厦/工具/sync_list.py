"""把节点清单里由数据生成的部分（分区与节点、公式、题型入口、规模）按 生成/data.py 重新写一遍。
用法（在 数学/二次函数大厦/ 下）：python3 工具/sync_list.py
手写部分（定位与受众、主题补充、三层说明、输出）不动。"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "生成"))
from data import NODES, E, ENTRIES, SECTIONS, TOOLS, METHODS  # noqa: E402

N = {n[0]: n for n in NODES}
TYPE = {"start": "起点", "green": "结论", "white": "中间结果", "orange": "结论（有条件）", "lorange": "中间结果（有条件）"}
cell = lambda x: x.replace("|", "\\|")


def came(i):
    out = []
    for s, t, k, ls, m, mn in E:
        if t == i and k == "derive":
            ms = "、".join(dict.fromkeys(re.findall(r"【(.+?)】", " ".join(ls)))) or "—"
            out.append(f"{s}：{ms}" + (f"（{m}）" if m else ""))
    return "；".join(out) or "起点，直接承认"


L = ["## 分区与节点", "", "以下由 `生成/data.py` 生成（改数据后运行 `python3 工具/sync_list.py` 同步）。编号：S 起点，R、P 是结论（有没有条件看类型和条件列，不看字母）。", ""]
for title, ids in SECTIONS:
    L += [f"### {title}", "| 编号 | 名称 | 类型 | 条件 | 内容 | 来路【方法】 |", "|---|---|---|---|---|---|"]
    for i in ids:
        n = N[i]
        L.append(f"| {i} | {cell(n[3].lstrip('★ ').strip())} | {TYPE[n[1]]} | {cell(n[2] or '—')} | {cell('；'.join(n[4]))} | {cell(came(i))} |")
    L.append("")
L += ["### 工具箱（借来的公式，不画线；主图节点本身就是工具）", "；".join(f"{no} {nm}：{f}" for no, nm, f, *_ in TOOLS), "",
      "### 题型入口（青绿虚线框，反推）", "| 入口 | 看到 | 反推 | 先查 | 去这里查 |", "|---|---|---|---|---|"]
for k, (see, back, check, codes) in enumerate(ENTRIES, 1):
    L.append(f"| {k} | {cell(see)} | {cell(back)} | {cell(check)} | {'、'.join(codes)} |")
L.append("")

p = os.path.join(HERE, "..", "二次函数大厦-节点清单.md")
s = open(p).read()
i, j = s.index("## 分区与节点"), s.index("### 三层：工具、方法、题型入口")
s = s[:i] + "\n".join(L) + "\n" + s[j:]
nst = sum(1 for n in NODES if n[1] == "start")
i, j = s.index("## 规模"), s.index("## 输出")
s = (s[:i] + f"## 规模\n起点 {nst}，结论与中间结果 {len(NODES) - nst}，共 {len(NODES)} 个节点；连线 {len(E)} 条（推导 "
     f"{sum(1 for x in E if x[2] == 'derive')}、前提 {sum(1 for x in E if x[2] == 'premise')}）；题型入口 {len(ENTRIES)} 个；"
     f"工具箱 {len(TOOLS)} 条、方法 {len(METHODS)} 类；分区 {len(SECTIONS)} 个。\n\n" + s[j:])
open(p, "w").write(s)
print(f"已同步：{len(NODES)} 个节点、{len(E)} 条连线、{len(ENTRIES)} 个入口")
