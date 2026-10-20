"""给没有名字的结论节点补上通行叫法或"出身"（v36）。只改标题，不动结构。
用法：python3 生成/add_names.py outputs/inequality-tree-v36.drawio
名字作为单独一行加在"★"后面，节点加高一行（上下各扩一半，中心不动）。重复运行不会重复添加。"""
import html, os, re, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex_convert import convert_label

F = sys.argv[1]
LINE_H = 18

NAMES = {
    # 教材或解题中的通行叫法
    'R55': '重要不等式',
    'R10': '指数切线不等式（切点 x=0）',
    'R26': '指数切线不等式（切点 x=1）',
    'P01': '对数切线不等式（切点 x=1）',
    'P14': '对数切线不等式（切点 x=e）',
    'P12': '对数切线不等式的变形（x 换成 1/x）',
    'P22': '对数切线不等式的变形（x 换成 1+x）',
    'P51': '泰勒放缩（二阶）',
    'R76': '泰勒放缩（二阶）',
    'P53': '泰勒放缩（二阶）',
    'P52': '泰勒放缩（三阶）',
    'P41': '柯西分式的特例（r=s=1）',
    'P31': '基本不等式的特例（对勾函数最小值）',
    # 没有公认名字：写出身
    'R67': '三组重要不等式相加',
    'P57': '三元均值不等式的多项式形式（a,b,c ≥ 0 时）',
    'P27': '排序不等式的特例（a,b ≥ 0 时）',
    'P34': '三次基本不等式相乘',
    'P16': '常用三角不等式（单位圆面积比较）',
    'R14': '常用三角不等式',
}
MARK = 'data-name'


def name_html(text):
    t = convert_label(html.escape(text, quote=False), [])
    return '<span %s="1" style="color:inherit;">%s</span>' % (MARK, t)


tree = ET.parse(F)
root = tree.getroot().find('.//root')
done = []
for el in root:
    num = el.get('编号')
    if num not in NAMES:
        continue
    lab = el.get('label')
    if MARK in lab:
        continue
    tag = name_html(NAMES[num])
    if '★ ' in lab:
        new = lab.replace('★ ', '★ %s<br>' % tag, 1)
    else:  # 无 ★ 的节点：名字加在编号后面一行
        new = re.sub(r'(%s</span>)' % num, r'\1<br>' + tag.replace('\\', '\\\\'), lab, count=1)
    assert new != lab, num
    el.set('label', new)
    g = el.find('mxCell').find('mxGeometry')
    g.set('height', '%g' % (float(g.get('height')) + LINE_H))
    g.set('y', '%g' % (float(g.get('y')) - LINE_H / 2))
    done.append(num)
tree.write(F, encoding='utf-8', xml_declaration=True)
print('named', len(done), sorted(done))
