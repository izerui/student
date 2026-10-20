import re, sys, xml.etree.ElementTree as ET
orig, f = sys.argv[1], sys.argv[2]
def geoms(path):
    r = ET.parse(path).getroot().find('.//root'); d = {}
    for el in r:
        c = el if el.tag == 'mxCell' else el.find('mxCell')
        if c is None or c.get('vertex') != '1': continue
        g = c.find('mxGeometry')
        d[el.get('id')] = dict(x=float(g.get('x', 0)), y=float(g.get('y', 0)), h=float(g.get('height', 0)))
    return d
A, B = geoms(orig), geoms(f)
s = open(f, encoding='utf-8').read()
def set_y(i, y, h=None):
    global s
    m = re.search(r'id="%s"' % re.escape(i), s)
    gs = s.index('<mxGeometry', m.end()); ge = s.index('>', gs)
    tag = s[gs:ge]
    tag = re.sub(r'\by="[\d.-]+"', 'y="%g"' % y, tag)
    if h is not None: tag = re.sub(r'height="[\d.]+"', 'height="%g"' % h, tag)
    s = s[:gs] + tag + s[ge:]
def stack(ids):
    ids = sorted(ids, key=lambda i: A[i]['y']); prev = None; bottom = None
    for i in ids:
        y = A[i]['y'] if prev is None else bottom + (A[i]['y'] - (A[prev]['y'] + A[prev]['h']))
        set_y(i, y); bottom = y + B[i]['h']; prev = i
    return bottom
col = lambda x, lo=-1e9, hi=1e9: [i for i in A if A[i]['x'] == x and lo <= A[i]['y'] < hi]
b1 = stack(col(-1780, 1900, 3091)); b2 = stack(col(-1390, 1900, 3091))
stack(col(-840, 80))
# 公式面板背景加高，下方面板下移
old_bottom = A['bg98']['y'] + A['bg98']['h']
new_bottom = max(b1, b2, old_bottom - 20) + 20
d = new_bottom - old_bottom
set_y('bg98', A['bg98']['y'], A['bg98']['h'] + d)
for i in ('bg99', 'bg100'): set_y(i, A[i]['y'] + d)
open(f, 'w', encoding='utf-8').write(s)
print('panel grew', d)
