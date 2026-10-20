"""方法与工具分开（v43 → v44）。
1. 推导线（及入口、节点）上的【】只保留 11 类方法（方向判断）；同类细分名写在后面，如"【放缩】裂项："；
   同一标签里同类方法第二次出现时不再加【】。只是在用工具或性质的步骤（展开、因式分解、逐项相加……）去掉【】。
   【前提】【公理】【定义】【工具】【研究对象】【方法】不动。
2. 方法索引面板重写为"方法卡"：开头是工具 / 方法 / 题型入口三层分工，再按 11 类写方向、依据、信号、范例、陷阱。
用法：cp outputs/inequality-tree-v43.drawio outputs/inequality-tree-v44.drawio
      python3 生成/methods.py outputs/inequality-tree-v44.drawio
      python3 生成/fixrefs.py outputs/inequality-tree-v44.drawio"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
DFRAC = re.compile(r'\\\(\{(?:(?!\\\)).)*?\\dfrac(?:(?!\\\)).)*?\}\\\)')


def tex(s):
    out = convert_label(html.escape(s, quote=False), [])
    return DFRAC.sub(lambda m: '<span style="display:inline-block;margin:3px 0;">' + m.group(0) + '</span>', out)


# 原标签 → (方法, 细分名)；细分名为 None 表示后文已说明具体做法
METHOD = {
    '作差法': ('比较', '作差'), '作商法': ('比较', '作商'),
    '配凑法': ('配凑', None), '配凑': ('配凑', None), '配方法': ('配凑', '配方'), '分组': ('配凑', '分组'),
    '分组代入': ('配凑', None), '补项': ('配凑', '补项'), '待定系数法': ('配凑', '待定系数'),
    '乘 1 法': ('配凑', '乘 1 法'), '求和平均法': ('配凑', '轮换求和'),
    '等价变形': ('等价变形', None), '移项': ('等价变形', '移项'), '移项法': ('等价变形', '移项'),
    '同加法': ('等价变形', None), '同减法': ('等价变形', None), '同乘法': ('等价变形', None),
    '同除法': ('等价变形', None), '同乘法+通分': ('等价变形', None), '平方法': ('等价变形', '平方'),
    '开平方': ('等价变形', '开平方'), '倒数法': ('等价变形', '取倒数'), '恒等变形': ('等价变形', None),
    '去掉 f': ('等价变形', '用单调性去掉 f'),
    '代换法': ('代换', None), '换元法': ('代换', None), '三角换元': ('代换', '三角换元'),
    '齐次化': ('代换', '齐次化'), '归一化': ('代换', '归一化'), '代入特定值': ('代换', '取特值'), '逐项代入': ('代换', None),
    '构造法': ('构造函数', None), '构造': ('构造函数', None), '求导': ('构造函数', '求导'),
    '单调性': ('构造函数', '单调性'), '极值判断': ('构造函数', '求最值'),
    '放缩法': ('放缩', None), '放缩': ('放缩', None), '裂项': ('放缩', '裂项'),
    '保留首项': ('放缩', '保留首项'), '递推': ('放缩', '逐项递推'),
    '代入消元': ('消元', '代入'), '参数分离': ('消元', '分离参数'), '调整法': ('消元', '调整'),
    '数形结合': ('数形结合', None), '平移法': ('数形结合', '平移直线'),
    '分类讨论': ('分类讨论', None), '分类代入': ('分类讨论', None), '分类合并': ('分类讨论', None),
    '对称性': ('分类讨论', '对称'), '对称交换': ('分类讨论', '对称'),
    '零向量': ('分类讨论', '零向量'), '非零向量': ('分类讨论', '非零向量'),
    '反证法': ('反证', None),
    '归纳法': ('归纳', None), '归纳法·奠基': ('归纳', '奠基'), '归纳法·递推': ('归纳', '递推'), '重复': ('归纳', '重复'),
}
OPERATION = {'展开法': '展开', '提公因式': '提公因式', '因式分解': '因式分解', '分母有理化': '分母有理化',
             '合并整理': '合并整理', '逐项相加': '逐项相加', '逐项相乘': '逐项相乘', '同向相乘': '同向相乘',
             '同号相乘': '同号相乘', '平方非负': '平方非负', '绝对值界': '绝对值界', '判别式': '判别式',
             '记号': '记号', '取等': '取等'}
KEEP = {'前提', '公理', '定义', '工具', '研究对象', '方法'}
TAG = re.compile(r'【([^】]{1,8})】')


def plain_start(rest, word):
    """后文已以该词开头（去掉标签）时，不再重复写。"""
    t = re.sub(r'<[^>]+>', '', rest).lstrip()
    return t.startswith(word[:2])


def relabel(lab, unknown):
    seen, out, pos = set(), [], 0
    for m in TAG.finditer(lab):
        out.append(lab[pos:m.start()]); pos = m.end()
        name, rest = m.group(1), lab[m.end():]
        if name in KEEP:
            out.append(m.group(0)); continue
        if name in OPERATION:
            w = OPERATION[name]
            out.append('' if plain_start(rest, w) else w + '：'); continue
        if name not in METHOD:
            unknown.add(name); out.append(m.group(0)); continue
        fam, sub = METHOD[name]
        head = '' if fam in seen else '【%s】' % fam
        seen.add(fam)
        out.append(head + (sub + '：' if sub and not plain_start(rest, sub) else ''))
    out.append(lab[pos:])
    return ''.join(out)


tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if '方法卡' in (byid['bg99'].get('value') or ''):
    sys.exit('已修改过，跳过')

unknown, changed = set(), 0
for el in root:
    a = 'label' if el.tag == 'UserObject' else 'value'
    lab = el.get(a)
    if not lab or '【' not in lab or el.get('id', '').startswith('lg'):
        continue
    new = relabel(lab, unknown)
    if new != lab:
        el.set(a, new); changed += 1
assert not unknown, unknown

# 图例
lg = byid['lg23']
a = 'label' if lg.tag == 'UserObject' else 'value'
assert '线上写【方法】和具体操作' in lg.get(a)
lg.set(a, lg.get(a).replace('线上写【方法】和具体操作', '线上【】里是方法（方向判断，共 11 类，见左侧方法卡），其余文字是具体操作'))

# 方法卡
S = '<span style="font-size:12px;color:#455A64;">%s</span>'
W = '<span style="font-size:12px;color:#BF360C;">⚠ %s</span>'


def card(name, alias, direction, signal, examples, trap):
    ex = '、'.join('%s〔%s · A1〕' % (tex(t), n) if n else tex(t) for t, n in examples)
    return ('<b style="font-size:15px;">【%s】</b>%s<br>' % (name, S % ('（%s）' % alias if alias else ''))
            + '<b>方向</b>：' + direction + '<br>'
            + S % ('<b>信号</b>：' + signal + '<br><b>范例</b>：' + ex) + '<br>' + W % trap + '<br><br>')


CARDS = [
    card('比较', '作差、作商', '比大小 → 看 ' + tex('a − b') + ' 的正负（正数也可看 ' + tex('a/b') + ' 与 1 比）；依据：大小就是差的符号〔S01 · A1〕',
         '两式比大小；含幂、指数的正数用作商',
         [('a³+b³ ≥ ab(a+b)', 'P27'), ('aᵃbᵇ ≥ aᵇbᵃ', 'P49')], '作商前先确认分母为正'),
    card('配凑', '配方、分组、补项、乘 1 法、待定系数', '凑成"平方 + 常数"，或凑出和、积为定值；依据：平方非负〔R28 · A1〕，均值不等式求最值要定值',
         '二次式定号、求最值；对称多项式不等式；条件最值',
         [('a²+b² ≥ 2ab', 'R55'), ('配方求最值', 'R17'), ('柯西不等式', 'R66')], '凑完要核对等号能否取到'),
    card('等价变形', '移项、两边同乘除、平方、取倒数、开方', '换成同解、更好处理的形式；依据：不等式的性质，每一步都要是 ⟺',
         '解不等式；把结论化成已知的形式',
         [('负数乘法反序', 'R06'), ('非负数平方保序', 'P03'), ('正数倒数反序', 'P17')], '乘除前先判正负；平方要求两边非负；取倒数要求两边同号'),
    card('代换', '换元、取特值、齐次化、归一化', '把新式子装进已知不等式的形状；依据：不等式对所有取值成立，代入什么都成立',
         '结构与已知结论相似；和、积同时出现；指对混合（同构）',
         [('x 换成 1/x', 'P12'), ('和积代换', 'R52'), ('同构', 'P60')], '换元后变量范围随之改变'),
    card('构造函数', '求导、单调性、求最值', '恒成立 → 函数最小值 ≥ 0；依据：单调性把一点处函数值的符号传到整个区间〔S04 · A1〕',
         '含 eˣ、ln x、sin x；含参恒成立；给出 f′ 与 f 的关系',
         [('ln x ≤ x−1', 'P01'), ('构造 ln x/x 比大小', 'P08'), ('f′+f 想 (eˣf)′', 'P05')], '同一区间内判单调；端点取不到时看极限'),
    card('放缩', '裂项、等比、切线', '难求的量 → 好求的界；依据：传递性〔S01 · A1〕',
         '数列求和证"< 常数"；超越式与多项式比较',
         [('裂项放缩', 'P24'), ('对数放缩求和', 'P21'), ('更紧的裂项', 'P55')], '放过头就证不出；留意从第几项开始放'),
    card('消元', '代入消元、分离参数、调整', '多个变量 → 一个变量；依据：约束等式可解出一个变量，参数与变量可分开',
         '有等式约束的多变量最值；含参恒成立',
         [('和定积最大', 'R61'), ('排序不等式的调整法', 'R41'), ('分离参数（见入口"含参不等式"）', None)], '消元后保留剩下变量的范围'),
    card('数形结合', '', '式子 → 图形；依据：代数式的几何意义（距离、斜率、图像高低）',
         '|x−a|+|x−b|；(y−b)/(x−a)；根的分布；二元一次约束',
         [('绝对值和的最小值', 'R53'), ('根的分布', 'R44'), ('线性规划', 'R74')], '图只作引导，结论要能用代数说清'),
    card('分类讨论', '含对称', '结论依赖符号或大小 → 分段各自处理；有对称性时只讨论一半',
         '含参；绝对值；二次项系数含参；两根大小不定',
         [('解一元二次不等式', 'R43'), ('绝对值不等式', 'R15'), ('三角不等式', 'R36')], '分类标准统一，不重不漏'),
    card('反证', '', '直接证明困难 → 假设结论不成立，推出矛盾',
         '至少、至多、唯一；逆命题已知（如由乘方保序推开方保序）',
         [('开方保序', 'P19'), ('用单调性去掉 f', 'P47')], '要否定整个结论'),
    card('归纳', '', '对所有 n ≥ n₀ 成立 → 奠基 + 递推〔S06 · A1〕',
         '含正整数 n 的不等式；能由 k 推到 k+1',
         [('伯努利不等式', 'P26'), ('2ᵏ 个数的均值不等式', 'P36')], '递推那一步必须用上归纳假设'),
]
TD = '<td style="border:1px solid #BCAAA4;padding:3px 6px;">%s</td>'
ROWS = [('<b>层</b>', '<b>回答</b>', '<b>是什么</b>', '<b>在图中</b>'),
        ('<b>工具</b>', '能用什么', '公式、定理，拿来直接套', '工具箱；节点里的"⇐ 工具"'),
        ('<b>方法</b>', '往哪走', '方向判断：把眼前的问题转化成什么', '推导线上的【】；下面的方法卡'),
        ('<b>题型入口</b>', '从哪进', '看到什么题，先想到哪个结论', '左侧"看到 …"卡片')]
table = ('<table style="border-collapse:collapse;font-size:13px;">'
         + ''.join('<tr>' + ''.join(TD % c for c in r) + '</tr>' for r in ROWS) + '</table>')
HEAD = (table + '先用<b>方法</b>定方向，再用<b>工具</b>完成每一步：方法决定能不能想到，工具决定能不能算对。<br>'
        '<b>正推（由因导果）= 综合法</b>：沿箭头往下读；<b>反推（执果索因）= 分析法</b>：题型入口里的"反推"。<br><br>')
bg100 = byid['bg100']
bg100.set('value', HEAD + ''.join(CARDS))
g = bg100.find('mxGeometry')
g.set('height', '1430')
byid['bg99'].set('value', byid['bg99'].get('value').replace('方法索引：按方法复习，到〔坐标〕找推导线',
                                                             '方法卡：每类方法往哪走、凭什么、何时用'))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('labels changed', changed)
