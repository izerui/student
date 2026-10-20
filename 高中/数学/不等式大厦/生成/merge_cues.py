"""把"看到什么 → 用哪个"中原入口缺的内容补进已有的题型入口（v35 → v36），不新增面板。
用法：cp outputs/inequality-tree-v35.drawio outputs/inequality-tree-v36.drawio
      python3 生成/merge_cues.py outputs/inequality-tree-v36.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v36.drawio
入口加高后，同一栏（x=-840）下方的入口和分组标题整体下移，间距不变。"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
COL_X = -840

DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')


def tex(s):
    """Unicode 文本（可含 <b></b>）→ 带 LaTeX 的 HTML。"""
    t = html.escape(s, quote=False).replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    out = convert_label(t, [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


def ref_line(text, ref):
    return '<span style="color:#004D40;">▸ %s <b>〔%s · A1〕</b></span>' % (tex(text), ref)


# 每项：(入口 id, 原片段, 新片段)。原片段必须在标签里恰好出现一次。
EDITS = [
    ('ent_solve',
     '二次：化成二次项系数 \\({\\gt 0 \\to}\\) 三个二次的关系；含参按系数、Δ、根的大小分类<br>'
     '分式：移项通分 → 化成整式（乘积）→ 穿根法，注意分母 \\({\\ne  0}\\)<br>',
     tex('二次：化成二次项系数 > 0 → 能分解先用<b>十字相乘</b>求根，如 x²−5x+6=(x−2)(x−3)；分解不出就算 <b>Δ</b> → 三个二次的关系') + '<br>'
     + tex('含参二次：先试十字相乘，如 x²−(a+1)x+a=(x−a)(x−1)，再按两根 a、1 的大小分类；二次项系数含参时先讨论它是否为 0') + '<br>'
     + tex('分式、高次：移项通分 → <b>因式分解</b>成一次因式的乘积 → <b>穿根法</b>，注意分母 ≠ 0') + '<br>'),
    ('ent_solve',
     '不等式组：分别解出再取交集；“或”取并集；最后用集合或区间写出解集<br>',
     '不等式组：分别解出再取交集；“或”取并集；最后用集合或区间写出解集<br>'
     + tex('已知解集反求系数：解集端点就是方程的根 → 写成 a(x−x₁)(x−x₂) 展开比较系数，或用<b>韦达定理</b>（左侧工具箱 ⑫）') + '<br>'),
    ('ent_cmp',
     '首选作差：\\({a-b}\\) 与 0 比较；',
     tex('首选作差：a−b 与 0 比较，差再用<b>因式分解</b>或<b>配方</b>定正负，如 a³+b³−ab(a+b)=(a+b)(a−b)²') + '<br>'),
    ('ent_cmp',
     '<span style="color:#004D40;">▸ 作商 → 作商法',
     ref_line('作差后分解 → a³+b³ ≥ ab(a+b)', 'P27') + '<br><span style="color:#004D40;">▸ 作商 → 作商法'),
    ('ent_seq',
     '<span style="color:#00695C;font-weight:bold;">去这里查：</span><br>',
     '<span style="color:#00695C;font-weight:bold;">去这里查：</span><br>'
     + ref_line('和 n 有关、要一步步推到 n+1 → 【工具】数学归纳法', 'S06') + '<br>'),
]


def extra_height(old, new):
    """按新增的行数估算加高：每行按可见字数折行（约 40 个汉字宽一行），普通行 17px，含分式的行 38px。"""
    def width(line):
        t = re.sub(r'\\\((.*?)\\\)', lambda m: 'x' * (len(m.group(1)) // 4), line)
        t = re.sub(r'<[^>]+>', '', t)
        return sum(1 if ord(ch) > 255 else 0.55 for ch in t)
    def h(s):
        return sum((38 if 'dfrac' in line else 17) * max(1, -(-int(width(line)) // 40))
                   for line in re.split(r'<br>', s) if line)
    return max(0, h(new) - h(old))


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
grow = {}
for eid, old, new in EDITS:
    el = byid[eid]
    lab = el.get('label')
    assert lab.count(old) == 1, (eid, old[:40], lab.count(old))
    el.set('label', lab.replace(old, new))
    grow[eid] = grow.get(eid, 0) + extra_height(old, new)


def geom(el):
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    return c.find('mxGeometry') if c is not None else None


# 入口一栏（含 bg 层的分组标题）按原顺序重排：加高的入口向下撑开，下方整体下移
col = []
for el in root:
    g = geom(el)
    if g is not None and g.get('relative') != '1' and float(g.get('x', 0)) == COL_X and float(g.get('y', 0)) > 0:
        col.append((float(g.get('y')), el))
col.sort(key=lambda t: t[0])
shift = 0
for y, el in col:
    g = geom(el)
    g.set('y', '%g' % (y + shift))
    d = grow.get(el.get('id'), 0)
    if d:
        g.set('height', '%g' % (float(g.get('height')) + d))
        shift += d
tree.write(F, encoding='utf-8', xml_declaration=True)
print('grown', grow, 'column shifted by', shift)
