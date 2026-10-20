"""左侧"方法"一栏拆成独立小块，和工具箱一样（v47 → v48）。
三层分工表单独一块（横跨两栏），12 类方法各一块，左右两栏各 6 块；原面板 bg100 只作背景。
每块标题写类名，下一行列出推导线上属于这一类的【具体做法】标签。块高按实际渲染测量（MEASURE 为空时用估算）。
用法：（在 methods4.py 之后）
      python3 生成/split_methods.py outputs/inequality-tree-v48.drawio            # 先按估算拆
      （逐块导出测高，写入 /tmp/mm/h.json，见 工具/measure_blocks.py）
      python3 生成/split_methods.py 拆分前的副本 measure                          # 再按实测高度拆
      python3 生成/fixrefs.py outputs/inequality-tree-v48.drawio"""
import math, re, sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
byid = {el.get('id'): el for el in root}
if 'm_head' in byid:
    sys.exit('已拆过，跳过')

bg = byid['bg100']
v = bg.get('value')
MARK = '<b style="font-size:15px;">【'
parts = v.split(MARK)
head = re.sub(r'(<br>)+$', '', parts[0])
cards = [re.sub(r'(<br>)+$', '', MARK + p) for p in parts[1:]]
assert len(cards) == 12, len(cards)
name = lambda c: re.search(r'【([^】]+)】', c).group(1)
ORDER = ['比较', '配凑', '恒等变形', '等价变形', '代换', '构造函数', '放缩', '消元', '数形结合', '分类讨论', '反证', '归纳']
cards.sort(key=lambda c: ORDER.index(name(c)))
TAGS = {'比较': '作差 作商', '配凑': '配凑 配方 分组 补项 待定系数 乘 1 法 轮换求和',
        '恒等变形': '展开 提公因式 因式分解 通分 合并整理 分母有理化',
        '等价变形': '等价转化 移项 同加 同减 同乘 同除 平方 开平方 取倒数 去掉 f',
        '代换': '代换 换元 三角换元 齐次化 归一化 取特值 指对同构', '构造函数': '构造函数 求导 求最值 隐零点 必要性探路',
        '放缩': '放缩 裂项 保留首项 逐项递推', '消元': '代入消元 分离参数 主元 调整', '数形结合': '数形结合 平移直线',
        '分类讨论': '分类讨论 分类代入 分类合并 对称', '反证': '反证', '归纳': '归纳 奠基 递推 重复'}
SMALL = '<span style="font-size:12px;color:#455A64;">%s</span>'
def retitle(c):
    n = name(c)
    body = c[c.index('<br>') + 4:]
    tags = ''.join('【%s】' % t for t in TAGS[n].replace('乘 1 法', '乘1法').replace('去掉 f', '去掉f').split())
    tags = tags.replace('乘1法', '乘 1 法').replace('去掉f', '去掉 f')
    return '<b style="font-size:15px;">%s</b><br>' % n + SMALL % ('线上标签：' + tags) + '<br>' + body
cards = [retitle(c) for c in cards]
head = head.replace('<b>正推（由因导果）', '推导线上【】写具体做法（如【同除】），它属于哪一类，看下面各块的“线上标签”；「」是套用的工具（公式）。<br><b>正推（由因导果）')
import json, os
MEASURE = json.load(open('/tmp/mm/h.json')) if os.path.exists('/tmp/mm/h.json') and len(sys.argv) > 2 else {}

STYLE = ('rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8D6E63;strokeWidth=1.5;'
         'fontFamily=PingFang SC;fontSize=13;fontColor=#3E2723;arcSize=8;align=left;verticalAlign=top;'
         'spacingLeft=8;spacingRight=8;spacingTop=6;')


def est(lab, width):
    """估算高度：按 <br> 分行，按字宽折行；含分式的行加高。"""
    h = 0
    for line in re.split(r'<br>|</tr>', lab):
        fs = 15 if 'font-size:15px' in line else 12 if 'font-size:12px' in line else 13
        t = re.sub(r'\\\((.*?)\\\)', lambda m: 'x' * max(1, int(len(re.sub(r'\\[a-z]+|[{}_^ ]', '', m.group(1))) * 0.9)), line, flags=re.S)
        t = re.sub(r'<[^>]+>', '', t)
        if not t.strip():
            continue
        w = sum(fs if ord(ch) > 255 else fs * 0.58 for ch in t)
        rows = max(1, math.ceil(w / (width - 22)))
        h += rows * fs * 1.5 + (22 if 'dfrac' in line else 0)
    return h + 18


X0, W1, GAP = -1780, 370, 20
y = float(bg.find('mxGeometry').get('y')) + 20
hh = MEASURE.get('m_head') or est(head.replace('</td>', ' '), 760) + 40   # 表格行有边框和内边距
ET.SubElement(ET.SubElement(root, 'mxCell', {'id': 'm_head', 'value': head, 'style': STYLE, 'vertex': '1', 'parent': '1'}),
              'mxGeometry', {'x': str(X0), 'y': '%g' % y, 'width': '760', 'height': '%g' % round(hh), 'as': 'geometry'})
y += hh + 16
hs = [MEASURE.get('m_%02d' % (k + 1)) or round(est(c, W1)) for k, c in enumerate(cards)]
cut = min(range(4, 9), key=lambda k: abs(sum(hs[:k]) - sum(hs[k:]) + 12 * (k - (12 - k))))   # 两栏尽量等高
bottoms = []
for col, rng in enumerate((range(0, cut), range(cut, 12))):
    yy = y
    for k in rng:
        ET.SubElement(ET.SubElement(root, 'mxCell', {'id': 'm_%02d' % (k + 1), 'value': cards[k], 'style': STYLE, 'vertex': '1', 'parent': '1'}),
                      'mxGeometry', {'x': str(X0 + col * (W1 + GAP)), 'y': '%g' % yy, 'width': str(W1), 'height': '%g' % hs[k], 'as': 'geometry'})
        yy += hs[k] + 12
    bottoms.append(yy)
bg.set('value', '')
g = bg.find('mxGeometry')
g.set('height', '%g' % (max(bottoms) + 8 - float(g.get('y'))))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('head', round(hh), 'columns end', [round(b) for b in bottoms])
