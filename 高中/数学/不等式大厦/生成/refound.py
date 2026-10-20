import re, sys, copy
import xml.etree.ElementTree as ET
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')

def cell(el): return el if el.tag == 'mxCell' else el.find('mxCell')
def label_attr(el): return 'label' if el.tag == 'UserObject' else 'value'
byid = {el.get('id'): el for el in root}

SEC_TOP, SEC_BOTTOM_OLD = 0, 1617
DELETE_NODES = ['xp', 'xn', 'x0', 'diff']
DELETE_EDGES = ['e4', 'e8', 'e9', 'e10', 'v17e5']

# ---------- 1. 新布局（左上角坐标） ----------
LAYOUT = {
    'ax_pos': (6370, 90), 'ax_order': (7830, 90),
    'sq_mono': (6080, 420), 'muln': (6490, 420), 'mulp': (6940, 420), 'add': (7460, 420),
    'sumadd': (7840, 420), 'recip': (8250, 420), 'sugar': (8640, 420),
    'sq': (6500, 760), 'divp': (6800, 760), 'mul_pos': (7100, 760), 'quotient': (7420, 760), 'sub_opp': (7800, 760),
    'pow_mono': (7070, 1050), 'div_opp': (7600, 1050),
}
# 内部边：入口 entryX、标签水平偏移、折线所在高度错开量
ROUTE = {
    'e2': (0.3, -60, 0), 'fx2': (0.75, 150, 14), 'e3': (0.3, -40, 28), 'fx3': (0.75, 0, 42),
    'e0': (0.5, 0, 0), 'e1': (0.5, 0, 14), 'e11': (0.5, 0, 28), 'p2e11': (0.5, 0, 42), 'gap1': (0.5, 0, 56),
    'e6': (0.75, -270, 0), 'e7': (0.3, -150, 14), 'e5': (0.5, 45, 28), 's1e3': (0.5, 0, 42), 'p2e10': (0.5, 30, 56),
    'v33e1': (0.5, 0, 0), 's1e4': (0.5, 0, 0), 'v33e2': (0.3, -150, 14), 'v33e3': (0.75, 150, 28),
}
SEC_IDS = set(LAYOUT) | set(DELETE_NODES)

def geo(i):
    g = cell(byid[i]).find('mxGeometry')
    return g, float(g.get('x', 0)), float(g.get('y', 0)), float(g.get('width', 0)), float(g.get('height', 0))

old_geo = {i: geo(i)[1:] for i in LAYOUT}
new_bottom = max(LAYOUT[i][1] + geo(i)[4] for i in LAYOUT) + 60
DELTA = SEC_BOTTOM_OLD - new_bottom          # 下方整体上移量
print('new section bottom', new_bottom, 'shift up', DELTA)

for i, (x, y) in LAYOUT.items():
    g = geo(i)[0]; g.set('x', '%g' % x); g.set('y', '%g' % y)
gsec = geo('bg23')[0]; gsec.set('height', '%g' % new_bottom)

# ---------- 2. 删除节点与边 ----------
for i in DELETE_NODES + DELETE_EDGES:
    root.remove(byid.pop(i))

