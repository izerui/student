"""② 工具箱：把常用公式卡的"⇒ 用于：编号"改成"▸ 用在什么问题、怎么用〔编号 · 坐标〕"（v36 → v37）。
在原卡片里改，不新增块。卡片加高后两栏重新排位，面板背景加高，下方"方法索引"随之下移。
用法：cp outputs/inequality-tree-v36.drawio outputs/inequality-tree-v37.drawio
      python3 生成/tool_uses.py outputs/inequality-tree-v37.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v37.drawio"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
COLS = (-1780, -1390)              # 工具箱两栏的 x
PANEL, BELOW = 'bg98', ('bg99', 'bg100')

USES = {
    'f_sq_diff': [
        ('作差比大小：b²−a² 拆成 (b+a)(b−a)，两个因式分别定号', 'P03'),
        ('根式裂项：(√k+√(k−1))(√k−√(k−1)) = 1，分子有理化', 'P25'),
    ],
    'f_sq_complete': [
        ('证明的起点：展开 (a−b)² ≥ 0 得 a²+b² ≥ 2ab；柯西推导中展开 (ad−bc)² ≥ 0', 'R37 R49'),
        ('反过来用就是配方：凑成 (…)² + 常数，判正负、求二次函数最值', 'R17'),
    ],
    'f_cube_sum': [
        ('作差后分解定号：a³+b³−ab(a+b) = (a+b)(a−b)²', 'P27'),
    ],
    'f_cube_diff': [
        ('高次不等式先分解：x³−1 = (x−1)(x²+x+1)，后一个因式恒正，可约去', 'R25'),
    ],
    'f_sym_sq': [
        ('已知 a+b、ab，求 a²+b²：均值代换 s、p', 'R52'),
        ('比较平方和与和的平方：2(a²+b²) ≥ (a+b)²', 'R60'),
    ],
    'f_vieta': [
        ('已知解集反求系数：解集端点就是两根，用两根之和、之积列方程', 'R34'),
        ('对称式 a+b、ab：把 a、b 看成 t²−st+p=0 的两根，实根要求 s² ≥ 4p', 'R52'),
    ],
    'f_log_rules': [
        ('对数放缩求和：ln(1+1/k) = ln(k+1) − ln k，逐项相消', 'P21'),
        ('对数平均：ln a − ln b = ln(a/b)，令 t = a/b 化成单变量', 'P07'),
        ('指数、对数不等式：先化成同底，再用单调性', 'P04'),
    ],
    'f_pyth': [
        ('正余弦有界：sin²θ = 1 − cos²θ ≤ 1', 'R01'),
        ('三角有界：配合柯西或 a²+b² ≥ 2ab，用 sin²θ+cos²θ = 1 化成常数', 'R03 R02'),
    ],
    'f_aux': [
        ('求 a sinθ + b cosθ 的最值或范围：化成 √(a²+b²)·sin(θ+φ)，再用 |sin| ≤ 1', 'R13'),
    ],
    'f_derivrule': [
        ('构造函数：看到 f′+f 想 (eˣf)′，看到 xf′−f 想 (f/x)′，凑成积或商的导数', 'P05'),
        ('对构造的函数求导，看导数正负判单调、求最值', 'S04'),
    ],
}

USED = re.compile(r'(<span style="font-size:10px;color:#1565C0;font-weight:normal;">)?⇒ 用于：[^<]*(</span>)?')
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')
SPAN = '<span style="font-size:10px;color:#1565C0;font-weight:normal;">%s</span>'


def line_html(text, ids):
    t = convert_label(html.escape(text, quote=False), [])
    t = DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', t)
    refs = ''.join('〔%s · A1〕' % i for i in ids.split())
    return SPAN % ('▸ 用在 ' + t + ' ' + refs)


def est_height(text):
    """10px 字号、卡片宽 350：约 30 个汉字一行，每行 14px；含分式的行 30px。"""
    t = convert_label(html.escape(text, quote=False), [])
    w = sum(1 if ord(ch) > 255 else 0.55 for ch in re.sub(r'\\\((.*?)\\\)', lambda m: 'x' * (len(m.group(1)) // 4), text))
    rows = max(1, -(-int(w + 8) // 30))
    return rows * (30 if 'dfrac' in t else 14)


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}


def geom(el):
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    return c.find('mxGeometry')


grow = {}
for cid, uses in USES.items():
    el = byid[cid]
    lab = el.get('label')
    if '▸ 用在' in lab:
        continue
    m = USED.search(lab)
    assert m, cid
    new = '<br>'.join(line_html(t, i) for t, i in uses)
    el.set('label', lab[:m.start()] + new + lab[m.end():])
    grow[cid] = sum(est_height(t) for t, _ in uses) - 14
    g = geom(el)
    g.set('height', '%g' % (float(g.get('height')) + grow[cid]))

# 两栏各自按原顺序、原间距重排
bottoms = []
for x in COLS:
    col = sorted((el for el in root if el.get('id', '').startswith('f_') and float(geom(el).get('x')) == x),
                 key=lambda e: float(geom(e).get('y')))
    shift = 0
    for el in col:
        g = geom(el)
        old_h = float(g.get('height')) - grow.get(el.get('id'), 0)
        g.set('y', '%g' % (float(g.get('y')) + shift))
        shift += grow.get(el.get('id'), 0)
    last = geom(col[-1])
    bottoms.append(float(last.get('y')) + float(last.get('height')))

gp = geom(byid[PANEL])
old_bottom = float(gp.get('y')) + float(gp.get('height'))
new_bottom = max(max(bottoms) + 20, old_bottom)
d = new_bottom - old_bottom
gp.set('height', '%g' % (float(gp.get('height')) + d))
for b in BELOW:
    g = geom(byid[b]); g.set('y', '%g' % (float(g.get('y')) + d))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('grown', grow, 'panel +%g' % d)
