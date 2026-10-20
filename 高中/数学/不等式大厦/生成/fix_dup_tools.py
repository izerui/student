"""去掉"⇐ 工具"行里重复写的编号和公式（原地修改，可重复运行）。
用法：python3 生成/fix_dup_tools.py outputs/inequality-tree-v38.drawio"""
import sys
import xml.etree.ElementTree as ET
F = sys.argv[1]
F10 = '\\({a^{3}+b^{3} = (a+b)^{3}-3ab(a+b)}\\)'
F11 = '\\({a^{2}+b^{2}+c^{2} = (a+b+c)^{2}-2(ab+bc+ca)}\\)'
EDITS = {
    'R02': ('⇐ 工具 ㉑ 倍角公式：㉑ ', '⇐ 工具 ㉑ 倍角公式：'),
    'P27': ('⇐ 工具 ⑩ %s：⑩ %s' % (F10, F10), '⇐ 工具 ⑩ 立方和与积的互换：%s' % F10),
    'R70': ('⇐ 工具 ⑪ %s：⑪ 平方和与交叉积互换' % F11, '⇐ 工具 ⑪ 平方和与交叉积互换：%s' % F11),
    'R34': ('⇐ 工具 ⑫ 韦达定理：⑫ 根与系数的关系', '⇐ 工具 ⑫ 韦达定理（根与系数的关系）'),
    'P05': ('⇐ 工具 ㊵ 求导法则：㊵ 积、商的求导法则', '⇐ 工具 ㊵ 求导法则：积、商的求导法则'),
    'R16': ('⇐ 工具 ㊶ 向量数量积：㊶ 数量积的两种表示', '⇐ 工具 ㊶ 向量数量积：数量积的两种表示'),
    'P25': ('⇐ 工具 ① 平方差公式：① 平方差：', '⇐ 工具 ① 平方差公式：'),
}
tree = ET.parse(F)
n = 0
for el in tree.getroot().find('.//root'):
    e = EDITS.get(el.get('编号'))
    if e and e[0] in el.get('label'):
        el.set('label', el.get('label').replace(e[0], e[1], 1)); n += 1
tree.write(F, encoding='utf-8', xml_declaration=True)
print('fixed', n)
