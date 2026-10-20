"""按"工具 = 能写成公式；方法 = 运算逻辑、变换方式，本身不是公式"再统一一次（v45 → v46）。
1. 推导线：展开、提公因式、因式分解、分母有理化、合并整理恢复为方法，新设【恒等变形】（变式子，用 =），
   与【等价变形】（变不等式，用 ⟺）区分；平方非负、同号相乘、逐项相加等是在套公式，改写为"由 工具名〔编号〕："。
   标签从 v43 的原文按新规则重新生成，再补上 v45 的"判单调"改动。
2. 节点标题用方法名、内容是公式的，改用公式命名（P11 R33 R52 P05 P08 R15 P56 P48），各处引用同步。
3. 写不成一个公式、是几种方法配合的流程（R43 R25 R72 R74）加棕色"解法"标记。
4. S04 类型【工具】→【定理】，S06 →【公理】；图例同步。方法卡加【恒等变形】，共 12 类。
用法：cp outputs/inequality-tree-v45.drawio outputs/inequality-tree-v46.drawio
      python3 生成/methods3.py outputs/inequality-tree-v46.drawio outputs/inequality-tree-v43.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v46.drawio"""
import os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

F, OLD = sys.argv[1], sys.argv[2]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'methods.py'), encoding='utf-8').read()
# 只取 methods.py 里的映射表和 relabel 函数，不执行它的改图部分
ns = {'re': re, 'tex': None}
exec(src[src.index('# 原标签 →'):src.index('tree = ET.parse(F)')], ns)
METHOD, OPERATION, relabel = ns['METHOD'], ns['OPERATION'], ns['relabel']
for k in ('展开法', '提公因式', '因式分解', '分母有理化', '合并整理'):
    METHOD[k] = ('恒等变形', {'展开法': '展开'}.get(k, k))
    OPERATION.pop(k)
TOOLREF = {'平方非负': '由平方非负〔R28 · A1〕', '同号相乘': '由正 × 正 = 正（有因子为 0 则积为 0）〔S02 · A1〕',
           '同向相乘': '由同向正数可乘〔P10 · A1〕', '逐项相乘': '由同向正数可乘〔P10 · A1〕',
           '逐项相加': '由同向可加〔R07 · A1〕', '绝对值界': '由 −|x| ≤ x ≤ |x|〔R09 · A1〕',
           '判别式': '由恒非负条件 Δ ≤ 0〔R30 · A1〕'}
for k, v in TOOLREF.items():
    OPERATION[k] = v
ns['plain_start'] = lambda rest, word: (not word.startswith('由')) and re.sub(r'<[^>]+>', '', rest).lstrip().startswith(word[:2])

tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
old = {el.get('id'): el for el in ET.parse(OLD).getroot().find('.//root')}
if '【恒等变形】' in open(F, encoding='utf-8').read():
    sys.exit('已修改过，跳过')


def attr(el):
    return 'label' if el.tag == 'UserObject' else 'value'


# 1. 推导线标签重新生成
unknown, n = set(), 0
for eid, el in byid.items():
    o = old.get(eid)
    if o is None or eid.startswith('lg') or eid.startswith('bg'):
        continue
    ol = o.get(attr(o)) or ''
    if '【' not in ol:
        continue
    new = relabel(ol, unknown)
    if eid in ('e132', 'e133'):
        new = new.replace('【分类讨论】', '判单调：', 1)
    cur = el.get(attr(el))
    if eid.startswith('ent_'):
        continue   # 入口卡 v43 之后另有改动，且不含受影响的标签
    if new != cur:
        el.set(attr(el), new); n += 1
assert not unknown, unknown

