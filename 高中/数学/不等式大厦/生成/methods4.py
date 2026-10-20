"""推导线标签改回具体做法名，恢复可读性（v47 → v48 的第一步）。
用户反馈 v44～v47 的连线"看不懂了"：具体做法名被换成大类名（【同除法】→【等价变形】）、套公式的步骤加了编号坐标、
多步推导里后几步没有【】。改为：
- 【】写具体做法名（去掉"法"字），每一步都加；12 大类只在左侧"方法"一栏出现，每块列出它包含的线上标签。
- 套用公式的步骤写成「工具名」，不带编号。
- 题型入口里的"【大类】细分："还原成"【细分】"。
标签从 v43 的原文重新生成（v43 已从 outputs 删除，git 对象 b52000d9aaeb85e64ca4dcfdb350e9f205846d24 可取回）。
用法：git cat-file -p b52000d9aaeb85e64ca4dcfdb350e9f205846d24 > /tmp/v43.drawio
      cp outputs/inequality-tree-v47.drawio outputs/inequality-tree-v48.drawio
      python3 生成/methods4.py outputs/inequality-tree-v48.drawio /tmp/v43.drawio"""
import re, sys
import xml.etree.ElementTree as ET

F, OLD = sys.argv[1], sys.argv[2]

# 原标签 → 线上显示的具体做法名（None 表示照原样）；左边的 12 大类归属见 FAMILY
CONCRETE = {
    '作差法': '作差', '作商法': '作商',
    '配凑法': '配凑', '配方法': '配方', '分组代入': '分组', '待定系数法': '待定系数', '求和平均法': '轮换求和',
    '展开法': '展开',
    '等价变形': '等价转化', '恒等变形': '等价转化', '移项法': '移项', '同加法': '同加', '同减法': '同减', '同乘法': '同乘',
    '同除法': '同除', '同乘法+通分': '同乘、通分', '平方法': '平方', '倒数法': '取倒数',
    '代换法': '代换', '换元法': '换元', '代入特定值': '取特值', '逐项代入': '取特值',
    '构造法': '构造函数', '构造': '构造函数', '极值判断': '求最值',
    '放缩法': '放缩', '递推': '逐项递推',
    '参数分离': '分离参数', '调整法': '调整', '平移法': '平移直线',
    '对称性': '对称', '对称交换': '对称', '零向量': '分类讨论', '非零向量': '非零向量',
    '反证法': '反证', '归纳法': '归纳', '归纳法·奠基': '奠基', '归纳法·递推': '递推',
}
TOOL = {'平方非负': '平方非负', '同号相乘': '同号相乘', '同向相乘': '同向正数可乘', '逐项相乘': '同向正数可乘',
        '逐项相加': '同向可加', '绝对值界': '绝对值界', '判别式': 'Δ ≤ 0', '单调性': '单调性'}
PLAIN = {'记号', '取等'}
KEEP = {'前提', '公理', '定义', '工具', '研究对象', '方法'}
TAG = re.compile(r'【([^】]{1,8})】')


def concrete(lab):
    def f(m):
        n = m.group(1)
        if n in KEEP:
            return m.group(0)
        if n in TOOL:
            return '「%s」' % TOOL[n]
        if n in PLAIN:
            return n + '：'
        if n == '非零向量':
            return '非零向量：'
        return '【%s】' % CONCRETE.get(n, n)
    return TAG.sub(f, lab)


tree = ET.parse(F)
root = tree.getroot().find('.//root')
old = {el.get('id'): el for el in ET.parse(OLD).getroot().find('.//root')}


def attr(el):
    return 'label' if el.tag == 'UserObject' else 'value'


n = 0
for el in root:
    eid = el.get('id', '')
    if eid.startswith(('ent_', 'lg', 'bg')) or eid not in old:
        continue
    c = el if el.tag == 'mxCell' else el.find('mxCell')
    if c is None or c.get('edge') != '1':
        continue   # 只改推导线；节点的类型标签（【定理】【公理】等）v43 之后改过，不能覆盖
    ol = old[eid].get(attr(old[eid])) or ''
    if '【' not in ol:
        continue
    new = concrete(ol)
    if eid in ('e132', 'e133'):   # 判断导数正负是在用"导数判单调"这条定理
        new = new.replace('【分类讨论】', '「导数判单调」', 1)
    if new != el.get(attr(el)):
        el.set(attr(el), new); n += 1

# 最简略的几条补上具体式子，线上能看出过程
DETAIL = {
    'e43': ('【展开】展开平方', '【展开】\\({(ad-bc)^{2} = a^{2}d^{2}-2abcd+b^{2}c^{2}}\\)'),
    'e50': ('【展开】展开乘积', '【展开】\\({(a_{2}-a_{1})(b_{2}-b_{1}) = a_{2}b_{2}-a_{2}b_{1}-a_{1}b_{2}+a_{1}b_{1}}\\)'),
    'e20': ('【展开】展开完全平方', '【展开】\\({(a-b)^{2} = a^{2}-2ab+b^{2}}\\)'),
    'e14': ('「同向可加」对应不等式相加', '「同向可加」\\({-|a|\\le a\\le |a|}\\) 与 \\({-|b|\\le b\\le |b|}\\) 两式相加'),
}
for eid, (a, b) in DETAIL.items():
    el = next(e for e in root if e.get('id') == eid)
    v = el.get(attr(el))
    assert v.count(a) == 1, eid
    el.set(attr(el), v.replace(a, b))

# 题型入口："【大类】细分：" → "【细分】"
FAMS = '比较|配凑|恒等变形|等价变形|代换|构造函数|放缩|消元|数形结合|分类讨论|反证|归纳'
m_ent = 0
for el in root:
    if el.get('id', '').startswith('ent_'):
        v = el.get(attr(el))
        nv = re.sub(r'【(?:%s)】([^：<【]{1,8})：' % FAMS, r'【\1】', v)
        if nv != v:
            el.set(attr(el), nv); m_ent += 1

# 图例
lg = next(el for el in root if el.get('id') == 'lg23')
v = lg.get(attr(lg))
a = '线上【】里是方法（方向判断，共 12 类，见左侧“方法”一栏），其余文字是具体操作'
assert a in v
lg.set(attr(lg), v.replace(a, '线上【】是方法（具体做法，归属 12 类见左侧“方法”一栏），「」是套用的工具（公式），其余是具体操作'))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('edges', n, 'entries', m_ent)
