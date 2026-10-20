"""左侧三块统一用名称称呼：工具箱、方法、题型入口，不叫"卡"（v46 → v47）。
用法：cp outputs/inequality-tree-v46.drawio outputs/inequality-tree-v47.drawio
      python3 生成/rename_panels.py outputs/inequality-tree-v47.drawio"""
import sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
EDITS = [
    ('bg99', '方法卡：每类方法往哪走、凭什么、何时用', '方法：每类方法往哪走、凭什么、何时用'),
    ('bg100', '推导线上的【】；下面的方法卡', '推导线上的【】；左侧“方法”一栏'),
    ('bg100', '左侧"看到 …"卡片', '左侧“题型入口”一栏'),
    ('bg100', '方法卡按方法查', '“方法”一栏按方法查'),
    ('lg23', '见左侧方法卡', '见左侧“方法”一栏'),
]
for eid, a, b in EDITS:
    el = byid[eid]
    k = 'label' if el.tag == 'UserObject' else 'value'
    v = el.get(k)
    if b in v:
        continue
    assert v.count(a) == 1, (eid, a)
    el.set(k, v.replace(a, b))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
