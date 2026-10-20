"""教材核对的补充第二批（v41 → v42）。不新增节点。
P26 补二项式放缩（多保留一项）；S01 补"虚数不能比较大小"；解不等式入口补一次不等式 ax > b 的分类。
用法：cp outputs/inequality-tree-v41.drawio outputs/inequality-tree-v42.drawio
      python3 生成/add_textbook2.py outputs/inequality-tree-v42.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v42.drawio"""
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
if '虚数' in byid['ax_order'].get('label'):
    sys.exit('已修改过，跳过')

# (元素 id, 原片段, 新片段, 加高)
EDITS = [
    ('bernoulli', '等号 \\({\\iff  x=0}\\) 或 \\({n=1}\\)',
     '等号 \\({\\iff  x=0}\\) 或 \\({n=1}\\)<br>二项式放缩（多留一项，' + tex('x ≥ 0') + '）：<br>'
     + tex('(1+x)ⁿ ≥ 1 + nx + n(n−1)x²/2') + '，比伯努利更紧', 56),
    ('ax_order', '（两者都表示 \\({a - b}\\) 是正数）',
     '（两者都表示 ' + tex('a − b') + ' 是正数）<br>边界：大小只对实数规定；虚数之间不能比较大小', 17),
    ('ent_solve', '<b>看到 解不等式（求解集）</b><br>',
     '<b>看到 解不等式（求解集）</b><br>一次：' + tex('ax > b') + '，' + tex('a > 0') + ' 时 ' + tex('x > b/a') + '；'
     + tex('a < 0') + ' 时 ' + tex('x < b/a') + '（不等号反向）；' + tex('a = 0') + ' 时看 b：' + tex('b < 0')
     + ' 解集为 ℝ，' + tex('b ≥ 0') + ' 无解<br>', 46),
]
for eid, a, b, dh in EDITS:
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
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done', len(EDITS))
