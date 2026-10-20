"""v38 第二轮复查后的修正（原地修改 v38）。
用法：python3 生成/fix_review2.py outputs/inequality-tree-v38.drawio && python3 生成/fixrefs.py outputs/inequality-tree-v38.drawio
内容：图例措辞、前提线样式、入口去向补全、P50 改成异向写法、R07/R30/P29 等补充、
      两条穿过节点的连线改道、P27/R27 加宽、P45 加高。只运行一次（脚本开头检查是否已改过）。"""
import html, math, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')


def tex(s):
    out = convert_label(html.escape(s, quote=False), [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


def ref(text, num):
    return '<span style="color:#004D40;">▸ %s <b>〔%s · A1〕</b></span>' % (tex(text), num)


def small(text):
    return '<span style="font-size:10px;color:#607D8B;font-weight:normal;">%s</span>' % text


EDITS = [
    # 图例
    ('lg5', '绿色：结论，对任意实数成立（不限正负）', '绿色：结论，主变量取任意实数（若有橙色标签，只限制标签里的参数）'),
    ('lg7', '白底：推导中间一步，对任意实数成立', '白底：推导中间一步，主变量取任意实数（橙色标签同上）'),
    ('lg20', 'R 实数域', 'R 实数域（参数条件见橙色标签）'),
    ('lg33', '⋯ 配合</span>', '⋯ 配合 / ⋯ 同源</span>'),
    ('bg93', '—— 图中绿色、白色节点</b>', '—— 图中绿色、白色节点（橙色标签只限制参数）</b>'),
    # 入口
    ('ent_fxprd', '实际应用（用料最省、费用最少、面积最大等）', '实际应用（用料最省、费用最少等）'),
    ('ent_fxsum', '<span style="color:#00695C;font-weight:bold;">去这里查：',
     tex('实际应用（周长固定求面积最大等）：设变量、列目标函数，看和是否为定值') + '<br><span style="color:#00695C;font-weight:bold;">去这里查：'),
    ('ent_solve', '二次项系数含参时先讨论它是否为 0', '二次项系数含参时先讨论它是否为 0 及其正负'),
    ('ent_sq', '<b>〔R67 · J4〕</b></span>',
     '<b>〔R67 · J4〕</b></span><br>' + ref('平方和开方与 a+b 比较 → 平方平均 ≥ 算术平均', 'R71')
     + '<br>' + ref('几种平均数一起比较 → 四种平均数不等式链', 'P42')),
    ('ent_prod', '<span style="color:#004D40;">▸ n 个数时',
     ref('三个正数的和与积 → 三元 AM ≥ GM', 'P44') + '<br><span style="color:#004D40;">▸ n 个数时'),
    ('ent_cauch', '<b>〔R66 · G3〕</b></span>',
     '<b>〔R66 · G3〕</b></span><br>' + ref('柯西不等式（三项）', 'R58') + '<br>' + ref('柯西不等式（n 项）', 'R42')),
    ('ent_order', '<b>〔R32 · A3〕</b></span>', '<b>〔R32 · A3〕</b></span><br>' + ref('排序不等式（n 个数）', 'R41')),
    ('ent_abs', '<b>〔R59 · C7〕</b></span>',
     '<b>〔R59 · C7〕</b></span><br>' + ref('|x−a| + |x−b| 求最小值、恒成立求参 → 绝对值和的最小值', 'R53')),
    # 主图节点
    ('div_opp', '\\({c\\gt d\\gt 0}\\)\xa0</span>', '\\({0\\lt d\\lt c}\\)\xa0</span>'),
    ('div_opp', '\\({c\\gt d\\gt 0 \\Rightarrow  \\dfrac{a}{d} \\gt  \\dfrac{b}{c}}\\)',
     '\\({0\\lt d\\lt c \\Rightarrow  \\dfrac{a}{d} \\gt  \\dfrac{b}{c}}\\)'),
    ('div_opp', '⚠ 同向正数不等式不能相除', '⚠ 同向正数不等式不能对应项相除'),
    ('sumadd', 'a+c \\ge  b+d}\\)', 'a+c \\ge  b+d}\\)<br>' + tex('其中一个为 > 时，结论为 >')),
    ('qall', '先讨论它是否为 0</div>', '先讨论它是否为 0；a < 0 时不可能恒非负</div>'),
    ('am', '★★ 基本不等式 ', '★★ 基本不等式（B 版教材称均值不等式）'),
    ('sqsum', '⋯ 配合：排序不等式（两数）', '⋯ 同源：排序不等式（两数）'),
    ('rearr_setup', '⋯ 配合：\\({a^{2}+b^{2} \\ge  2ab}\\)', '⋯ 同源：\\({a^{2}+b^{2} \\ge  2ab}\\)'),
    ('f_sum_sq', '排序不等式（n 个数）、伯努利不等式（估计和）', '排序不等式（n 个数）'),
    ('schur_setup', '⋯ 配合：⑩ 立方和与积的互换——用⑩互换 \\({a^{3}+b^{3}}\\) 与 \\({ab(a+b)}\\)',
     '⋯ 配合：⑩ 立方和与积的互换——整理展开式时可把 \\({a^{3}+b^{3}}\\) 写成 \\({(a+b)^{3}-3ab(a+b)}\\)'),
    ('schur_group', '<br><span style="font-size:10px;color:#607D8B;font-weight:normal;">⋯ 配合：③ 立方和公式——舒尔不等式展开后用③④整理立方项</span>', ''),
    # 连线标签
    ('e11', '（\\({b-a \\gt  0}\\)，\\({ab \\gt  0}\\)）', tex('（b−a > 0，ab > 0：正数 × 正数为正）')),
    ('e113', '\\({-\\dfrac{\\Delta }{4a} \\le  0 \\iff  \\Delta \\ge 0}\\)</span>',
     '\\({-\\dfrac{\\Delta }{4a} \\le  0 \\iff  \\Delta \\ge 0}\\)</span><br>' + tex('a < 0 时两边乘 −1，同理')),
    ('fx3', '', '【前提】同上'),
]
ATTRS = {'div_opp': {'适用范围': 'a>b>0；0<d<c'}}
LIGHTEN = ['e39', 'e40', 'e41', 'fx2', 'fx3', 's1e7']      # 标【前提】却画成深色粗线的
DARK = 'strokeColor=#263238;strokeWidth=4;fontSize=12;fontColor=#263238;fontStyle=1;'
LIGHT = 'strokeColor=#90A4AE;strokeWidth=2;fontSize=11;fontColor=#263238;'

tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if '主变量取任意实数' in (byid['lg5'].get('value') or byid['lg5'].get('label') or ''):
    sys.exit('已修改过，跳过')


def attr(el):
    return 'label' if el.tag == 'UserObject' else 'value'


def geom(el):
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    return c, c.find('mxGeometry')


def est(lab, width):
    h = 0
    for line in re.split(r'<br>|</div>', lab):
        sm = 'font-size:10px' in line
        t = re.sub(r'\\\((.*?)\\\)', lambda m: 'x' * max(1, len(re.sub(r'\\[a-z]+|[{}_^ ]', '', m.group(1)))), line, flags=re.S)
        t = re.sub(r'<[^>]+>', '', t)
        if not t.strip():
            continue
        cw = 10 if sm else 13
        w = sum(cw if ord(ch) > 255 else cw * 0.55 for ch in t)
        h += max(1, math.ceil(w / max(60, width - 24))) * (14 if sm else 17) + (20 if 'dfrac' in line else 0)
    return h


old = {}
for eid, a, b in EDITS:
    el = byid[eid]
    lab = el.get(attr(el)) or ''
    old.setdefault(eid, lab)
    if a == '':
        assert lab == '', eid
        el.set(attr(el), b)
        continue
    assert lab.count(a) == 1, (eid, a[:50], lab.count(a))
    el.set(attr(el), lab.replace(a, b))
for eid, kv in ATTRS.items():
    for k, v in kv.items():
        byid[eid].set(k, v)
idx = byid['bg100']
v = idx.get('value')
m = re.search(r'(<b>换元 / 代换</b>（)(\d+)( 处）[^<]*<br><span[^>]*>)(.*?)(</span>)', v)
items = [i for i in m.group(4).split('、') if not i.startswith('P33〔')]
idx.set('value', v[:m.start()] + m.group(1) + str(len(items)) + m.group(3) + '、'.join(items) + m.group(5) + v[m.end():])
for eid in LIGHTEN:
    c, _ = geom(byid[eid])
    assert DARK in c.get('style'), eid
    c.set('style', c.get('style').replace(DARK, LIGHT))

# 加高：入口一栏重排，其余节点上下各扩一半
grow = {}
for eid, lab in old.items():
    el = byid[eid]
    c, g = geom(el)
    if c.get('vertex') != '1' or g is None or g.get('relative') == '1':
        continue
    d = est(el.get(attr(el)), float(g.get('width'))) - est(lab, float(g.get('width')))
    if d > 0:
        grow[eid] = d
col = []
for el in root:
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    if c is None or c.get('vertex') != '1':
        continue
    g = c.find('mxGeometry')
    if g is not None and g.get('relative') != '1' and float(g.get('x', 0)) == -840 and float(g.get('y', 0)) > 0:
        col.append(el)
col.sort(key=lambda e: float(geom(e)[1].get('y')))
shift = 0
for el in col:
    _, g = geom(el)
    g.set('y', '%g' % (float(g.get('y')) + shift))
    d = grow.pop(el.get('id'), 0)
    if d:
        g.set('height', '%g' % (float(g.get('height')) + d)); shift += d
grow['n_p45'] = 0
for eid, d in grow.items():
    if eid in byid and d:
        _, g = geom(byid[eid])
        g.set('height', '%g' % (float(g.get('height')) + d)); g.set('y', '%g' % (float(g.get('y')) - d / 2))


# 版面：加宽两个溢出的节点，P45 加高
def resize(num, dw=0, dh=0):
    el = next(e for e in root if e.get('编号') == num)
    _, g = geom(el)
    g.set('x', '%g' % (float(g.get('x')) - dw / 2)); g.set('width', '%g' % (float(g.get('width')) + dw))
    g.set('y', '%g' % (float(g.get('y')) - dh / 2)); g.set('height', '%g' % (float(g.get('height')) + dh))


resize('P27', dw=170, dh=10)
resize('R27', dw=160, dh=20)
resize('P45', dh=24)


# 两条穿过别的节点的连线改道
def reroute(eid, style_sub, pts):
    c, g = geom(byid[eid])
    st = re.sub(r'(exit|entry)(X|Y|Dx|Dy)=[^;]*;', '', c.get('style')) + style_sub
    c.set('style', st)
    arr = g.find('Array')
    for p in list(arr):
        arr.remove(p)
    for x, y in pts:
        ET.SubElement(arr, 'mxPoint', {'x': '%g' % x, 'y': '%g' % y})


# R43→R72：原来横穿 R44、R38；改为从 R43 底部出，走 R38 与 R47 之间的空档
reroute('v29e2', 'exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;',
        [(5982, 3250), (4017.4, 3250), (4017.4, 3349.8)])
# R42→P45：原来横穿 P42、P44；改为在这一排节点下方走，从 P45 底部进入
reroute('p2e28', 'exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;',
        [(8761.2, 3297.7), (8761.2, 4575), (11669, 4575)])
tree.write(F, encoding='utf-8', xml_declaration=True)
print('edits', len(EDITS), 'entry column shifted', shift)
