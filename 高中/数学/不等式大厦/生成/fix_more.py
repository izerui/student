"""v38 补充：R23→R31 的连线改从 R17 出发；"积定和最小"入口补实际应用题提示。
用法：python3 生成/fix_more.py outputs/inequality-tree-v38.drawio（原地修改，可重复运行）"""
import html, os, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}

# 1. e26：起点 R23 → R17（配方结果所在节点），从 R17 左侧出，沿原通道到 R31
el = byid['e26']
c = el.find('mxCell')
if c.get('source') != 'quad_sq':
    c.set('source', 'quad_sq')
    st = c.get('style').replace('exitX=0.0000;exitY=0.3361;', 'exitX=0;exitY=0.5;')
    c.set('style', st)
    g = byid['quad_sq'].find('mxCell').find('mxGeometry')
    y = float(g.get('y')) + float(g.get('height')) / 2
    pts = c.find('mxGeometry').find('Array')
    pts[0].set('y', '%g' % y)
    el.set('label', el.get('label').replace('代入 R17 的配方结果', '代入配方结果'))

# 2. 积定和最小入口：补实际应用题
el = byid['ent_fxprd']
line = ('实际应用（用料最省、费用最少、面积最大等）：设变量、列目标函数 → 看和或积是否为定值 → '
        '用基本不等式，并检查取等时的变量值在实际范围内')
if '实际应用' not in el.get('label'):
    new = convert_label(html.escape(line, quote=False), []) + '<br>'
    lab = el.get('label').replace('<span style="color:#00695C;font-weight:bold;">去这里查：', new + '<span style="color:#00695C;font-weight:bold;">去这里查：', 1)
    el.set('label', lab)
    grow = 40
    g0 = el.find('mxCell').find('mxGeometry')
    y0 = float(g0.get('y'))
    g0.set('height', '%g' % (float(g0.get('height')) + grow))
    for other in root:   # 入口一栏中它下方的卡片和分组标题整体下移
        oc = other if other.tag == 'mxCell' else other.find('mxCell')
        if oc is None or oc.get('vertex') != '1':
            continue
        og = oc.find('mxGeometry')
        if og is not None and og.get('relative') != '1' and float(og.get('x', 0)) == -840 and float(og.get('y', 0)) > y0:
            og.set('y', '%g' % (float(og.get('y')) + grow))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
