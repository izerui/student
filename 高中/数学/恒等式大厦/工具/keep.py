"""只保留指定编号的节点及它们之间的连线，另存为 drawio，便于单独检查几条跨城干道。
用法：python3 工具/keep.py 源.drawio 目标.drawio R01,R15,P49"""
import sys, xml.etree.ElementTree as ET
src,dst=sys.argv[1],sys.argv[2]; ids=set(sys.argv[3].split(','))
t=ET.parse(src); root=t.getroot().find('.//root')
for el in list(root):
    c=el if el.tag=='mxCell' else el.find('mxCell')
    i=el.get('id')
    if i in ('0','1','bg'): continue
    if c is not None and c.get('edge')=='1':
        if c.get('source') in ids and c.get('target') in ids: continue
        root.remove(el)
    elif i not in ids: root.remove(el)
t.write(dst,encoding='utf-8',xml_declaration=True)
