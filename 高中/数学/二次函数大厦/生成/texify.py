"""把节点、连线文字里的公式片段（Unicode 写法）转成 MathJax 行内公式 \\( ... \\)。中文与〔编号〕原样保留。"""
import re

SUP = {"²": "2", "³": "3", "ⁿ": "n", "ᵏ": "k", "ˣ": "x", "⁺": "+", "⁻": "-", "¹": "1", "⁰": "0"}
SUB = {"ᵢ": "i", "₀": "0", "₁": "1", "₂": "2", "₃": "3", "ₖ": "k", "₊": "+", "ₙ": "n"}
SYM = [("⟺", r"\iff "), ("⟹", r"\Rightarrow "), ("⇒", r"\Rightarrow "), ("⇐", r"\Leftarrow "), ("→", r"\to "),
       ("≥", r"\ge "), ("≤", r"\le "), ("≠", r"\ne "), ("∈", r"\in "), ("∞", r"\infty "), ("ℝ", r"\mathbb{R}"),
       ("·", r"\cdot "), ("±", r"\pm "), ("×", r"\times "), ("Δ′", r"\Delta'"), ("Δ", r"\Delta "), ("−", "-"), ("′", "'"), ("θ", r"\theta "),
       ("…", r"\ldots "), ("≈", r"\approx "), ("Σ", r"\sum "), ("μ", r"\mu "), ("σ", r"\sigma ")]
MATHCH = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=<>()[]|/.,·^_ '!") | set(SUP) | set(SUB) | \
         {"−", "≥", "≤", "≠", "∈", "∞", "ℝ", "±", "×", "Δ", "√", "⟺", "⟹", "⇒", "→", "′", "θ", "…", "≈", "α", "β", "λ", "Σ", "μ", "σ"}
FUNC = ["sin", "cos", "tan", "ln", "log", "lg"]


def _sup_sub(s):
    s = re.sub("[" + "".join(SUP) + "]+", lambda m: "^{" + "".join(SUP[c] for c in m.group()) + "}", s)
    s = re.sub("[" + "".join(SUB) + "]+", lambda m: "_{" + "".join(SUB[c] for c in m.group()) + "}", s)
    while "^(" in s:                                  # ^(…) 整组作上标：^(m²−m) → ^{m²−m}
        i = s.index("^("); d = 0; j = len(s) - 1
        for j in range(i + 1, len(s)):
            d += {"(": 1, ")": -1}.get(s[j], 0)
            if d == 0:
                break
        s = s[:i] + "^{" + s[i + 2:j] + "}" + s[j + 1:]
    return s


def _group(s, i, direction):
    """从位置 i 取一个原子：f(x) 这样的函数调用、括号组、|…| 绝对值、或连续的字母数字（含上下标、\\命令）。"""
    W = lambda c: c.isalnum() or c in "^{}_\\'"
    def match(j, op, cl, step):
        d = 0
        while 0 <= j < len(s):
            d += 1 if s[j] == op else (-1 if s[j] == cl else 0)
            if d == 0:
                return j
            j += step
        return None
    if direction > 0:
        j = i
        if j < len(s) and s[j] == "|":
            e = s.index("|", j + 1); return i, e + 1
        if j < len(s) and s[j] == "(":
            e = match(j, "(", ")", 1); return (i, e + 1) if e is not None else (i, i)
        if j < len(s) and s[j] == "\\":                  # 命令开头：\sqrt{…}、\Delta 等，读命令名和紧随的 {…}
            j += 1
            while j < len(s) and s[j].isalpha():
                j += 1
            while j < len(s) and s[j] == "{":
                d = 0
                while j < len(s):
                    d += 1 if s[j] == "{" else (-1 if s[j] == "}" else 0)
                    j += 1
                    if d == 0:
                        break
            while j < len(s) and s[j] in "^_{}" + "".join(c for c in "0123456789"):
                j += 1
            return i, j
        while j < len(s) and (s[j].isalnum() or s[j] in "^{}_'"):
            j += 1
        if j < len(s) and s[j] == "(" and j > i:          # 函数名后紧跟括号：g(x)
            j = match(j, "(", ")", 1) + 1
        return i, j
    else:
        j = i
        if j >= 0 and s[j] == "|":
            b = s.rindex("|", 0, j); return b, i + 1
        if j >= 0 and s[j] == ")":
            j = match(j, ")", "(", -1) - 1
            while j >= 0 and s[j].isalpha():                # 括号前的函数名：f(x)
                j -= 1
            return j + 1, i + 1
        while j >= 0 and W(s[j]):
            j -= 1
        return j + 1, i + 1


