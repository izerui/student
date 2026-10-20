import re, html, sys

SUP = {'²':'2','³':'3','¹':'1','⁴':'4','⁰':'0','ⁿ':'n','ˣ':'x','ᵏ':'k','ᵗ':'t','⁻':'-','⁺':'+',
       '⁽':'(','⁾':')','ᵃ':'a','ᵇ':'b','ᵖ':'p','ᵐ':'m','ᶠ':'f','ᵍ':'g'}
SUB = {'₀':'0','₁':'1','₂':'2','₃':'3','ₙ':'n','ᵢ':'i','ₖ':'k','ₐ':'a','₌':'=','₊':'+','ₚ':'p','ⱼ':'j'}
SYM = {'≥':r'\ge ','≤':r'\le ','≠':r'\ne ','⟺':r'\iff ','⇔':r'\Leftrightarrow ','⇒':r'\Rightarrow ',
       '⇐':r'\Leftarrow ','→':r'\to ','←':r'\leftarrow ','·':r'\cdot ','×':r'\times ','÷':r'\div ',
       '±':r'\pm ','−':'-','Σ':r'\sum ','∏':r'\prod ','Δ':r'\Delta ','θ':r'\theta ','φ':r'\varphi ',
       'α':r'\alpha ','π':r'\pi ','∞':r'\infty ','∈':r'\in ','ℝ':r'\mathbb{R}','∀':r'\forall ',
       '∃':r'\exists ','∪':r'\cup ','∩':r'\cap ','⊂':r'\subset ','∴':r'\therefore ','′':"'",'″':"''",
       '<':r'\lt ','>':r'\gt ','½':r'\tfrac12 '}
DIG = set('0123456789')
BIGOP = re.compile(r'\\(sum|prod)\b')
FUNC_RE = re.compile(r'\\(sin|cos|tan|log|ln|max|min)(?![a-z])')
FUNCS = ['sin','cos','tan','log','ln','max','min']
WORDS = ['Nesbitt','AM','GM','HM','QM']
MATHCH = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-=<>()[]|,.'^{}_/ ") \
         | set(SUP) | set(SUB) | set(SYM) | set('√∛…̄')
OPS = set('+-=<>,|') | {'≥','≤','≠','⟺','⇔','⇒','⇐','→','←','·','×','÷','±','−','∈','∪','∩','⊂','∴'}
INDICATOR = set('=<>/^_+') | set(SUP) | set(SUB) | {'≥','≤','≠','⟺','⇔','⇒','⇐','·','×','÷','±','−','√','∛','Σ','∏','∈','′','″','½','̄'}


