import re, sys
from xml.sax.saxutils import escape, unescape
f = sys.argv[1]
s = open(f, encoding='utf-8').read()
BR = re.compile(r'<br\s*/?>')
def text(l): return re.sub(r'<[^>]+>', '', l).strip()
n_changed = 0
def fix_block(m):
    global n_changed
    blk = m.group(0)
    if 'vertex="1"' not in blk or 'parent="1"' not in blk: return blk
    sm = re.search(r'style="([^"]*)"', blk[blk.find('<mxCell'):] if blk.startswith('<UserObject') else blk)
    st = sm.group(1)
    if 'align=left' in st or st.startswith('text;') or 'html=1' not in st: return blk
    am = re.search(r'\b(label|value)="([^"]*)"', blk)
    lab = unescape(am.group(2), {'&quot;': '"'})
    if '<div' in lab: return blk
    lines = BR.split(lab)
    h = 0
    if lines and lines[0].startswith('<span') and 'font-size:10px' in lines[0]: h = 1
    if len(lines) > h:
        t = text(lines[h])
        if t.startswith(('★', '【')) or '\\(' not in lines[h]: h += 1
    if h == 0 or len(lines) - h < 2: return blk
    new = ('<div style="text-align:center">' + '<br>'.join(lines[:h]) + '</div>'
           '<div style="text-align:left">' + '<br>'.join(lines[h:]) + '</div>')
    blk = blk[:am.start(2)] + escape(new, {'"': '&quot;'}) + blk[am.end(2):]
    blk = blk.replace(st, st + ('' if st.endswith(';') else ';') + 'spacingLeft=8;spacingRight=8;', 1)
    n_changed += 1
    return blk
pat = re.compile(r'<UserObject\b.*?</UserObject>|<mxCell\b[^>]*\bvalue="[^"]*"[^>]*?(?:/>|>.*?</mxCell>)', re.S)
s = pat.sub(fix_block, s)
open(f, 'w', encoding='utf-8').write(s)
print('changed', n_changed)
