"""跨表联系：统计中的两个不等式在本图里的出处（v42 → v43）。只加"⋯ 应用"注释行，不展开统计内容。
R42 柯西（n 项）→ 相关系数 |r| ≤ 1；R71 平方平均 ≥ 算术平均 → 方差非负。
用法：cp outputs/inequality-tree-v42.drawio outputs/inequality-tree-v43.drawio
      python3 生成/add_stats.py outputs/inequality-tree-v43.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v43.drawio"""
import sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
NOTE = '<br><span style="font-size:10px;color:#607D8B;font-weight:normal;">%s</span>'

tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if '相关系数' in byid['cauchy_n'].get('label'):
    sys.exit('已修改过，跳过')

# (元素 id, 追加在其后的原片段, 注释, 加高)
EDITS = [
    ('cauchy_n', '或 \\({a_{i}}\\) 全为 0',
     '⋯ 应用（统计）：取 \\({a_{i}=x_{i}-\\bar{x}}\\)、\\({b_{i}=y_{i}-\\bar{y}}\\)，得相关系数 \\({|r| \\le  1}\\)；'
     '\\({|r|=1 \\iff}\\) 样本点都在一条直线上', 30),
    ('qmgeam', '等号 \\({\\iff  a=b \\ge  0}\\)',
     '⋯ 应用（统计）：n 个数时 \\({\\dfrac{x_{1}^{2}+\\cdots +x_{n}^{2}}{n} \\ge  \\bar{x}^{2}}\\)，'
     '即方差 \\({s^{2} = \\dfrac{x_{1}^{2}+\\cdots +x_{n}^{2}}{n}-\\bar{x}^{2} \\ge  0}\\)', 46),
]
for eid, a, note, dh in EDITS:
    el = byid[eid]
    lab = el.get('label')
    assert lab.count(a) == 1, eid
    el.set('label', lab.replace(a, a + NOTE % note))
    g = el.find('mxCell').find('mxGeometry')
    g.set('height', '%g' % (float(g.get('height')) + dh)); g.set('y', '%g' % (float(g.get('y')) - dh / 2))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done', len(EDITS))
