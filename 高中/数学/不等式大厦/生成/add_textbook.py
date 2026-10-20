"""对照新教材（人教 B 版 7 册）和老教材（代数上下册目录 + 下册第五章）后的补充（v40 → v41）。不新增节点。
需要改的：解不等式入口补三角不等式；S06 归纳起点改为 n₀；P29 区分均值不等式（a,b>0）与基本不等式（a,b≥0）；
          R36 补 n 项形式和 |a−b| ≤ |a|+|b|。
顺带补的：P31 补 x<0；R27 补复数模；P29 补半圆几何意义；R15 补平方去绝对值；P19 补有理数指数、奇次幂。
用法：cp outputs/inequality-tree-v40.drawio outputs/inequality-tree-v41.drawio
      python3 生成/add_textbook.py outputs/inequality-tree-v41.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v41.drawio"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')


def tex(s):
    out = convert_label(html.escape(s, quote=False), [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


def small(s):
    return '<span style="font-size:10px;color:#607D8B;font-weight:normal;">%s</span>' % s


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if '2k\\pi' in byid['ent_solve'].get('label'):
    sys.exit('已修改过，跳过')

# (元素 id, 原片段, 新片段, 加高, 加宽)
EDITS = [
    ('ent_solve', '<br>不等式组：',
     '<br>三角：用三角函数线或图象，先在一个周期内找出范围，再加周期（sin、cos 加 2kπ，tan 加 kπ），如 '
     + tex('sin x ≥ 1/2 ⟺ π/6 + 2kπ ≤ x ≤ 5π/6 + 2kπ') + '（\\({k\\in \\mathbb{Z}}\\)）<br>不等式组：', 36, 0),
    ('ax_induction', 'P(1)成立 且 \\({P(k)\\Rightarrow P(k+1)}\\)<br>⇒ 对所有正整数 n 成立',
     tex('P(n₀) 成立，且 k ≥ n₀ 时 P(k) ⇒ P(k+1)') + '<br>⇒ 对所有 ' + tex('n ≥ n₀') + ' 的正整数 n 成立（'
     + tex('n₀') + ' 不一定是 1，如证 ' + tex('n ≥ 5 时 2ⁿ > n²') + '）', 0, 0),
    ('am', '★★ 基本不等式（人教 B 版称均值不等式）', '★★ 基本不等式 / 均值不等式'),
    ('am', '\\({a,b \\ge  0}\\)；等号 \\({\\iff  a=b}\\)',
     '\\({a,b \\ge  0}\\)；等号 \\({\\iff  a=b}\\)<br>' + small('人教 B 版：均值不等式要求 a、b 都是正数；基本不等式中 a、b 还可以为 0')
     + '<br>' + small('几何意义：半圆直径被分成 a、b 两段，' + tex('半弦 √(ab) ≤ 半径 (a+b)/2')), 50, 0),
    ('triangle', '等号 \\({\\iff  ab \\ge  0}\\)',
     '等号 \\({\\iff  ab \\ge  0}\\)<br>b 换成 −b：' + tex('|a−b| ≤ |a| + |b|')
     + '<br>推广到 n 项：<br>\\({|a_{1}+\\cdots +a_{n}| \\le  |a_{1}|+\\cdots +|a_{n}|}\\)', 54, 90),
    ('recip_sum', '等号 \\({\\iff  x=1}\\)',
     '等号 \\({\\iff  x=1}\\)<br>' + tex('x < 0 时：x + 1/x ≤ −2') + '（对 ' + tex('−x > 0') + ' 用上式）<br>合起来：'
     + tex('|x + 1/x| ≥ 2（x ≠ 0）'), 120, 0),
    ('vec_tri', '<br>坐标形式（闵可夫斯基）',
     '<br>复数同理：' + tex('||z₁|−|z₂|| ≤ |z₁ ± z₂| ≤ |z₁| + |z₂|') + '<br>坐标形式（闵可夫斯基）', 20, 0),
    ('abs_solve', '<br>多个绝对值：',
     '<br>两边都非负可平方：' + tex('|x| < a ⟺ x² < a²') + '〔P03 · A1〕<br>多个绝对值：', 20, 0),
    ('pow_mono', '\\({a\\gt b\\ge 0}\\)；n 为正整数\xa0</span>', '\\({a\\gt b\\ge 0}\\)；奇次幂见末行\xa0</span>'),
    ('pow_mono', '（n 为正整数）',
     '（n 为正整数）<br>推广：s 为正有理数时 \\({a^{s} \\gt  b^{s}}\\)<br>奇次幂对任意实数保序：' + tex('a > b ⟺ a³ > b³'), 70, 0),
]
for e in EDITS:
    eid, a, b = e[:3]
    dh, dw = (e[3], e[4]) if len(e) > 3 else (0, 0)
    side = e[5] if len(e) > 5 else 'both'
    el = byid[eid]
    lab = el.get('label')
    assert lab.count(a) == 1, (eid, a[:40])
    el.set('label', lab.replace(a, b))
    g = el.find('mxCell').find('mxGeometry')
    if eid == 'ent_solve':   # 入口一栏：本卡加高，下方整体下移
        y0 = float(g.get('y'))
        g.set('height', '%g' % (float(g.get('height')) + dh))
        for o in root:
            c = o if o.tag == 'mxCell' else o.find('mxCell')
            if c is None or c.get('vertex') != '1':
                continue
            og = c.find('mxGeometry')
            if og is not None and og.get('relative') != '1' and float(og.get('x', 0)) == -840 and float(og.get('y', 0)) > y0:
                og.set('y', '%g' % (float(og.get('y')) + dh))
        continue
    g.set('height', '%g' % (float(g.get('height')) + dh)); g.set('y', '%g' % (float(g.get('y')) - dh / 2))
    g.set('width', '%g' % (float(g.get('width')) + dw))
    if side == 'both':   # 左右各扩一半；'right' 只向右扩
        g.set('x', '%g' % (float(g.get('x')) - dw / 2))
byid['pow_mono'].set('适用范围', 'a>b≥0；奇次幂任意实数')
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done', len(EDITS))
