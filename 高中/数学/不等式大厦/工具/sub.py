import sys,re
import xml.etree.ElementTree as ET
src,dst,x0,y0,x1,y1=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:7])
t=ET.parse(src); root=t.getroot().find('.//root')
geo={}
def cell(el): return el if el.tag=='mxCell' else el.find('mxCell')
keep=set()
for el in list(root):
    c=cell(el)
    if c is None: continue
    g=c.find('mxGeometry')
    if c.get('vertex')=='1' and g is not None and c.get('parent')=='1':
        x=float(g.get('x',0)); y=float(g.get('y',0)); w=float(g.get('width',0)); h=float(g.get('height',0))
        if x<x1 and x+w>x0 and y<y1 and y+h>y0: keep.add(el.get('id'))
for el in list(root):
    c=cell(el)
    if c is None: continue
    i=el.get('id')
    if i in ('0','1'): continue
    if c.get('edge')=='1':
        if c.get('source') in keep or c.get('target') in keep: continue
        root.remove(el)
    elif i not in keep: root.remove(el)
t.write(dst,encoding='utf-8',xml_declaration=True)
print(len(keep))