class P:
    """把一段 Unicode 公式解析成 TeX。"""
    def __init__(self, s):
        self.s = s; self.i = 0

    def peek(self, k=0):
        j = self.i + k
        return self.s[j] if j < len(self.s) else ''

    def skipsp(self):
        while self.peek() == ' ': self.i += 1

    def scripts(self, base):
        # 上下标 + 撇号 + 上横线
        while True:
            c = self.peek()
            if c == '̄':
                base = r'\bar{%s}' % base; self.i += 1
            elif c in ('′', '″'):
                base += "'" if c == '′' else "''"; self.i += 1
            elif c in SUB:
                t = ''
                while self.peek() in SUB and self.peek(): t += SUB[self.peek()]; self.i += 1
                base += '_{%s}' % t
            elif c in SUP and not self.peek(1) == '√':
                t = ''
                while self.peek() in SUP and self.peek() and not self.peek(1) == '√':
                    t += SUP[self.peek()]; self.i += 1
                t = re.sub(r'\(([^()]*)\)', r'(\1)', t)
                base += '^{%s}' % t
            elif c == '^':
                self.i += 1
                if self.peek() == '{':
                    j = self.s.index('}', self.i); base += '^{%s}' % P(self.s[self.i+1:j]).expr(); self.i = j + 1
                elif self.peek() == '(' and self.group_ok():
                    g = self.group(); base += '^{%s}' % g[1].replace(r'\dfrac', r'\frac')
                else:
                    a = self.atom(simple=True); base += '^{%s}' % a[0]
            elif c == '_' :
                self.i += 1
                a = self.atom(simple=True); base += '_{%s}' % a[0]
            else:
                return base

    def group_ok(self):
        j = self.i; g = self.group(); self.i = j
        return g is not None

    def group(self):
        o = self.peek(); c = {'(': ')', '[': ']'}[o]
        depth = 0; j = self.i
        while j < len(self.s):
            if self.s[j] == o: depth += 1
            elif self.s[j] == c:
                depth -= 1
                if depth == 0: break
            j += 1
        else:
            self.i += 1
            return None
        inner = P(self.s[self.i+1:j]).expr()
        self.i = j + 1
        lo, rc = (r'\left(', r'\right)') if o == '(' else (r'\left[', r'\right]')
        if 'frac' not in inner and r'\sum' not in inner and r'\sqrt' not in inner:
            lo, rc = o, c
        return (lo + inner + rc, inner)

    def atom(self, simple=False):
        """返回 (tex, 去括号的 tex 或 None)。"""
        c = self.peek()
        if c == '(' or c == '[':
            g = self.group()
            if g is None:
                return (c, None)
            tex, inner = g
            out = self.scripts(tex)
            return (out, inner if out == tex else None)
        if c in ('√', '∛') or (c in SUP and self.peek(1) == '√'):
            idx = ''
            if c in SUP: idx = '[%s]' % SUP[c]; self.i += 1
            if self.peek() == '∛': idx = '[3]'
            self.i += 1
            if self.peek() == '(':
                _, inner = self.group()
            else:
                inner = self.atom(simple=True)[0]
                if re.fullmatch(r'[fgh]', inner) and self.peek() == '(':
                    inner += self.atom()[0]
            return (self.scripts(r'\sqrt%s{%s}' % (idx, inner)), None)
        if c == '|' and '|' in self.s[self.i+1:]:
            j = self.s.index('|', self.i + 1)
            inner = P(self.s[self.i+1:j]).expr(); self.i = j + 1
            return (self.scripts('|%s|' % inner), None)
        if c in DIG:
            j = self.i
            while self.peek() in DIG or (self.peek() == '.' and self.peek(1) in DIG): self.i += 1
            return (self.scripts(self.s[j:self.i]), None)
        if c.isalpha() and c.isascii():
            for w in WORDS:
                if self.s.startswith(w, self.i):
                    self.i += len(w); return (r'\text{%s}' % w, None)
            for f in FUNCS:
                if self.s.startswith(f, self.i):
                    self.i += len(f)
                    sub = self.scripts('')
                    return ('\\' + f + sub + ' ', None)
            self.i += 1
            return (self.scripts(c), None)
        if c in SYM and c not in OPS and c not in '<>':
            self.i += 1
            return (self.scripts(SYM[c].strip() + ' '), None)
        if c == '…':
            self.i += 1
            return (r'\cdots ', None)
        if c == '½':
            self.i += 1; return (r'\tfrac12 ', None)
        raise ValueError('bad atom %r' % c)

    def is_atom_start(self):
        c = self.peek()
        return c and (c in '([√∛…|' or c in DIG or (c.isascii() and c.isalpha())
                      or (c in SYM and c not in OPS and c not in '<>') or (c in SUP and self.peek(1) == '√'))

    def expr(self):
        out = []          # 元素：('atom', tex, inner) 或 ('op', tex)
        while self.i < len(self.s):
            c = self.peek()
            if c == ' ':
                self.i += 1
                if out and out[-1][0] != 'sp': out.append(('sp', ' '))
                continue
            if c == '/':
                self.i += 1; self.skipsp()
                # 分子：左侧连续并置的原子；函数名（ln x / x）连同参数算进来；Σ、∏ 不进分子
                while out and out[-1][0] == 'sp': out.pop()
                k = len(out)
                while k > 0:
                    if out[k-1][0] == 'atom' and not BIGOP.match(out[k-1][1]): k -= 1
                    elif out[k-1][0] == 'sp' and k >= 2 and FUNC_RE.match(out[k-2][1]): k -= 1
                    else: break
                num = [x for x in out[k:] if x[0] == 'atom']
                if not num or not self.is_atom_start():
                    out.append(('op', '/')); continue
                del out[k:]
                ntex = num[0][2] if len(num) == 1 and num[0][2] is not None else ''.join(x[1] for x in num)
                # 分母：一个原子；字母/数字串连读；f(…) 与 sin A、cos²θ 带上参数
                d = self.atom()
                dtex = d[1] if d[1] is not None else d[0]
                if FUNC_RE.match(d[0]):
                    self.skipsp(); dtex = d[0] + self.atom()[0]
                elif not d[0].startswith(('(', '\\', '|')):
                    while self.peek() and (self.peek() in DIG or (self.peek().isascii() and self.peek().isalpha())) \
                            and not any(self.s.startswith(f, self.i) for f in FUNCS):
                        dtex += self.atom()[0]
                    if self.peek() == '(' and re.fullmatch(r'[fgh]', dtex):
                        dtex += self.atom()[0]
                out.append(('atom', r'\dfrac{%s}{%s}' % (ntex, dtex), None))
                continue
            if c == '|' and '|' in self.s[self.i+1:]:
                a = self.atom(); out.append(('atom', a[0], a[1])); continue
            if c in OPS or c in '<>':
                self.i += 1
                if c == '.' : out.append(('op', '.')); continue
                out.append(('op', SYM.get(c, c)))
                continue
            if c == '.':
                self.i += 1; out.append(('op', '.')); continue
            if c in ')]':
                self.i += 1; out.append(('op', c)); continue
            if c in '{}':
                self.i += 1; out.append(('op', '\\' + c)); continue
            a = self.atom()
            out.append(('atom', a[0], a[1]))
        return ''.join(x[1] for x in out).strip()


