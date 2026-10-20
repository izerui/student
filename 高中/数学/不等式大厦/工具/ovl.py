import sys, xml.etree.ElementTree as ET
def boxes(f):
    r=ET.parse(f).getroot().find('.//root'); b={}
    for el in r:
        c=el if el.tag=='mxCell' else el.find('mxCell')
        if c is None or c.get('vertex')!='1' or c.get('parent')!='1': continue
        g=c.find('mxGeometry'); x,y,w,h=(float(g.get(k,0)) for k in ('x','y','width','height'))
        b[el.get('id')]=(x,y,x+w,y+h)
    return b
def ov(a,b,m=4): return a[0]<b[2]-m and b[0]<a[2]-m and a[1]<b[3]-m and b[1]<a[3]-m
A=boxes(sys.argv[1]); B=boxes(sys.argv[2]); ids=list(B)
for i in range(len(ids)):
    for j in range(i+1,len(ids)):
        p,q=ids[i],ids[j]
        if ov(B[p],B[q]) and not ov(A[p],A[q],-6 if False else 4): print(p,q,B[p],B[q])
