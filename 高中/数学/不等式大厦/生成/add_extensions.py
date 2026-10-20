"""两项扩展（v38 → v39）：
1. 导数区新增 P60「同构 + 切线放缩」：在 eˣ ≥ 1+x（R10）中令 t = x + ln x，得 xeˣ ≥ x + ln x + 1（x>0）；
   连线 R10 → P60，导数压轴入口加去向，方法索引"换元/代换"补 P60。
2. P07 对数平均补一行推论：x>1 时 ln x > 2(x−1)/(x+1)、ln x < ½(x − 1/x)。
用法：cp outputs/inequality-tree-v38.drawio outputs/inequality-tree-v39.drawio
      python3 生成/add_extensions.py outputs/inequality-tree-v39.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v39.drawio"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')


def tex(s):
    out = convert_label(html.escape(s, quote=False), [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if 'tong_gou' in byid:
    sys.exit('已添加过，跳过')

BADGE = '<span style="background-color:#E65100;color:#FFFFFF;font-size:10px;font-weight:bold;">\xa0%s\xa0</span> '
NUM = '<span style="font-size:10px;color:#78909C;font-weight:normal;">P60</span>'
GK = ' <span style="font-size:10px;color:#FFFFFF;background-color:#1565C0;font-weight:bold;">\xa0高考常用\xa0</span>'
NOTE = '<span style="font-size:10px;color:#607D8B;font-weight:normal;">%s</span>'

# 1. 新节点 P60
label = ('<div style="text-align:center">' + BADGE % tex('x > 0') + NUM + GK + '<br>★ 同构 + 切线放缩</div>'
         '<div style="text-align:left">' + tex('xeˣ ≥ x + ln x + 1（x > 0）') + '<br>'
         + tex('等号 ⟺ x + ln x = 0') + '<br>'
         + NOTE % tex('⋯ 同理：eˣ/x = e^{x−ln x} ≥ x − ln x + 1（x > 0）') + '</div>')
node = ET.SubElement(root, 'UserObject', {'id': 'tong_gou', 'label': label, '类型': '结论', '适用范围': 'x>0',
                                           '编号': 'P60', '层级': '2', '高考常用': '是'})
c = ET.SubElement(node, 'mxCell', {'parent': '1', 'vertex': '1', 'style': byid['exp2'].find('mxCell').get('style')})
ET.SubElement(c, 'mxGeometry', {'x': '4610', 'y': '6330', 'width': '420', 'height': '118', 'as': 'geometry'})

# 连线 R10 → P60：从 R10 左侧出，沿 R26 与 P51 之间的空档下行，再折到 P60 上方
edge = ET.SubElement(root, 'UserObject', {'id': 'tg_e1', '类型': '推导',
                                           'label': tex('【代换法】令 t = x + ln x（x > 0）') + '<br>' + tex('e^{x+ln x} = xeˣ ≥ 1 + x + ln x')})
ec = ET.SubElement(edge, 'mxCell', {'parent': '1', 'edge': '1', 'source': 'expineq', 'target': 'tong_gou',
                                     'style': 'html=1;rounded=1;edgeStyle=orthogonalEdgeStyle;fontFamily=PingFang SC;'
                                              'labelBackgroundColor=#FFFFFF;strokeColor=#455A64;strokeWidth=2.5;fontSize=11;'
                                              'fontColor=#263238;endArrow=block;endSize=7;exitX=0;exitY=0.5;exitDx=0;exitDy=0;'
                                              'entryX=0.5;entryY=0;entryDx=0;entryDy=0;curved=1;'})
eg = ET.SubElement(ec, 'mxGeometry', {'relative': '1', 'as': 'geometry', 'x': '1', 'y': '0'})
arr = ET.SubElement(eg, 'Array', {'as': 'points'})
for x, y in ((4570, 5684), (4570, 6145), (4820, 6145)):
    ET.SubElement(arr, 'mxPoint', {'x': str(x), 'y': str(y)})
ET.SubElement(eg, 'mxPoint', {'x': '0', 'y': '-52', 'as': 'offset'})

# 导数压轴入口：加去向
ent = byid['ent_adv']
lab = ent.get('label')
anchor = '<span style="color:#004D40;">▸ 切线放缩 → '
assert lab.count(anchor) == 1
ent.set('label', lab.replace(anchor, '<span style="color:#004D40;">▸ 指对同构 → ' + tex('xeˣ ≥ x + ln x + 1')
                             + ' <b>〔P60 · A1〕</b></span><br>' + anchor, 1))
eg0 = ent.find('mxCell').find('mxGeometry')
grow, y0 = 22, float(eg0.get('y'))
eg0.set('height', '%g' % (float(eg0.get('height')) + grow))
for el in root:   # 入口一栏下方整体下移
    cc = el if el.tag == 'mxCell' else el.find('mxCell')
    if cc is None or cc.get('vertex') != '1':
        continue
    g = cc.find('mxGeometry')
    if g is not None and g.get('relative') != '1' and float(g.get('x', 0)) == -840 and float(g.get('y', 0)) > y0:
        g.set('y', '%g' % (float(g.get('y')) + grow))

# 方法索引：换元 / 代换 补 P60
idx = byid['bg100']
v = idx.get('value')
m = re.search(r'(<b>换元 / 代换</b>（)(\d+)( 处）[^<]*<br><span[^>]*>)(.*?)(</span>)', v)
items = sorted(m.group(4).split('、') + ['P60〔A1〕'])
idx.set('value', v[:m.start()] + m.group(1) + str(len(items)) + m.group(3) + '、'.join(items) + m.group(5) + v[m.end():])

# 2. P07 对数平均：补推论
p07 = byid['log_mean']
lab = p07.get('label')
anchor = '<br>用途：极值点偏移'
assert lab.count(anchor) == 1
extra = '<br>' + tex('推论（x > 1）：取 a = x、b = 1 得 ln x > 2(x−1)/(x+1)；取 a = x²、b = 1 得 ln x < ½(x − 1/x)；都比 ln x ≤ x−1 更紧')
p07.set('label', lab.replace(anchor, extra + anchor, 1))
g = p07.find('mxCell').find('mxGeometry')
g.set('height', '%g' % (float(g.get('height')) + 86)); g.set('y', '%g' % (float(g.get('y')) - 43))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
