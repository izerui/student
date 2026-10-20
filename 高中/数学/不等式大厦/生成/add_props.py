"""补 B 版必修一 2.2.1 的三条性质名称（v39 → v40）：传递性、对称性写进 S01，移项法则写进 R04。不新增节点。
用法：cp outputs/inequality-tree-v39.drawio outputs/inequality-tree-v40.drawio
      python3 生成/add_props.py outputs/inequality-tree-v40.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v40.drawio"""
import html, os, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]


def tex(s):
    return convert_label(html.escape(s, quote=False), [])


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if '传递性' in byid['ax_order'].get('label'):
    sys.exit('已修改过，跳过')

# (元素 id, 原片段, 新片段, 加高)
EDITS = [
    ('ax_order', '正数 + 正数 = 正数（由此：\\({a\\gt b}\\)、\\({b\\gt c \\Rightarrow  a\\gt c}\\)）',
     '正数 + 正数 = 正数（由此得<b>传递性</b>：' + tex('a > b，b > c ⇒ a > c') + '）<br>'
     + '<b>对称性</b>：' + tex('a > b ⟺ b < a') + '（两者都表示 ' + tex('a − b') + ' 是正数）', 17),
    ('add', '\\({a\\gt b \\Rightarrow  a+c \\gt  b+c}\\)',
     '\\({a\\gt b \\Rightarrow  a+c \\gt  b+c}\\)<br><span style="font-size:11px;">推论：<b>移项法则</b><br>'
     + tex('a + b > c ⇒ a > c − b') + '（两边加 ' + tex('−b') + '）</span>', 30),
]
for eid, a, b, dh in EDITS:
    el = byid[eid]
    lab = el.get('label')
    assert lab.count(a) == 1, eid
    el.set('label', lab.replace(a, b))
    g = el.find('mxCell').find('mxGeometry')
    g.set('height', '%g' % (float(g.get('height')) + dh)); g.set('y', '%g' % (float(g.get('y')) - dh / 2))
g = byid['add'].find('mxCell').find('mxGeometry')   # R04 加宽 40，中心不动
g.set('width', '%g' % (float(g.get('width')) + 40)); g.set('x', '%g' % (float(g.get('x')) - 20))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
