import re, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from tex_convert import convert_label
from xml.sax.saxutils import escape, unescape
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
log = []

def extra_height(lab):
    ex = 0
    for line in re.split(r'<br\s*/?>', lab):
        n = len(re.findall(r'\\dfrac', line))
        if not n: continue
        nested = re.search(r'\\dfrac\{[^{}]*\\(d?frac|sqrt)|\\sqrt\{\\dfrac', line)
        ex += 16 + (8 if nested else 0)
    return ex

def rep_attr(m):
    attr, raw = m.group(1), m.group(2)
    lab = unescape(raw, {'&quot;': '"'})
    new = convert_label(lab, log)
    return '%s="%s"' % (attr, escape(new, {'"': '&quot;'})), new

# 逐个元素处理，顶点按新增分式行数加高（上下各扩一半，保持中心不动）
out = []; pos = 0; grown = []
pat = re.compile(r'(<UserObject\b[^>]*?\blabel="[^"]*"[^>]*>.*?</UserObject>|<mxCell\b[^>]*?\bvalue="[^"]*"[^>]*?(?:/>|>.*?</mxCell>))', re.S)
for m in pat.finditer(s):
    blk = m.group(0); newlab = ['']
    def r(mm):
        a, n = rep_attr(mm); newlab[0] = n; return a
    blk2 = re.sub(r'\b(label|value)="([^"]*)"', r, blk, count=1)
    if 'vertex="1"' in blk2:
        ex = extra_height(newlab[0])
        if ex:
            def g(gm):
                h = float(gm.group(1)); y = float(gm.group(2))
                return 'height="%g"%sy="%g"' % (h + ex, gm.group(3), y - ex / 2)
            def fix(gm):
                tag = gm.group(0)
                h = re.search(r'height="([\d.]+)"', tag); y = re.search(r'\by="([\d.-]+)"', tag)
                if not h or not y: return tag
                tag = tag.replace(h.group(0), 'height="%g"' % (float(h.group(1)) + ex))
                return tag.replace(y.group(0), 'y="%g"' % (float(y.group(1)) - ex / 2))
            blk3 = re.sub(r'<mxGeometry [^>]*>', fix, blk2, count=1)
            if blk3 != blk2: grown.append(ex)
            blk2 = blk3
    out.append(s[pos:m.start()]); out.append(blk2); pos = m.end()
out.append(s[pos:])
s2 = ''.join(out).replace('math="0"', 'math="1"', 1)
open(dst, 'w', encoding='utf-8').write(s2)
with open('/tmp/convlog.txt', 'w') as f:
    for k, a, b in log: f.write('%s\t%s\t%s\n' % (k, a, b))
print('ok', sum(1 for l in log if l[0]=='OK'), 'fail', sum(1 for l in log if l[0]=='FAIL'), 'grown', len(grown))
