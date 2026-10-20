"""只保留指定编号的节点及它们之间的连线（含线上标注：连线 id 后加 L 的独立文字块），另存为 drawio，便于单独检查一条推导路径。
用法：python3 工具/keep.py 源.drawio 目标.drawio S02,R01,R18,P02"""
import sys
import xml.etree.ElementTree as ET

src, dst = sys.argv[1], sys.argv[2]
ids = set(sys.argv[3].split(","))
t = ET.parse(src)
root = t.getroot().find(".//root")
edges = set()
for el in root:
    if el.tag == "mxCell" and el.get("edge") == "1" and el.get("source") in ids and el.get("target") in ids:
        edges.add(el.get("id"))
for el in list(root):
    i = el.get("id")
    if i in ("0", "1", "bg") or i in ids or i in edges or el.get("parent") in edges or (i or "")[:-1] in edges:
        continue
    root.remove(el)
t.write(dst, encoding="utf-8", xml_declaration=True)