# 2. 节点改名（节点标题 + 各处引用）
RENAME = [
    ('P11', '★ 作商法（', '★ 商与 1 比较（'),
    ('R33', '★ 判别式法求范围', '★ 有实数解 ⟺ Δ ≥ 0（判别式求范围）'),
    ('R52', '★ 和积代换', '★ 和与积的关系'),
    ('P05', '★ 构造函数（抽象函数；', '★ 积、商的导数定号（抽象函数；'),
    ('P08', '★ 构造 ', '★ 函数 '),
    ('P08', '比大小（\\({x\\gt 0}\\)）</div>', '的单调性（\\({x\\gt 0}\\)）</div>'),
    ('R15', '★ 绝对值不等式的解法（', '★ 绝对值不等式的等价形式（'),
    ('P56', '★ 根式（无理）不等式的解法', '★ 根式（无理）不等式的等价形式'),
    ('P48', '★ 奇偶性 + 单调性解不等式', '★ 奇偶性 + 单调性的等价转化'),
]
REFS = [
    ('ent_cmp', '▸ 作商 → 作商法（', '▸ 作商 → 商与 1 比较（'),
    ('ent_para', '→ 判别式法求范围 <b>〔', '→ 有实数解 ⟺ Δ ≥ 0（判别式求范围） <b>〔'),
    ('ent_homo', '→ 判别式法求范围 <b>〔', '→ 有实数解 ⟺ Δ ≥ 0（判别式求范围） <b>〔'),
    ('ent_sym', '▸ 和积代换 <b>〔', '▸ 和积代换 → 和与积的关系 <b>〔'),
    ('ent_multi', '→ 和积代换 <b>〔', '→ 和与积的关系 <b>〔'),
    ('ent_adv', '→ 构造函数（抽象函数） <b>〔', '→ 积、商的导数定号（抽象函数） <b>〔'),
    ('ent_absfn', '→ 构造函数（抽象函数） <b>〔', '→ 积、商的导数定号（抽象函数） <b>〔'),
    ('ent_solve', '→ 绝对值不等式的解法（', '→ 绝对值不等式的等价形式（'),
    ('ent_solve', '→ 根式（无理）不等式的解法 <b>〔', '→ 根式（无理）不等式的等价形式 <b>〔'),
    ('ent_absfn', '→ 奇偶性 + 单调性解不等式 <b>〔', '→ 奇偶性 + 单调性的等价转化 <b>〔'),
    # 类型标签
    ('S04', '【工具】导数判单调', '【定理】导数判单调'),
    ('S06', '【工具】数学归纳法', '【公理】数学归纳法'),
    ('lg2', '【公理】【定义】【工具】', '【公理】【定义】【定理】'),
    ('lg12', '① 公式与工具', '工具箱公式'),
    ('lg13', '蓝色：推导中用到的公式（只作工具，不画线）', '蓝色：借用的公式（也是工具），不画线'),
    ('lg23', '共 11 类', '共 12 类'),
    ('lg20', '高考常用的结论或方法', '高考常用的结论或方法；棕色“解法”：几种方法配合工具的解题流程，写不成一个公式'),
]
num = {el.get('编号'): el for el in root if el.get('编号')}
for key, a, b in RENAME + REFS:
    el = num[key] if key in num else byid[key]
    v = el.get(attr(el))
    assert v.count(a) == 1, (key, a, v.count(a))
    el.set(attr(el), v.replace(a, b))
for el in root:   # 入口卡里其余引用 S04、S06 的地方
    v = el.get(attr(el)) or ''
    if '【工具】导数判单调' in v or '【工具】数学归纳法' in v:
        el.set(attr(el), v.replace('【工具】导数判单调', '【定理】导数判单调').replace('【工具】数学归纳法', '【公理】数学归纳法'))

# 3. 解法标记
BADGE = ' <span style="font-size:10px;color:#FFFFFF;background-color:#6D4C41;font-weight:bold;">\xa0解法\xa0</span>'
for key in ('R43', 'R25', 'R72', 'R74'):
    el = num[key]
    v = el.get('label')
    m = re.search(r'>%s</span>' % key, v)
    assert m, key
    el.set('label', v[:m.end()] + BADGE + v[m.end():])
    el.set('类型标记', '解法')

# 4. 方法卡加【恒等变形】
bg = byid['bg100']
v = bg.get('value')
anchor = '<b style="font-size:15px;">【等价变形】</b>'
S = '<span style="font-size:12px;color:#455A64;">%s</span>'
W = '<span style="font-size:12px;color:#BF360C;">⚠ %s</span>'
card = ('<b style="font-size:15px;">【恒等变形】</b>' + S % '（展开、提公因式、因式分解、通分、分母有理化）' + '<br>'
        '<b>方向</b>：把式子换成相等、更好用的样子（用 = 连接）；依据：运算律和工具箱里的恒等式<br>'
        + S % ('<b>信号</b>：要定正负就分解成因式之积；要比较就展开合并；根式和就有理化<br>'
               '<b>范例</b>：作差后分解 \\({a^{3}+b^{3}-ab(a+b)=(a+b)(a-b)^{2}}\\)〔P27 · A1〕、分母有理化〔P25 · A1〕、穿根前分解〔R25 · A1〕')
        + '<br>' + W % '与等价变形分清：恒等变形变式子（=），等价变形变不等式（⟺）' + '<br><br>')
assert v.count(anchor) == 1
v = v.replace(anchor, card + anchor)
bg.set('value', v)
g = bg.find('mxGeometry')
g.set('height', '%g' % (float(g.get('height')) + 110))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('edge labels regenerated', n)
