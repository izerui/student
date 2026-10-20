"""赫尔德不等式（P59）的推导补成高中可完成（v49 → v50）。
原推导从加权 AM-GM（P43，权为正整数）出发，只覆盖 p 为有理数，"一般实数需取极限"。
改为：权为有理数时仍可用 P43；任意实数 p 用导数证 Young 不等式——g(x)=x/p+1/q−x^{1/p}，x=1 处取最小值 0，只用到幂函数求导。
用法：cp outputs/inequality-tree-v49.drawio outputs/inequality-tree-v50.drawio
      python3 生成/fix_holder.py outputs/inequality-tree-v50.drawio"""
import sys
import xml.etree.ElementTree as ET

F = sys.argv[1]
tree = ET.parse(F)
root = tree.getroot().find('.//root')
el = next(e for e in root if e.get('id') == 'v33e14')
k = 'label' if el.tag == 'UserObject' else 'value'
v = el.get(k)
a = 'p 为有理数时用加权均值即可；一般实数需取极限'
assert v.count(a) == 1
b = ('p 为有理数时用加权均值即可；<br>任意实数 p：【构造函数】\\({g(x)=\\dfrac{x}{p}+\\dfrac{1}{q}-x^{\\frac{1}{p}}}\\)（\\({x\\gt 0}\\)），'
     '【求导】\\({g\'(x)=\\dfrac{1}{p}\\left(1-x^{\\frac{1}{p}-1}\\right)}\\)，\\({x=1}\\) 处取最小值 0；'
     '【代换】令 \\({x=\\dfrac{X}{Y}}\\)（\\({Y\\gt 0}\\)），两边乘 Y 即得上式')
el.set(k, v.replace(a, b))
p43 = next(e for e in root if e.get('编号') == 'P43')
lv = p43.get('label')
a2 = '正实数需取极限，超出高中'
assert lv.count(a2) == 1
p43.set('label', lv.replace(a2, '一般正实数需取极限，超出高中；两个数时可用导数证，见通往赫尔德的推导'))
g = p43.find('mxCell').find('mxGeometry')   # 多一行，加高
g.set('height', '%g' % (float(g.get('height')) + 20)); g.set('y', '%g' % (float(g.get('y')) - 10))
tree.write(F, encoding='utf-8', xml_declaration=True)
print('done')
