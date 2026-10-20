"""给"教材没单列、但高考常用"的结论加蓝色「高考常用」标签，图例补说明（原地修改，可重复运行）。
用法：python3 生成/mark_gaokao.py outputs/inequality-tree-v38.drawio
名单写在 GAOKAO 里；窄节点加高一行，防止标签折行后压字。"""
import re, sys
import xml.etree.ElementTree as ET
F = sys.argv[1]
GAOKAO = [
    # 比较与最值
    'P20', 'P40', 'P42', 'R52', 'P41', 'P34', 'R67', 'P27',
    # 解不等式与含参
    'R25', 'R33', 'R44',
    # 导数：切线、泰勒、构造
    'R10', 'P01', 'R26', 'P14', 'P12', 'P22', 'P06', 'P05', 'P08',
    'P51', 'P52', 'P53', 'R76', 'P16', 'R14',
    # 数列放缩
    'P21', 'P24', 'P25', 'P54', 'P55', 'P13',
    # 旧教材选修 4-5，新教材已删、高考仍常用
    'R66', 'P33', 'R36', 'R59', 'R53',
]
TAG = ' <span style="font-size:10px;color:#FFFFFF;background-color:#1565C0;font-weight:bold;">\xa0高考常用\xa0</span>'
tree = ET.parse(F)
root = tree.getroot().find('.//root')
done = []
for el in root:
    n = el.get('编号')
    if n not in GAOKAO or el.get('高考常用') == '是':
        continue
    lab = el.get('label')
    key = '>%s</span>' % n
    assert lab.count(key) == 1, n
    el.set('label', lab.replace(key, key + TAG, 1))
    el.set('高考常用', '是')
    g = el.find('mxCell').find('mxGeometry')
    if float(g.get('width')) < 330:
        g.set('height', '%g' % (float(g.get('height')) + 14)); g.set('y', '%g' % (float(g.get('y')) - 7))
    done.append(n)
for el in root:
    if el.get('id') == 'lg20' and '高考常用' not in el.get('value'):
        el.set('value', el.get('value') + '；蓝色“高考常用”：教材没单列、高考常用的结论或方法')
tree.write(F, encoding='utf-8', xml_declaration=True)
print('marked', len(done), sorted(set(GAOKAO) - set(done)))
