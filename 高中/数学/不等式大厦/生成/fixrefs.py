import re, sys, xml.etree.ElementTree as ET
F = sys.argv[1]
s = open(F, encoding='utf-8').read()
# 删除已不存在节点的方法索引条目并更新计数
def fix_list(name, remove):
    global s
    pat = re.compile(r'(&lt;b&gt;%s&lt;/b&gt;（)(\d+)( 处）.*?&lt;span .*?&gt;)(.*?)(&lt;/span&gt;)' % re.escape(name), re.S)
    m = pat.search(s)
    if m is None:   # v44 起方法索引改为方法卡，没有这类条目
        return
    items = [i for i in m.group(4).split('、') if not any(i.startswith(r + '〔') for r in remove)]
    s = s[:m.start()] + m.group(1) + str(len(items)) + m.group(3) + '、'.join(items) + m.group(5) + s[m.end():]
fix_list('换元 / 代换', ['R18', 'R20', 'R21'])
fix_list('分类讨论', ['R08'])
s = s.replace('▸ 作差 → 作差判大小 &lt;b&gt;〔R18 · H1〕', '▸ 作差 → 实数大小（作差法的依据） &lt;b&gt;〔S01 · H1〕')
# 重算所有网格坐标引用
r = ET.fromstring(s.encode('utf-8')).find('.//root')
pos = {}
for el in r:
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    if el.get('编号') and c is not None:
        g = c.find('mxGeometry'); x, y, w, h = (float(g.get(k, 0)) for k in ('x', 'y', 'width', 'height'))
        pos[el.get('编号')] = 'ABCDEFGHJKLMN'[int((x + w / 2 + 80) // 1165)] + str(int((y + h / 2 + 80) // 1116) + 1)
changed = set(); missing = set()
def rep(m):
    i = m.group(1)
    if i not in pos: missing.add(i); return m.group(0)
    if pos[i] != m.group(3): changed.add((i, m.group(3), pos[i]))
    return i + m.group(2) + pos[i]
s = re.sub(r'\b([PRS]\d\d)(〔| · )([A-N]\d)', rep, s)
open(F, 'w', encoding='utf-8').write(s)
print('changed', sorted(changed)); print('missing', missing)