def to_tex(s):
    return P(s).expr()


RUN = re.compile('[' + re.escape(''.join(sorted(MATHCH))) + ']+')


def has_math(run):
    if not any(ch.isalnum() or ch in 'ΣΔθφαπ∞ℝ√∛' for ch in run):
        return False
    if set(run) & INDICATOR: return True
    return False


def convert_text(t, log):
    """t 为已解码的纯文本片段。返回 HTML 片段（已转义）。"""
    res = []; pos = 0
    for m in RUN.finditer(t):
        run = m.group()
        # 去掉首尾空格及尾部的逗号/句号
        a, b = m.start(), m.end()
        while a < b and t[a] == ' ': a += 1
        while b > a and t[b-1] in ' ,.': b -= 1
        run = t[a:b]
        if not run or not has_math(run) or re.fullmatch(r'[A-Z]\d+\s*·\s*[A-Z]\d+', run):
            continue
        # 括号不平衡时，去掉多余的首尾括号
        try:
            tex = to_tex(run)
        except Exception as e:
            log.append(('FAIL', run, str(e)))
            continue
        res.append(html.escape(t[pos:a], quote=False))
        res.append(html.escape(r'\({' + tex + r'}\)', quote=False))
        log.append(('OK', run, tex))
        pos = b
    res.append(html.escape(t[pos:], quote=False))
    return ''.join(res)


def convert_label(lab, log):
    parts = re.split(r'(<[^>]+>)', lab)
    out = []
    for p in parts:
        if p.startswith('<'): out.append(p); continue
        t = html.unescape(p)
        out.append(convert_text(t, log))
    return ''.join(out)


if __name__ == '__main__':
    for s in sys.argv[1:]:
        print(s, '=>', to_tex(s))
