"""工具 / 方法定义按用户的说法统一（v44 → v45）。
工具 = 公理、定义、定理、公式，凡能拿来直接用的；主图每个节点都是工具，工具箱是借用的公式。
方法 = 换元、同乘、配凑等，解题的方向和思路。
改动：方法卡三层表"工具"一行；面板标题去掉 ①②（避免与工具箱公式编号混淆）；入口标题补"走哪个方向"；
      方法卡补入口里出现的主元、必要性探路、隐零点、同构，并写明入口与方法卡的分工；
      构造函数推导中判断导数正负一步由【分类讨论】并回"判单调"。
用法：cp outputs/inequality-tree-v44.drawio outputs/inequality-tree-v45.drawio
      python3 生成/methods2.py outputs/inequality-tree-v45.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v45.drawio"""
import sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}


def attr(el):
    return 'label' if el.tag == 'UserObject' else 'value'


if '本图推出的' in byid['bg100'].get('value'):
    sys.exit('已修改过，跳过')

EDITS = [
    ('bg85', '① 看到什么 → 用哪个工具：', '题型入口：看到什么 → 用哪个工具、走哪个方向；'),
    ('bg97', '② 工具本身：公式原文，按编号查（不画线）', '工具箱：借用的公式原文，按圈号查（不画线）'),
    ('bg100', '公式、定理，拿来直接套', '公理、定义、定理、公式——凡能拿来直接用的'),
    ('bg100', '工具箱；节点里的"⇐ 工具"', '主图每个节点（本图推出的）；工具箱（借用的公式）'),
    ('bg100', '方向判断：把眼前的问题转化成什么', '解题的方向和思路：把眼前的问题转化成什么'),
    ('bg100', '看到什么题，先想到哪个结论', '看到什么题，用哪个工具、走哪个方向'),
    ('bg100', '先用<b>方法</b>定方向，再用<b>工具</b>完成每一步：方法决定能不能想到，工具决定能不能算对。<br>',
     '先用<b>方法</b>找方向，再用熟悉的<b>工具</b>完成每一步：方法决定能不能想到，工具决定能不能算对。<br>'
     '题型入口按题型查（这道题用哪些工具、方法），方法卡按方法查（这个方法用在哪些题），是同一张表的两种查法。<br>'),
    ('bg100', '（代换、取特值', '（代换、取特值'),  # 占位，下面单独处理别名
]
EDITS.pop()
ALIAS = [('（换元、取特值、齐次化、归一化）', '（换元、取特值、齐次化、归一化、指对同构）'),
         ('（求导、单调性、求最值）', '（求导、单调性、求最值、隐零点、必要性探路）'),
         ('（代入消元、分离参数、调整）', '（代入消元、分离参数、主元、调整）')]
for eid, a, b in EDITS:
    el = byid[eid]
    v = el.get(attr(el))
    assert v.count(a) == 1, (eid, a)
    el.set(attr(el), v.replace(a, b))
v = byid['bg100'].get('value')
for a, b in ALIAS:
    assert v.count(a) == 1, a
    v = v.replace(a, b)
byid['bg100'].set('value', v)
g = byid['bg100'].find('mxGeometry')
g.set('height', '%g' % (float(g.get('height')) + 40))
for eid in ('e132', 'e133'):
    el = byid[eid]
    v = el.get(attr(el))
    assert v.count('【分类讨论】') == 1, eid
    el.set(attr(el), v.replace('【分类讨论】', '判单调：'))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
