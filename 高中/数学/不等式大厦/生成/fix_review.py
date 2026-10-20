"""按 v37 内容审查结果修正（v37 → v38）。
用法：cp outputs/inequality-tree-v37.drawio outputs/inequality-tree-v38.drawio
      python3 生成/fix_review.py outputs/inequality-tree-v38.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v38.drawio
每处修改都写成"原片段 → 新片段"，原片段必须在该元素标签里恰好出现一次。
改完按估算的行数加高：主图节点上下各扩一半；题型入口一栏、工具箱两栏按原间距重排。"""
import html, math, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')
RED_BADGE = '<span style="background-color:#E65100;color:#FFFFFF;font-size:10px;font-weight:bold;">\xa0%s\xa0</span> '


def tex(s):
    t = html.escape(s, quote=False)
    out = convert_label(t, [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


def ref(text, num):
    return '<span style="color:#004D40;">▸ %s <b>〔%s · A1〕</b></span>' % (tex(text), num)


# (元素 id, 原片段, 新片段)
EDITS = [
    # 一、错误
    ('high_ineq', '如 \\({x^{3}-1 = (x-1)(x^{2}+x+1) x^{2}+x+1 \\gt  0}\\) 恒成立',
     '如 ' + tex('x³−1 = (x−1)(x²+x+1)，其中 x²+x+1 > 0 恒成立')),
    ('ent_adv', ' <b>〔P51 · ', ' ' + tex('（x ≥ 0；x < 0 时反向）') + ' <b>〔P51 · '),
    ('ent_adv', ' <b>〔P53 · ', ' ' + tex('（x ≥ 0；−1 < x ≤ 0 时反向）') + ' <b>〔P53 · '),
    ('ent_cmp', ' <b>〔P27 · ', tex('（a+b ≥ 0）') + ' <b>〔P27 · '),
    # 二、缺前提
    ('qall', '（\\({a\\gt 0}\\)）</div>',
     '（\\({a\\gt 0}\\)）<br>' + tex('恒 > 0 ⟺ Δ < 0；二次项系数含参时，先讨论它是否为 0') + '</div>'),
    ('three_two', '\\({f(x)\\lt 0}\\) 无解<br>\\({\\Delta \\lt 0}\\)',
     '\\({f(x)\\lt 0}\\) 无解；' + tex('f(x) ≥ 0 对一切 x 成立，f(x) ≤ 0 仅在 x = −b/(2a) 处成立') + '<br>\\({\\Delta \\lt 0}\\)'),
    ('three_two', '<br><span style="font-size:10px;color:#1565C0;',
     '<br>' + tex('不等号带等号（≥、≤）时，解集要把根也算进去') + '<br><span style="font-size:10px;color:#1565C0;'),
    ('delta_range', 'x 有实数解 \\({\\Rightarrow  \\Delta \\ge 0}\\)',
     tex('x 有实数解 ⟺ Δ ≥ 0（二次项系数 ≠ 0）')),
    ('delta_range', '（\\({g(x)\\ne 0}\\)）</div>',
     '（\\({g(x)\\ne 0}\\)）<br>' + tex('③ x 被限制在某个区间内（如换元后 t > 0）时，Δ ≥ 0 不够，改用根的分布') + '〔R44 · A1〕</div>'),
    ('solve_quad', '依次讨论二次项系数的符号', '依次讨论二次项系数是否为 0 及其正负'),
    ('frac_ineq', '<div style="text-align:left">',
     '<div style="text-align:left">' + tex('先移项通分，化成 f(x)/g(x) 与 0 比较，不能直接乘分母') + '<br>'),
    ('ent_solve', '已知解集反求系数：',
     '已知解集反求系数：' + tex('先由解集形状定二次项系数的符号（如 > 0 的解集在两根之间 ⇒ a < 0）；')),
    # 三、名字、连线标签、配合、索引、工具箱、标签
    ('sin_tan', '常用三角不等式（单位圆面积比较）', '常用三角不等式（也可用单位圆面积比较）'),
    ('e26', '代入配方结果', '代入 R17 的配方结果'),
    ('p2e0', '之间在下方', '之间在下方<br>' + tex('【等价变形】Δ ≤ 0：最小值 −Δ/(4a) ≥ 0，Δ = 0 时只有顶点处等于 0')),
    ('e113', '方程 \\({f(x)=0}\\) 有实数解', '二次方程 \\({h(x)=0}\\) 有实数解'),
    ('e11', '\\gt  0}\\)</span>', '\\gt  0}\\)</span>' + tex('（b−a > 0，ab > 0）')),
    ('p2e11', '\\gt  0}\\)</span>', '\\gt  0}\\)</span>' + tex('（分子、分母都是正数之积）')),
    ('p2e27', '再取倒数得', '再取倒数（正数倒数反序〔P17 · A1〕）得'),
    ('s1e3', '(a-b)c + b(c-d) \\ge  0}\\)', '(a-b)c + b(c-d) \\ge  0}\\)（两项都是非负数之积）'),
    ('f_sq_diff', '；排序不等式（两数）的展开步', ''),
    ('am_n', '<br><span style="font-size:10px;color:#607D8B;font-weight:normal;">⋯ 配合：㊴ 前 n 项立方和——n 元均值题中处理立方和时常用</span>', ''),
    ('f_sum_cube', '<br><span style="font-size:10px;color:#607D8B;font-weight:normal;">⋯ 配合：n 元均值不等式</span>', ''),
    ('bernoulli', '<br><span style="font-size:10px;color:#607D8B;font-weight:normal;">⋯ 配合：㊳ 前 n 项平方和——数列放缩题中常与伯努利不等式一起用于估计和</span>', ''),
    ('f_derivrule', '正整数 n 另含 \\({x\\le 0}\\)）<br>',
     '正整数 n 另含 \\({x\\le 0}\\)）<br>' + tex('(sin x)′ = cos x；(cos x)′ = −sin x') + '<br>'),
    ('abs_solve', '<div style="text-align:center"><span style="font-size:10px;color:#78909C;',
     '<div style="text-align:center">' + RED_BADGE % '\\({a\\gt 0}\\)' + '<span style="font-size:10px;color:#78909C;'),
    ('root_dist', '\xa0\\({a\\gt 0}\\)\xa0</span>', '\xa0\\({x\\in \\mathbb{R}}\\)；\\({a\\gt 0}\\)\xa0</span>'),
    ('ent_prod', '<span style="color:#004D40;">▸ n 个数时',
     ref('三个因子 (a+b)(b+c)(c+a) → 三次基本不等式相乘', 'P34') + '<br><span style="color:#004D40;">▸ n 个数时'),
    ('ent_frac', '\\dfrac{u^{2}}{x} + \\dfrac{v^{2}}{y}', '\\dfrac{r^{2}}{u} + \\dfrac{s^{2}}{v}'),
    ('ent_frac', '\\dfrac{u}{x} = \\dfrac{v}{y}', '\\dfrac{r}{u} = \\dfrac{s}{v}'),
    ('c2', ' 后展开）', '）'),
    # 五、导数压轴补隐零点、指对同构（补进原入口）
    ('ent_adv', '<span style="color:#00695C;font-weight:bold;">去这里查：</span>',
     tex('隐零点：f′(x₀) = 0 解不出 x₀ 时设而不求，用 f′(x₀) = 0 把 e^{x₀}、ln x₀ 换成 x₀ 的代数式，再代回 f(x₀) 化简') + '<br>'
     + tex('指对同构：如 xeˣ = e^{x+ln x}、x + ln x = ln(xeˣ)，把两边化成同一个函数 g 的形式，再用 g 的单调性比较') + '<br>'
     + '<span style="color:#00695C;font-weight:bold;">去这里查：</span>'),
]
ATTRS = {'abs_solve': {'适用范围': 'a>0'}, 'root_dist': {'适用范围': 'x∈ℝ；a>0'}}


def fix_index(s):
    """方法索引：放缩补 P13、P21；换元去掉只是代入的 R61、P30、P43；构造函数说明补判别式。"""
    def edit(name, add=(), drop=()):
        nonlocal s
        m = re.search(r'(<b>%s</b>（)(\d+)( 处）[^<]*<br><span[^>]*>)(.*?)(</span>)' % re.escape(name), s)
        items = [i for i in m.group(4).split('、') if i.split('〔')[0] not in drop] + ['%s〔A1〕' % a for a in add]
        items.sort()
        s = s[:m.start()] + m.group(1) + str(len(items)) + m.group(3) + '、'.join(items) + m.group(5) + s[m.end():]
    edit('放缩', add=('P13', 'P21'))
    edit('换元 / 代换', drop=('R61', 'P30', 'P43'))
    s = s.replace('构造函数，用导数判单调、求最值', '构造函数，用导数判单调、求最值（R42 是构造二次式，用判别式）')
    return s


def est(lab, width):
    """估算标签高度：按 <br>/div 分行，按可见字宽折行；10px 字号行高 14，其余 17；含分式的行再加 20。"""
    h = 0
    for line in re.split(r'<br>|</div>', lab):
        small = 'font-size:10px' in line
        text = re.sub(r'\\\((.*?)\\\)', lambda m: 'x' * max(1, len(re.sub(r'\\[a-z]+|[{}_^ ]', '', m.group(1)))), line, flags=re.S)
        text = re.sub(r'<[^>]+>', '', text)
        if not text.strip():
            continue
        cw = 10 if small else 13
        w = sum(cw if ord(ch) > 255 else cw * 0.55 for ch in text)
        rows = max(1, math.ceil(w / max(60, width - 24)))
        h += rows * (14 if small else 17) + (20 if 'dfrac' in line else 0)
    return h


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}


def attr(el):
    return 'label' if el.tag == 'UserObject' else 'value'


def geom(el):
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    return c, c.find('mxGeometry')


old_lab = {}
for eid, old, new in EDITS:
    el = byid[eid]
    lab = el.get(attr(el))
    old_lab.setdefault(eid, lab)
    assert lab.count(old) == 1, (eid, old[:50], lab.count(old))
    el.set(attr(el), lab.replace(old, new))
for eid, kv in ATTRS.items():
    for k, v in kv.items():
        byid[eid].set(k, v)
bg100 = byid['bg100']
old_lab['bg100'] = bg100.get('value')
bg100.set('value', fix_index(bg100.get('value')))

# 全图"均值代换"改名"和积代换"（R52 实际是令 a+b=s、ab=p）
for el in root:
    a = attr(el)
    if el.get(a) and '均值代换' in el.get(a):
        old_lab.setdefault(el.get('id'), el.get(a))
        el.set(a, el.get(a).replace('均值代换', '和积代换'))

# 估算加高
grow = {}
for eid, old in old_lab.items():
    el = byid[eid]
    c, g = geom(el)
    if c.get('vertex') != '1' or g is None or g.get('relative') == '1':
        continue
    d = est(el.get(attr(el)), float(g.get('width'))) - est(old, float(g.get('width')))
    if d > 0:
        grow[eid] = d


def restack(ids_sorted):
    shift = 0
    for el in ids_sorted:
        _, g = geom(el)
        g.set('y', '%g' % (float(g.get('y')) + shift))
        d = grow.pop(el.get('id'), 0)
        if d:
            g.set('height', '%g' % (float(g.get('height')) + d))
            shift += d
    return shift


def column(x, pred):
    out = []
    for el in root:
        c, g = geom(el) if (el.tag == 'mxCell' or el.find('mxCell') is not None) else (None, None)
        if g is None or g.get('relative') == '1' or c.get('vertex') != '1':
            continue
        if float(g.get('x', 0)) == x and pred(el, g):
            out.append(el)
    return sorted(out, key=lambda e: float(geom(e)[1].get('y')))


# 题型入口一栏（含分组标题）
restack(column(-840, lambda el, g: float(g.get('y')) > 0))
# 工具箱两栏，面板背景随最高一栏加高，方法索引下移
bottoms = []
for x in (-1780, -1390):
    col = column(x, lambda el, g: el.get('id', '').startswith('f_'))
    restack(col)
    _, g = geom(col[-1]); bottoms.append(float(g.get('y')) + float(g.get('height')))
_, gp = geom(byid['bg98'])
d = max(0, max(bottoms) + 20 - (float(gp.get('y')) + float(gp.get('height'))))
gp.set('height', '%g' % (float(gp.get('height')) + d))
for b in ('bg99', 'bg100'):
    _, g = geom(byid[b]); g.set('y', '%g' % (float(g.get('y')) + d))
# 方法索引自身
if 'bg100' in grow:
    _, g = geom(bg100); g.set('height', '%g' % (float(g.get('height')) + grow.pop('bg100')))
# 主图节点：上下各扩一半
for eid, dd in grow.items():
    _, g = geom(byid[eid])
    g.set('height', '%g' % (float(g.get('height')) + dd))
    g.set('y', '%g' % (float(g.get('y')) - dd / 2))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('edited', len(EDITS), 'main-graph nodes grown', grow, 'toolbox panel +%g' % d)
