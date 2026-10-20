"""伯努利不等式 (1+x)ⁿ ≥ 1+nx 在新教材里有（选必二"二项式定理"例题、选必三"数学归纳法"练习，只是没写名字），
P26 及其推导 R12、P23 去掉"拓展"标签（v48 → v49）。
另：v48 的 methods4.py 误把 S04、S06 的类型标签覆盖回【工具】，这里改回【定理】【公理】（methods4.py 已修正为只改推导线）。
用法：cp outputs/inequality-tree-v48.drawio outputs/inequality-tree-v49.drawio
      python3 生成/untag_bernoulli.py outputs/inequality-tree-v49.drawio"""
import re, sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
EXT = re.compile(r' ?<span style="font-size:10px;color:#FFFFFF;background-color:#9E9E9E;font-weight:bold;">\xa0拓展\xa0</span>')
done = []
for el in root:
    if el.get('编号') in ('P26', 'R12', 'P23'):
        v = el.get('label')
        nv, k = EXT.subn('', v)
        if k:
            el.set('label', nv); done.append(el.get('编号'))
        if el.get('拓展'):
            del el.attrib['拓展']
for el in root:
    if el.get('编号') == 'S04':
        el.set('label', el.get('label').replace('【工具】导数判单调', '【定理】导数判单调'))
    if el.get('编号') == 'S06':
        el.set('label', el.get('label').replace('【工具】数学归纳法', '【公理】数学归纳法'))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('untagged', done)
