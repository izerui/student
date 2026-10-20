"""v38 收尾：按第二轮修改的独立复审建议做 5 处措辞修正（原地修改，可重复运行）。
用法：python3 生成/fix_final.py outputs/inequality-tree-v38.drawio"""
import html, os, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label
tex = lambda s: convert_label(html.escape(s, quote=False), [])
F = sys.argv[1]
EDITS = {
    'fx3': ('【前提】同上', '【前提】a>b ⟺ a−b>0；正 × 负为负'),
    'e113': ('\\({a \\lt  0}\\) 时两边乘 \\({-1}\\)，同理', tex('a < 0 时方程两边乘 −1（Δ 不变），同理')),
    'am': ('（B 版教材称均值不等式）', '（人教 B 版称均值不等式）'),
    'schur_setup': ('⋯ 配合：⑩ 立方和与积的互换——整理展开式时', '⋯ 配合：⑩ 立方和与积的互换——t = 1 时整理展开式'),
    'v33e3': ('\\({c\\gt d\\gt 0 \\Rightarrow  \\dfrac{1}{d} \\gt  \\dfrac{1}{c}}\\)',
              '\\({0\\lt d\\lt c \\Rightarrow  \\dfrac{1}{d} \\gt  \\dfrac{1}{c}}\\)'),
}
EDITS['fx3'] = ('【前提】同上', tex('【前提】a>b ⟺ a−b>0；正 × 负为负'))
tree = ET.parse(F)
n = 0
for el in tree.getroot().find('.//root'):
    e = EDITS.get(el.get('id'))
    if not e:
        continue
    a = 'label' if el.tag == 'UserObject' else 'value'
    if e[0] in el.get(a):
        el.set(a, el.get(a).replace(e[0], e[1], 1)); n += 1
tree.write(F, encoding='utf-8', xml_declaration=True)
print('fixed', n)