# ---------- 3. 改边：重定向 + 新标签 ----------
RED = '<span style="color:#D84315;font-weight:bold;">▼ 进入正数域：%s</span><br>'
EDGES = {
    'e0':  (None, None, '【作差法】(a+c)−(b+c) = a−b > 0'),
    'e1':  (None, None, '【作差法】(a+c)−(b+d) = (a−b)+(c−d) ≥ 0'),
    'e2':  (None, None, '【作差法】c>0：(a−b)c > 0'),
    'e3':  (None, None, '【作差法】c<0：(a−b)(−c) > 0 ⇒ ac < bc'),
    'fx2': (None, None, '【前提】a>b ⟺ a−b>0'),
    'fx3': (None, None, ''),
    'e5':  (None, None, '【代换法】c = 1/d<br>1/d>0：否则 d·(1/d) ≤ 0，与 =1 矛盾'),
    'e6':  (None, 'sq', '【分类讨论】x>0：令 a=c=x, b=0 ⇒ x²>0'),
    'e7':  (None, 'sq', '【分类讨论】x<0：令 a=0, b=c=x ⇒ x²>0<br>x=0 时 x²=0'),
    'gap1': (None, None, RED % '0≤a<b' + '【作差法】b²−a² = (b+a)(b−a) > 0<br>【反证法】反过来 a²<b²：若 a≥b 则 a²≥b²，矛盾'),
    's1e3': (None, None, '【作差法】ac−bd = (a−b)c + b(c−d) ≥ 0<br>严格时 c>d≥0 ⇒ c>0，(a−b)c>0 ⇒ ac>bd'),
    's1e4': (None, None, '【归纳法】aᵏ>bᵏ≥0 与 a>b≥0 相乘 ⇒ aᵏ⁺¹>bᵏ⁺¹<br>【反证法】开方：若 ⁿ√a ≤ ⁿ√b，乘方得 a≤b，矛盾'),
    'p2e10': (None, None, RED % 'b>0' + '【同乘法】两边乘 b'),
    'e11': ('ax_order', None, RED % '0<a<b' + '【作差法】1/a − 1/b = (b−a)/(ab) > 0'),
    'p2e11': ('ax_order', None, RED % 'b>a>0, m>0' + '【作差法】差 = m(b−a)/[b(b+m)] > 0'),
    'v33e1': (None, None, '【作差法】(a−c)−(b−d) = (a−b)+(d−c) > 0'),
    'v33e2': (None, None, '【同向相乘】a>b>0 与 1/d>1/c>0 相乘'),
    'v33e3': (None, None, '【前提】c>d>0 ⇒ 1/d > 1/c'),
}
PORT = re.compile(r'(exit|entry)(X|Y|Dx|Dy)=[^;]*;')
for eid, (src, tgt, text) in EDGES.items():
    el = byid[eid]; c = cell(el)
    if src: c.set('source', src)
    if tgt: c.set('target', tgt)
    parts = re.split(r'(<br>|<span style="[^"]*">|</span>)', text)
    text = ''.join(p if p.startswith('<') and (p in ('<br>', '</span>') or p.startswith('<span style=')) else p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') for p in parts)
    lab = convert_label(text, []) if text else ''
    lab = re.sub(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)',
                 lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', lab)
    el.set(label_attr(el), lab)
    entry, ldx, stag = ROUTE[eid]
    c.set('style', PORT.sub('', c.get('style')) + 'exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=%g;entryY=0;entryDx=0;entryDy=0;' % entry)
    g = c.find('mxGeometry')
    for a in list(g): g.remove(a)
    sx, sy, sw, sh = (LAYOUT[c.get('source')][0], LAYOUT[c.get('source')][1], geo(c.get('source'))[3], geo(c.get('source'))[4])
    tx, ty, tw, th = (LAYOUT[c.get('target')][0], LAYOUT[c.get('target')][1], geo(c.get('target'))[3], geo(c.get('target'))[4])
    lines = lab.split('<br>') if lab else []
    lh = sum(16 + (22 if 'dfrac' in l else 0) for l in lines)
    x1, x2 = sx + sw / 2, tx + tw * entry
    ymid = ty - lh - 34 - stag - (52 if eid == 'e7' else 0)
    if c.get('source') == 'recip' and c.get('target') == 'div_opp':
        ymid = ty - 70
    arr = ET.SubElement(g, 'Array', {'as': 'points'})
    if abs(x1 - x2) > 1:
        ET.SubElement(arr, 'mxPoint', {'x': '%g' % x1, 'y': '%g' % ymid})
        ET.SubElement(arr, 'mxPoint', {'x': '%g' % x2, 'y': '%g' % ymid})
    g.set('relative', '1'); g.set('x', '1'); g.set('y', '0')
    dy = -(lh / 2 + 10) - (52 if eid == 'e7' else 0)
    ET.SubElement(g, 'mxPoint', {'x': '%g' % ldx, 'y': '%g' % dy, 'as': 'offset'})

# ---------- 4. 下方内容整体上移 ----------
GRID = {'bg%d' % k for k in range(45, 85)}
shifted = set()
for el in root:
    c = cell(el)
    if c is None or c.get('vertex') != '1' or el.get('id') in GRID or el.get('id') in SEC_IDS: continue
    g = c.find('mxGeometry')
    if g is None or g.get('relative') == '1': continue
    x, y = float(g.get('x', 0)), float(g.get('y', 0))
    if x >= -180 + 90 and y >= SEC_BOTTOM_OLD:
        g.set('y', '%g' % (y - DELTA)); shifted.add(el.get('id'))

def box(i):
    _, x, y, w, h = geo(i); return x, y, w, h

# 跨区边：本区内的旧折点换成新通道，本区以下的折点上移
LANES = {  # 源节点: (出口, 通道 x)
    'sq': ('bottom', None), 'recip': ('bottom', None), 'quotient': ('bottom', None), 'pow_mono': ('bottom', None),
    'mul_pos': ('left', 7045), 'muln': ('left', 6440), 'mulp': ('bottomlane', 7060),
    'sq_mono': ('left', 6055), 'sumadd': ('right', 8215), 'ax_pos': ('left', 6042),
}
for el in root:
    c = cell(el)
    if c is None or c.get('edge') != '1': continue
    s, t = c.get('source'), c.get('target')
    g = c.find('mxGeometry'); arr = g.find('Array')
    if s in LAYOUT and t not in SEC_IDS:
        pts = [] if arr is None else [(float(p.get('x')), float(p.get('y'))) for p in arr]
        kept = [(x, y - DELTA) for x, y in pts if y >= 1650]
        side, lane = LANES[s]
        x, y, w, h = box(s)
        st = PORT.sub('', c.get('style'))
        bus = kept[0][1] if kept else new_bottom + 40
        if side == 'bottom':
            st += 'exitX=0.5;exitY=1;exitDx=0;exitDy=0;'
            new = [(x + w / 2, bus)]
        elif side == 'bottomlane':
            st += 'exitX=%.4f;exitY=1;exitDx=0;exitDy=0;' % ((lane - x) / w)
            new = [(lane, bus)]
        else:
            ex = 0 if side == 'left' else 1
            st += 'exitX=%d;exitY=0.5;exitDx=0;exitDy=0;' % ex
            new = [(lane, y + h / 2), (lane, bus)]
        # 保留原入口
        m = re.findall(r'(entry(?:X|Y|Dx|Dy)=[^;]*;)', c.get('style'))
        st += ''.join(m)
        c.set('style', st)
        if arr is None:
            arr = ET.SubElement(g, 'Array', {'as': 'points'})
        for p in list(arr): arr.remove(p)
        for x2, y2 in new + kept:
            ET.SubElement(arr, 'mxPoint', {'x': '%.1f' % x2, 'y': '%.1f' % y2})
    elif arr is not None and s not in SEC_IDS:
        for p in arr:
            y = float(p.get('y'))
            if y >= SEC_BOTTOM_OLD: p.set('y', '%.1f' % (y - DELTA))

tree.write(F, encoding='utf-8', xml_declaration=True)
print('shifted', len(shifted))