def _strip(g):
    if g.startswith("(") and g.endswith(")"):
        d = 0
        for k, c in enumerate(g):
            d += 1 if c == "(" else (-1 if c == ")" else 0)
            if d == 0 and k < len(g) - 1:
                return g          # 形如 (a)(b)，外层括号不是一对
        return g[1:-1]
    return g


def _fracs(s):
    s = re.sub(r"\s*/\s*", "/", s)
    while "/" in s:
        k = s.index("/")
        a0, a1 = _group(s, k - 1, -1)
        b0, b1 = _group(s, k + 1, 1)
        if a0 == a1 or b0 == b1:
            s = s[:k] + "\u2215" + s[k + 1:]   # 不是分式，保留斜杠
            continue
        s = s[:a0] + r"\frac{" + _strip(s[a0:a1]) + "}{" + _strip(s[b0:b1]) + "}" + s[b1:]
    return s.replace("\u2215", "/")


def _sqrt(s):
    while "√" in s:
        k = s.index("√")
        b0, b1 = _group(s, k + 1, 1)
        if b0 == b1:                                  # √ 后面不是可读的原子（如括号里夹中文），原样当根号符号
            s = s[:k] + r"\surd " + s[k + 1:]
            continue
        s = s[:k] + r"\sqrt{" + _strip(s[b0:b1]) + "}" + s[b1:]
    return s


def to_tex(seg):
    t = _sup_sub(seg)
    for f in FUNC:
        t = re.sub(rf"(?<![A-Za-z\\]){f}(?![a-z])", "\\\\" + f + " ", t)
    for a, b in SYM:
        t = t.replace(a, b if a not in "Δ" else b)
    t = re.sub(r"\\Delta\s+(?=[A-Za-z0-9(])", r"\\Delta ", t)
    t = _sqrt(t)
    t = _fracs(t)
    return t.strip()


CODE = re.compile(r"^[SJRPF]\d\d$|^[A-L]\d$")


def texify(text):
    """text 已是转义前的纯文本；返回 HTML 片段（中文已转义，公式包在 \\( \\) 里）。"""
    from xml.sax.saxutils import escape
    out, buf = [], ""

    def flush():
        nonlocal buf
        if not buf:
            return
        core = buf.strip()
        lead, trail = buf[:len(buf) - len(buf.lstrip())], buf[len(buf.rstrip()):]
        mathy = core and not CODE.match(core) and re.search(r"[A-Za-z0-9ΔℝΔ√θ²³ⁿˣ₀₁₂⟺⇒⟹≥≤≠∈]", core) and not re.fullmatch(r"[\d.]+", core)
        if mathy and not re.fullmatch(r"[A-Za-z]{2,}", core):
            out.append(escape(lead) + r"\(" + escape(to_tex(core)) + r"\)" + escape(trail))
        else:
            out.append(escape(buf))
        buf = ""

    depth = 0
    for ch in text:
        if ch == "〔":
            flush(); depth += 1; out.append(ch); continue
        if ch == "〕":
            depth -= 1; out.append(ch); continue
        if depth:
            out.append(escape(ch)); continue
        if ch in MATHCH:
            buf += ch
        else:
            flush(); out.append(escape(ch))
    flush()
    return "".join(out)
