"""恒等式大厦：节点与连线数据（依据 ../恒等式大厦-节点清单.md）。

文本里的公式一律写成 $LaTeX$，中文原样。格式（每条记录一行起头，后续行以 - 或 ~ 开头）：
  SEC 键 | 标题条文字
  N 编号 类型 分区 [ext] | 条件标签 | 标题        类型：start / green / white / orange / lorange
    - 正文行（以“✗”开头的是反例）
    ~ 注释行（同源、互逆、接口等）
  E 源 目标 derive|premise [main] | ▼标记（可空）
    - 线上标签行
"""
TITLE = "恒等式大厦"
SUBTITLE = [
    "从 20 个起点（运算律、集合、指数与对数、单位圆、数量积、复数、计数原理、数列、导数、函数、坐标法、空间向量、体积、概率）出发，不跳步推出高中全部恒等式与公式",
    "主干：源头 → 变形 → 结论；变形手法写在线上【方法】里。橙色 = 要加条件：〔定义域〕〔结构前提〕〔符号分支〕三类，各自独立",
]

RAW = r'''
SEC base | 地基：实数运算律 · 初中几何 · 计数原理 · 数学归纳法（直接承认，不依赖别的起点）
SEC alg | ① 代数：运算律 → 分配律展开 → 乘法公式、因式分解 → 配方、求根公式、韦达定理
SEC exp | ② 指数、根式与对数：指数运算律 → 整数、实数指数 → 根式；对数（逆运算）→ 运算律、换底
SEC tri | ③ 三角：单位圆 → 勾股、诱导；数量积 → 和差角 → 倍角、降幂、半角、辅助角；解三角形
SEC vec | ③a 向量与解三角形：数量积 → 运算公式 → 余弦定理；面积 → 正弦定理
SEC cpx | ③b 复数：$i^2=-1$ → 乘法、共轭与模 → 三角形式：模相乘、辐角相加 → 棣莫弗
SEC seq | ④ 数列：累加相消 → 等差、等比的通项与求和 → 裂项、自然数幂和
SEC cnt | ⑤ 计数：两个计数原理 → 排列 → 组合 → 二项式定理
SEC der | ⑥ 导数：导数定义 → 求导法则；导数表的由来
SEC fun | ⑦ 函数性质：奇偶、周期、图像的定义 → 对称、周期的恒等关系 → 图像变换 → 正弦型函数
SEC geo | ⑧ 解析几何：斜率 → 直线方程 → 平行垂直、距离（投影）→ 圆（配方）→ 圆锥曲线 → 联立（韦达）
SEC sp | ③c 空间向量与立体几何：空间坐标数量积 → 空间角、距离（投影）；体积：台 = 大锥 − 小锥
SEC prob | ⑨ 概率统计：事件与概率 → 加法、乘法、全概率、贝叶斯 → 期望与方差 → 二项、超几何；统计：方差、回归

# ───────── ① 代数 ─────────
N S01 start base | | 【公理】运算律、等式性质与绝对值
- 交换律、结合律；分配律 $a(b+c)=ab+ac$
- 等式两边同加、同乘一个数仍相等；同除一个非零数仍相等
- 减 $b$ 即加 $-b$；除以 $b$（$b\ne 0$）即乘 $\dfrac{1}{b}$
- 绝对值：$a\ge 0$ 时 $|a|=a$，$a<0$ 时 $|a|=-a$
~ 起点：实数运算的基本规定，所有恒等式的地基

N R01 green alg | | ★★★ 多项式乘法
- $(a+b)(c+d)=ac+ad+bc+bd$
~ 枢纽：本图所有“展开”都从这里出发
~ ⚡ 第一反应：看到括号相乘 → 逐项展开

N R36 green alg | | ★ 去括号与合并同类项
- $a-(b-c)=a-b+c$，$-(a+b)=-a-b$
- $ma+na=(m+n)a$
~ 用于：一切化简、解方程
~ ⚡ 第一反应：括号前是负号 → 去括号全变号

N R37 green alg | | ★ 绝对值运算
- $|ab|=|a||b|$，$|a|^2=a^2$；$\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$（$b\ne 0$）
~ 用于：不等式大厦 R09（绝对值界）
~ ⋯ 同源：复数模的乘法〔R25〕
~ ⚡ 第一反应：看到含绝对值的乘除、平方 → $|ab|=|a||b|$，$|a|^2=a^2$；去绝对值按正负分类

N P42 orange alg | 〔定义域〕分母 $\ne 0$ | ★ 分式运算
- 约分 $\dfrac{ac}{bc}=\dfrac{a}{b}$（$c\ne 0$）；$\dfrac{a}{b}\pm\dfrac{c}{d}=\dfrac{ad\pm bc}{bd}$
- $\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd}$，$\dfrac{a}{b}\div\dfrac{c}{d}=\dfrac{ad}{bc}$（$c\ne 0$）
- ✗ $\dfrac{x^2-1}{x-1}=x+1$ 只在 $x\ne 1$ 时成立：约掉的因式不能为 0
~ 用于：裂项、复数除法、商的求导、弦化切
~ ⚡ 第一反应：看到分式 → 先因式分解，再约分、通分

N R02 green alg | | ★ 平方差
- $a^2-b^2=(a+b)(a-b)$
~ 同见不等式大厦 P03、P25
~ ⋯ 配合：分母有理化〔P44〕、共轭〔R23〕
~ ⚡ 第一反应：看到两个平方相减，或“和×差” → 平方差

N R03 green alg | | ★★ 完全平方
- $(a\pm b)^2=a^2\pm 2ab+b^2$
~ 同见不等式大厦 R37、R49
~ ⋯ 配合：配方〔P01〕、$(\sin\alpha\pm\cos\alpha)^2$〔R38〕
~ ⚡ 第一反应：看到 $a^2\pm 2ab+b^2$ 三项 → 写成完全平方

N R04 white alg | | 三数和的平方
- $(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$
~ 同见不等式大厦 R64

N R05 green alg | | ★ 两数和（差）的立方
- $(a\pm b)^3=a^3\pm 3a^2b+3ab^2\pm b^3$

N R06 green alg | | ★ 立方和（差）
- $a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$
~ 同见不等式大厦 P27、R25
~ 用于：高次式分解
~ ⚡ 第一反应：看到两个立方相加减 → 立方公式

N R07 green alg | | ★ 互换式
- $a^2+b^2=(a+b)^2-2ab$
- $(a-b)^2=(a+b)^2-4ab$
- $a^3+b^3=(a+b)^3-3ab(a+b)$
- $a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$
~ 同见不等式大厦 R60、R52
~ ⋯ 配合：韦达〔P03〕→ 两根的对称式〔P45〕
~ ⚡ 第一反应：看到平方和 $a^2+b^2$、对称式（交换 $a,b$ 不变）→ 化成 $a+b$ 与 $ab$

N R08 white alg | | 因式分解
- 提公因式：分配律倒用
- 公式法：平方差、完全平方、立方和（差）倒用
- 十字相乘：$acx^2+(ad+bc)x+bd=(ax+b)(cx+d)$
- 特例 $x^2+(p+q)x+pq=(x+p)(x+q)$：找两数乘得常数项、加得一次项系数
- 分组分解；顺序：一提、二套、三检查
- 十字相乘不行时，用求根公式〔P02〕求两根，写成交点式〔P04〕
~ 用于：解一元二次、高次方程；不等式大厦 R25（穿根法）
~ ⋯ 配合：约分〔P42〕
~ ⚡ 第一反应：看到二次式要拆开 → 先试十字相乘

N P01 orange alg | 〔定义域〕$a\ne 0$ | ★★ 配方
- $ax^2+bx+c=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$
- ✗ $a=0$ 时 $\dfrac{b}{2a}$ 无意义
~ 同见不等式大厦 R17；同见二次函数大厦 R01
~ 用于：求二次式的最值；不等式大厦 R23
~ ⚡ 第一反应：看到求二次式的最值、值域 → 配方

N P02 lorange alg | 〔定义域〕$\Delta\ge 0$ | 求根公式
- $ax^2+bx+c=0$（$a\ne 0$）的根 $x=\dfrac{-b\pm\sqrt{\Delta}}{2a}$，$\Delta=b^2-4ac$
- $\Delta>0$ 两个不等实根，$\Delta=0$ 两个相等的实根（重根），$\Delta<0$ 无实根
- ✗ $\Delta<0$ 时 $\sqrt{\Delta}$ 在实数范围内无意义
~ 同见二次函数大厦 J05
~ 用于：解方程、二次函数零点
~ ⚡ 第一反应：十字相乘拆不开 → 求根公式（先看 $\Delta$）

N P03 orange alg | 〔定义域〕$a\ne 0$，$x_1,x_2$ 为两实根（$\Delta\ge 0$） | ★★ 韦达定理
- $x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$（重根算两个）
- ✗ $x^2+x+1=0$：$\Delta=-3<0$，照公式得 $x_1+x_2=-1$，但实根不存在
~ 同见不等式大厦 R52；同见二次函数大厦 J06
~ 用于：二次函数大厦 R11（根的符号）；不等式大厦 R34
~ ⋯ 配合：互换式〔R07〕
~ ⚡ 第一反应：不解方程求两根的式子 → 韦达

N P04 lorange alg | 〔定义域〕$\Delta\ge 0$（实根存在） | 交点式
- $ax^2+bx+c=a(x-x_1)(x-x_2)$
~ 同见二次函数大厦 P01
~ 用于：不等式大厦 R34（三个二次）
~ ⚡ 第一反应：已知两根或两个零点 → 交点式

N P45 orange alg | 〔定义域〕$x_1,x_2$ 为两实根（$\Delta\ge 0$） | ★★ 两根的对称式
- $x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2$；$\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{x_1+x_2}{x_1x_2}$（$c\ne 0$）
- $|x_1-x_2|=\sqrt{(x_1+x_2)^2-4x_1x_2}=\dfrac{\sqrt{\Delta}}{|a|}$
- ✗ $x^2+x+1=0$ 无实根，硬套得 $x_1^2+x_2^2=(-1)^2-2=-1$，实数平方和不可能为负
~ 用于：解析几何——联立消元后求弦长、中点
~ ⋯ 配合：弦长 $|AB|=\sqrt{1+k^2}\,|x_1-x_2|$
~ ⚡ 第一反应：看到 $x_1^2+x_2^2$、$|x_1-x_2|$ → 韦达代入互换式

N R09 white alg ext | | $x^n-y^n$ 的分解
- $x^n-y^n=(x-y)(x^{n-1}+x^{n-2}y+\cdots+y^{n-1})$（$n$ 为正整数）
- $n=2,3$ 即平方差、立方差
~ 用于：高次式分解
~ ⚡ 第一反应：看到 $x^n-1$ → 提出 $x-1$

N R10 white alg ext | | 三元立方和
- $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$
- $=\dfrac{1}{2}(a+b+c)\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$
- 推论：$a+b+c=0\Rightarrow a^3+b^3+c^3=3abc$
~ 用于：已知 $a+b+c=0$ 的求值
~ ⚡ 第一反应：看到 $a+b+c=0$ 和立方和 → 等于 $3abc$

N R11 white alg ext | | 拉格朗日恒等式
- $(a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2$
~ 同见不等式大厦 R66：由 $(ad-bc)^2\ge 0$ 得柯西不等式
~ ⋯ 同源：模的乘法 $|z_1z_2|=|z_1||z_2|$〔R25〕
~ 用于：不等式大厦 R66（柯西不等式）
~ ⚡ 第一反应：看到两个平方和相乘 → 拆成两个平方和（柯西）

E S01 R01 derive main |
- 【展开】分配律用两次
E R01 R02 derive |
- 【展开】交叉项 $-ab+ab$ 抵消
E R01 R03 derive main |
- 【展开】两个交叉项合并成 $\pm 2ab$
- 减号：【代换】$b\to -b$
E R01 R04 derive |
- 【展开】9 项合并
E R03 R05 derive |
- 【展开】$(a+b)^2(a+b)$
- 差：【代换】$b\to -b$
E R01 R06 derive |
- 【展开验证】右边展开，中间项抵消
- 差：【代换】$b\to -b$
E R03 R07 derive |
- 【移项】展开后移项
E R05 R07 derive |
- 【移项】立方式
E R04 R07 derive |
- 【移项】三元式
E R01 R08 derive |
- 【逆用】展开式、乘法公式从右往左读
E R03 P01 derive main | ▼ 加条件〔定义域〕：$a\ne 0$
- 【配方法】提出 $a$，补上 $\left(\dfrac{b}{2a}\right)^2$ 再减去
E P01 P02 derive | ▼ 加条件〔定义域〕：$\Delta\ge 0$
- 【开平方】$\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}$
E P02 P03 derive main | ▼ 加条件〔定义域〕：$x_1,x_2$ 为两实根（$\Delta\ge 0$）
- 【代入】两根相加；两根相乘用平方差
E R02 P03 premise |
- 【前提】$\dfrac{(-b)^2-\Delta}{4a^2}=\dfrac{c}{a}$
E P03 P04 derive |
- 【展开】右边展开，用韦达对比系数
E R01 R09 derive |
- 【展开验证】相邻项错位抵消
E R01 R10 derive |
- 【展开验证】第二式用完全平方配成三个平方
E R01 R11 derive |
- 【展开】两边都是 $a^2c^2+a^2d^2+b^2c^2+b^2d^2$

# ───────── ② 指数与对数 ─────────
N S02 start exp | | 【定义】乘方与指数幂
- $a^n$：$n$ 个 $a$ 相乘（$n$ 为正整数）
- $a^0=1$，$a^{-n}=\dfrac{1}{a^n}$（$a\ne 0$）
- $a^{\frac{m}{n}}=\sqrt[n]{a^m}$（$a>0$；$m,n$ 为正整数，$n>1$）
- $a^{-\frac{m}{n}}=\dfrac{1}{a^{\frac{m}{n}}}$（$a>0$）
- 无理数指数幂（$a>0$）课本承认

N S03 start exp | | 【定义】对数
- $a>0$，$a\ne 1$，$N>0$ 时：$a^b=N\iff b=\log_a N$
- $\lg N=\log_{10}N$，$\ln N=\log_e N$

N R12 green exp | | ★ 指数运算律（正整数指数）
- $a^m\cdot a^n=a^{m+n}$，$(a^m)^n=a^{mn}$，$(ab)^n=a^nb^n$
~ 用于：指数函数性质、比大小（不等式大厦 P04）
~ ⚡ 第一反应：看到同底数幂相乘除、幂的乘方 → 先化成同底，再用指数运算律

N P41 orange exp | 〔定义域〕$a\ne 0,\ b\ne 0$ | ★ 整数指数幂运算律
- $a^m\div a^n=a^{m-n}$，$\left(\dfrac{a}{b}\right)^n=\dfrac{a^n}{b^n}$
- $m,n$ 为整数时，正整数指数的三条运算律仍成立
- ✗ $a=0$：$0^{-1}$ 无意义
~ ⚡ 第一反应：看到负指数、零指数 → $a^{-n}=\dfrac{1}{a^n}$，$a^0=1$

N P05 orange exp | 〔定义域〕$a>0,\ b>0$ | ★ 实数指数运算律
- $a^ra^s=a^{r+s}$，$(a^r)^s=a^{rs}$，$(ab)^r=a^rb^r$，$\dfrac{a^r}{a^s}=a^{r-s}$（$r,s\in\mathbb{R}$）
- ✗ 若允许负底数：$(-8)^{\frac{2}{6}}=\sqrt[6]{64}=2$，而 $(-8)^{\frac{1}{3}}=-2$，同一个数得出两个值
~ ⚡ 第一反应：看到分数、实数指数 → 先化成同底（底数 $>0$），再用指数运算律

N P43 orange exp | 〔定义域〕被开方数 $\ge 0$；〔符号分支〕开方要定号 | ★ 根式运算
- $\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}$（$a,b\ge 0$）；$\dfrac{\sqrt{a}}{\sqrt{b}}=\sqrt{\dfrac{a}{b}}$（$a\ge 0$，$b>0$）
- $(\sqrt{a})^2=a$（$a\ge 0$）；$\sqrt{a^2}=|a|$
- $n$ 次根式：$(\sqrt[n]{a})^n=a$；$\sqrt[n]{a^n}=a$（$n$ 奇），$\sqrt[n]{a^n}=|a|$（$n$ 偶）；例 $\sqrt[4]{(-3)^4}=3$
- ✗ $a=-3$：$\sqrt{(-3)^2}=3\ne -3$；$\sqrt{(-2)(-8)}=4$，但 $\sqrt{-2}$ 无意义
~ 用于：复数的模；含根式的化简
~ ⋯ 配合：已知一值求其余〔P46〕、升幂后开方〔R19〕都要定号
~ ⚡ 第一反应：看到根号 → 化成分数指数幂；开偶次方要带绝对值

N P44 lorange exp | 〔定义域〕$a,b\ge 0,\ a\ne b$ | 分母有理化
- $\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{a-b}$
~ 同见不等式大厦 P25、P54（根式裂项）
~ ⚡ 第一反应：分母是根式的和或差 → 乘它的“共轭”，用平方差

N P06 orange exp | 〔定义域〕$a>0,\ a\ne 1,\ N>0$ | ★ 对数恒等式
- $a^{\log_a N}=N$，$\log_a a^b=b$
- $\log_a 1=0$，$\log_a a=1$
- ✗ $N=-2$ 时 $\log_a N$ 无意义
~ ⚡ 第一反应：看到 $a^{\log_a N}$ 或 $\log_a a^b$ → 直接等于 $N$、$b$

N P07 orange exp | 〔定义域〕$M>0,\ N>0$ | ★★ 对数运算律
- $\log_a(MN)=\log_a M+\log_a N$
- $\log_a\dfrac{M}{N}=\log_a M-\log_a N$
- $\log_a M^n=n\log_a M$（$n\in\mathbb{R}$）
- ✗ $\log_2[(-2)(-4)]=3$ 有意义，$\log_2(-2)$ 无意义；$\log_a x^2=2\log_a|x|$（$x\ne 0$）
~ 同见不等式大厦 P21、P04
~ ⚡ 第一反应：看到同底对数相加减 → 合成积、商的对数

N P08 orange exp | 〔定义域〕$a,c>0$ 且 $\ne 1$，$b>0$ | ★ 换底公式
- $\log_a b=\dfrac{\log_c b}{\log_c a}$
~ 用于：对数式化简
~ ⚡ 第一反应：看到底数不同的对数 → 换成同底（常换成 lg 或 ln）

N P09 lorange exp | 〔定义域〕底数 $>0$ 且 $\ne 1$ | 换底推论
- $\log_a b\cdot\log_b a=1$（$a,b>0$ 且 $\ne 1$）
- $\log_{a^m}b^n=\dfrac{n}{m}\log_a b$（$m\ne 0$）
- 链式：$\log_a b\cdot\log_b c=\log_a c$（$c>0$）；例 $\log_2 3\cdot\log_3 8=\log_2 8=3$
~ 用于：对数式化简求值
~ ⚡ 第一反应：看到 $\log_a b\cdot\log_b c$ 连乘 → 链式相消

N P10 orange exp | 〔定义域〕$a>0,\ a\ne 1$ | ★ 指数函数与对数函数互为反函数
- $y=a^x$ 与 $y=\log_a x$ 的图像关于 $y=x$ 对称
- $\log_a(a^x)=x$（$x\in\mathbb{R}$），$a^{\log_a x}=x$（$x>0$）
- 特例：$e^x$ 与 $\ln x$
~ ⋯ 互逆：指数式 ⟷ 对数式
~ 用于：指数、对数函数的图像与性质
~ ⚡ 第一反应：指数式和对数式要互相转化 → 指对互化

E S02 R12 derive main |
- 【数个数】$m$ 个 $a$ 再乘 $n$ 个 $a$，共 $m+n$ 个
E S01 R12 premise |
- 【前提】结合律、交换律重排
E S03 P06 derive main | ▼ 加条件〔定义域〕：$a>0,\ a\ne 1,\ N>0$
- 【代入】把 $b=\log_a N$ 代回 $a^b=N$
E P05 P07 derive main |
- 【设】$M=a^p$，$N=a^q$：积 $a^pa^q=a^{p+q}$；商 $a^p\div a^q=a^{p-q}$；幂 $(a^p)^n=a^{pn}$，再取对数
E P06 P07 premise |
- 【前提】指数式与对数式互化
E P07 P08 derive |
- 【设】$\log_a b=x\Rightarrow a^x=b$，两边取 $\log_c$
- $x\log_c a=\log_c b$；$a\ne 1\Rightarrow\log_c a\ne 0$，两边同除
E P08 P09 derive |
- 【代入】都换成以 $c$ 为底
E P06 P10 derive |
- 【逆运算】指数式与对数式互化

# ───────── ③ 三角 ─────────
N S04 start tri | | 【定义】三角函数（单位圆）
- 角 $\alpha$ 终边与单位圆交于 $P(x,y)$
- $\sin\alpha=y$，$\cos\alpha=x$，$\tan\alpha=\dfrac{y}{x}$（$x\ne 0$）
- 终边上任一点 $P(x,y)$（非原点），$r=\sqrt{x^2+y^2}$：$\sin\alpha=\dfrac{y}{r}$，$\cos\alpha=\dfrac{x}{r}$，$\tan\alpha=\dfrac{y}{x}$；单位圆是 $r=1$ 的特例（相似三角形）
- 终边相同的角 $\alpha+2k\pi$（$k\in\mathbb{Z}$）三角函数值相同

N S05 start vec | | 【定义】向量数量积
- $\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$（$\theta\in[0,\pi]$ 为夹角）
- 交换律、数乘结合律、分配律（课本给出）
- 单位正交基：$\vec i\cdot\vec i=\vec j\cdot\vec j=1$，$\vec i\cdot\vec j=0$
- 线性运算（加减、数乘、坐标、共线）见起点〔S21〕；B 版先学线性运算（必修二），再学数量积（必修三）
- $\vec a\cdot\vec a=|\vec a|^2$；$\vec e$ 为单位向量时 $\vec a\cdot\vec e=|\vec a|\cos\langle\vec a,\vec e\rangle$

N S06 start cpx | | 【定义】复数
- $i^2=-1$；$z=a+bi$（$a,b\in\mathbb{R}$）；$a+bi=c+di\iff a=c$ 且 $b=d$
- $z$ ↔ 点 $(a,b)$ ↔ 向量；模 $|z|=\sqrt{a^2+b^2}$，共轭 $\bar z=a-bi$
- 加、乘按多项式运算，运算律照常成立；相反数 $-z=-a-bi$，减法 $z_1-z_2=(a-c)+(b-d)i$
- 乘法公式照常成立：$(z_1+z_2)^2=z_1^2+2z_1z_2+z_2^2$，$z_1^2-z_2^2=(z_1+z_2)(z_1-z_2)$
- ✗ $\sqrt{a}$ 只用于 $a\ge 0$：$\sqrt{-1}\times\sqrt{-4}=\sqrt{4}=2$ 是错的（应为 $i\cdot 2i=-2$）

N S11 start cpx ext | | 【承认】欧拉公式
- $e^{i\theta}=\cos\theta+i\sin\theta$；$\theta=\pi$ 时 $e^{i\pi}+1=0$
- 要用级数或复变函数才能证明，高中只承认
~ ⋯ 同源：三角形式乘法“辐角相加”与 $e^ae^b=e^{a+b}$ 是同一件事〔R26〕
~ 用于：拓展——复数的乘方、三角恒等式的另一种推法

N R13 green tri | | ★★★ 勾股恒等式
- $\sin^2\alpha+\cos^2\alpha=1$
~ 同见不等式大厦 R01、R02、R03
~ ⚡ 第一反应：看到 $\sin^2$、$\cos^2$ 同时出现，或已知一个求另一个 → 勾股恒等式

N P11 lorange tri | 〔定义域〕$\cos\alpha\ne 0$ | 商数关系
- $\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- ✗ $\alpha=\dfrac{\pi}{2}$：$\cos\alpha=0$，两边都无意义
~ ⚡ 第一反应：看到 tan 与 sin、cos 混在一起 → 切化弦

N P12 lorange tri | 〔定义域〕$\cos\alpha\ne 0$ | 正切与余弦
- $1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$
~ 同见不等式大厦 P16
~ 用于：已知 $\tan\alpha$ 求 $\cos^2\alpha$；不等式大厦 P16
~ ⚡ 第一反应：看到 $1+\tan^2\alpha$ 或 $\dfrac{1}{\cos^2\alpha}$ → 互化

N R14 green tri | | ★★ 诱导公式（sin、cos 对任意实数 $\alpha$ 成立）
- ① $\alpha+2k\pi$：值不变
- ② $\sin(\pi+\alpha)=-\sin\alpha$，$\cos(\pi+\alpha)=-\cos\alpha$
- ③ $\sin(-\alpha)=-\sin\alpha$，$\cos(-\alpha)=\cos\alpha$
- ④ $\sin(\pi-\alpha)=\sin\alpha$，$\cos(\pi-\alpha)=-\cos\alpha$
- ⑤ $\sin\left(\dfrac{\pi}{2}-\alpha\right)=\cos\alpha$，$\cos\left(\dfrac{\pi}{2}-\alpha\right)=\sin\alpha$
- ⑥ $\sin\left(\dfrac{\pi}{2}+\alpha\right)=\cos\alpha$，$\cos\left(\dfrac{\pi}{2}+\alpha\right)=-\sin\alpha$
- ⑦ $\sin\left(\dfrac{3\pi}{2}-\alpha\right)=-\cos\alpha$，$\cos\left(\dfrac{3\pi}{2}-\alpha\right)=-\sin\alpha$
- ⑧ $\sin\left(\dfrac{3\pi}{2}+\alpha\right)=-\cos\alpha$，$\cos\left(\dfrac{3\pi}{2}+\alpha\right)=\sin\alpha$（B 版：①～⑧都称诱导公式）
~ 口诀“奇变偶不变，符号看象限”（把 $\alpha$ 看作锐角定符号）只用于记忆，不是条件
~ ⚡ 第一反应：看到 $\pi\pm\alpha$、$\dfrac{\pi}{2}\pm\alpha$、$-\alpha$ → 诱导公式化成锐角

N P13 lorange tri | 〔定义域〕两边的 tan 都有定义 | tan 的诱导公式
- $\tan(\pi+\alpha)=\tan\alpha$，$\tan(-\alpha)=-\tan\alpha$，$\tan(\pi-\alpha)=-\tan\alpha$
- $\tan\left(\dfrac{\pi}{2}-\alpha\right)=\dfrac{1}{\tan\alpha}$（$\alpha\ne\dfrac{k\pi}{2}$）
~ 用于：含 tan 的化简求值
~ ⚡ 第一反应：看到 $\tan(\pi\pm\alpha)$ 等 → tan 的诱导公式

N P46 orange tri | 〔符号分支〕± 由 $\alpha$ 所在象限定 | ★ 已知一个三角函数值求其余
- $\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，$\cos\alpha=\pm\sqrt{1-\sin^2\alpha}$，再 $\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- ✗ $\cos\alpha=\dfrac{3}{5}$ 且 $\alpha$ 在第四象限：$\sin\alpha=-\dfrac{4}{5}$，取 $+\dfrac{4}{5}$ 就错
~ ⚡ 第一反应：已知一个三角函数值求其余 → 勾股开方，按象限定号

N R38 green tri | | ★ 同角关系的常用变形
- $(\sin\alpha\pm\cos\alpha)^2=1\pm 2\sin\alpha\cos\alpha=1\pm\sin 2\alpha$
- “1”的代换：$1=\sin^2\alpha+\cos^2\alpha$
~ ⚡ 第一反应：看到 $\sin\alpha\pm\cos\alpha$ 与 $\sin\alpha\cos\alpha$ → 两边平方互求

N P47 lorange tri | 〔定义域〕$\cos\alpha\ne 0$，分母 $\ne 0$ | 弦化切（齐次式）
- $\dfrac{a\sin\alpha+b\cos\alpha}{c\sin\alpha+d\cos\alpha}=\dfrac{a\tan\alpha+b}{c\tan\alpha+d}$
- $\sin\alpha\cos\alpha=\dfrac{\tan\alpha}{1+\tan^2\alpha}$，$\sin^2\alpha=\dfrac{\tan^2\alpha}{1+\tan^2\alpha}$
- ✗ $\alpha=\dfrac{\pi}{2}$ 时 $\cos\alpha=0$，不能同除
~ ⚡ 第一反应：已知 $\tan\alpha$ 求 sin、cos 的齐次式 → 弦化切

N R15 green vec | | ★★ 数量积坐标式
- $\vec a=(x_1,y_1)$，$\vec b=(x_2,y_2)\Rightarrow\vec a\cdot\vec b=x_1x_2+y_1y_2$
- $|\vec a|^2=x_1^2+y_1^2$
~ 同见不等式大厦 R16
~ ⚡ 第一反应：已知坐标求数量积 → 坐标式

N R16 green tri | | ★★★ 两角差的余弦
- $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
~ ⚡ 第一反应：看到两角差的余弦，或能把角拆成已知角的差 → 两角差余弦

N R17 green tri | | ★★ 其余和差角
- $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$
- $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
~ ⚡ 第一反应：看到两角和差，或角能拆成已知角的和差 → 和差角公式（拆角配角）

N P14 lorange tri | 〔定义域〕三个 tan 都有定义 | 两角和差的正切
- $\tan(\alpha\pm\beta)=\dfrac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$
- 变形：$\tan\alpha+\tan\beta=\tan(\alpha+\beta)(1-\tan\alpha\tan\beta)$
- $\tan\left(\dfrac{\pi}{4}\pm\theta\right)=\dfrac{1\pm\tan\theta}{1\mp\tan\theta}=\dfrac{\cos\theta\pm\sin\theta}{\cos\theta\mp\sin\theta}$（教材例题）
- ✗ $\alpha=\beta=\dfrac{\pi}{4}$：$\tan(\alpha+\beta)$ 无定义，右边分母 $1-1=0$
~ 用于：解析几何——两直线夹角 $\tan\theta=\left|\dfrac{k_2-k_1}{1+k_1k_2}\right|$
~ ⚡ 第一反应：看到 tan 的和差，或 $\tan\alpha+\tan\beta$ 与 $\tan\alpha\tan\beta$ 同时出现 → 正切和角

N R18 green tri | | ★★ 倍角
- $\sin 2\alpha=2\sin\alpha\cos\alpha$
- $\cos 2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$
~ 同见不等式大厦 R02
~ 用于：三角函数的图像与性质
~ ⚡ 第一反应：看到 $2\alpha$ 与 $\alpha$ 同时出现 → 倍角

N P15 lorange tri | 〔定义域〕$\tan\alpha$、$\tan 2\alpha$ 有定义 | 正切倍角
- $\tan 2\alpha=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$
- 即 $\alpha\ne\dfrac{\pi}{2}+k\pi$ 且 $\alpha\ne\dfrac{\pi}{4}+\dfrac{k\pi}{2}$
~ 用于：已知 $\tan\alpha$ 求 $\tan 2\alpha$
~ ⚡ 第一反应：已知 $\tan\alpha$ 求 $\tan 2\alpha$ → 正切倍角

N R19 white tri | | 降幂
- $\cos^2\alpha=\dfrac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\dfrac{1-\cos 2\alpha}{2}$
- $\sin\alpha\cos\alpha=\dfrac{1}{2}\sin 2\alpha$
- 升幂：$1+\cos 2\alpha=2\cos^2\alpha$，$1-\cos 2\alpha=2\sin^2\alpha$
~ ⋯ 配合：$\sqrt{1+\cos 2\alpha}=\sqrt{2}|\cos\alpha|$，开方要用〔P43〕定号
~ ⚡ 第一反应：求周期、最值、单调性时看到 $\sin^2$、$\cos^2$ → 降幂；看到 $1\pm\cos 2\alpha$ → 升幂

N P16 orange tri | 〔符号分支〕± 由 $\frac{\alpha}{2}$ 所在象限定 | ★ 半角
- $\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$，$\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$
- $\tan\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{1+\cos\alpha}}$（$\cos\alpha\ne -1$，± 同样按象限定）
- ✗ $\alpha=300^\circ$：$\cos 150^\circ=-\dfrac{\sqrt{3}}{2}$，取正号得 $+\dfrac{\sqrt{3}}{2}$，错
- $\tan\dfrac{\alpha}{2}=\dfrac{\sin\alpha}{1+\cos\alpha}=\dfrac{1-\cos\alpha}{\sin\alpha}$（无 ±；前式 $\cos\alpha\ne -1$，后式 $\sin\alpha\ne 0$）
~ 用于：求 $15^\circ$、$22.5^\circ$ 等的值
~ ⚡ 第一反应：求 $\dfrac{\alpha}{2}$ 的三角函数值 → 半角（定号）

N R20 white tri | | 积化和差
- $\sin\alpha\cos\beta=\dfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$
- $\cos\alpha\cos\beta=\dfrac{1}{2}[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$
- $\cos\alpha\sin\beta=\dfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)]$
- $\sin\alpha\sin\beta=-\dfrac{1}{2}[\cos(\alpha+\beta)-\cos(\alpha-\beta)]$
~ 用于：三角式的积和互化、证明
~ ⚡ 第一反应：看到两个三角函数相乘要化成和 → 积化和差

N R21 white tri | | 和差化积
- $\sin\theta+\sin\varphi=2\sin\dfrac{\theta+\varphi}{2}\cos\dfrac{\theta-\varphi}{2}$
- $\sin\theta-\sin\varphi=2\cos\dfrac{\theta+\varphi}{2}\sin\dfrac{\theta-\varphi}{2}$
- $\cos\theta+\cos\varphi=2\cos\dfrac{\theta+\varphi}{2}\cos\dfrac{\theta-\varphi}{2}$
- $\cos\theta-\cos\varphi=-2\sin\dfrac{\theta+\varphi}{2}\sin\dfrac{\theta-\varphi}{2}$
~ ⋯ 互逆：积化和差〔R20〕
~ 用于：三角式的积和互化、证明
~ ⚡ 第一反应：看到两个三角函数相加减要化成积 → 和差化积

N P17 orange tri | 〔定义域〕$a,b$ 不全为 0；〔符号分支〕$\varphi$ 由 $a,b$ 正负定 | ★★ 辅助角
- $a\sin x+b\cos x=\sqrt{a^2+b^2}\,\sin(x+\varphi)$
- $\cos\varphi=\dfrac{a}{\sqrt{a^2+b^2}}$，$\sin\varphi=\dfrac{b}{\sqrt{a^2+b^2}}$
- ✗ $a=b=-1$ 应取 $\varphi=\dfrac{5\pi}{4}$；只看 $\tan\varphi=1$ 取 $\dfrac{\pi}{4}$，得 $\sin x+\cos x$，错
~ 同见不等式大厦 R13
~ ⋯ 配合：先降幂〔R19〕、倍角〔R18〕，再辅助角
~ ⚡ 第一反应：看到同角的 $a\sin\omega x+b\cos\omega x$ → 辅助角化成一个正弦

N P18 lorange tri ext | 〔定义域〕$\alpha\ne\pi+2k\pi$ | 万能公式
- 令 $t=\tan\dfrac{\alpha}{2}$：$\sin\alpha=\dfrac{2t}{1+t^2}$，$\cos\alpha=\dfrac{1-t^2}{1+t^2}$
- $\tan\alpha=\dfrac{2t}{1-t^2}$（还要 $t^2\ne 1$）
~ 用于：三角式化成有理式（换元）
~ ⚡ 第一反应：要把三角式化成 $\tan\dfrac{\alpha}{2}$ 的有理式 → 万能公式（拓展）

N P19 lorange vec | 〔结构前提〕$A+B+C=\pi$ | 三角形内角关系
- $\sin(A+B)=\sin C$，$\cos(A+B)=-\cos C$
- $\sin\dfrac{A+B}{2}=\cos\dfrac{C}{2}$
- $\cos\dfrac{A+B}{2}=\sin\dfrac{C}{2}$；$\tan(A+B)=-\tan C$（$C\ne\dfrac{\pi}{2}$）
- 教材例题：$\sin A+\sin B+\sin C=4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\cos\dfrac{C}{2}$（和差化积 + $\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$）
~ 用于：三角形中的化简
~ ⚡ 第一反应：三角形中出现 $A+B$ → 换成 $\pi-C$

N P20 lorange vec | 〔结构前提〕$a,b$ 夹角 $C$ | 三角形面积
- $S=\dfrac{1}{2}ab\sin C=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B$
- 拓展：$\overrightarrow{OA}=(x_1,y_1)$，$\overrightarrow{OB}=(x_2,y_2)$：$S_{\triangle OAB}=\dfrac{1}{2}|x_1y_2-x_2y_1|$（必修三拓展阅读）
- ✗ 直角边 $a=b=1$、$C=90^\circ$：$S=\dfrac{1}{2}$；误用非夹角 $A=45^\circ$ 得 $\dfrac{\sqrt{2}}{4}$
~ ⚡ 第一反应：求三角形面积 → $\dfrac{1}{2}ab\sin C$

N P21 orange vec | 〔结构前提〕同一三角形的边与对角 | ★★ 正弦定理
- $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$（$R$ 为外接圆半径；“$=2R$”是教材探索题）
- 推论：$a=2R\sin A$，$a:b:c=\sin A:\sin B:\sin C$（边角互化）
- 推论：$a>b\iff A>B\iff\sin A>\sin B$（大边对大角）
- 拓展：$S=\dfrac{abc}{4R}$
- ✗ $a=2$，$b=1$，$A=B=60^\circ$ 不来自同一三角形：$\dfrac{a}{\sin A}\ne\dfrac{b}{\sin B}$
~ 用于：不等式大厦 R13（三角形中求最值）
~ ⋯ 配合：余弦定理〔P22〕做边角互化
~ ⚡ 第一反应：已知两角一边，或边角混在一起（各项中边的次数相同）→ 正弦定理边角互化

N P22 orange vec | 〔结构前提〕$a$ 为 $A$ 的对边，$b,c$ 夹 $A$ | ★★ 余弦定理
- $a^2=b^2+c^2-2bc\cos A$（其余两式同理）
- 推论 $\cos A=\dfrac{b^2+c^2-a^2}{2bc}$（已知三边求角）；$A=90^\circ$ 时即勾股定理
- 射影定理 $a=b\cos C+c\cos B$（必修四 9.1.2 例 5，可反推余弦定理）
- ✗ 3、4、5 的直角三角形 $A=90^\circ$，误把 $a$ 取成 3（不是 $A$ 的对边）：右边 $=4^2+5^2-0=41$，左边 $=9$
~ ⋯ 同源：勾股恒等式〔R13〕
~ ⚡ 第一反应：已知三边，或两边及夹角 → 余弦定理

N P48 lorange vec ext | 〔结构前提〕$a,b,c$ 为三角形三边 | 海伦公式
- $S=\sqrt{p(p-a)(p-b)(p-c)}$，$p=\dfrac{a+b+c}{2}$
- 秦九韶三斜求积：$S=\sqrt{\dfrac{1}{4}\left[c^2a^2-\left(\dfrac{c^2+a^2-b^2}{2}\right)^2\right]}$（必修四拓展阅读，与海伦公式等价）
~ ⚡ 第一反应：已知三边求面积 → 海伦公式（拓展）

N P49 orange vec | 〔定义域〕夹角公式要求 $\vec a,\vec b\ne\vec 0$ | ★★ 数量积的运算公式
- $|\vec a\pm\vec b|^2=|\vec a|^2\pm 2\vec a\cdot\vec b+|\vec b|^2$；$(\vec a+\vec b)\cdot(\vec a-\vec b)=|\vec a|^2-|\vec b|^2$
- $\vec a\perp\vec b\iff\vec a\cdot\vec b=0$（规定零向量与任意向量垂直）；$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$
- 坐标：$\vec a\parallel\vec b\iff x_1y_2-x_2y_1=0$；$\vec a\perp\vec b\iff x_1x_2+y_1y_2=0$
- $\cos\theta=\dfrac{x_1x_2+y_1y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}$
- ✗ $\vec b=\vec 0$ 时夹角无定义，$\cos\theta$ 的分母为 0
~ 同见不等式大厦 R16、R27
~ 用于：解析几何中的垂直、夹角
~ ⋯ 同源：完全平方〔R03〕、平方差〔R02〕
~ ⚡ 第一反应：模 → 平方；夹角 → $\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；垂直 → $\vec a\cdot\vec b=0$

N R22 white cpx | | 复数乘法
- $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$
~ ⚡ 第一反应：复数相乘 → 展开，用 $i^2=-1$

N R23 green cpx | | ★ 共轭与模
- $z\bar z=|z|^2=a^2+b^2$；$z+\bar z=2a$，$z-\bar z=2bi$
- $\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$，$\overline{z_1z_2}=\bar z_1\bar z_2$，$\overline{\left(\dfrac{z_1}{z_2}\right)}=\dfrac{\bar z_1}{\bar z_2}$
- $z\ne 0$ 时 $\dfrac{1}{z}=\dfrac{\bar z}{|z|^2}$
~ ⚡ 第一反应：求 $|z|$、$z\bar z$ → 共轭相乘

N P23 lorange cpx | 〔定义域〕$c+di\ne 0$ | 复数除法
- $\dfrac{a+bi}{c+di}=\dfrac{(ac+bd)+(bc-ad)i}{c^2+d^2}$
- ✗ $c=d=0$ 时分母为 0
~ 用于：复数计算
~ ⚡ 第一反应：复数除法 → 分母实数化

N R24 white cpx | | $i^n$ 以 4 为周期
- $i^1=i$，$i^2=-1$，$i^3=-i$，$i^4=1$；$i^{n+4}=i^n$
- 复数乘方：$z^mz^n=z^{m+n}$，$(z^m)^n=z^{mn}$，$(z_1z_2)^n=z_1^nz_2^n$；$z\ne 0$ 时 $z^0=1$，$z^{-n}=\dfrac{1}{z^n}$
- $(1+i)^2=2i$，$(1-i)^2=-2i$，$\dfrac{1+i}{1-i}=i$（教材例题）
~ 用于：复数的高次幂
~ ⚡ 第一反应：看到 $i$ 的高次幂 → 指数除以 4 看余数

N R25 white cpx | | 模的乘法
- $|z_1z_2|=|z_1||z_2|$
- $|\bar z|=|z|$；$|z_1-z_2|$ = 复平面上两点间的距离（$|z-z_0|=r$ 表示圆）
~ ⋯ 同源：拉格朗日恒等式〔R11〕
~ 用于：复数求模
~ ⚡ 第一反应：求积的模 → 模相乘；看到 $|z-z_0|$ → 两点距离

N P24 orange cpx | 〔定义域〕$z\ne 0$；〔符号分支〕$\theta$ 由 $a,b$ 正负定 | ★ 三角形式
- $z=a+bi=r(\cos\theta+i\sin\theta)$，$r=|z|$
- $\cos\theta=\dfrac{a}{r}$，$\sin\theta=\dfrac{b}{r}$
- $\theta$ 可加 $2k\pi$；辐角主值取 $[0,2\pi)$
- $\bar z=r[\cos(-\theta)+i\sin(-\theta)]$，$\dfrac{1}{z}=\dfrac{1}{r}[\cos(-\theta)+i\sin(-\theta)]$
- ✗ $z=-1-i$：只看 $\tan\theta=1$ 取 $\dfrac{\pi}{4}$，得 $1+i\ne z$
~ ⚡ 第一反应：复数化三角形式 → 求 $r$，按 $a,b$ 正负定辐角

N R26 green cpx | | ★★ 三角形式乘法
- $r_1(\cos\theta_1+i\sin\theta_1)\cdot r_2(\cos\theta_2+i\sin\theta_2)$
- $=r_1r_2[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)]$
- 模相乘，辐角相加
- 几何意义：乘 $r_2(\cos\theta_2+i\sin\theta_2)$ = 把 $\overrightarrow{OZ_1}$ 绕原点逆时针转 $\theta_2$、模变为 $r_2$ 倍；乘 $i$ 即逆时针转 $\dfrac{\pi}{2}$
- ✗ 辐角主值不能直接相加：$z_1=z_2=-1$，主值都是 $\pi$，相加得 $2\pi$，而 $\arg(1)=0$
~ ⚡ 第一反应：三角形式相乘 → 模相乘、辐角相加

N P25 lorange cpx | 〔定义域〕$z_2\ne 0$ | 三角形式除法
- $\dfrac{z_1}{z_2}=\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]$
~ 用于：复数计算

N R27 green cpx | | ★ 棣莫弗公式
- $[r(\cos\theta+i\sin\theta)]^n=r^n(\cos n\theta+i\sin n\theta)$（$n$ 为正整数；教材习题推广到一切整数 $n$，$z\ne 0$）
~ 教材必修四 10.3
~ 用于：复数的乘方、方根
~ ⚡ 第一反应：复数的高次幂 → 先看能否用 $(1\pm i)^2=\pm 2i$ 或 $i^n$ 的周期；不行再化三角形式用棣莫弗

E S04 R13 derive main |
- 【代入】$P(\cos\alpha,\sin\alpha)$ 在单位圆 $x^2+y^2=1$ 上
E S04 P11 derive | ▼ 加条件〔定义域〕：$\cos\alpha\ne 0$
- 【定义】$\tan\alpha=\dfrac{y}{x}$
E R13 P12 derive |
- 【同除】两边除以 $\cos^2\alpha$
E P11 P12 premise |
- 【前提】$\dfrac{\sin\alpha}{\cos\alpha}=\tan\alpha$
E S04 R14 derive main |
- 【对称】终边关于原点、$x$ 轴、$y$ 轴、$y=x$ 对称
- 交点 $(x,y)$ 变为 $(-x,-y)$、$(x,-y)$、$(-x,y)$、$(y,x)$
- ⑥：⑤ 中 $\alpha\to-\alpha$，再用 ③；⑦⑧：$\dfrac{3\pi}{2}\pm\alpha=\pi+\left(\dfrac{\pi}{2}\pm\alpha\right)$，用 ② 再用 ⑤⑥
E R14 P13 derive | ▼ 加条件〔定义域〕：两边的 tan 都有定义
- 【相除】sin 式除以 cos 式
E S05 R15 derive main |
- 【展开】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$
- 分配律展开，$\vec i\cdot\vec j=0$
E R01 R15 premise |
- 【前提】与多项式乘法同样逐项展开
E R15 R16 derive main |
- 【数量积】$\overrightarrow{OA}=(\cos\alpha,\sin\alpha)$，$\overrightarrow{OB}=(\cos\beta,\sin\beta)$
- 按坐标 $=\cos\alpha\cos\beta+\sin\alpha\sin\beta$；按定义 $=\cos\theta$
E R14 R16 premise |
- 【前提】$\alpha-\beta=\pm\theta+2k\pi$，由 ①③ 得 $\cos(\alpha-\beta)=\cos\theta$
E R16 R17 derive main |
- 【代换】$\beta\to -\beta$ 得 $\cos(\alpha+\beta)$
- $\sin(\alpha+\beta)=\cos\left[\left(\dfrac{\pi}{2}-\alpha\right)-\beta\right]$ 再展开
E R14 R17 premise |
- 【前提】诱导公式 ③⑤
E R17 P14 derive | ▼ 加条件〔定义域〕：三个 tan 都有定义
- 【相除】分子、分母同除 $\cos\alpha\cos\beta$
E R17 R18 derive main |
- 【特例】令 $\beta=\alpha$
E R13 R18 premise |
- 【前提】用 $\sin^2\alpha+\cos^2\alpha=1$ 换成单一函数
E P14 P15 derive |
- 【特例】令 $\beta=\alpha$
E R18 R19 derive |
- 【移项】再两边除以 2
E R19 P16 derive | ▼ 加条件〔符号分支〕：± 由 $\frac{\alpha}{2}$ 所在象限定
- 【代换】$\alpha\to\dfrac{\alpha}{2}$ 后开平方
- tan 式：前式分子、分母同乘 $2\cos\dfrac{\alpha}{2}$，后式同乘 $2\sin\dfrac{\alpha}{2}$
E R17 R20 derive |
- 【相加减】两个和差角公式相加或相减
E R20 R21 derive |
- 【代换】令 $\alpha+\beta=\theta$，$\alpha-\beta=\varphi$
E R17 P17 derive main | ▼ 加条件〔定义域〕〔符号分支〕：$a,b$ 不全为 0；$\varphi$ 看 $a,b$ 正负
- 【提取】提出 $r=\sqrt{a^2+b^2}$，倒用 sin 和角公式
E R13 P17 premise |
- 【前提】$\left(\dfrac{a}{r}\right)^2+\left(\dfrac{b}{r}\right)^2=1$，故有 $\varphi$
E R18 P18 derive | ▼ 加条件〔定义域〕：$\alpha\ne\pi+2k\pi$
- 【同除】$\sin\alpha=\dfrac{2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}}{\sin^2\frac{\alpha}{2}+\cos^2\frac{\alpha}{2}}$，同除 $\cos^2\dfrac{\alpha}{2}$
E R14 P19 derive | ▼ 加条件〔结构前提〕：$A+B+C=\pi$
- 【代换】$A+B=\pi-C$，用 ④
- $\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$，用 ⑤
E S04 P20 derive | ▼ 加条件〔结构前提〕：$a,b$ 夹角 $C$
- 【定义】高 $h=b\sin C$
- $C$ 为钝角时 $h=b\sin(\pi-C)=b\sin C$（用 ④）
E R14 P20 premise |
- 【前提】诱导公式 ④
E P20 P21 derive main |
- 【面积法】三式相等，同除 $\dfrac{1}{2}abc$
- $=2R$：作直径 $BD$，$\angle BCD=90^\circ$，$\angle BDC$ 与 $A$ 相等或互补，$a=2R\sin\angle BDC=2R\sin A$
- $A=90^\circ$ 时 $BC$ 就是直径，$a=2R$ 直接成立
E S06 R22 derive main |
- 【展开】用 $i^2=-1$ 合并
E R01 R22 premise |
- 【前提】多项式乘法展开
E R22 R23 derive |
- 【展开】$(a+bi)(a-bi)=a^2-(bi)^2=a^2+b^2$
E R02 R23 premise |
- 【前提】与平方差同型
E R23 P23 derive | ▼ 加条件〔定义域〕：$c+di\ne 0$
- 【分母实数化】分子、分母同乘 $c-di$
E S06 R24 derive |
- 【代入】$i^4=(i^2)^2=1$
E R12 R24 premise |
- 【前提】指数运算律
E R23 R25 derive |
- 【代入】$|z_1z_2|^2=z_1z_2\cdot\overline{z_1z_2}=(z_1\bar z_1)(z_2\bar z_2)$，再开方
E S06 P24 derive | ▼ 加条件〔定义域〕〔符号分支〕：$z\ne 0$；$\theta$ 看 $a,b$ 正负
- 【单位圆】$\left(\dfrac{a}{r},\dfrac{b}{r}\right)$ 在单位圆上
E S04 P24 premise |
- 【前提】单位圆定义
E P24 R26 derive main |
- 【展开】实部、虚部分别合并
E R17 R26 derive main |
- 【和角】实部 $\cos(\theta_1+\theta_2)$，虚部 $\sin(\theta_1+\theta_2)$
E R26 P25 derive | ▼ 加条件〔定义域〕：$z_2\ne 0$
- 【逆运算】商乘 $z_2$ 等于 $z_1$
E R26 R27 derive |
- 【归纳法】$n=k$ 成立时再乘一次
E S10 R27 premise |
- 【前提】数学归纳法

# ───────── ④ 数列 ─────────
N S09 start seq | | 【定义】数列
- $S_n=a_1+a_2+\cdots+a_n$
- 等差：$a_{n+1}-a_n=d$（常数）
- 等比：$\dfrac{a_{n+1}}{a_n}=q$（常数，$a_n\ne 0$，$q\ne 0$）

N S10 start base | | 【公理】数学归纳法
- $n=n_0$ 成立；$n=k$ 成立 $\Rightarrow n=k+1$ 成立
- $\Rightarrow$ 对一切 $n\ge n_0$ 成立
~ 同见不等式大厦 P23（伯努利归纳步）

N R28 green seq | | ★ 累加相消
- $(b_2-b_1)+(b_3-b_2)+\cdots+(b_{n+1}-b_n)=b_{n+1}-b_1$
~ ⚡ 第一反应：看到“相邻项相减”的和 → 累加相消

N P50 orange seq | 〔定义域〕$n\ge 2$，$n=1$ 单独验证 | ★★ 累加法、累乘法（求通项）
- $a_{n+1}-a_n=f(n)\Rightarrow a_n=a_1+\displaystyle\sum_{k=1}^{n-1}f(k)$
- $\dfrac{a_{n+1}}{a_n}=g(n)\Rightarrow a_n=a_1\displaystyle\prod_{k=1}^{n-1}g(k)$（$a_n\ne 0$）
- 等差、等比的通项是 $f(n)=d$、$g(n)=q$ 的特例
~ ⚡ 第一反应：看到 $a_{n+1}-a_n=f(n)$ → 累加；$\dfrac{a_{n+1}}{a_n}=g(n)$ → 累乘

N P51 lorange seq | 〔结构前提〕等差、等比 | 等差中项、等比中项
- $a,b,c$ 成等差 $\iff 2b=a+c$
- $a,b,c$ 成等比 $\Rightarrow b^2=ac$（反过来还要 $a,b,c\ne 0$）
- $x,y$ 的等比中项 $G=\pm\sqrt{xy}$（$xy>0$）
- ✗ $0,0,0$ 满足 $b^2=ac$，但不是等比数列
~ ⚡ 第一反应：三个数成等差或等比 → 中项（等比中项 $G^2=ab$，要求 $ab>0$）

N P26 orange seq | 〔结构前提〕等差数列 | ★ 等差通项
- $a_n=a_1+(n-1)d$，$a_n=a_m+(n-m)d$
- $d=\dfrac{a_n-a_m}{n-m}$（$n\ne m$）：点 $(n,a_n)$ 连线的斜率；$\{a_n\}$ 等差 $\iff a_n=kn+b$（$k=d$）
~ ⚡ 第一反应：已知等差数列的两项 → $a_n=a_m+(n-m)d$ 求公差

N P27 lorange seq | 〔结构前提〕等差数列 | 等差下标性质
- $m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$
- ✗ 1, 2, 4, 7 不是等差：$a_1+a_4=8$，$a_2+a_3=6$
~ ⚡ 第一反应：等差数列中下标和相等 → 两项之和相等

N P28 orange seq | 〔结构前提〕等差数列 | ★★ 等差求和
- $S_n=\dfrac{n(a_1+a_n)}{2}=na_1+\dfrac{n(n-1)}{2}d$
- $S_n=\dfrac{d}{2}n^2+\left(a_1-\dfrac{d}{2}\right)n$；反过来 $S_n=An^2+Bn\iff\{a_n\}$ 等差
- ✗ $S_n=n^2+1$ 常数项不为 0：$a_1=2$，$a_2=3$，$a_3=5$，不是等差
- $S_{2n-1}=(2n-1)a_n$；两等差数列 $\dfrac{a_n}{b_n}=\dfrac{S_{2n-1}}{T_{2n-1}}$
- 拓展：$\left\{\dfrac{S_n}{n}\right\}$ 也是等差数列，公差 $\dfrac{d}{2}$
- ✗ 1, 2, 4, 7：$S_4=14$，而 $\dfrac{4\times(1+7)}{2}=16$
~ ⚡ 第一反应：等差求和：知首末项用 $\dfrac{n(a_1+a_n)}{2}$；项数为奇数的前 $n$ 项和（如 $S_9=9a_5$）想到 $S_{2n-1}=(2n-1)a_n$

N R29 white seq | | 自然数求和
- $1+2+\cdots+n=\dfrac{n(n+1)}{2}$
- $a_k=k$ 本身是等差数列，无需另加条件
~ ⚡ 第一反应：看到 $1+2+\cdots+n$ → $\dfrac{n(n+1)}{2}$

N P29 orange seq | 〔结构前提〕等比数列 | ★ 等比通项
- $a_n=a_1q^{n-1}$
- $a_n=a_mq^{n-m}$（$n<m$ 时用整数指数）
- $\{a_n\}$ 等比 $\iff a_n=kq^n$（$k,q$ 为非零常数）；$a_n>0$ 时 $\{\lg a_n\}$ 是等差数列（公差 $\lg q$）
~ ⚡ 第一反应：已知等比数列的两项 → $a_n=a_mq^{n-m}$ 求公比

N P30 lorange seq | 〔结构前提〕等比数列 | 等比下标性质
- $m+n=p+q\Rightarrow a_ma_n=a_pa_q$
- ✗ 1, 2, 4, 7：$a_1a_4=7$，$a_2a_3=8$
~ 用于：等比数列的性质速算
~ ⚡ 第一反应：等比数列中下标和相等 → 两项之积相等

N P31 orange seq | 〔结构前提〕等比数列；〔定义域〕$q\ne 1$ | ★★ 等比求和
- $q\ne 1$：$S_n=\dfrac{a_1(1-q^n)}{1-q}$；$q=1$：$S_n=na_1$
- $q\ne 1$ 时 $S_n=Aq^n-A$，$A=\dfrac{a_1}{q-1}$
- 另一形式：$q\ne 1$ 时 $S_n=\dfrac{a_1-a_nq}{1-q}$（已知 $a_1,q,a_n$ 时直接用）
- ✗ $q=1$ 时分母为 0
~ 同见不等式大厦 P13
~ 用于：差比数列求和
~ ⚡ 第一反应：等比求和 → 先看 $q$ 是否为 1

N P54 lorange seq | 〔结构前提〕等差、等比 | 片段和（选必三复习题）
- 等差：$S_m,\ S_{2m}-S_m,\ S_{3m}-S_{2m}$ 成等差（公差 $m^2d$）
- 等比：片段和都不为 0 时成等比（公比 $q^m$）
- ✗ $q=-1$，$m=2$：片段和都是 0，$0,0,0$ 不是等比数列
~ ⚡ 第一反应：等差、等比的前 $m$、$2m$、$3m$ 项和 → 片段和

N P32 lorange seq | 〔定义域〕$n\ge 2$ | $a_n$ 与 $S_n$
- $a_1=S_1$；$n\ge 2$ 时 $a_n=S_n-S_{n-1}$
- ✗ $S_n=n^2+1$：$a_1=2$，而 $2n-1$ 在 $n=1$ 时得 1
~ 用于：已知 $S_n$ 求 $a_n$
~ ⚡ 第一反应：给出 $S_n$ 求 $a_n$ → 作差，$n=1$ 单独验证

N P52 orange seq | 〔结构前提〕$c_n=a_nb_n$，等差×等比；〔定义域〕$q\ne 1$ | ★ 差比数列求和（错位相减）
- 例：$\displaystyle\sum_{k=1}^{n}k\,q^{k-1}=\dfrac{1-(n+1)q^n+nq^{n+1}}{(1-q)^2}$
- 核对 $n=1$：$\dfrac{1-2q+q^2}{(1-q)^2}=1$
- ✗ $q=1$ 时分母为 0，应为 $\sum k=\dfrac{n(n+1)}{2}$
~ ⋯ 配合：等比求和〔P31〕
~ ⚡ 第一反应：通项是“等差 × 等比” → 错位相减

N R30 green seq | | ★ 裂项
- $\dfrac{1}{k(k+1)}=\dfrac{1}{k}-\dfrac{1}{k+1}$（$k$ 为正整数）
- $\displaystyle\sum_{k=1}^{n}\dfrac{1}{k(k+1)}=1-\dfrac{1}{n+1}$
~ 同见不等式大厦 P24
~ ⋯ 配合：累加相消〔R28〕
~ ⚡ 第一反应：通项是 $\dfrac{1}{k(k+1)}$ → 裂项相消

N P53 orange seq | 〔定义域〕$d\ne 0$；根式形 $k\ge 0$ | ★ 裂项的其他形式
- $\dfrac{1}{k(k+d)}=\dfrac{1}{d}\left(\dfrac{1}{k}-\dfrac{1}{k+d}\right)$
- $\dfrac{1}{\sqrt{k}+\sqrt{k+1}}=\sqrt{k+1}-\sqrt{k}$
- 一般：$\{a_n\}$ 等差、$d\ne 0$、各项 $\ne 0$：$\dfrac{1}{a_ka_{k+1}}=\dfrac{1}{d}\left(\dfrac{1}{a_k}-\dfrac{1}{a_{k+1}}\right)$；例 $\dfrac{1}{(2k-1)(2k+1)}=\dfrac{1}{2}\left(\dfrac{1}{2k-1}-\dfrac{1}{2k+1}\right)$
~ 同见不等式大厦 P25、P54、P55
~ ⚡ 第一反应：通项是 $\dfrac{1}{a_ka_{k+1}}$ 或 $\dfrac{1}{\sqrt{k}+\sqrt{k+1}}$ → 裂项

N R31 green seq | | ★ 平方和
- $1^2+2^2+\cdots+n^2=\dfrac{n(n+1)(2n+1)}{6}$
~ 用于：数列求和、放缩估计
~ ⚡ 第一反应：看到 $1^2+2^2+\cdots$ → 平方和公式

N R32 white seq | | 立方和
- $1^3+2^3+\cdots+n^3=\left[\dfrac{n(n+1)}{2}\right]^2=(1+2+\cdots+n)^2$
~ ⋯ 同源：平方和〔R31〕
~ 用于：数列求和
~ ⚡ 第一反应：看到 $1^3+2^3+\cdots$ → 立方和公式

E S01 R28 derive |
- 【结合律】相邻项抵消
E S09 P26 derive main | ▼ 加条件〔结构前提〕：等差数列
- 【累加】$(n-1)$ 个 $d$ 相加
E P26 P27 derive |
- 【代入】两边都等于 $2a_1+(m+n-2)d$
E P27 P28 derive main |
- 【倒序相加】正写、倒写各一遍，对应项和都等于 $a_1+a_n$
E P28 R29 derive |
- 【特例】$a_1=1$，$d=1$
E S09 P29 derive main | ▼ 加条件〔结构前提〕：等比数列
- 【累乘】$(n-1)$ 个 $q$ 相乘
E P29 P30 derive |
- 【代入】两边都等于 $a_1^2q^{m+n-2}$
E P29 P31 derive main | ▼ 加条件〔定义域〕：$q\ne 1$
- 【错位相减】$S_n-qS_n=a_1-a_1q^n$，两边除以 $1-q$
E R09 P31 premise |
- 【因式分解】$1-q^n=(1-q)(1+q+\cdots+q^{n-1})$（另一路）
E S09 P32 derive | ▼ 加条件〔定义域〕：$n\ge 2$（$S_n$ 公式代入 $n=0$ 不为 0 时，$n=1$ 不能合并）
- 【作差】$S_n-S_{n-1}$
E R28 R30 derive |
- 【通分验证】右边通分；求和用累加相消
E R05 R31 derive main |
- 【累加相消】$(k+1)^3-k^3=3k^2+3k+1$，$k$ 从 1 加到 $n$
- $(n+1)^3-1=3\sum k^2+\dfrac{3n(n+1)}{2}+n$，解出 $\sum k^2$
E R28 R31 premise |
- 【前提】累加相消
E R29 R31 premise |
- 【前提】$\sum k=\dfrac{n(n+1)}{2}$
E R29 R32 derive |
- 【归纳法】$\left[\dfrac{k(k+1)}{2}\right]^2+(k+1)^3=\dfrac{(k+1)^2(k+2)^2}{4}$
E S10 R32 premise |
- 【前提】数学归纳法

# ───────── ⑤ 计数 ─────────
N S07 start base | | 【原理】两个计数原理
- 分类加法：各类方法数相加
- 分步乘法：各步方法数相乘

N P33 lorange cnt | 〔定义域〕$m\le n$（自然数） | 排列数
- $A_n^m=n(n-1)\cdots(n-m+1)=\dfrac{n!}{(n-m)!}$（$0!=1$；约定 $A_n^0=C_n^0=1$）
- $A_n^m+mA_n^{m-1}=A_{n+1}^m$（教材例题：按是否含某个元素分类）
~ ⚡ 第一反应：从 $n$ 个中选 $m$ 个排成一列（有序）→ 排列数

N P34 orange cnt | 〔定义域〕$0\le m\le n$ | ★★ 组合数
- $C_n^m=\dfrac{A_n^m}{m!}=\dfrac{n!}{m!(n-m)!}$
~ ⚡ 第一反应：只选不排（无序）→ 组合数

N P35 lorange cnt | 〔定义域〕下标范围见各式 | 组合数性质
- $C_n^m=C_n^{n-m}$（$0\le m\le n$）
- $C_{n+1}^m=C_n^m+C_n^{m-1}$（$1\le m\le n$，杨辉三角的递推）
~ 用于：组合数化简、证明
~ ⚡ 第一反应：组合数化简 → 对称性、杨辉三角递推

N R33 green cnt | | ★★★ 二项式定理
- $(a+b)^n=\displaystyle\sum_{k=0}^{n}C_n^k a^{n-k}b^k$（$n$ 为正整数）
- 通项 $T_{k+1}=C_n^k a^{n-k}b^k$
~ 同见不等式大厦 P26（伯努利不等式）
~ ⋯ 配合：区分二项式系数〔R34〕与项的系数〔R39〕
~ ⚡ 第一反应：看到 $(a+b)^n$ 展开、求某一项 → 通项 $T_{k+1}$

N R34 white cnt | | 二项式系数性质
- $C_n^0+C_n^1+\cdots+C_n^n=2^n$
- 奇数项的二项式系数和 = 偶数项的二项式系数和 $=2^{n-1}$（$n\ge 1$）
- 注意：二项式系数 $C_n^k$ 不等于项的系数〔R39〕
~ ⚡ 第一反应：求二项式系数和 → $2^n$

N R39 green cnt | | ★ 展开式的各项系数和
- $f(x)=a_0+a_1x+\cdots+a_nx^n$：$a_0+a_1+\cdots+a_n=f(1)$，$a_0-a_1+a_2-\cdots=f(-1)$
- 偶次项系数和 $=\dfrac{f(1)+f(-1)}{2}$，奇次项 $=\dfrac{f(1)-f(-1)}{2}$，常数项 $a_0=f(0)$
- 例 $(2x-1)^5$：各项系数和 $=1$，二项式系数和 $=2^5=32$
~ ⚡ 第一反应：求展开式各项系数和 → 赋值 $x=1$、$-1$、$0$

N P36 lorange cnt ext | 〔定义域〕$1\le k\le n$ | 组合数的提取
- $kC_n^k=nC_{n-1}^{k-1}$
~ 用于：组合数求和
~ ⚡ 第一反应：看到 $kC_n^k$ → 提取成 $nC_{n-1}^{k-1}$

E S07 P33 derive main | ▼ 加条件〔定义域〕：$m\le n$
- 【分步计数】第 1 位 $n$ 种，第 2 位 $n-1$ 种……相乘
E P33 P34 derive main |
- 【分步计数】先选 $m$ 个再排列：$A_n^m=C_n^m\cdot m!$
E P34 P35 derive |
- 【对应】选出 $m$ 个 ⟺ 留下 $n-m$ 个
- 【分类计数】某个指定元素选或不选
E P34 R33 derive main |
- 【分步计数】$n$ 个 $(a+b)$ 相乘，每个括号选 $a$ 或 $b$
- 恰好选 $k$ 个 $b$ 有 $C_n^k$ 种
E R01 R33 premise |
- 【前提】多项式乘法逐项展开
E R33 R34 derive |
- 【赋值】令 $a=b=1$；令 $a=1,\ b=-1$ 得交错和为 0
E P34 P36 derive |
- 【代入】公式化简；或【双计数】选 $k$ 人委员会再选主席
E R33 R05 premise |
- 【特例】$n=3$（另一路）

# ───────── ⑥ 导数 ─────────
N S08 start der | | 【定义】导数
- $f'(x_0)=\displaystyle\lim_{\Delta x\to 0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$

N S12 start der | | 【课本给出】导数表与链式法则
- $C'=0$；$(\sin x)'=\cos x$，$(\cos x)'=-\sin x$；$(e^x)'=e^x$（$x\in\mathbb{R}$）
- $(x^\alpha)'=\alpha x^{\alpha-1}$（$\alpha$ 为任意实数时取 $x>0$；$\alpha$ 为正整数时 $x\in\mathbb{R}$）
- $(a^x)'=a^x\ln a$（$a>0$，$x\in\mathbb{R}$）
- $(\log_a x)'=\dfrac{1}{x\ln a}$（$a>0,\ a\ne 1,\ x>0$）；$(\ln x)'=\dfrac{1}{x}$（$x>0$）
- 有定义不等于可导：$\sqrt{x}$ 在 $x=0$ 有定义，但没有有限导数
- 链式法则：$g$ 在 $x$ 处可导、$f$ 在 $u=g(x)$ 处可导 $\Rightarrow y'_x=f'(u)\cdot g'(x)$
~ 课本直接给出（链式法则课本写“可以证明”）；B 版先给 $(a^x)'$、$(\log_a x)'$，再令 $a=e$；下面的 R35、P39、P40 只说明由来（拓展）
~ ⚡ 第一反应：求基本初等函数的导数 → 查表；复合函数 → 链式法则

N S13 start base | | 【初中定理】平面几何基础
- 勾股定理 $a^2+b^2=c^2$（直角三角形，$c$ 为斜边）；两点距离 $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$（B 版另用向量 $\overrightarrow{AB}$ 的模重新推出〔R41〕〔R15〕）
- 三角形面积 $=\dfrac{1}{2}\times$ 底 $\times$ 高
- 圆周角定理：同弧所对的圆周角相等；直径所对的圆周角是直角（课本承认）
- 垂径定理：圆心到弦的垂线平分弦；圆的切线垂直于过切点的半径

N R35 white der ext | | 正整数幂求导的由来
- $(x^n)'=nx^{n-1}$（$n$ 为正整数，$x\in\mathbb{R}$）
~ 用于：多项式函数求导

N P37 orange der | 〔定义域〕$u,v$ 在该点可导 | ★★ 和、差、积的求导法则
- $(u\pm v)'=u'\pm v'$
- $(uv)'=u'v+uv'$
- $(Cu)'=Cu'$（积法则加 $C'=0$）
- ✗ $u=|x|$，$v=-|x|$，$x=0$：$(u+v)'=0$，右边 $u'$、$v'$ 不存在
~ 用于：切线、单调性、极值
~ ⚡ 第一反应：看到函数的和、差、积 → 和差积法则

N P38 orange der | 〔定义域〕$u,v$ 可导，$v(x)\ne 0$ | ★ 商的求导法则
- $\left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^2}$（同时得出 $\dfrac{u}{v}$ 可导）
- 特例：$\left(\dfrac{1}{g}\right)'=-\dfrac{g'}{g^2}$
- ✗ $v(x)=0$ 时 $\dfrac{u}{v}$ 在该点无定义
~ 用于：不等式大厦 P05（构造函数判单调）；切线、单调性、极值
~ ⚡ 第一反应：看到分式函数 → 商法则

N P39 lorange der ext | 〔定义域〕$x>0$ | $(\ln x)'$ 的由来
- $(\ln x)'=\dfrac{1}{x}$

N P40 lorange der ext | 〔定义域〕$a>0,\ a\ne 1$；对数式 $x>0$ | 一般指数、对数求导的由来
- $(a^x)'=a^x\ln a$，$(\log_a x)'=\dfrac{1}{x\ln a}$
~ 用于：一般指数、对数函数求导
~ ⚡ 第一反应：底数不是 $e$ 的指数、对数 → $a^x\ln a$、$\dfrac{1}{x\ln a}$

N P55 orange der | 〔定义域〕各式括号内 | ★ 常用导数
- $\left(\dfrac{1}{x}\right)'=-\dfrac{1}{x^2}$（$x\ne 0$）；$(\sqrt{x})'=\dfrac{1}{2\sqrt{x}}$（$x>0$）
- $(e^{ax+b})'=ae^{ax+b}$；$[\ln(ax+b)]'=\dfrac{a}{ax+b}$（$ax+b>0$）
- $(\tan x)'=\dfrac{1}{\cos^2x}$（$\cos x\ne 0$；教材例题：商法则 + $\sin^2x+\cos^2x=1$）
- ✗ $(\sqrt{x})'$ 在 $x=0$ 处不存在
~ ⚡ 第一反应：看到 $\dfrac{1}{x}$、$\sqrt{x}$、$e^{ax+b}$、$\ln(ax+b)$ → 常用导数

E S08 R35 derive |
- 【按定义】$\dfrac{(x+\Delta x)^n-x^n}{\Delta x}=nx^{n-1}+C_n^2x^{n-2}\Delta x+\cdots$，令 $\Delta x\to 0$
E R33 R35 derive |
- 【二项式展开】$(x+\Delta x)^n$
E S08 P37 derive main | ▼ 加条件〔定义域〕：$u,v$ 在该点可导
- 【配凑】$u(x+\Delta x)v(x+\Delta x)-u(x)v(x)$
- $=[u(x+\Delta x)-u(x)]v(x+\Delta x)+u(x)[v(x+\Delta x)-v(x)]$
- $v$ 可导 $\Rightarrow v$ 连续（课本承认）
E S08 P38 derive | ▼ 加条件〔定义域〕：$v(x)\ne 0$
- 【通分】【配凑】差商 $=\dfrac{\frac{u(x+\Delta x)-u(x)}{\Delta x}v(x)-u(x)\frac{v(x+\Delta x)-v(x)}{\Delta x}}{v(x+\Delta x)v(x)}$
- $v$ 连续且 $v(x)\ne 0$：$\Delta x$ 足够小时 $v(x+\Delta x)\ne 0$；令 $\Delta x\to 0$
E P37 P38 premise |
- 【前提】$u,v$ 可导，配凑手法同积法则
E P10 P39 derive main |
- 【链式法则】对 $\ln(e^x)=x$ 两边求导：$(\ln)'(e^x)\cdot e^x=1$
- 令 $u=e^x$：$(\ln u)'=\dfrac{1}{u}$，$u$ 取遍 $(0,+\infty)$
E S12 P39 premise |
- 【前提】链式法则；$\ln x$ 可导由导数表给出
E P05 P40 derive |
- 【代换】$a^x=e^{x\ln a}$，用链式法则
E P08 P40 derive |
- 【代换】换底：$\log_a x=\dfrac{\ln x}{\ln a}$
E P39 P40 premise |
- 【前提】$(\ln x)'=\dfrac{1}{x}$
E S01 R36 derive |
- 【逆用】分配律：乘 $-1$ 去括号；合并同类项即分配律倒用
E S01 R37 derive |
- 【分类讨论】按 $a,b$ 正负分四种情况
E S01 P42 derive | ▼ 加条件〔定义域〕：分母 $\ne 0$
- 【通分】除以 $b$ 即乘 $\dfrac{1}{b}$；约分即分子、分母同除非零式
E P03 P45 derive main | ▼ 加条件〔定义域〕：两实根，$\Delta\ge 0$
- 【代入】韦达代入互换式
E R07 P45 premise |
- 【前提】互换式
E P02 P04 premise |
- 【因式分解】求出两根后写成 $a(x-x_1)(x-x_2)$（另一路）
E R12 P41 derive main | ▼ 加条件〔定义域〕：$a\ne 0,\ b\ne 0$
- 【代入】零指数、负指数的定义
E S02 P41 premise |
- 【前提】$a^0=1$，$a^{-n}=\dfrac{1}{a^n}$
E P41 P05 derive main | ▼ 加条件〔定义域〕：$a>0,\ b>0$
- 【推广】由整数指数推广；有理、实数指数课本说明运算律仍成立
E P05 P43 derive | ▼ 加条件〔定义域〕〔符号分支〕：被开方数 $\ge 0$；$\sqrt{a^2}=|a|$
- 【特例】取 $r=\dfrac{1}{2}$；算术平方根非负
E P43 P44 derive | ▼ 加条件〔定义域〕：$a,b\ge 0,\ a\ne b$
- 【同乘】分子、分母同乘 $\sqrt{a}-\sqrt{b}$
E R02 P44 premise |
- 【前提】分母用平方差
E R13 P46 derive | ▼ 加条件〔符号分支〕：± 按象限定
- 【移项】【开平方】
E P43 P46 premise |
- 【前提】$\sqrt{a^2}=|a|$，开方要定号
E R18 R38 derive |
- 【展开】完全平方展开；$2\sin\alpha\cos\alpha=\sin 2\alpha$
E R13 R38 premise |
- 【前提】$\sin^2\alpha+\cos^2\alpha=1$ 合并
E R03 R38 premise |
- 【前提】完全平方
E P11 P47 derive | ▼ 加条件〔定义域〕：$\cos\alpha\ne 0$
- 【同除】分子、分母同除 $\cos\alpha$；二次式先用“1”的代换再同除 $\cos^2\alpha$
E R13 P47 premise |
- 【前提】$1=\sin^2\alpha+\cos^2\alpha$
E S13 P21 premise |
- 【前提】圆周角定理：$\angle BDC$ 与 $A$ 相等或互补
E S05 P49 derive main | ▼ 加条件〔定义域〕：夹角公式要求非零向量
- 【展开】前两式用分配律，与完全平方、平方差同型
- 垂直、夹角：由数量积的定义变形
E P49 P22 derive main | ▼ 加条件〔结构前提〕：$a$ 为 $A$ 的对边
- 【向量】$\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$，用 $|\vec a-\vec b|^2$ 展开
- $|\overrightarrow{BC}|^2=b^2+c^2-2bc\cos A$
E P20 P48 derive | ▼ 加条件〔结构前提〕：$a,b,c$ 为三边
- 【代入】$S^2=\dfrac{1}{4}a^2b^2(1-\cos^2C)$，$\cos C$ 用余弦定理推论，两次平方差
E P22 P48 premise |
- 【前提】$\cos C=\dfrac{a^2+b^2-c^2}{2ab}$
E R02 P48 premise |
- 【前提】平方差分解
E R28 P50 derive main | ▼ 加条件〔定义域〕：$n\ge 2$
- 【累加相消】【累乘】
E P50 P26 premise |
- 【特例】$f(n)=d$
E P50 P29 premise |
- 【特例】$g(n)=q$
E S09 P51 derive | ▼ 加条件〔结构前提〕：等差、等比
- 【代入】$b-a=c-b$，$\dfrac{b}{a}=\dfrac{c}{b}$
E P31 P52 derive | ▼ 加条件〔结构前提〕〔定义域〕：等差×等比；$q\ne 1$
- 【错位相减】$S-qS=\sum q^{k-1}-nq^n$，再用等比求和
E R30 P53 derive | ▼ 加条件〔定义域〕：$d\ne 0$
- 【推广】通分验证
E P44 P53 premise |
- 【同乘】根式形用分母有理化
E P28 P54 derive |
- 等差：【作差】相邻片段和相减
E R33 R39 derive |
- 【赋值】令 $x=1,\ -1,\ 0$
E S12 P55 derive | ▼ 加条件〔定义域〕：各式括号内
- 【特例】$\alpha=-1,\ \dfrac{1}{2}$；【链式法则】$u=ax+b$
E S01 S02 define |
- 【定义】乘方 = $n$ 个相同因数连乘
E S02 S03 define |
- 【定义】对数是指数的逆运算
E S13 S04 define |
- 【定义】单位圆 $x^2+y^2=1$（勾股定理）；三角函数 = 单位圆上点的坐标
E S01 S05 define |
- 【定义】坐标运算用实数运算律
E S01 S06 define |
- 【定义】把实数运算律推广到含 $i$ 的数
E S01 S09 define |
- 【定义】$S_n$ = 前 $n$ 项连加
E S01 S08 define |
- 【定义】差商 = 作差再相除，再取极限（极限课本承认）
E S08 S12 define |
- 【课本给出】按定义求出的结果列成表
E S06 S11 define |
- 【承认】把指数推广到虚数（拓展）
E S13 R13 premise |
- 【前提】单位圆方程由勾股定理得到
E S13 P20 premise |
- 【前提】面积 $=\dfrac{1}{2}\times$ 底 $\times$ 高
E P42 P14 premise |
- 【前提】分子、分母同除非零式
E P42 P47 premise |
- 【前提】分子、分母同除非零式
E P42 R30 premise |
- 【前提】通分
E P42 P31 premise |
- 【前提】两边除以 $1-q$
E P42 P23 premise |
- 【前提】分式化简（分母 $\ne 0$）
E P42 P38 premise |
- 【前提】分式化简（分母 $\ne 0$）
E P43 P02 premise |
- 【前提】开平方
E P43 P16 premise |
- 【前提】开平方要定号

N Q01 problem alg | | 看到：求方程 $ax^2+bx+c=0$ 的根
- 路径：① 试十字相乘〔R08〕→ ② 拆不开用求根公式〔P02〕（或配方〔P01〕）
- 注意：$a\ne 0$；$\Delta<0$ 无实根
~ 同见二次函数大厦 J04、J05

N Q02 problem alg | | 看到：解二次不等式
- 路径：① 化 $a>0$（乘 $-1$ 变号）→ ② 因式分解〔R08〕或求根〔P02〕→ ③ 看区间正负
- 注意：$\Delta\le 0$ 时单独看
~ 同见不等式大厦 R43；二次函数大厦 R09

N Q03 problem alg | | 看到：求二次函数的零点
- 路径：写成交点式〔P04〕（十字相乘〔R08〕或求根公式〔P02〕）
- 注意：$\Delta<0$ 时无零点
~ 同见二次函数大厦 R08

N Q04 problem alg | | 看到：含参数的二次式
- 路径：① 把参数拆进因式〔R08〕→ ② 比较两根大小，分类讨论
- 注意：两根相等的参数值单独看
~ 同见二次函数大厦 R10

N Q05 problem alg | | 看到：已知两根，写方程或解析式
- 路径：交点式〔P04〕逆用：根 → 因式 → 展开〔R01〕；或用韦达〔P03〕
- 注意：二次项系数 $a\ne 0$ 要保留

N Q06 problem alg | | 看到：高次式分解、降次
- 路径：① 试根：首项系数为 1 时试常数项的因数；一般试 $\pm\dfrac{p}{q}$（$p$ 整除常数项，$q$ 整除首项系数）
- ② $f(r)=0\Rightarrow f(x)$ 含因式 $x-r$，用分组或待定系数提出 → ③ 剩下的二次式再十字相乘〔R08〕
- 立方〔R06〕、$x^n-1$〔R09〕直接套
- 注意：整数根试不出时，未必不能分解
~ 同见不等式大厦 R25（穿根法）

N Q07 problem alg | | 看到：二次式对一切 $x$ 恒成立
- 路径：$a\ne 0$ 时，$ax^2+bx+c\ge 0$ 恒成立 $\iff a>0$ 且 $\Delta\le 0$（判别式〔P02〕）
- 注意：$a$ 含参数时先讨论 $a=0$；整数范围分解不出来不代表无实根，要看 $\Delta$
~ 同见二次函数大厦 P08；不等式大厦 R30

N Q08 problem alg | | 看到：求二次式的最值、值域
- 路径：配方〔P01〕，读出顶点
- 注意：限定区间时看对称轴位置
~ 同见二次函数大厦 P03、P05；不等式大厦 R23

N Q09 problem alg | | 看到：不解方程求两根的式子
- 路径：① 韦达〔P03〕→ ② 代入互换式〔R07〕，即〔P45〕
- 注意：先验 $\Delta\ge 0$

N Q10 problem alg | | 看到：已知 $a+b$、$ab$（或 $a+b+c$ 等），求对称式
- 路径：互换式〔R07〕、三数和的平方〔R04〕、三元立方和〔R10〕
- 倒数型：$x^2+\dfrac{1}{x^2}=\left(x+\dfrac{1}{x}\right)^2-2$；$x+\dfrac{1}{x}=3\Rightarrow x^2+\dfrac{1}{x^2}=7$

N Q11 problem alg | | 看到：分式化简求值
- 路径：① 分子、分母因式分解〔R08〕〔R02〕〔R06〕→ ② 约分、通分〔P42〕
- 注意：约掉的因式 $\ne 0$，化简后标注取值限制

N Q12 problem alg | | 看到：整式化简、简便计算
- 路径：去括号〔R36〕、乘法公式〔R02〕〔R03〕，整体代入

N Q13 problem alg | | 看到：证明代数恒等式
- 路径：两边展开〔R01〕或分解〔R08〕，左右化归、作差为 0
- 注意：每一步要等价

N Q14 problem alg | | 看到：比较大小、证明不等式
- 路径：① 作差 → ② 因式分解〔R08〕或配方〔R03〕→ ③ 定号
- 注意：因式的正负要逐个判断
~ 同见不等式大厦 S01、R37、P27

N Q15 problem alg | | 看到：根的符号、根的分布
- 路径：韦达〔P03〕+ 判别式〔P02〕
- 注意：两正根要同时满足三个条件
~ 同见二次函数大厦 R11、P10

N Q16 problem alg | | 看到：解析几何中的弦长
- 路径：① 联立消元 → ② 韦达〔P03〕→ ③ $|x_1-x_2|$〔P45〕→ ④ 乘 $\sqrt{1+k^2}$
- 注意：消元后二次项系数 $\ne 0$ 且 $\Delta>0$；斜率不存在时直接用 $|y_1-y_2|$
~ 用于：解析几何（圆锥曲线）
~ 同见解析几何〔Q91〕：圆锥曲线的弦长、中点

E R08 Q01 apply |
- 【分解后令每个因式 $=0$】$x^2-5x+6=(x-2)(x-3)=0\Rightarrow x=2,3$
E P02 Q01 apply |
- 【十字相乘拆不开时用】$x^2-2x-1=0\Rightarrow x=1\pm\sqrt{2}$
E P01 Q01 apply |
- 【配成平方再开方】$x^2+6x+2=0\Rightarrow(x+3)^2=7\Rightarrow x=-3\pm\sqrt{7}$
E R08 Q02 apply |
- 【分解后看区间正负】$(x-2)(x-3)>0\Rightarrow x<2$ 或 $x>3$
E R08 Q03 apply |
- 【分解就是交点式】$y=(x-2)(x-3)$，零点 2、3 直接读出
E R08 Q04 apply |
- 【把参数拆进因式】$x^2-(a+1)x+a=(x-a)(x-1)$，再按 $a$ 与 1 的大小讨论
E P04 Q05 apply |
- 【逆用：根 → 因式 → 展开】根 $3,-5\Rightarrow y=a(x-3)(x+5)$，$a=1$ 时 $x^2+2x-15$
E P03 Q05 apply |
- 【用两根之和、之积写方程】$x^2-(3-5)x+3\times(-5)=x^2+2x-15$
E R08 Q06 apply |
- 【提出一个根，剩下的再十字相乘】$x^3-6x^2+11x-6=(x-1)(x^2-5x+6)=(x-1)(x-2)(x-3)$
E R06 Q06 apply |
- 【直接套立方公式】$x^3-8=(x-2)(x^2+2x+4)$
E R09 Q06 apply |
- 【提出 $x-1$】$x^4-1=(x-1)(x^3+x^2+x+1)=(x-1)(x+1)(x^2+1)$
E P02 Q07 apply |
- 【用判别式定参数范围】$x^2+mx+1\ge 0$ 恒成立 $\iff m^2-4\le 0\iff -2\le m\le 2$
E P01 Q08 apply |
- 【配方读顶点】$x^2-4x+5=(x-2)^2+1\ge 1$，$x=2$ 时取最小值 1
E P03 Q09 apply |
- 【两根和、积代入】$x^2-3x+1=0$（$\Delta=5>0$）：$x_1+x_2=3$，$x_1x_2=1$
E P45 Q09 apply |
- 【代入对称式公式】同上：$x_1^2+x_2^2=3^2-2\times 1=7$；$|x_1-x_2|=\sqrt{5}$
E R07 Q10 apply |
- 【化成 $a+b$ 与 $ab$】$a+b=3$，$ab=1\Rightarrow a^2+b^2=7$，$a^3+b^3=27-9=18$
E R04 Q10 apply |
- 【三数和的平方移项】$a+b+c=3$，$ab+bc+ca=1\Rightarrow a^2+b^2+c^2=9-2=7$
E R10 Q10 apply |
- 【$a+b+c=0$ 时立方和 $=3abc$】$a=1,b=2,c=-3$：$1+8-27=-18=3\times 1\times 2\times(-3)$
E P42 Q11 apply |
- 【先分解再约分】$\dfrac{x^2-4}{x^2+x-6}=\dfrac{x+2}{x+3}$（$x\ne 2$，$x\ne -3$）
E R02 Q11 apply |
- 【用平方差分解】$\dfrac{x^2-1}{x-1}=x+1$（$x\ne 1$）
E R06 Q11 apply |
- 【用立方差分解】$\dfrac{x^3-1}{x-1}=x^2+x+1$（$x\ne 1$）
E R02 Q12 apply |
- 【凑成“和×差”】$99\times 101=100^2-1=9999$
E R36 Q12 apply |
- 【去括号合并】$(a+b)^2-(a-b)^2=4ab$
E R01 Q13 apply |
- 【两边展开比较】验证 $(a+b)(a^2-ab+b^2)=a^3+b^3$
E R03 Q14 apply |
- 【作差后配成完全平方定号】$a^2+b^2-2ab=(a-b)^2\ge 0$
E R08 Q14 apply |
- 【作差后因式分解定号】$a^3+b^3-a^2b-ab^2=(a+b)(a-b)^2\ge 0$（$a+b\ge 0$）
E R11 Q14 apply |
- 【拆成两个平方和，去掉一项】$(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2$
E P03 Q15 apply |
- 【韦达加判别式列条件】$x^2-5x+m=0$ 有两正根 $\iff 25-4m\ge 0$ 且 $m>0\iff 0<m\le\dfrac{25}{4}$
E P45 Q16 apply |
- 【联立后求 $|x_1-x_2|$，再乘 $\sqrt{1+k^2}$】$y=x$ 与 $y=x^2-2$：$x^2-x-2=0$，$|x_1-x_2|=3$，弦长 $3\sqrt{2}$

E P41 P29 premise |
- 【前提】$q^0=1$，$q\cdot q^{n-2}=q^{n-1}$
E P29 P54 premise |
- 等比：【作比】$S_{2m}-S_m=q^mS_m$（每项乘 $q^m$）
E P06 P40 premise |
- 【前提】$a=e^{\ln a}$
E S12 P40 premise |
- 【前提】链式法则；$(e^x)'=e^x$
E P38 P55 premise |
- 【商法则】$\left(\dfrac{1}{x}\right)'=\dfrac{0\cdot x-1}{x^2}$，$x<0$ 时同样成立
E S04 R16 premise |
- 【前提】单位圆上的点 $(\cos\alpha,\sin\alpha)$
E R15 P49 premise |
- 【前提】坐标运算

N Q17 problem exp | | 看到：指数式、根式化简求值
- 路径：① 根式化成分数指数〔P43〕→ ② 同底合并〔P05〕
- 注意：底数 $a>0$

N Q18 problem exp | | 看到：已知 $a^{\frac{1}{2}}+a^{-\frac{1}{2}}$，求 $a+a^{-1}$ 等
- 路径：整体平方：完全平方〔R03〕+ 指数运算〔P05〕
- 注意：开方时注意正负

N Q19 problem exp | | 看到：对数式化简求值
- 路径：① 换底统一〔P08〕→ ② 合并〔P07〕→ ③ 对数恒等式〔P06〕；连乘用链式〔P09〕
- 注意：真数 $>0$，底数 $>0$ 且 $\ne 1$

N Q20 problem exp | | 看到：解指数方程
- 路径：① 化同底〔P05〕或换元 $t=a^x>0$ → ② 解二次方程〔R08〕→ ③ 指对互化〔P10〕
- 注意：换元后 $t>0$

N Q21 problem exp | | 看到：解对数方程
- 路径：① 先写定义域 → ② 合并〔P07〕→ ③ 指对互化〔P10〕→ ④ 检验
- 注意：合并后定义域可能变大，必须检验

N Q22 problem exp | | 看到：比较指数、对数的大小
- 路径：化同底看单调；找中间值 0、1〔P06〕；互为倒数〔P09〕
- 注意：底数 $>1$ 与 $0<$ 底数 $<1$ 单调性相反
~ 同见不等式大厦 P04

N Q23 problem exp | | 看到：含根式的化简、有理化
- 路径：分母有理化〔P44〕；$\sqrt{a^2}=|a|$ 定号〔P43〕
- 注意：去绝对值看正负
~ 同见不等式大厦 P25（根式裂项）

N Q24 problem exp | | 看到：已知 $a^x=b^y=c$ 型，求 $\dfrac{1}{x}+\dfrac{1}{y}$ 等
- 路径：① 指对互化〔P10〕→ ② 倒数关系〔P09〕→ ③ 合并〔P07〕
- 注意：$c\ne 1$（否则 $x=0$，没有倒数）

E P05 Q17 apply |
- 【同底合并】$a^{\frac{1}{2}}\cdot a^{\frac{1}{3}}\div a^{\frac{1}{6}}=a^{\frac{1}{2}+\frac{1}{3}-\frac{1}{6}}=a^{\frac{2}{3}}$
E P43 Q17 apply |
- 【根式化分数指数】$\sqrt[3]{a^2}\cdot\sqrt{a}=a^{\frac{2}{3}+\frac{1}{2}}=a^{\frac{7}{6}}$（$a>0$）
E P05 Q18 apply |
- 【整体平方】$a^{\frac{1}{2}}+a^{-\frac{1}{2}}=3\Rightarrow a+a^{-1}=9-2=7$，$a^2+a^{-2}=49-2=47$
E P08 Q19 apply |
- 【换成同底】$\log_4 8=\dfrac{\lg 8}{\lg 4}=\dfrac{3\lg 2}{2\lg 2}=\dfrac{3}{2}$
E P07 Q19 apply |
- 【合成积的对数】$\lg 2+\lg 5=\lg 10=1$
E P06 Q19 apply |
- 【直接取值】$2^{\log_2 5}=5$；$\log_3 81=\log_3 3^4=4$
E P09 Q19 apply |
- 【链式相消】$\log_2 3\cdot\log_3 4\cdot\log_4 8=\log_2 8=3$
E P05 Q20 apply |
- 【化同底后换元】$4^x-3\cdot 2^x+2=0$：$t=2^x>0$，$t^2-3t+2=0$，$t=1$ 或 2，$x=0$ 或 1
E P10 Q20 apply |
- 【指对互化】$2^x=3\Rightarrow x=\log_2 3$
E P07 Q21 apply |
- 【合并后去对数】$\log_2 x+\log_2(x-2)=3$：$x(x-2)=8$，$x=4$ 或 $-2$，舍 $-2$（真数要正）
E P10 Q21 apply |
- 【对数式化指数式】$\log_2(x+1)=3\Rightarrow x+1=8$，$x=7$
E P06 Q22 apply |
- 【找中间值】$\log_2 3>\log_2 2=1$，$\log_3 2<\log_3 3=1\Rightarrow\log_2 3>\log_3 2$
E P09 Q22 apply |
- 【互为倒数】$\log_2 3\cdot\log_3 2=1$
E P44 Q23 apply |
- 【乘共轭有理化】$\dfrac{1}{\sqrt{3}+\sqrt{2}}=\sqrt{3}-\sqrt{2}$
E P43 Q23 apply |
- 【开方定号】$\sqrt{(1-\sqrt{2})^2}=|1-\sqrt{2}|=\sqrt{2}-1$
E P10 Q24 apply |
- 【指对互化】$2^a=3^b=6\Rightarrow a=\log_2 6$，$b=\log_3 6$
E P09 Q24 apply |
- 【倒数关系再合并】$\dfrac{1}{a}+\dfrac{1}{b}=\log_6 2+\log_6 3=\log_6 6=1$

N Q25 problem tri | | 看到：已知一个三角函数值，求其余
- 路径：① 勾股开方〔P46〕→ ② 按象限定号 → ③ 切化弦求 tan〔P11〕
- 注意：先定 $\alpha$ 所在象限；象限未知时分两种情况讨论

N Q26 problem tri | | 看到：已知 $\tan\alpha$，求 sin、cos 的齐次式
- 路径：分子、分母同除 $\cos\alpha$（二次式先用“1”的代换）〔P47〕
- 注意：$\cos\alpha\ne 0$

N Q27 problem tri | | 看到：已知 $\sin\alpha\pm\cos\alpha$，求 $\sin\alpha\cos\alpha$ 或 $\sin 2\alpha$
- 路径：两边平方〔R38〕，用勾股恒等式〔R13〕合并
- 注意：反过来开方时按象限定号

N Q28 problem tri | | 看到：诱导公式化简求值
- 路径：负角化正角 → 大角减去 $2k\pi$ → 化成锐角〔R14〕
- 注意：“把 $\alpha$ 看作锐角”只是判断符号的办法，公式对任意 $\alpha$ 成立

N Q29 problem tri | | 看到：求 $15^\circ$、$75^\circ$ 等非特殊角的值
- 路径：拆成特殊角的和差〔R17〕；或用半角〔P16〕
~ 用于：特殊角值表 T1

N Q30 problem tri | | 看到：给值求值（已知 $\alpha$、$\alpha+\beta$ 的值求 $\beta$ 的值）
- 路径：配角 $\beta=(\alpha+\beta)-\alpha$〔R16〕〔R17〕
- 注意：先由角的范围定出所需正弦、余弦的符号

N Q31 problem tri | | 看到：三角函数的最值、周期、单调区间
- 路径：① 降幂〔R19〕、倍角〔R18〕→ ② 辅助角化成 $A\sin(\omega x+\varphi)+k$〔P17〕→ ③ 读出最值、周期 $T=\dfrac{2\pi}{|\omega|}$
- 单调区间：把 $\omega x+\varphi$ 当整体代入 $\sin$ 的单调区间（$\omega<0$ 先化正）；给定 $x$ 的区间时，先求 $\omega x+\varphi$ 的范围再定最值
- 注意：$\varphi$ 由 $a,b$ 的正负定
~ 同见不等式大厦 R13（三角有界）

N Q32 problem tri | | 看到：化简 $\sqrt{1\pm\sin 2\alpha}$、$\sqrt{1\pm\cos 2\alpha}$
- 路径：配成完全平方〔R38〕或升幂〔R19〕→ 开方带绝对值〔P43〕
- 注意：按 $\alpha$ 的范围去绝对值

N Q33 problem tri | | 看到：含 tan 的和角求值
- 路径：正切和角及其变形〔P14〕
- 注意：$\tan(\alpha+\beta)$ 要有定义

N Q34 problem tri | | 看到：三角函数的积与和互化（求值、证明）
- 路径：积化和差〔R20〕、和差化积〔R21〕

N Q35 problem tri | | 看到：求半角的三角函数值
- 路径：半角公式〔P16〕；tan 用无 ± 的有理式
- 注意：sin、cos 半角按 $\dfrac{\alpha}{2}$ 的象限定号

N Q36 problem vec | | 看到：解三角形——已知三边，或两边及夹角
- 路径：余弦定理〔P22〕求边或角
- 注意：求角用推论 $\cos A=\dfrac{b^2+c^2-a^2}{2bc}$，角唯一

N Q37 problem vec | | 看到：解三角形——已知两角一边，或边角混在一起
- 路径：正弦定理〔P21〕边角互化；内角和〔P19〕
- 注意：已知 $a,b,A$ 求 $B$：$\sin B$ 对应锐角、钝角两个值；$a\ge b$ 时只取锐角，$a<b$ 时两个都要检验 $A+B<\pi$，可能两解（例 $a=\sqrt{3}$，$b=2$，$A=45^\circ$ 有两解）

N Q38 problem vec | | 看到：求三角形面积
- 路径：$S=\dfrac{1}{2}ab\sin C$〔P20〕；已知三边可用海伦公式〔P48〕或先用余弦定理求角

N Q39 problem vec | | 看到：判断三角形的形状
- 路径：边角互化〔P21〕〔P22〕，化成只含边或只含角
- 注意：两边同除时注意除数 $\ne 0$；$\sin 2A=\sin 2B$ 有两种情况；$a^2+b^2>c^2$ 只说明 $C$ 是锐角，判断锐角三角形看最大边所对的角

N Q40 problem vec | | 看到：三角形中的三角式化简
- 路径：$A+B=\pi-C$〔P19〕，再用和差角〔R17〕

N Q41 problem vec | | 看到：向量的模、夹角、垂直
- 路径：模用平方〔P49〕；坐标已知用坐标式〔R15〕
- 注意：求夹角要非零向量；夹角为锐角 $\iff\vec a\cdot\vec b>0$ 且不同向，钝角同理要排除反向
~ 同见不等式大厦 R16、R27

N Q42 problem vec | | 看到：三角形中求边、周长、面积的最值或范围
- 路径：① 正弦定理边化角〔P21〕→ ② 和差角、辅助角化成一个三角函数〔P17〕→ ③ 由角的范围求最值；只求最值时也可用余弦定理〔P22〕+ 基本不等式
- 注意：角的范围要由三角形条件定出
~ 同见不等式大厦 R13

N Q43 problem cpx | | 看到：复数四则运算
- 路径：乘法展开〔R22〕；除法分母实数化〔P23〕
- 注意：$i^2=-1$

N Q44 problem cpx | | 看到：复数的模、共轭、几何意义
- 路径：$z\bar z=|z|^2$〔R23〕；积的模 = 模的积、$|z-z_0|$ 是距离〔R25〕

N Q45 problem cpx | | 看到：复数的高次幂
- 路径：$i^n$ 看指数除以 4 的余数〔R24〕；一般复数化三角形式用棣莫弗〔R27〕

N Q46 problem cpx | | 看到：复数的三角形式与乘除
- 路径：求模 $r$、按 $a,b$ 正负定辐角〔P24〕→ 模相乘、辐角相加〔R26〕；除法：模相除、辐角相减〔P25〕
- 注意：辐角可加 $2k\pi$；三角形式要求 $r>0$，写成 $\cos\theta+i\sin\theta$（同角、中间是加号）

E P46 Q25 apply |
- 【勾股开方定号】$\cos\alpha=\dfrac{3}{5}$，$\alpha$ 在第四象限 $\Rightarrow\sin\alpha=-\dfrac{4}{5}$
E P11 Q25 apply |
- 【切化弦】$\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}=-\dfrac{4}{3}$
E P47 Q26 apply |
- 【同除 $\cos\alpha$】$\tan\alpha=2$：$\dfrac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}=\dfrac{2+1}{2-1}=3$；$\sin\alpha\cos\alpha=\dfrac{2}{1+4}=\dfrac{2}{5}$
E R38 Q27 apply |
- 【两边平方】$\sin\alpha+\cos\alpha=\dfrac{1}{5}\Rightarrow 1+2\sin\alpha\cos\alpha=\dfrac{1}{25}\Rightarrow\sin\alpha\cos\alpha=-\dfrac{12}{25}$，$\sin 2\alpha=-\dfrac{24}{25}$
E R14 Q28 apply |
- 【化成锐角】$\sin\dfrac{5\pi}{6}=\sin\left(\pi-\dfrac{\pi}{6}\right)=\dfrac{1}{2}$；$\cos\left(-\dfrac{4\pi}{3}\right)=\cos\dfrac{4\pi}{3}=\cos\left(\pi+\dfrac{\pi}{3}\right)=-\dfrac{1}{2}$
E R17 Q29 apply |
- 【拆成特殊角】$\sin 15^\circ=\sin(45^\circ-30^\circ)=\dfrac{\sqrt{6}-\sqrt{2}}{4}$；$\cos 75^\circ=\cos(45^\circ+30^\circ)=\dfrac{\sqrt{6}-\sqrt{2}}{4}$
E P16 Q29 apply |
- 【用半角】$\tan 15^\circ=\dfrac{1-\cos 30^\circ}{\sin 30^\circ}=2-\sqrt{3}$
E R16 Q30 apply |
- 【配角】$\alpha,\beta$ 锐角，$\cos\alpha=\dfrac{4}{5}$，$\cos(\alpha+\beta)=\dfrac{5}{13}$：$\cos\beta=\cos[(\alpha+\beta)-\alpha]=\dfrac{5}{13}\cdot\dfrac{4}{5}+\dfrac{12}{13}\cdot\dfrac{3}{5}=\dfrac{56}{65}$
E P17 Q31 apply |
- 【辅助角】$y=\sin x+\sqrt{3}\cos x=2\sin\left(x+\dfrac{\pi}{3}\right)$，最大值 2，周期 $2\pi$
E R19 Q31 apply |
- 【先降幂再辅助角】$y=\sin^2x+\sqrt{3}\sin x\cos x=\sin\left(2x-\dfrac{\pi}{6}\right)+\dfrac{1}{2}$，最大值 $\dfrac{3}{2}$，周期 $\pi$
E R38 Q32 apply |
- 【配成完全平方】$\sqrt{1+\sin 2\alpha}=\sqrt{(\sin\alpha+\cos\alpha)^2}=|\sin\alpha+\cos\alpha|$
E R19 Q32 apply |
- 【升幂】$\sqrt{1+\cos 2\alpha}=\sqrt{2\cos^2\alpha}=\sqrt{2}|\cos\alpha|$
E P14 Q33 apply |
- 【正切和角变形】$\alpha+\beta=\dfrac{\pi}{4}\Rightarrow\tan\alpha+\tan\beta=1-\tan\alpha\tan\beta\Rightarrow(1+\tan\alpha)(1+\tan\beta)=2$
E R21 Q34 apply |
- 【和差化积】$\sin 75^\circ+\sin 15^\circ=2\sin 45^\circ\cos 30^\circ=\dfrac{\sqrt{6}}{2}$
E R20 Q34 apply |
- 【积化和差】$\sin 75^\circ\cos 15^\circ=\dfrac{1}{2}(\sin 90^\circ+\sin 60^\circ)=\dfrac{2+\sqrt{3}}{4}$
E P16 Q35 apply |
- 【无 ± 的有理式】$\tan 22.5^\circ=\dfrac{1-\cos 45^\circ}{\sin 45^\circ}=\sqrt{2}-1$
E P22 Q36 apply |
- 【代入求边、求角】$b=2$，$c=3$，$A=60^\circ$：$a^2=4+9-6=7$，$a=\sqrt{7}$；三边 3、5、7：$\cos C=\dfrac{9+25-49}{30}=-\dfrac{1}{2}$，$C=120^\circ$
E P21 Q37 apply |
- 【边角互化】$A=45^\circ$，$B=60^\circ$，$a=2$：$b=\dfrac{a\sin B}{\sin A}=\sqrt{6}$
E P19 Q37 apply |
- 【内角和】$C=180^\circ-45^\circ-60^\circ=75^\circ$
E P20 Q38 apply |
- 【两边夹角】$a=2$，$b=3$，$C=30^\circ$：$S=\dfrac{1}{2}\cdot 2\cdot 3\cdot\dfrac{1}{2}=\dfrac{3}{2}$
E P48 Q38 apply |
- 【已知三边】3、4、5：$p=6$，$S=\sqrt{6\cdot 3\cdot 2\cdot 1}=6$
E P21 Q39 apply |
- 【边化角】$a\cos A=b\cos B\Rightarrow\sin 2A=\sin 2B\Rightarrow A=B$ 或 $A+B=\dfrac{\pi}{2}$（等腰或直角）
E P22 Q39 apply |
- 【看边的关系】$a^2+b^2<c^2\Rightarrow\cos C<0$，$C$ 为钝角
E P19 Q40 apply |
- 【$A+B=\pi-C$】$\sin C=2\sin A\cos B\Rightarrow\sin(A+B)=2\sin A\cos B\Rightarrow\sin(B-A)=0\Rightarrow A=B$
E P49 Q41 apply |
- 【平方求模】$|\vec a|=2$，$|\vec b|=1$，夹角 $60^\circ$：$|\vec a+\vec b|^2=4+2+1=7$，$|\vec a+\vec b|=\sqrt{7}$
E R15 Q41 apply |
- 【坐标判垂直】$\vec a=(1,2)$，$\vec b=(2,-1)$：$\vec a\cdot\vec b=0\Rightarrow\vec a\perp\vec b$
E P21 Q42 apply |
- 【边化角】$a=\sqrt{3}$，$A=60^\circ$：$2R=2$，$b+c=2(\sin B+\sin C)$
E P17 Q42 apply |
- 【辅助角求最值】$C=120^\circ-B$，$B\in(0^\circ,120^\circ)$：$b+c=2\sqrt{3}\sin(B+30^\circ)\in(\sqrt{3},2\sqrt{3}]$，$B=60^\circ$ 时取最大
E P23 Q43 apply |
- 【分母实数化】$\dfrac{1+2i}{1-i}=\dfrac{(1+2i)(1+i)}{2}=\dfrac{-1+3i}{2}$
E R22 Q43 apply |
- 【展开】$(2+i)(3-i)=6-2i+3i-i^2=7+i$
E R23 Q44 apply |
- 【共轭相乘】$z=3-4i$：$z\bar z=25$，$|z|=5$
E R25 Q44 apply |
- 【模的乘法、距离】$|(1+i)(3-4i)|=\sqrt{2}\cdot 5=5\sqrt{2}$；$|z-i|=1$ 表示以 $(0,1)$ 为圆心、1 为半径的圆
E R24 Q45 apply |
- 【指数除以 4】$i^{2023}=i^{3}=-i$
E R27 Q45 apply |
- 【棣莫弗】$(1+i)^8=(\sqrt{2})^8(\cos 2\pi+i\sin 2\pi)=16$
E P24 Q46 apply |
- 【求模定辐角】$-1+\sqrt{3}i=2\left(\cos\dfrac{2\pi}{3}+i\sin\dfrac{2\pi}{3}\right)$
E R26 Q46 apply |
- 【模乘辐角加】$2\left(\cos\dfrac{\pi}{6}+i\sin\dfrac{\pi}{6}\right)\cdot 3\left(\cos\dfrac{\pi}{3}+i\sin\dfrac{\pi}{3}\right)=6i$

N Q47 problem seq | | 看到：已知递推关系，求通项
- 路径：$a_{n+1}-a_n=f(n)$ 用累加，$\dfrac{a_{n+1}}{a_n}=g(n)$ 用累乘〔P50〕；求和用自然数求和〔R29〕
- 注意：$n=1$ 单独验证

N Q48 problem seq | | 看到：已知 $S_n$，求 $a_n$
- 路径：$a_n=S_n-S_{n-1}$（$n\ge 2$）〔P32〕，再验 $n=1$
- 注意：以 $n=1$ 代入验证为准；$S_n$ 是 $n$ 的多项式且常数项 $\ne 0$ 时首项必须分开写（$S_n=2^n-1$ 这类可能不用分开）

N Q49 problem seq | | 看到：等差、等比数列的基本量（知三求二）
- 路径：列方程求 $a_1$、$d$ 或 $q$〔P26〕〔P29〕，再代求和公式〔P28〕〔P31〕
- 注意：等比求和先看 $q$ 是否为 1

N Q50 problem seq | | 看到：等差、等比的性质速算
- 路径：下标性质〔P27〕〔P30〕、中项〔P51〕、$S_{2n-1}=(2n-1)a_n$〔P28〕、片段和〔P54〕
- 注意：先确认是等差还是等比

N Q51 problem seq | | 看到：通项是“等差 × 等比”的数列求和
- 路径：错位相减〔P52〕：$S-qS$，中间是等比求和〔P31〕
- 注意：中间等比部分的项数（常为 $n-1$ 项）、最后一项的符号、最后除以 $1-q$；$q=1$ 单独算

N Q52 problem seq | | 看到：通项是分式或根式差的数列求和
- 路径：裂项〔R30〕〔P53〕，再累加相消〔R28〕
- 注意：看清首尾剩下哪几项；裂项后核对系数（如 $\dfrac{1}{2}$）

N Q53 problem seq | | 看到：通项是多项式（或几部分之和）的数列求和
- 路径：拆成几部分分别求和：$\sum k$〔R29〕、$\sum k^2$〔R31〕、$\sum k^3$〔R32〕；等比部分用等比求和〔P31〕

N Q54 problem seq | | 看到：已知前 $m$、$2m$ 项和，求前 $3m$ 项和
- 路径：片段和〔P54〕
- 注意：等比数列片段和为 0 时不成等比

N Q55 problem seq | | 看到：数列和的不等式（放缩证明）
- 路径：先放缩成可裂项的形式，再裂项相消〔R30〕
- 注意：从第几项开始放缩要说清
~ 同见不等式大厦 P24、P55（裂项放缩）

N Q56 problem cnt | | 看到：求展开式的特定项、常数项、某项系数
- 路径：写通项 $T_{k+1}=C_n^ka^{n-k}b^k$〔R33〕，令次数满足条件求 $k$
- 注意：$T_{k+1}$ 是第 $k+1$ 项；系数要连同符号和常数一起算

N Q57 problem cnt | | 看到：求展开式的系数和
- 路径：赋值 $x=1$、$-1$、$0$〔R39〕；二项式系数和是 $2^n$〔R34〕
- 注意：区分“项的系数”和“二项式系数”

N Q58 problem cnt | | 看到：组合数化简、求和、证明
- 路径：对称性、杨辉三角递推〔P35〕；$kC_n^k=nC_{n-1}^{k-1}$〔P36〕

N Q59 problem cnt | | 看到：计数（排队、选人）
- 路径：有序用排列数〔P33〕，无序用组合数〔P34〕；先分类、再分步
- 注意：特殊元素、特殊位置优先

N Q60 problem cnt | | 看到：近似计算、整除与余数
- 路径：把底数写成“整数 + 小量”，用二项式展开〔R33〕取前几项
- 注意：求余数时余数要非负，展开后为负要加上除数调整

N Q61 problem der | | 看到：求导数
- 路径：识别结构：和差积〔P37〕、商〔P38〕、复合（链式法则）〔S12〕；常用导数〔P55〕
- 注意：链式法则别漏乘内层导数；商法则分子是 $u'v-uv'$，顺序不能反

N Q62 problem der | | 看到：求曲线在某点的切线方程
- 路径：① 求导得斜率 $k=f'(x_0)$〔S12〕→ ② 点斜式 $y-f(x_0)=f'(x_0)(x-x_0)$
- 注意：“在点处”与“过点”不同：过点时切点要设出来

N Q63 problem der | | 看到：判断单调性、求极值和最值
- 路径：① 求导〔P37〕→ ② 导数因式分解〔R08〕→ ③ 看导数正负 → ④ 列表得极值；闭区间求最值时比较极值与端点值
- 注意：先写定义域；极值点处导数为 0，但导数为 0 不一定是极值点
~ 同见不等式大厦 P05（构造函数判单调）

N Q64 problem der | | 看到：构造函数证明不等式
- 路径：移项作差构造 $g(x)$ → 求导〔P37〕〔P55〕〔P39〕→ 看单调性和最值
- 注意：先写定义域（如 $x>0$）
~ 同见不等式大厦 P05

E P50 Q47 apply |
- 【累加或累乘】$a_1=1$，$a_{n+1}=a_n+2n\Rightarrow a_n=1+2[1+2+\cdots+(n-1)]=n^2-n+1$；$a_1=1$，$a_{n+1}=\dfrac{n+1}{n}a_n\Rightarrow a_n=n$
E R29 Q47 apply |
- 【自然数求和】$1+2+\cdots+(n-1)=\dfrac{n(n-1)}{2}$
E P32 Q48 apply |
- 【作差】$S_n=n^2+n\Rightarrow a_n=2n$（$n\ge 2$），$a_1=S_1=2$ 也符合，故 $a_n=2n$
E P26 Q49 apply |
- 【列方程】等差 $a_3=5$，$a_7=13\Rightarrow d=2$，$a_1=1$
E P28 Q49 apply |
- 【代入求和】$S_{10}=10\times 1+\dfrac{10\times 9}{2}\times 2=100$
E P29 Q49 apply |
- 【列方程】等比 $a_2=2$，$a_5=16\Rightarrow q^3=8$，$q=2$，$a_1=1$
E P31 Q49 apply |
- 【代入求和】$S_5=\dfrac{1-2^5}{1-2}=31$
E P27 Q50 apply |
- 【下标和】等差 $a_2+a_8=10\Rightarrow a_5=5$
E P28 Q50 apply |
- 【$S_{2n-1}=(2n-1)a_n$】$S_9=9a_5=45$
E P30 Q50 apply |
- 【下标和】等比 $a_2a_8=16\Rightarrow a_4a_6=a_5^2=16$
E P52 Q51 apply |
- 【错位相减】$\displaystyle\sum_{k=1}^{n}k\cdot 2^{k-1}=(n-1)2^n+1$
E R30 Q52 apply |
- 【裂项】$\displaystyle\sum_{k=1}^{n}\dfrac{1}{k(k+1)}=1-\dfrac{1}{n+1}=\dfrac{n}{n+1}$
E P53 Q52 apply |
- 【裂项】$\displaystyle\sum_{k=1}^{n}\dfrac{1}{(2k-1)(2k+1)}=\dfrac{n}{2n+1}$；$\displaystyle\sum_{k=1}^{n}\dfrac{1}{\sqrt{k}+\sqrt{k+1}}=\sqrt{n+1}-1$
E R29 Q53 apply |
- 【分组】$\displaystyle\sum_{k=1}^{n}(2k+1)=n(n+1)+n=n^2+2n$
E R31 Q53 apply |
- 【拆成平方和加自然数和】$\displaystyle\sum_{k=1}^{n}k(k+1)=\sum k^2+\sum k=\dfrac{n(n+1)(n+2)}{3}$
E P54 Q54 apply |
- 【片段和】等差 $S_{10}=10$，$S_{20}=30$：片段和 10、20、30 成等差 $\Rightarrow S_{30}=60$
E R30 Q55 apply |
- 【放缩后裂项】$k\ge 2$ 时 $\dfrac{1}{k^2}<\dfrac{1}{k(k-1)}=\dfrac{1}{k-1}-\dfrac{1}{k}\Rightarrow n\ge 2$ 时 $\displaystyle\sum_{k=1}^{n}\dfrac{1}{k^2}<1+\left(1-\dfrac{1}{n}\right)=2-\dfrac{1}{n}<2$（$n=1$ 时和为 1，也 $<2$）
E R33 Q56 apply |
- 【写通项】$\left(x+\dfrac{1}{x}\right)^6$：$T_{k+1}=C_6^kx^{6-2k}$，$k=3$ 得常数项 20；$(2x-1)^5$ 中 $x^3$ 的系数 $C_5^2\cdot 2^3\cdot(-1)^2=80$
E R39 Q57 apply |
- 【赋值】$(2x-1)^5$：各项系数和 $f(1)=1$；奇次项系数和 $\dfrac{f(1)-f(-1)}{2}=122$
E R34 Q57 apply |
- 【二项式系数和】$(2x-1)^5$ 的二项式系数和 $2^5=32$
E P35 Q58 apply |
- 【杨辉递推、对称】$C_7^3+C_7^4=C_8^4=70$；$C_{10}^8=C_{10}^2=45$
E P36 Q58 apply |
- 【提取 $n$】$\displaystyle\sum_{k=0}^{n}kC_n^k=n\cdot 2^{n-1}$
E P33 Q59 apply |
- 【有序】5 人选 3 人排成一排：$A_5^3=60$
E P34 Q59 apply |
- 【无序】5 人选 3 人：$C_5^3=10$
E R33 Q60 apply |
- 【展开取前几项】$1.02^5=(1+0.02)^5\approx 1+5\times 0.02+10\times 0.0004=1.104$；$9^{10}-1=(8+1)^{10}-1$ 能被 8 整除
E P37 Q61 apply |
- 【积法则】$(x^2e^x)'=2xe^x+x^2e^x$
E P38 Q61 apply |
- 【商法则】$\left(\dfrac{\ln x}{x}\right)'=\dfrac{1-\ln x}{x^2}$
E S12 Q61 apply |
- 【链式法则】$[\sin(2x+1)]'=2\cos(2x+1)$
E P55 Q61 apply |
- 【常用导数（含复合）】$[\ln(3x+1)]'=\dfrac{3}{3x+1}$
E S12 Q62 apply |
- 【求斜率再点斜式】$y=x^3$ 在 $(1,1)$：$k=3$，切线 $y=3x-2$
E P37 Q63 apply |
- 【求导看正负】$f(x)=x^3-3x$：$f'(x)=3(x-1)(x+1)$，$(-1,1)$ 递减，$(-\infty,-1)$、$(1,+\infty)$ 递增（不能用 ∪ 连接）；极大值 $f(-1)=2$，极小值 $f(1)=-2$
E P39 Q64 apply |
- 【构造作差函数】证 $\ln x\le x-1$：$g(x)=\ln x-x+1$，$g'(x)=\dfrac{1}{x}-1$，$x=1$ 处取最大值 0

N Q65 problem alg | | 看到：二次三项式因式分解
- 路径：① 先提公因式 → ② 试十字相乘〔R08〕→ ③ 拆不开用求根公式〔P02〕求两根，写成交点式〔P04〕
- 注意：$\Delta<0$ 时在实数范围内不能分解；$ax^2+bx+c=a(x-x_1)(x-x_2)$，不要漏 $a$

N Q66 problem tri | | 看到：三角式化简求值（角不同、名不同、次数高）
- 路径：角不同 → 拆角配角〔R17〕；名不同 → 切化弦〔P11〕；次数高 → 降幂〔R19〕；倍角逆用〔R18〕
- 注意：一看角、二看名、三看次数；降幂会把角变成 $2\alpha$，降幂后再统一角；常以辅助角〔P17〕收尾

N Q67 problem tri | | 看到：证明三角恒等式
- 路径：切化弦〔P11〕，“1”的代换〔R13〕，倍角〔R18〕；从繁的一边化向简的一边
- 注意：从一边连等推到另一边，或两边分别化到同一式；不把结论当条件用；注意 $\alpha$ 使各式有意义

E R08 Q65 apply |
- 【十字相乘】$2x^2-5x-3=(2x+1)(x-3)$
E P02 Q65 apply |
- 【求两根再写交点式】$x^2-2x-1=(x-1-\sqrt{2})(x-1+\sqrt{2})$
E R17 Q66 apply |
- 【和差角展开】$\sin(\alpha+30^\circ)-\sin(\alpha-30^\circ)=2\cos\alpha\sin 30^\circ=\cos\alpha$
E R18 Q66 apply |
- 【倍角逆用】$2\sin 15^\circ\cos 15^\circ=\sin 30^\circ=\dfrac{1}{2}$
E P11 Q66 apply |
- 【切化弦】$\tan\alpha\cos\alpha=\sin\alpha$
E P11 Q67 apply |
- 【切化弦、通分】$\tan\alpha+\dfrac{1}{\tan\alpha}=\dfrac{\sin^2\alpha+\cos^2\alpha}{\sin\alpha\cos\alpha}=\dfrac{2}{\sin 2\alpha}$
E R13 Q67 apply |
- 【“1”的代换】$\dfrac{1}{\cos^2\alpha}-\tan^2\alpha=\dfrac{\sin^2\alpha+\cos^2\alpha-\sin^2\alpha}{\cos^2\alpha}=1$

E P51 Q50 apply |
- 【中项】$2,x,8$ 成等比 $\Rightarrow x^2=16$，$x=\pm 4$；$a,b,c$ 成等差 $\Rightarrow 2b=a+c$

N Q68 problem seq | | 看到：递推 $a_{n+1}=pa_n+q$ 或 $a_{n+1}=\dfrac{a_n}{ka_n+1}$，求通项
- 路径：$a_{n+1}=pa_n+q$（$p\ne 1$）：待定系数，$a_{n+1}+\lambda=p(a_n+\lambda)$，$\lambda=\dfrac{q}{p-1}$，构造等比〔P29〕；$a_{n+1}=\dfrac{a_n}{ka_n+1}$：取倒数构造等差〔P26〕
- 注意：构造出的新数列首项不能为 0

N Q69 problem seq | | 看到：已知 $S_n$ 与 $a_n$ 的关系式（如 $S_n=2a_n-1$），求通项
- 路径：写出 $n-1$ 时的同式，两式相减〔P32〕，得 $a_n$ 与 $a_{n-1}$ 的关系，再按等差或等比求通项〔P29〕
- 注意：相减只对 $n\ge 2$ 成立，$n=1$ 由原式单独求 $a_1$

N Q70 problem der | | 看到：含参数的函数求单调区间
- 路径：① 求导〔P37〕→ ② 导数因式分解〔R08〕→ ③ 按导数零点的有无、大小、是否在定义域内分类讨论
- 注意：先写定义域；分类的分界点要不重不漏
~ 同见二次函数大厦 R10（含参二次式）

N Q71 problem der | | 看到：过某点作曲线的切线（点不一定在曲线上）
- 路径：① 设切点 $(x_0,f(x_0))$ → ② 写切线 $y-f(x_0)=f'(x_0)(x-x_0)$〔S12〕→ ③ 代入已知点解 $x_0$
- 注意：“过点”可能有多条切线；“在点处”则该点就是切点

E P29 Q68 apply |
- 【构造等比】$a_1=1$，$a_{n+1}=2a_n+1\Rightarrow a_{n+1}+1=2(a_n+1)$，$a_n+1=2^n$，$a_n=2^n-1$
E P26 Q68 apply |
- 【取倒数构造等差】$a_1=1$，$a_{n+1}=\dfrac{a_n}{a_n+1}\Rightarrow\dfrac{1}{a_{n+1}}=\dfrac{1}{a_n}+1\Rightarrow a_n=\dfrac{1}{n}$
E P32 Q69 apply |
- 【两式相减】$S_n=2a_n-1$：$n\ge 2$ 时 $a_n=2a_n-2a_{n-1}\Rightarrow a_n=2a_{n-1}$；$n=1$ 时 $a_1=1$
E P29 Q69 apply |
- 【按等比写通项】$a_n=2^{n-1}$
E P37 Q70 apply |
- 【求导后分类】$f(x)=x^3-3ax$：$f'(x)=3(x^2-a)$；$a\le 0$ 时在 $\mathbb{R}$ 上递增；$a>0$ 时在 $(-\sqrt{a},\sqrt{a})$ 递减，在 $(-\infty,-\sqrt{a})$、$(\sqrt{a},+\infty)$ 递增
E S12 Q71 apply |
- 【设切点】过 $(0,-2)$ 作 $y=x^3$ 的切线：切线 $y-x_0^3=3x_0^2(x-x_0)$，代入得 $-2-x_0^3=-3x_0^3$，$x_0=1$，切线 $y=3x-2$

# ═════════ v4 扩充：覆盖高中全部内容 ═════════
# ───────── 地基、计数：集合 ─────────
N S14 start base | | 【定义】集合的运算
- $A\cap B=\{x\mid x\in A$ 且 $x\in B\}$，$A\cup B=\{x\mid x\in A$ 或 $x\in B\}$
- 补集 $\complement_U A=\{x\mid x\in U$ 且 $x\notin A\}$
- $\mathrm{card}(A)$：有限集 $A$ 的元素个数

N R40 white cnt | | 子集个数与容斥原理
- $n$ 元集合的子集有 $2^n$ 个，真子集有 $2^n-1$ 个
- 容斥：$\mathrm{card}(A\cup B)=\mathrm{card}(A)+\mathrm{card}(B)-\mathrm{card}(A\cap B)$
- 德摩根律 $\complement_U(A\cup B)=(\complement_U A)\cap(\complement_U B)$，$\complement_U(A\cap B)=(\complement_U A)\cup(\complement_U B)$（必修一例题、习题）
- ✗ 50 人中 30 人会英语、25 人会日语：直接相加得 55 > 50，两种都会的人数了两次
~ ⋯ 同源：二项式系数和 $2^n$〔R34〕；概率的加法公式〔R47〕
~ ⚡ 第一反应：两类有重叠的计数 → 相加再减去重叠部分；求子集个数 → $2^n$

E S14 R40 derive main |
- 【分类计数】$A\cup B$ 分成“只在 $A$”“只在 $B$”“在 $A\cap B$”三类；$\mathrm{card}(A)+\mathrm{card}(B)$ 把 $A\cap B$ 数了两次
E S07 R40 premise |
- 【前提】分步乘法：每个元素“选或不选”2 种，共 $2^n$ 种
E R40 R34 premise |
- 【双计数】子集共 $2^n$ 个，按元素个数分类为 $\sum C_n^k$（另一路）
E S14 S07 define |
- 【定义】分类 = 把集合分成互不相交的子集，各部分元素个数相加

N Q72 problem cnt | | 看到：集合的子集个数、两类有重叠的计数
- 路径：子集个数 $2^n$；有重叠时用容斥〔R40〕，或画韦恩图
- 注意：真子集不含集合本身，非空真子集再减去空集
E R40 Q72 apply |
- 【容斥】50 人中 30 人会英语、25 人会日语、10 人两种都会：至少会一种的有 $30+25-10=45$ 人；$\{1,2,3\}$ 的子集有 $2^3=8$ 个

# ───────── 代数：因式定理、待定系数（拓展）─────────
N P59 lorange alg ext | 〔结构前提〕$f(x)$ 是多项式 | 余数定理与因式定理
- $f(x)$ 除以 $x-a$ 的余数等于 $f(a)$
- 因式定理：$f(a)=0\iff x-a$ 是 $f(x)$ 的因式
- 例：$f(x)=x^3-6x^2+11x-6$，$f(1)=0\Rightarrow f(x)=(x-1)(x^2-5x+6)$
~ ⚡ 第一反应：高次式分解 → 试根，$f(a)=0$ 就提出 $x-a$

N R43 white alg ext | | 恒等的多项式：系数对应相等（待定系数法）
- 待定系数法本身是教材方法（必修一 3.1.1 例 7：过三点设 $y=ax^2+bx+c$）；“系数对应相等”这条定理教材没给，属拓展
- $a_nx^n+\cdots+a_1x+a_0=b_nx^n+\cdots+b_1x+b_0$ 对一切 $x$ 成立 $\iff a_k=b_k$（$k=0,1,\cdots,n$）
- 例：$x^2+3x+5=(x+1)^2+m(x+1)+n$：展开比较得 $m=1$，$n=3$
- ✗ 只对某个 $x$ 成立的等式不能比较系数：$x^2=x$ 在 $x=1$ 时成立，但两边系数不同
~ ⋯ 同源：复数相等实部、虚部分别相等〔S06〕；平面向量基本定理的系数唯一〔P56〕
~ ⚡ 第一反应：两个多项式恒等、要求未知系数 → 展开后对应系数相等

E R01 P59 derive | ▼ 加条件〔结构前提〕：$f(x)$ 是多项式
- 【带余除法】$f(x)=(x-a)q(x)+r$，令 $x=a$ 得 $r=f(a)$
E P59 R43 derive |
- 【反证】两边之差若不是零多项式，最多有 $n$ 个根（每个根提出一个因式），与“对一切 $x$ 成立”矛盾
E R01 R43 premise |
- 【前提】展开后合并同类项

N Q79 problem alg | | 看到：已知恒等式（对一切 $x$ 成立），求待定的系数
- 路径：① 展开、合并同类项〔R01〕→ ② 对应系数相等〔R43〕，列方程组；或赋特殊值
- 注意：赋值法只能给出必要条件，个数不够时要补；“对一切 $x$ 成立”才能比较系数
E R43 Q79 apply |
- 【展开比较系数】$x^2+3x+5=(x+1)^2+m(x+1)+n$：右边 $=x^2+(2+m)x+(1+m+n)$，$m=1$，$n=3$
E P59 Q06 apply |
- 【试根后提因式】$f(x)=x^3-2x^2-5x+6$：$f(1)=0\Rightarrow(x-1)(x^2-x-6)=(x-1)(x-3)(x+2)$
E R43 Q68 apply |
- 【待定系数】$a_{n+1}+\lambda=2(a_n+\lambda)$ 即 $a_{n+1}=2a_n+\lambda$，与 $a_{n+1}=2a_n+1$ 比较得 $\lambda=1$

# ───────── 三角：三倍角（拓展）、三角形中的正切恒等式（拓展）─────────
N R44 white tri ext | | 三倍角
- $\sin 3\alpha=3\sin\alpha-4\sin^3\alpha$
- $\cos 3\alpha=4\cos^3\alpha-3\cos\alpha$
~ ⚡ 第一反应：看到 $3\alpha$ 与 $\alpha$ 同时出现 → 拆成 $2\alpha+\alpha$，或直接用三倍角（拓展）
E R17 R44 derive |
- 【拆角】$\sin 3\alpha=\sin(2\alpha+\alpha)=\sin 2\alpha\cos\alpha+\cos 2\alpha\sin\alpha$
- 再用倍角、勾股恒等式化成只含 $\sin\alpha$（或 $\cos\alpha$）
E R18 R44 premise |
- 【前提】倍角
E R13 R44 premise |
- 【前提】$\cos^2\alpha=1-\sin^2\alpha$
E R44 Q66 apply |
- 【三倍角】$\sin\alpha=\dfrac{1}{2}$ 时 $\sin 3\alpha=\dfrac{3}{2}-4\times\dfrac{1}{8}=1$（$\alpha=30^\circ$，$\sin 90^\circ=1$）

N P60 lorange vec ext | 〔结构前提〕$A+B+C=\pi$，且都不是直角 | 三角形中的正切恒等式
- $\tan A+\tan B+\tan C=\tan A\tan B\tan C$
~ ⚡ 第一反应：三角形中三个正切的和与积同时出现 → 正切恒等式
E P19 P60 derive | ▼ 加条件〔结构前提〕：三个角都不是直角
- 【变形】$\tan(A+B)=-\tan C$，代入 $\tan A+\tan B=\tan(A+B)(1-\tan A\tan B)$，移项
E P14 P60 premise |
- 【前提】正切和角的变形
E P60 Q40 apply |
- 【正切恒等式】$\tan A=1$，$\tan B=2\Rightarrow\tan C=-\tan(A+B)=-\dfrac{1+2}{1-2}=3$，验证 $1+2+3=1\times 2\times 3$

# ───────── 向量：线性运算坐标、基本定理、投影、极化 ─────────
N R41 green vec | | ★ 线性运算的坐标、中点与重心
- $\vec a\pm\vec b=(x_1\pm x_2,\ y_1\pm y_2)$，$\lambda\vec a=(\lambda x_1,\ \lambda y_1)$
- $\overrightarrow{AB}=(x_2-x_1,\ y_2-y_1)$：终点坐标减起点坐标
- 中点：$\overrightarrow{OM}=\dfrac{1}{2}(\overrightarrow{OA}+\overrightarrow{OB})$，$M\left(\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\right)$
- 重心：$G\left(\dfrac{x_1+x_2+x_3}{3},\dfrac{y_1+y_2+y_3}{3}\right)$，$\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}=\vec 0$
- 两向量相等 $\iff$ 坐标对应相等；与 $\vec a$ 同向的单位向量 $\dfrac{\vec a}{|\vec a|}$；数轴上两点距离 $|a-b|$、中点 $\dfrac{a+b}{2}$
~ ⚡ 第一反应：已知点的坐标求向量 → 终点减起点；中点 → 坐标取平均
E S21 R41 derive main |
- 【展开】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$，按分配律合并
- 中点：$\overrightarrow{AM}=\overrightarrow{MB}$，即 $\overrightarrow{OM}-\overrightarrow{OA}=\overrightarrow{OB}-\overrightarrow{OM}$

N P56 orange vec | 〔结构前提〕$\vec e_1,\vec e_2$ 不共线；$A,B$ 不重合 | ★ 平面向量基本定理与三点共线
- $\vec e_1,\vec e_2$ 不共线 $\Rightarrow$ 平面内任一 $\vec a=\lambda_1\vec e_1+\lambda_2\vec e_2$，且 $\lambda_1,\lambda_2$ 唯一（课本给出）
- 唯一 $\Rightarrow$ 对应系数相等：$\lambda_1\vec e_1+\lambda_2\vec e_2=\mu_1\vec e_1+\mu_2\vec e_2\Rightarrow\lambda_1=\mu_1$，$\lambda_2=\mu_2$
- $P$ 在直线 $AB$ 上 $\iff\overrightarrow{OP}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}$（系数和为 1，$O$ 任取）
- 拓展（老教材）：定比分点 $\overrightarrow{AP}=\lambda\overrightarrow{PB}$（$\lambda\ne -1$）$\Rightarrow x=\dfrac{x_1+\lambda x_2}{1+\lambda}$，$y=\dfrac{y_1+\lambda y_2}{1+\lambda}$
- ✗ $\vec e_1=(1,0)$，$\vec e_2=(2,0)$ 共线：$(0,1)$ 无法用它们表示
~ ⚡ 第一反应：图形中用两个不共线向量表示其他向量 → 选基底；三点共线 → 系数和为 1
E S21 P56 derive main | ▼ 加条件〔结构前提〕：基底不共线
- 【共线】$\overrightarrow{AP}=t\overrightarrow{AB}\Rightarrow\overrightarrow{OP}-\overrightarrow{OA}=t(\overrightarrow{OB}-\overrightarrow{OA})$
- 整理得 $\overrightarrow{OP}=(1-t)\overrightarrow{OA}+t\overrightarrow{OB}$
E R41 P56 premise |
- 【前提】向量的加减与数乘

N P57 lorange vec | 〔定义域〕$\vec b\ne\vec 0$ | ★ 投影向量与投影的数量
- 投影的数量（$\vec a$ 在 $\vec b$ 方向上）：$|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}$，可正可负
- 投影向量（B 版也简称“投影”）：$\dfrac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$
- 几何意义：$\vec a\cdot\vec b$ 等于 $|\vec b|$ 乘 $\vec a$ 在 $\vec b$ 方向上投影的数量
- 正交分解：$\vec a=(\vec a\cdot\vec e_1)\vec e_1+(\vec a\cdot\vec e_2)\vec e_2$：坐标就是在基向量上投影的数量
- 叫法：B 版“投影” = 投影向量，“投影的数量” = $|\vec a|\cos\theta$；有的教材把后者叫“投影”
~ ⚡ 第一反应：一个向量在另一个方向上的“影子”、到直线或平面的距离 → 投影 $\dfrac{\vec a\cdot\vec b}{|\vec b|}$
E P49 P57 derive | ▼ 加条件〔定义域〕：$\vec b\ne\vec 0$
- 【代入】$|\vec a|\cos\theta$，$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；投影向量 = 投影 × 单位向量 $\dfrac{\vec b}{|\vec b|}$

N R42 white vec | | 平行四边形恒等式、中线长与极化恒等式
- $|\vec a+\vec b|^2+|\vec a-\vec b|^2=2\left(|\vec a|^2+|\vec b|^2\right)$：平行四边形对角线平方和 = 四边平方和（选必一 2.1 正文）
- $\vec a\cdot\vec b=\dfrac{1}{2}\left(|\vec a+\vec b|^2-|\vec a|^2-|\vec b|^2\right)$（教材练习）
- 拓展：极化恒等式 $\vec a\cdot\vec b=\dfrac{1}{4}\left(|\vec a+\vec b|^2-|\vec a-\vec b|^2\right)$
- $M$ 为 $BC$ 中点：$\overrightarrow{AB}\cdot\overrightarrow{AC}=|AM|^2-|BM|^2$
- 中线长：$|AM|^2=\dfrac{1}{4}(2b^2+2c^2-a^2)$
~ ⚡ 第一反应：数量积的两个向量共起点、且能找到中点 → 化成“中线平方 − 半边平方”
E P49 R42 derive |
- 【相减】$|\vec a+\vec b|^2-|\vec a-\vec b|^2=4\vec a\cdot\vec b$
- $\overrightarrow{AB}=\overrightarrow{AM}+\overrightarrow{MB}$，$\overrightarrow{AC}=\overrightarrow{AM}-\overrightarrow{MB}$，相乘用“和×差”
E R41 R42 premise |
- 【前提】中点：$\overrightarrow{AM}=\dfrac{1}{2}(\overrightarrow{AB}+\overrightarrow{AC})$，平方后用余弦定理推论
E P22 R42 premise |
- 【前提】$2bc\cos A=b^2+c^2-a^2$

N Q73 problem vec | | 看到：用基底表示向量、求系数 $\lambda,\mu$
- 路径：① 选两个不共线的向量作基底 → ② 沿图形“走路”表示目标向量 → ③ 系数唯一，对应相等〔P56〕
- 注意：三点共线 $\iff$ 系数和为 1（起点相同时）
E P56 Q73 apply |
- 【基底与系数和】$D$ 为 $BC$ 中点：$\overrightarrow{AD}=\dfrac{1}{2}\overrightarrow{AB}+\dfrac{1}{2}\overrightarrow{AC}$；$P$ 在 $BC$ 上且 $\overrightarrow{AP}=\dfrac{1}{3}\overrightarrow{AB}+\mu\overrightarrow{AC}\Rightarrow\mu=\dfrac{2}{3}$

N Q74 problem vec | | 看到：已知坐标，判断平行、垂直，求中点或参数
- 路径：向量坐标 = 终点减起点〔R41〕；平行 $x_1y_2-x_2y_1=0$，垂直 $x_1x_2+y_1y_2=0$〔P49〕
- 注意：平行的坐标条件不要写成比例式（分母可能为 0）
E P49 Q74 apply |
- 【坐标条件】$\vec a=(1,2)$，$\vec b=(x,4)$ 平行 $\Rightarrow 1\times 4-2x=0$，$x=2$；垂直 $\Rightarrow x+8=0$，$x=-8$
E R41 Q74 apply |
- 【终点减起点、取平均】$A(1,2)$，$B(3,-4)$：$\overrightarrow{AB}=(2,-6)$，中点 $(2,-1)$

N Q75 problem vec | | 看到：动点的数量积求最值或范围
- 路径：① 极化恒等式化成 $|PM|^2-$ 常数〔R42〕，转为求距离的最值；② 或建坐标系用坐标式〔R15〕化成函数
- 注意：$M$ 取两个向量终点连线的中点
E R42 Q75 apply |
- 【化成距离】$|AB|=2$，$M$ 为中点，$P$ 在直线 $l$ 上，$M$ 到 $l$ 的距离为 1：$\overrightarrow{PA}\cdot\overrightarrow{PB}=|PM|^2-1\ge 0$，最小值 0

N Q76 problem vec | | 看到：求一个向量在另一个向量上的投影向量、投影的数量
- 路径：投影的数量 $\dfrac{\vec a\cdot\vec b}{|\vec b|}$，投影向量 $\dfrac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$〔P57〕
- 注意：投影的数量可正可负；投影向量是向量（B 版简称“投影”）
E P57 Q76 apply |
- 【代入公式】$\vec a=(1,2)$，$\vec b=(3,4)$：$\vec a\cdot\vec b=11$，投影的数量 $\dfrac{11}{5}$，投影向量 $\dfrac{11}{25}(3,4)$

# ───────── 复数：实系数方程的虚根 ─────────
N P58 lorange cpx | 〔结构前提〕实系数一元二次方程，$\Delta<0$ | 实系数方程的虚根
- $ax^2+bx+c=0$（$a,b,c\in\mathbb{R}$，$a\ne 0$，$\Delta<0$）：$x=\dfrac{-b\pm\sqrt{-\Delta}\,i}{2a}$，两根互为共轭
- 韦达定理仍成立：$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$
- 特例：$a>0$ 时 $x^2=-a$ 的解为 $\pm\sqrt{a}\,i$；注意写 $\sqrt{-\Delta}\,i$，不写 $\sqrt{\Delta}$（$\Delta<0$）
- ✗ 系数不全是实数时虚根不一定成对：$x^2-ix=0$ 的根是 $0$、$i$
~ ⚡ 第一反应：实系数二次方程有一个虚根 $p+qi$ → 另一根是 $p-qi$，再用韦达
E S06 P58 derive main | ▼ 加条件〔结构前提〕：实系数，$\Delta<0$
- 【代入】$\left(\pm\sqrt{-\Delta}\,i\right)^2=\Delta$，所以 $x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{-\Delta}\,i}{2a}$
E P01 P58 derive |
- 【配方】$\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}<0$，在复数范围内开方
E P03 P58 premise |
- 【前提】两根相加、相乘的算法与实根时相同

N Q77 problem cpx | | 看到：复数相等求参数，在复数范围内解方程
- 路径：复数相等 $\iff$ 实部、虚部分别相等〔S06〕；实系数二次方程 $\Delta<0$ 时求出共轭虚根〔P58〕
- 注意：$a+bi$ 中 $a,b$ 必须是实数才能比较；纯虚数要求 $a=0$ 且 $b\ne 0$
E S06 Q77 apply |
- 【实部、虚部分别相等】$(x+yi)(1+i)=2$（$x,y\in\mathbb{R}$）：$(x-y)+(x+y)i=2\Rightarrow x=1$，$y=-1$
E P58 Q77 apply |
- 【求共轭虚根】$x^2+2x+5=0$：$\Delta=-16$，$x=-1\pm 2i$

# ───────── 数列：等差 Sn 的最值 ─────────
N Q78 problem seq | | 看到：等差数列前 $n$ 项和的最值
- 路径：① $S_n=An^2+Bn$ 配方，看离对称轴最近的正整数〔P28〕〔P01〕；② 或看 $a_n$ 何时由正变负〔P26〕
- 注意：$n$ 只取正整数；对称轴不是整数时比较两侧的整数
E P28 Q78 apply |
- 【配方看对称轴】$a_1=13$，$d=-2$：$S_n=-n^2+14n=-(n-7)^2+49$，$n=7$ 时最大 49
E P26 Q78 apply |
- 【看变号】$a_n=15-2n$：$a_7=1>0$，$a_8=-1<0$，前 7 项和最大

# ───────── ⑦ 函数性质 ─────────
N S15 start fun | | 【定义】函数的图像、奇偶性、周期性
- 图像：点 $(x,y)$ 在 $y=f(x)$ 的图像上 $\iff y=f(x)$
- 定义域关于原点对称，对每个 $x$：$f(-x)=f(x)$ 为偶函数，$f(-x)=-f(x)$ 为奇函数
- 存在非零常数 $T$，对定义域内每个 $x$ 有 $f(x+T)=f(x)$：周期函数；最小的正周期叫最小正周期
E S01 S15 define |
- 【定义】函数值之间的等式对定义域内每个 $x$ 都成立

N P61 orange fun | 〔定义域〕定义域关于原点对称 | ★ 奇偶函数的性质
- 偶函数图像关于 $y$ 轴对称，奇函数图像关于原点对称
- 奇函数在 $x=0$ 处有定义 $\Rightarrow f(0)=0$
- 两个奇函数或两个偶函数之积为偶函数；奇函数与偶函数之积为奇函数（在公共定义域上）
- 奇函数在两个对称区间上单调性相同，偶函数相反
- $x^{2n}$ 为偶函数，$x^{2n-1}$ 为奇函数（$n$ 为正整数）：只含奇次项的多项式是奇函数
- ✗ $f(x)=x^2$，$x\in[-1,2]$：定义域不关于原点对称，不是偶函数
~ ⋯ 同源：$\sin(-\alpha)=-\sin\alpha$、$\cos(-\alpha)=\cos\alpha$〔R14〕：正弦是奇函数，余弦是偶函数
~ ⚡ 第一反应：已知函数在一侧的式子求另一侧，或 $f(a)$ 求 $f(-a)$ → 奇偶性
E S15 P61 derive main | ▼ 加条件〔定义域〕：定义域关于原点对称
- 【代入】令 $x=0$：$f(0)=-f(0)$，故 $f(0)=0$
- 积：$f(-x)g(-x)=[-f(x)][-g(x)]=f(x)g(x)$；点 $(x,y)$ 与 $(-x,y)$ 或 $(-x,-y)$ 同在图像上

N P62 orange fun | 〔结构前提〕关系式对定义域内每个 $x$ 都成立 | ★★ 对称轴与对称中心
- $f(a+x)=f(a-x)\iff$ 图像关于直线 $x=a$ 对称；一般 $f(a+x)=f(b-x)$：对称轴 $x=\dfrac{a+b}{2}$
- $f(a+x)+f(a-x)=2b\iff$ 图像关于点 $(a,b)$ 对称
- 偶函数、奇函数是 $a=0$（$b=0$）的特例
- ✗ $y=f(1+x)$ 与 $y=f(1-x)$ 是两个函数，它们的图像关于直线 $x=0$ 对称，不是 $x=1$
~ ⚡ 第一反应：看到 $f(a+x)=f(b-x)$ → 对称轴取中点 $x=\dfrac{a+b}{2}$
E P61 P62 derive main | ▼ 加条件〔结构前提〕：关系式对每个 $x$ 成立
- 【平移】令 $g(x)=f(x+a)$：$g$ 为偶函数 $\iff f(a+x)=f(a-x)$
- $g(x)=f(x+a)-b$ 为奇函数 $\iff f(a+x)+f(a-x)=2b$

N P63 lorange fun ext | 〔结构前提〕关系式对每个 $x$ 成立，$a\ne 0$ | 周期的常用判定
- $f(x+a)=-f(x)\Rightarrow T=2a$；$f(x+a)=\dfrac{1}{f(x)}$（$f(x)\ne 0$）$\Rightarrow T=2a$
- 图像有两条对称轴 $x=a$、$x=b$（$a\ne b$）$\Rightarrow T=2|a-b|$
- 有对称中心 $(a,0)$ 和对称轴 $x=b$（$a\ne b$）$\Rightarrow T=4|a-b|$
- ✗ $f(x)=\sin 2\pi x$ 满足 $f(x+2)=f(x)$，但最小正周期是 1：推出的 $T$ 是周期，不一定是最小正周期
~ ⚡ 第一反应：看到 $f(x+a)=-f(x)$ 或两条对称轴 → 先求周期，再把大自变量化小
E S15 P63 derive | ▼ 加条件〔结构前提〕：关系式对每个 $x$ 成立
- 【代换】用两次：$f(x+2a)=-f(x+a)=f(x)$
E P62 P63 derive |
- 【代换】$f(x)=f(2a-x)=f[2b-(2a-x)]=f(x+2b-2a)$

N R45 white fun | | 图像变换：平移、伸缩、对称
- 平移：$y=f(x+h)$ 由 $y=f(x)$ 向左平移 $h$（$h>0$）；$y=f(x)+k$ 向上平移 $k$（$k>0$）
- 伸缩：$y=f(\omega x)$（$\omega>0$）横坐标变为原来的 $\dfrac{1}{\omega}$；$y=Af(x)$（$A>0$）纵坐标变为原来的 $A$ 倍
- 对称：$y=f(-x)$ 与 $y=f(x)$ 关于 $y$ 轴，$y=-f(x)$ 关于 $x$ 轴，$y=-f(-x)$ 关于原点
- 拓展（老教材）：坐标轴平移 $x=x'+h$，$y=y'+k$：曲线方程中把 $x$ 换成 $x'+h$，$y$ 换成 $y'+k$
- ✗ $y=\sin 2x$ 向左平移 $\dfrac{\pi}{6}$ 得 $y=\sin 2\left(x+\dfrac{\pi}{6}\right)=\sin\left(2x+\dfrac{\pi}{3}\right)$，不是 $\sin\left(2x+\dfrac{\pi}{6}\right)$
~ ⚡ 第一反应：问图像怎么变 → 平移、伸缩都只对 $x$ 本身操作（先提出 $\omega$）
E S15 R45 derive main |
- 【代入】$(x_0,y_0)$ 在 $y=f(x)$ 上 $\iff(x_0-h,\ y_0)$ 在 $y=f(x+h)$ 上 $\iff\left(\dfrac{x_0}{\omega},\ y_0\right)$ 在 $y=f(\omega x)$ 上

N P64 orange fun | 〔定义域〕$\omega\ne 0$，$A\ne 0$ | ★★ 正弦型函数 $y=A\sin(\omega x+\varphi)$
- 周期 $T=\dfrac{2\pi}{|\omega|}$，频率 $f=\dfrac{1}{T}$；振幅 $A$、初相 $\varphi$；最大值 $|A|$，最小值 $-|A|$
- 余弦曲线：对称轴 $x=k\pi$，对称中心 $\left(\dfrac{\pi}{2}+k\pi,0\right)$；正弦曲线：对称轴 $x=\dfrac{\pi}{2}+k\pi$，对称中心 $(k\pi,0)$
- 由 $y=\sin x$：向左（$\varphi>0$）或向右平移 $|\varphi|$ → 横坐标变为 $\dfrac{1}{\omega}$ 倍 → 纵坐标变为 $A$ 倍（$\omega>0$，$A>0$）
- 对称轴：$\omega x+\varphi=\dfrac{\pi}{2}+k\pi$；对称中心：$\omega x+\varphi=k\pi$，纵坐标 0
- 增区间（$\omega>0$，$A>0$）：$-\dfrac{\pi}{2}+2k\pi\le\omega x+\varphi\le\dfrac{\pi}{2}+2k\pi$
- ✗ $y=\sin(-2x)$ 的周期是 $\pi$，不是 $-\pi$：周期要用 $|\omega|$
~ ⚡ 第一反应：化成 $A\sin(\omega x+\varphi)$ 之后 → 把 $\omega x+\varphi$ 当整体，代入 $\sin$ 的性质
E R45 P64 derive main | ▼ 加条件〔定义域〕：$\omega\ne 0$，$A\ne 0$
- 【平移、伸缩】先 $x\to x+\varphi$，再 $x\to\omega x$，最后乘 $A$
E S15 P64 premise |
- 【前提】周期定义：$\sin\left[\omega\left(x+\dfrac{2\pi}{\omega}\right)+\varphi\right]=\sin(\omega x+\varphi+2\pi)$
E R14 P64 premise |
- 【前提】诱导公式 ①：$\sin(\alpha+2\pi)=\sin\alpha$
E P17 P64 premise |
- 【前提】辅助角把 $a\sin\omega x+b\cos\omega x$ 化成一个正弦

N Q80 problem fun | | 看到：判断奇偶性，或由奇偶性求值、求解析式
- 路径：① 先看定义域是否关于原点对称 → ② 算 $f(-x)$ 与 $f(x)$ 比较〔P61〕
- 注意：求另一侧解析式时设 $x<0$，则 $-x>0$ 代入已知式；奇函数 $0$ 在定义域内才有 $f(0)=0$
E P61 Q80 apply |
- 【设 $x<0$，用 $-x>0$】$f$ 为奇函数，$x>0$ 时 $f(x)=x^2+x$：$x<0$ 时 $f(x)=-f(-x)=-x^2+x$；$f(x)=ax^3+bx+1$，$f(2)=5\Rightarrow f(-2)=-3$

N Q81 problem fun | | 看到：$f(a+x)=f(b-x)$ 一类关系，求对称轴、对称中心
- 路径：对称轴 $x=\dfrac{a+b}{2}$；$f(a+x)+f(a-x)=2b$ 则对称中心 $(a,b)$〔P62〕
- 注意：区分“一个函数自身对称”与“两个函数图像互相对称”
E P62 Q81 apply |
- 【取中点】$f(x)=x^2+bx$ 满足 $f(1+x)=f(1-x)$：对称轴 $x=1=-\dfrac{b}{2}$，$b=-2$

N Q82 problem fun | | 看到：抽象函数求 $f(2025)$ 这类大自变量的值
- 路径：由关系式推出周期〔P63〕，再把自变量减去周期的整数倍
- 注意：先验证推出的是周期；结合奇偶性时把负值化正
E P63 Q82 apply |
- 【先求周期】$f(x+2)=-f(x)$，$f(1)=3$：$T=4$，$2025=4\times 506+1$，$f(2025)=f(1)=3$

N Q83 problem fun | | 看到：图像平移、伸缩后的解析式
- 路径：平移只对 $x$ 本身加减，伸缩把 $x$ 换成 $\omega x$〔R45〕；正弦型函数按顺序变换〔P64〕
- 注意：先伸缩后平移时，平移量要除以 $\omega$
E R45 Q83 apply |
- 【按顺序换 $x$】$y=\sin x$ 先左移 $\dfrac{\pi}{3}$ 得 $y=\sin\left(x+\dfrac{\pi}{3}\right)$，再横坐标缩为 $\dfrac{1}{2}$ 得 $y=\sin\left(2x+\dfrac{\pi}{3}\right)$
E P64 Q83 apply |
- 【先伸缩后平移】$y=\sin 2x$ 左移 $\dfrac{\pi}{6}$：$y=\sin\left(2x+\dfrac{\pi}{3}\right)$，与上一条结果相同

N Q84 problem fun | | 看到：正弦型函数的对称轴、对称中心、单调区间
- 路径：把 $\omega x+\varphi$ 当整体，令它等于 $\dfrac{\pi}{2}+k\pi$（对称轴）、$k\pi$（对称中心）〔P64〕
- 注意：$\omega<0$ 先用诱导公式化正；对称中心的纵坐标是上下平移量 $k$
E P64 Q84 apply |
- 【整体代入】$y=2\sin\left(2x+\dfrac{\pi}{6}\right)$：对称轴 $x=\dfrac{\pi}{6}+\dfrac{k\pi}{2}$，对称中心 $\left(-\dfrac{\pi}{12}+\dfrac{k\pi}{2},\ 0\right)$

# ───────── ⑧ 解析几何 ─────────
N S16 start geo | | 【定义】坐标法：倾斜角与斜率，曲线与方程
- 倾斜角 $\alpha\in[0,\pi)$；$\alpha\ne\dfrac{\pi}{2}$ 时斜率 $k=\tan\alpha$
- 曲线上点的坐标都是方程的解，以方程的解为坐标的点都在曲线上
- 圆：到定点距离为定长；椭圆：到两定点距离之和为 $2a$（$2a>|F_1F_2|$）
- 双曲线：到两定点距离之差的绝对值为 $2a$（$0<2a<|F_1F_2|$）；抛物线：到定点与定直线距离相等（定点不在定直线上）
E S04 S16 define |
- 【定义】斜率是倾斜角的正切
E S13 S16 define |
- 【定义】圆、椭圆、双曲线、抛物线都用两点距离公式写成方程

N P65 orange geo | 〔定义域〕$x_1\ne x_2$ | ★ 斜率公式与直线方程
- 斜率 $k=\dfrac{y_2-y_1}{x_2-x_1}$
- 点斜式 $y-y_0=k(x-x_0)$；斜截式 $y=kx+b$；截距式 $\dfrac{x}{a}+\dfrac{y}{b}=1$（$a,b\ne 0$）
- 两点式 $\dfrac{y-y_1}{y_2-y_1}=\dfrac{x-x_1}{x_2-x_1}$（$x_1\ne x_2$，$y_1\ne y_2$）
- 一般式 $Ax+By+C=0$（$A,B$ 不全为 0）：法向量 $(A,B)$，方向向量 $(B,-A)$；$B\ne 0$ 时 $k=-\dfrac{A}{B}$
- 方向向量 $(\cos\theta,\sin\theta)$，斜率存在时 $(1,k)$；方向向量 $(u,v)$、$u\ne 0$ 时 $k=\dfrac{v}{u}$
- 点法式 $A(x-x_0)+B(y-y_0)=0$；两点式的整式形式 $(x-x_1)(y_2-y_1)=(x_2-x_1)(y-y_1)$ 对任意两点都成立
- 三点共线 $\iff$ 任两点连线的斜率都相等（或都不存在）
- ✗ 点斜式、斜截式表示不了竖直线 $x=x_0$；两点式表示不了与坐标轴平行的直线；截距式表示不了过原点或与坐标轴平行的直线
~ ⚡ 第一反应：已知一点和斜率 → 点斜式；设直线时先想斜率是否存在
E S16 P65 derive main | ▼ 加条件〔定义域〕：$x_1\ne x_2$
- 【定义】$\tan\alpha=\dfrac{y_2-y_1}{x_2-x_1}$；直线上任一点与 $(x_0,y_0)$ 连线的斜率都是 $k$

N P66 orange geo | 〔定义域〕斜率式要求两条斜率都存在 | ★★ 两直线平行与垂直
- $l_1\parallel l_2\iff k_1=k_2$ 且 $b_1\ne b_2$；$l_1\perp l_2\iff k_1k_2=-1$
- 一般式：$l_1\perp l_2\iff A_1A_2+B_1B_2=0$；$l_1\parallel l_2\Rightarrow A_1B_2-A_2B_1=0$（还要排除重合）
- 重合 $\iff$ 有 $\lambda$ 使 $A_1=\lambda A_2$，$B_1=\lambda B_2$，$C_1=\lambda C_2$；$Ax+By+C_1=0$ 与 $Ax+By+C_2=0$ 平行 $\iff C_1\ne C_2$；相交 $\iff A_1B_2\ne A_2B_1$
- 与 $Ax+By+C=0$ 平行的设 $Ax+By+m=0$，垂直的设 $Bx-Ay+m=0$
- 拓展：夹角 $\tan\theta=\left|\dfrac{k_2-k_1}{1+k_1k_2}\right|$（$1+k_1k_2\ne 0$）；到角（老教材，有方向）$\tan\theta=\dfrac{k_2-k_1}{1+k_1k_2}$
- ✗ $x=1$ 与 $y=2$ 垂直，但 $x=1$ 没有斜率，$k_1k_2=-1$ 用不上
~ ⚡ 第一反应：两直线垂直 → 一般式 $A_1A_2+B_1B_2=0$，不用讨论斜率
E P49 P66 derive main |
- 【向量】两直线垂直 $\iff$ 法向量 $(A_1,B_1)\perp(A_2,B_2)\iff A_1A_2+B_1B_2=0$；平行 $\iff$ 法向量共线
E P65 P66 premise |
- 【前提】法向量 $(A,B)$；$k=-\dfrac{A}{B}$，$k_1k_2=-1\iff A_1A_2=-B_1B_2$
E P14 P66 premise |
- 【前提】夹角：$\tan(\alpha_2-\alpha_1)$ 用正切差角

N P67 orange geo | 〔定义域〕$A,B$ 不全为 0 | ★★ 点到直线、两平行线间的距离
- 点 $P(x_0,y_0)$ 到 $Ax+By+C=0$：$d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$
- 平行线 $Ax+By+C_1=0$ 与 $Ax+By+C_2=0$：$d=\dfrac{|C_1-C_2|}{\sqrt{A^2+B^2}}$
- ✗ $3x+4y-5=0$ 与 $6x+8y+1=0$：要先化成 $6x+8y-10=0$，$d=\dfrac{11}{10}$；直接用 $\dfrac{|-5-1|}{5}$ 错
~ ⚡ 第一反应：点到直线距离 → 代入 $|Ax_0+By_0+C|$，再除以 $\sqrt{A^2+B^2}$
E P57 P67 derive main |
- 【投影】在直线上取一点 $Q(x_1,y_1)$，$d=\dfrac{|\overrightarrow{QP}\cdot\vec n|}{|\vec n|}$，$\vec n=(A,B)$，$Ax_1+By_1=-C$
E P65 P67 premise |
- 【前提】一般式的法向量 $(A,B)$

N P68 orange geo | 〔定义域〕$D^2+E^2-4F>0$ | ★★ 圆的方程（配方）
- 标准方程 $(x-a)^2+(y-b)^2=r^2$
- 一般方程 $x^2+y^2+Dx+Ey+F=0$ 配方：$\left(x+\dfrac{D}{2}\right)^2+\left(y+\dfrac{E}{2}\right)^2=\dfrac{D^2+E^2-4F}{4}$
- 圆心 $\left(-\dfrac{D}{2},-\dfrac{E}{2}\right)$，半径 $\dfrac{1}{2}\sqrt{D^2+E^2-4F}$
- 二元二次方程表示圆：$x^2$、$y^2$ 系数相等且不含 $xy$ 项，再验 $D^2+E^2-4F>0$
- 点 $(x_1,y_1)$ 与圆：$(x_1-a)^2+(y_1-b)^2$ 大于、等于、小于 $r^2$ 分别为圆外、圆上、圆内
- 以 $A(x_1,y_1)$、$B(x_2,y_2)$ 为直径的圆：$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0$（由 $\overrightarrow{PA}\cdot\overrightarrow{PB}=0$）
- ✗ $x^2+y^2+2x+2=0$：$D^2+E^2-4F=4-8<0$，不表示任何图形
~ ⚡ 第一反应：看到 $x^2+y^2+Dx+Ey+F=0$ → 配方读圆心、半径
E S16 P68 derive main |
- 【定义】到圆心距离为 $r$：$\sqrt{(x-a)^2+(y-b)^2}=r$，两边平方
E R03 P68 derive | ▼ 加条件〔定义域〕：$D^2+E^2-4F>0$
- 【配方】$x^2+Dx=\left(x+\dfrac{D}{2}\right)^2-\dfrac{D^2}{4}$，$y$ 同理

N P69 orange geo | 〔结构前提〕$d$ 为圆心到直线的距离，$r$ 为半径 | ★★ 直线与圆：位置关系、弦长、切线
- $d<r$ 相交，$d=r$ 相切，$d>r$ 相离
- 弦长 $|AB|=2\sqrt{r^2-d^2}$
- 圆 $x^2+y^2=r^2$ 上一点 $(x_0,y_0)$ 处的切线：$x_0x+y_0y=r^2$
- 两圆：圆心距 $d$ 与 $r_1+r_2$、$|r_1-r_2|$ 比较；两圆相交时，两方程相减得公共弦所在直线
- 外离 $d>r_1+r_2$，外切 $d=r_1+r_2$，相交 $|r_1-r_2|<d<r_1+r_2$，内切 $d=|r_1-r_2|$，内含 $d<|r_1-r_2|$
~ ⚡ 第一反应：直线与圆的问题 → 先算圆心到直线的距离 $d$，再与 $r$ 比
E P67 P69 derive main |
- 【勾股】半弦长、$d$、$r$ 构成直角三角形（垂径定理）
E S13 P69 premise |
- 【前提】垂径定理、勾股定理
E P49 P69 premise |
- 【前提】切线垂直于半径：$(x-x_0,\ y-y_0)\cdot(x_0,y_0)=0$，展开用 $x_0^2+y_0^2=r^2$

N P70 orange geo | 〔结构前提〕椭圆 $a>b>0$，双曲线 $a>0,b>0$，中心在原点、焦点在坐标轴上 | ★★ 椭圆、双曲线的基本量
- 椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$：$a^2=b^2+c^2$，$e=\dfrac{c}{a}\in(0,1)$，$e^2=1-\dfrac{b^2}{a^2}$
- 双曲线 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$：$c^2=a^2+b^2$，$e=\dfrac{c}{a}>1$，$e^2=1+\dfrac{b^2}{a^2}$，渐近线 $y=\pm\dfrac{b}{a}x$
- 椭圆上的点 $P$：$|PF_1|+|PF_2|=2a$；双曲线上的点：$|PF_1|$ 与 $|PF_2|$ 之差的绝对值为 $2a$
- 焦点在 $y$ 轴：椭圆 $\dfrac{y^2}{a^2}+\dfrac{x^2}{b^2}=1$；双曲线 $\dfrac{y^2}{a^2}-\dfrac{x^2}{b^2}=1$，渐近线 $y=\pm\dfrac{a}{b}x$（不是 $\dfrac{b}{a}$）
- 顶点：椭圆 $(\pm a,0)$、$(0,\pm b)$，长轴 $2a$、短轴 $2b$；双曲线 $(\pm a,0)$，实轴 $2a$、虚轴 $2b$；等轴双曲线 $a=b$，$e=\sqrt{2}$，渐近线 $y=\pm x$
- 焦半径（标准方程推导中的式子）：椭圆 $|PF_1|=a+ex_0$，$|PF_2|=a-ex_0$；双曲线 $|PF_1|=|ex_0+a|$
- 椭圆上点到焦点的距离最小 $a-c$、最大 $a+c$（长轴端点）；双曲线上点到焦点的距离最小 $c-a$
- 设方程：两点定椭圆设 $mx^2+ny^2=1$；共渐近线的双曲线设 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=\lambda$（$\lambda\ne 0$）
- ✗ 椭圆 $\dfrac{x^2}{4}+\dfrac{y^2}{9}=1$ 焦点在 $y$ 轴：$a^2=9$，$c=\sqrt{5}$；误取 $a^2=4$ 得 $c^2=4-9<0$
~ ⚡ 第一反应：已知 $a,b,c,e$ 中的两个 → 椭圆用 $a^2=b^2+c^2$，双曲线用 $c^2=a^2+b^2$；求 $e$ 列 $a,c$ 的齐次式
E S16 P70 derive main | ▼ 加条件〔结构前提〕：标准位置
- 【定义】$\sqrt{(x+c)^2+y^2}+\sqrt{(x-c)^2+y^2}=2a$，移项、平方两次，令 $b^2=a^2-c^2$
- 双曲线同理，令 $b^2=c^2-a^2$
E R03 P70 premise |
- 【前提】两边平方用完全平方展开

N P71 lorange geo | 〔结构前提〕抛物线标准方程（$p>0$） | 抛物线：四种标准方程、焦半径与焦点弦
- $y^2=2px$：焦点 $\left(\dfrac{p}{2},0\right)$，准线 $x=-\dfrac{p}{2}$；$y^2=-2px$：焦点 $\left(-\dfrac{p}{2},0\right)$，准线 $x=\dfrac{p}{2}$
- $x^2=2py$：焦点 $\left(0,\dfrac{p}{2}\right)$，准线 $y=-\dfrac{p}{2}$；$x^2=-2py$：焦点 $\left(0,-\dfrac{p}{2}\right)$，准线 $y=\dfrac{p}{2}$；$y=ax^2$ 先化成 $x^2=\dfrac{1}{a}y$
- 焦半径 $|PF|=x_0+\dfrac{p}{2}$（$y^2=2px$）：到焦点的距离 = 到准线的距离；$x^2=2py$ 时 $|PF|=y_0+\dfrac{p}{2}$
- 过焦点的弦 $|AB|=x_1+x_2+p$（两段焦半径相加；教材习题中使用）
- 过焦点的弦 $y_1y_2=-p^2$（选必一练习 A）；拓展：$x_1x_2=\dfrac{p^2}{4}$
~ ⚡ 第一反应：抛物线上的点到焦点的距离 → 换成到准线的距离
E S16 P71 derive main | ▼ 加条件〔结构前提〕：标准位置
- 【定义】到焦点距离 = 到准线 $x=-\dfrac{p}{2}$ 的距离 $x_0+\dfrac{p}{2}$；焦点弦 = 两段焦半径之和
E P03 P71 premise |
- 【前提】韦达：设 $x=my+\dfrac{p}{2}$ 代入得 $y^2-2pmy-p^2=0$，$y_1y_2=-p^2$

N P72 orange geo | 〔定义域〕联立后二次项系数 $\ne 0$，且 $\Delta>0$ | ★★ 直线与圆锥曲线：联立、弦长、中点
- 联立消 $y$ 得 $Ax^2+Bx+C=0$：$x_1+x_2=-\dfrac{B}{A}$，$x_1x_2=\dfrac{C}{A}$
- 弦长 $|AB|=\sqrt{1+k^2}\,|x_1-x_2|=\sqrt{1+\dfrac{1}{k^2}}\,|y_1-y_2|$（后式 $k\ne 0$）
- 中点 $\left(\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\right)$
- ✗ $x^2-y^2=1$ 与 $y=x+1$：消元后二次项系数为 0（直线平行于渐近线），只有一个交点 $(-1,0)$
- 相切 $\iff$ 消元后的一元二次方程 $\Delta=0$；与抛物线只有一个公共点还可能是平行于对称轴的直线（不是相切）
~ ⚡ 第一反应：直线与曲线交于两点 → 设而不求：联立、判别式、韦达、整体代入
E P45 P72 derive main | ▼ 加条件〔定义域〕：二次项系数 $\ne 0$，$\Delta>0$
- 【代入】$|AB|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$，$y_1-y_2=k(x_1-x_2)$
E S13 P72 premise |
- 【前提】两点距离公式
E P65 P72 premise |
- 【前提】设直线 $y=kx+m$（斜率不存在时另算）

N P73 lorange geo | 〔结构前提〕弦 $AB$ 的中点 $M(x_0,y_0)$，$x_1\ne x_2$，$x_0\ne 0$ | 点差法（中点弦；选必一复习题 B13、B23）
- 椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$：$k_{AB}\cdot k_{OM}=-\dfrac{b^2}{a^2}$
- 双曲线 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$：$k_{AB}\cdot k_{OM}=\dfrac{b^2}{a^2}$
- 抛物线 $y^2=2px$：$k_{AB}=\dfrac{p}{y_0}$（$y_0\ne 0$）
- ✗ 双曲线 $x^2-\dfrac{y^2}{2}=1$ 以 $(1,1)$ 为中点：点差得 $y=2x-1$，代回 $\Delta=16-24<0$，这样的弦不存在
~ ⚡ 第一反应：已知弦的中点求斜率 → 点差法，求完要回代验 $\Delta>0$
E P70 P73 derive | ▼ 加条件〔结构前提〕：已知中点
- 【作差】两点坐标分别代入方程再相减：$\dfrac{(x_1+x_2)(x_1-x_2)}{a^2}+\dfrac{(y_1+y_2)(y_1-y_2)}{b^2}=0$
E R02 P73 premise |
- 【前提】平方差

N Q85 problem geo | | 看到：求直线方程，判断两直线平行、垂直
- 路径：已知点和斜率用点斜式〔P65〕；与已知直线平行或垂直时，按一般式设方程〔P66〕
- 注意：平行要排除重合；设斜率时单独讨论斜率不存在的情形
E P66 Q85 apply |
- 【垂直设方程】过 $(1,2)$ 且与 $2x-y+1=0$ 垂直：设 $x+2y+m=0$，代入得 $m=-5$，即 $x+2y-5=0$
E P65 Q85 apply |
- 【两点求斜率】过 $(1,2)$、$(3,6)$：$k=2$，$y-2=2(x-1)$，即 $y=2x$

N Q86 problem geo | | 看到：点到直线的距离、两平行线间的距离
- 路径：代入距离公式〔P67〕
- 注意：直线先化成一般式；两平行线的 $x,y$ 系数要化成相同
E P67 Q86 apply |
- 【代入公式】$(1,2)$ 到 $3x+4y-1=0$：$d=\dfrac{|3+8-1|}{5}=2$

N Q87 problem geo | | 看到：圆的一般方程，求圆心和半径
- 路径：配方化成标准方程〔P68〕
- 注意：先验 $D^2+E^2-4F>0$；$x^2$、$y^2$ 系数不为 1 时先同除
E P68 Q87 apply |
- 【配方】$x^2+y^2-4x+2y-4=0\Rightarrow(x-2)^2+(y+1)^2=9$：圆心 $(2,-1)$，半径 3

N Q88 problem geo | | 看到：直线与圆的位置关系、弦长、切线
- 路径：圆心到直线的距离 $d$ 与 $r$ 比较；弦长 $2\sqrt{r^2-d^2}$〔P69〕
- 注意：过圆外一点的切线有两条，斜率不存在的那条容易漏
E P69 Q88 apply |
- 【先求 $d$】圆 $x^2+y^2=4$，直线 $x+y-2=0$：$d=\sqrt{2}<2$，相交，弦长 $2\sqrt{4-2}=2\sqrt{2}$；圆 $x^2+y^2=5$ 上点 $(1,2)$ 处的切线 $x+2y=5$

N Q89 problem geo | | 看到：椭圆、双曲线求离心率、渐近线
- 路径：$a,b,c$ 的关系〔P70〕；求 $e$ 时把条件化成 $a,c$ 的齐次式
- 注意：先看焦点在哪条轴上；椭圆 $0<e<1$，双曲线 $e>1$
E P70 Q89 apply |
- 【用 $a,b,c$ 关系】$\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$：$c=4$，$e=\dfrac{4}{5}$；双曲线渐近线 $y=\pm 2x$：$\dfrac{b}{a}=2$，$e=\sqrt{1+4}=\sqrt{5}$

N Q90 problem geo | | 看到：抛物线上的点到焦点的距离、焦点弦长
- 路径：到焦点的距离换成到准线的距离〔P71〕
- 注意：先把方程化成标准形，读出 $p$（$y^2=4x$ 中 $2p=4$）
E P71 Q90 apply |
- 【换成到准线的距离】$y^2=4x$（$p=2$）上横坐标为 3 的点：$|PF|=3+1=4$；过焦点的弦 $x_1+x_2=6$：$|AB|=8$

N Q91 problem geo | | 看到：直线与圆锥曲线相交，求弦长、中点、面积
- 路径：① 设直线 → ② 联立消元，判别式 $\Delta>0$ → ③ 韦达 → ④ 弦长、中点整体代入〔P72〕
- 注意：消元后二次项系数可能为 0；斜率不存在的直线单独讨论
~ 同见代数〔Q16〕
E P72 Q91 apply |
- 【设而不求】$\dfrac{x^2}{4}+y^2=1$ 与 $y=x+1$：$\dfrac{5}{4}x^2+2x=0$，$x_1+x_2=-\dfrac{8}{5}$，$x_1x_2=0$，弦长 $\sqrt{2}\times\dfrac{8}{5}=\dfrac{8\sqrt{2}}{5}$，中点 $\left(-\dfrac{4}{5},\dfrac{1}{5}\right)$

N Q92 problem geo | | 看到：已知弦的中点，求弦所在直线
- 路径：点差法〔P73〕得斜率，点斜式写方程，再回代验 $\Delta>0$
- 注意：中点在椭圆内时弦一定存在；双曲线要验证
E P73 Q92 apply |
- 【点差】$\dfrac{x^2}{4}+\dfrac{y^2}{2}=1$ 中以 $M(1,1)$ 为中点的弦：$k\times 1=-\dfrac{2}{4}$，$k=-\dfrac{1}{2}$，直线 $x+2y-3=0$

# ───────── ③c 空间向量与立体几何 ─────────
N S17 start sp | | 【定义】空间向量与空间直角坐标系
- 单位正交基 $\vec i,\vec j,\vec k$ 两两垂直、长度为 1；$\vec a=x\vec i+y\vec j+z\vec k$ 记作 $(x,y,z)$
- 直线的方向向量 $\vec u$；平面的法向量 $\vec n$：与平面垂直的非零向量
- 运算律与平面向量相同（课本给出）
- 直线：$B\in l\iff\overrightarrow{AB}=\lambda\vec u$；平面：$B\in\alpha\iff\overrightarrow{AB}\cdot\vec n=0$
E S05 S17 define |
- 【定义】把平面向量推广到空间，基底多一个 $\vec k$

N R46 green sp | | ★★ 空间向量的坐标运算
- $\vec a\cdot\vec b=x_1x_2+y_1y_2+z_1z_2$，$|\vec a|=\sqrt{x_1^2+y_1^2+z_1^2}$
- $\vec a\perp\vec b\iff x_1x_2+y_1y_2+z_1z_2=0$；非零向量 $\cos\langle\vec a,\vec b\rangle=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$
- 两点距离 $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2}$；长方体对角线 $l^2=a^2+b^2+c^2$
- 线性运算：$\vec a\pm\vec b$、$\lambda\vec a$ 按分量；$\overrightarrow{AB}$ = 终点减起点；中点坐标取平均
- 平行：$\vec a\ne\vec 0$ 时 $\vec a\parallel\vec b\iff\vec b=\lambda\vec a$；分量都不为 0 时 $\dfrac{x_2}{x_1}=\dfrac{y_2}{y_1}=\dfrac{z_2}{z_1}$
- 基底法求长：$|\vec a+\vec b+\vec c|^2=|\vec a|^2+|\vec b|^2+|\vec c|^2+2(\vec a\cdot\vec b+\vec b\cdot\vec c+\vec c\cdot\vec a)$（与三数和的平方同型）
~ ⚡ 第一反应：立体几何能建系 → 写出点的坐标，用坐标数量积
E S17 R46 derive main |
- 【展开】与平面坐标式相同，多一项 $z_1z_2$
E R15 R46 premise |
- 【前提】平面数量积坐标式的推法

N P74 orange sp | 〔定义域〕$\vec n\ne\vec 0$；〔符号分支〕二面角是锐角还是钝角看图 | ★★ 法向量与空间角
- 求 $\vec n$：设 $\vec n=(x,y,z)$，令 $\vec n\cdot\overrightarrow{AB}=0$，$\vec n\cdot\overrightarrow{AC}=0$（$\overrightarrow{AB},\overrightarrow{AC}$ 不共线），取一组非零解
- 线线角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\cos\theta=|\cos\langle\vec u_1,\vec u_2\rangle|$
- 线面角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\sin\theta=|\cos\langle\vec u,\vec n\rangle|$
- 二面角 $\theta\in[0,\pi]$：$|\cos\theta|=|\cos\langle\vec n_1,\vec n_2\rangle|$，锐角还是钝角由图形判断
- 两平面所成角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\cos\theta=|\cos\langle\vec n_1,\vec n_2\rangle|$，$\sin\theta=\sin\langle\vec n_1,\vec n_2\rangle$，不用判断锐钝
- 平行、垂直：$l\perp\alpha\iff\vec u\parallel\vec n$；$l\parallel\alpha$ 或 $l\subset\alpha\iff\vec u\cdot\vec n=0$；$\vec n_1\perp\vec n_2\Rightarrow\alpha_1\perp\alpha_2$，$\vec n_1\parallel\vec n_2\Rightarrow\alpha_1\parallel\alpha_2$ 或重合
- ✗ 线面角写成 $\cos\theta=|\cos\langle\vec u,\vec n\rangle|$ 是错的：法向量与平面垂直，两角互余
~ ⚡ 第一反应：求空间角 → 方向向量、法向量的夹角；线面角取正弦
E R46 P74 derive main | ▼ 加条件〔定义域〕〔符号分支〕：$\vec n\ne\vec 0$；二面角看图
- 【夹角】线线角取不超过 $\dfrac{\pi}{2}$ 的那个，加绝对值
- 线面角 $\theta$ 与 $\langle\vec u,\vec n\rangle$ 互余（或差 $\dfrac{\pi}{2}$），用诱导公式化成正弦
E R14 P74 premise |
- 【前提】诱导公式 ⑤⑥：$\cos\left(\dfrac{\pi}{2}\pm\theta\right)=\mp\sin\theta$

N P75 orange sp | 〔定义域〕$\vec n\ne\vec 0$ | ★ 点到平面的距离
- $d=\dfrac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}$（$A$ 为平面内任一点）
- 直线到平行平面、两平行平面间的距离：都化成点到平面的距离
~ ⋯ 同源：点到直线的距离〔P67〕，都是向量在法向量上的投影
~ ⚡ 第一反应：点到平面的距离 → 平面内任取一点连向该点，求在法向量上的投影
E P57 P75 derive main | ▼ 加条件〔定义域〕：$\vec n\ne\vec 0$
- 【投影】$\overrightarrow{AP}$ 在法向量方向上投影的绝对值
E P74 P75 premise |
- 【前提】先求法向量

N S18 start sp | | 【课本给出】祖暅原理，柱、锥、球的体积与面积
- 祖暅原理：夹在两个平行平面间的两个几何体，被平行于这两个平面的任意平面所截，截面积总相等，则体积相等
- 柱体 $V=Sh$；锥体 $V=\dfrac{1}{3}Sh$；球 $V=\dfrac{4}{3}\pi R^3$，$S=4\pi R^2$
- 圆柱侧面积 $2\pi rl$；圆锥侧面积 $\pi rl$（由侧面展开图得出：矩形、扇形〔P83〕）
E S13 S18 define |
- 【定义】底面积用平面图形的面积

N P76 lorange sp | 〔结构前提〕台体：上下底平行且相似，截面积之比为对应边之比的平方 | 台体的体积与侧面积
- $V=\dfrac{1}{3}h\left(S+\sqrt{SS'}+S'\right)$（$S$、$S'$ 为下、上底面积）
- $S'=S$ 时即柱体 $Sh$，$S'=0$ 时即锥体 $\dfrac{1}{3}Sh$
- 圆台侧面积 $\pi(r+r')l$；全面积：圆柱 $2\pi r(r+l)$，圆锥 $\pi r(r+l)$，圆台 $\pi(r'^2+r^2+r'l+rl)$
- 侧面积：直棱柱 $ch$，正棱锥 $\dfrac{1}{2}ch'$，正棱台 $\dfrac{1}{2}(c+c')h'$（$c$ 底面周长，$h'$ 斜高；$c'=c$、$c'=0$ 时得前两式）
- 拓展（老教材）：拟柱体 $V=\dfrac{h}{6}(S+4S_0+S')$（$S_0$ 为中截面面积），柱、锥、台、球都适用
~ ⚡ 第一反应：台体 → 补成大锥再减去小锥
E S18 P76 derive main | ▼ 加条件〔结构前提〕：台体
- 【补形相减】台体 = 大锥 − 小锥；小锥高 $x$ 满足 $\dfrac{x}{x+h}=\dfrac{\sqrt{S'}}{\sqrt{S}}$
- $V=\dfrac{1}{3}S(x+h)-\dfrac{1}{3}S'x=\dfrac{1}{3}\left[Sh+x(S-S')\right]$，代入 $x=\dfrac{h\sqrt{S'}}{\sqrt{S}-\sqrt{S'}}$
E R02 P76 premise |
- 【前提】$S-S'=(\sqrt{S}-\sqrt{S'})(\sqrt{S}+\sqrt{S'})$

N P77 lorange sp ext | 〔结构前提〕长方体，或能补成长方体的几何体 | 外接球半径（补形）
- 长方体棱长 $a,b,c$：外接球直径 $2R=\sqrt{a^2+b^2+c^2}$
- 正方体棱长 $a$：外接球 $R=\dfrac{\sqrt{3}}{2}a$，内切球 $r=\dfrac{a}{2}$
- 三条侧棱两两垂直的三棱锥：补成长方体
~ ⚡ 第一反应：求外接球 → 能补成长方体就用体对角线
E R46 P77 derive | ▼ 加条件〔结构前提〕：能补成长方体
- 【补形】长方体的体对角线就是外接球的直径

N Q93 problem sp | | 看到：求异面直线所成角、线面角、二面角
- 路径：① 建系写坐标〔R46〕→ ② 求方向向量、法向量 → ③ 套夹角公式〔P74〕
- 注意：线面角用正弦；二面角的锐、钝要看图；异面直线所成角取绝对值
E P74 Q93 apply |
- 【线面角取正弦】棱长 1 的正方体，$A$ 为原点：$\overrightarrow{A_1C}=(1,1,-1)$，底面法向量 $(0,0,1)$，$\sin\theta=\dfrac{1}{\sqrt{3}}=\dfrac{\sqrt{3}}{3}$

N Q94 problem sp | | 看到：点到平面的距离
- 路径：求平面的法向量〔P74〕，再求投影〔P75〕；也可用等体积法〔S18〕
- 注意：$\overrightarrow{AP}$ 的起点 $A$ 要在平面内
E P75 Q94 apply |
- 【投影】平面过 $(1,0,0)$、$(0,1,0)$、$(0,0,1)$，$\vec n=(1,1,1)$：原点到平面的距离 $\dfrac{1}{\sqrt{3}}=\dfrac{\sqrt{3}}{3}$

N Q95 problem sp | | 看到：求几何体的体积、表面积、外接球
- 路径：柱、锥、球直接代公式〔S18〕；台体〔P76〕；外接球先补形〔P77〕
- 注意：锥体别漏 $\dfrac{1}{3}$；表面积要加上底面
E P76 Q95 apply |
- 【台体公式】圆台上下底半径 1、2，高 3：$V=\dfrac{1}{3}\times 3\times(\pi+2\pi+4\pi)=7\pi$
E P77 Q95 apply |
- 【补形】棱长 2 的正方体：外接球 $R=\sqrt{3}$，表面积 $12\pi$

N Q96 problem sp | | 看到：用向量证明线面平行、垂直
- 路径：直线方向向量与平面法向量：共线 $\Rightarrow$ 垂直，数量积为 0 $\Rightarrow$ 平行或在平面内〔P74〕
- 注意：证线面平行还要说明直线不在平面内
E P74 Q96 apply |
- 【看方向向量与法向量】$\vec u=(1,2,-1)$，$\vec n=(2,4,-2)=2\vec u\Rightarrow l\perp\alpha$；$\vec u=(1,0,1)$，$\vec n=(1,1,-1)$，$\vec u\cdot\vec n=0\Rightarrow l\parallel\alpha$ 或 $l\subset\alpha$

# ───────── ⑨ 概率统计 ─────────
N S19 start prob | | 【定义】古典概型、事件的关系、独立与条件概率
- 古典概型：$P(A)=\dfrac{k}{n}$（$n$ 为样本点总数，$k$ 为 $A$ 包含的样本点数）
- 互斥：$A\cap B=\varnothing$；对立：互斥且 $A\cup B=\Omega$
- 性质（课本给出）：$0\le P(A)\le 1$，$P(\Omega)=1$；$A,B$ 互斥时 $P(A\cup B)=P(A)+P(B)$
- 独立：$P(AB)=P(A)P(B)$；条件概率：$P(B|A)=\dfrac{P(AB)}{P(A)}$（$P(A)>0$）
E S07 S19 define |
- 【定义】古典概型用计数原理数样本点
E S14 S19 define |
- 【定义】事件是样本空间 $\Omega$ 的子集，事件的运算就是集合的运算

N R47 green prob | | ★★ 概率的加法公式、对立事件
- 对立事件：$P(\bar A)=1-P(A)$
- 一般：$P(A\cup B)=P(A)+P(B)-P(A\cap B)$（必修二 5.3 探究题；B 版记作 $P(A+B)$、$P(AB)$）
- ✗ 掷骰子，$A$=偶数点，$B$=点数 $\le 3$：$P(A)+P(B)=1$，但 $A,B$ 不对立，$P(A\cup B)=\dfrac{5}{6}$
~ ⋯ 同源：容斥原理〔R40〕
~ ⚡ 第一反应：“至少一个”“不都是” → 先算对立事件，再用 1 减
E S19 R47 derive main |
- 【拆成互斥】$A\cup B=A\cup(\bar AB)$，$B=AB\cup(\bar AB)$，两式用互斥加法后相减
- 对立：$A\cup\bar A=\Omega$，$P(A)+P(\bar A)=1$
E R40 R47 premise |
- 【前提】与容斥原理同型：重叠部分减一次

N P78 orange prob | 〔定义域〕$P(A)>0$ | ★★ 条件概率与乘法公式、独立的判断
- 乘法公式：$P(AB)=P(A)P(B|A)$
- 古典概型中 $P(B|A)=\dfrac{n(AB)}{n(A)}$：在 $A$ 里数 $B$
- $A,B$ 独立 $\iff P(B|A)=P(B)$；$A,B$ 独立则 $A$ 与 $\bar B$、$\bar A$ 与 $\bar B$ 也独立
- 推广：$P(A_1A_2A_3)=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)$；$A,B,C$ 相互独立时 $P(ABC)=P(A)P(B)P(C)$
- 条件概率也满足概率的性质：$P(\bar B|A)=1-P(B|A)$；$B,C$ 互斥时 $P(B\cup C|A)=P(B|A)+P(C|A)$
- ✗ $P(B|A)$ 与 $P(A|B)$ 不同：掷骰子，$A$=点数为 2，$B$=偶数点：$P(B|A)=1$，$P(A|B)=\dfrac{1}{3}$
~ ⚡ 第一反应：“在……发生的条件下” → 条件概率，缩小样本空间；“相互独立” → 概率相乘
E S19 P78 derive main | ▼ 加条件〔定义域〕：$P(A)>0$
- 【变形】条件概率定义两边乘 $P(A)$；古典概型分子、分母同除 $n(\Omega)$
- $P(A\bar B)=P(A)-P(AB)=P(A)[1-P(B)]$
E R47 P78 premise |
- 【前提】对立事件 $P(\bar B)=1-P(B)$

N P79 orange prob | 〔结构前提〕$A_1,\cdots,A_n$ 两两互斥、并为 $\Omega$，$P(A_i)>0$ | ★ 全概率公式与贝叶斯公式
- 全概率：$P(B)=\displaystyle\sum_{i=1}^{n}P(A_i)P(B|A_i)$
- 贝叶斯：$P(A_i|B)=\dfrac{P(A_i)P(B|A_i)}{P(B)}$（$P(B)>0$）
- ✗ 掷骰子，$A_1$=点数 $\le 4$，$A_2$=点数 $\ge 3$ 有重叠，$B$=点数为 3：套公式得 $\dfrac{1}{3}$，而 $P(B)=\dfrac{1}{6}$
~ ⚡ 第一反应：结果由几种“来源”造成 → 全概率（分来源相加）；已知结果反问来源 → 贝叶斯
E P78 P79 derive main | ▼ 加条件〔结构前提〕：完备事件组
- 【拆成互斥】$B=A_1B\cup\cdots\cup A_nB$，各项两两互斥，每项用乘法公式
- 贝叶斯：$P(A_iB)$ 用两种乘法公式表示，相等后相除
E S19 P79 premise |
- 【前提】互斥事件的加法

N S20 start prob | | 【定义】离散型随机变量的分布列、均值与方差
- 分布列 $P(X=x_i)=p_i$，$p_i\ge 0$，$p_1+p_2+\cdots+p_n=1$
- 均值 $E(X)=\sum x_ip_i$；方差 $D(X)=\sum\left[x_i-E(X)\right]^2p_i$
- $P(X\le a)+P(X>a)=1$；$Y=aX+b$（$a\ne 0$）时 $P(X=t)=P(Y=at+b)$，两个分布列的概率行相同
E S19 S20 define |
- 【定义】随机变量的每个取值对应一个事件

N R48 green prob | | ★★ 均值与方差的性质
- $E(aX+b)=aE(X)+b$；$D(aX+b)=a^2D(X)$
- $D(X)=E(X^2)-[E(X)]^2$
- ✗ $D(2X+1)\ne 2D(X)+1$：$X$ 取 0、1 各 $\dfrac{1}{2}$，$D(X)=\dfrac{1}{4}$，$D(2X+1)=1$
~ ⚡ 第一反应：已知 $X$ 的均值、方差，求 $aX+b$ 的 → 线性性质；方差难算 → $E(X^2)-[E(X)]^2$
E S20 R48 derive main |
- 【展开】$\sum(ax_i+b)p_i=a\sum x_ip_i+b\sum p_i$
- $D(X)=\sum\left[x_i^2-2x_iE(X)+E(X)^2\right]p_i$，逐项求和
E R03 R48 premise |
- 【前提】完全平方展开

N R49 white prob | | 样本的平均数与方差（含分层）
- $\bar x=\dfrac{1}{n}\sum x_i$，$s^2=\dfrac{1}{n}\sum(x_i-\bar x)^2=\dfrac{1}{n}\sum x_i^2-\bar x^2$
- 数据 $ax_i+b$：平均数 $a\bar x+b$，方差 $a^2s^2$
- 分层：两层各 $m$、$n$ 个，平均数 $\bar x$、$\bar y$，方差 $s_1^2$、$s_2^2$：总平均数 $\bar w=\dfrac{m\bar x+n\bar y}{m+n}$
- 总方差 $=\dfrac{m\left[s_1^2+(\bar x-\bar w)^2\right]+n\left[s_2^2+(\bar y-\bar w)^2\right]}{m+n}$
~ ⚡ 第一反应：数据整体乘加 → 平均数跟着变，方差只乘 $a^2$；两组合并 → 分层公式
E R48 R49 derive |
- 【特例】把每个数据看作取值概率为 $\dfrac{1}{n}$
- 分层：$\sum(x_i-\bar w)^2=\sum(x_i-\bar x)^2+m(\bar x-\bar w)^2$（交叉项 $\sum(x_i-\bar x)=0$）

N P82 lorange prob | 〔定义域〕$\sum(x_i-\bar x)^2\ne 0$ | 回归直线（最小二乘法）与相关系数
- $\hat y=\hat bx+\hat a$：$\hat b=\dfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}=\dfrac{\sum x_iy_i-n\bar x\bar y}{\sum x_i^2-n\bar x^2}$，$\hat a=\bar y-\hat b\bar x$
- 最小二乘：使残差 $e_i=y_i-\hat y_i$ 的平方和 $\sum(y_i-\hat bx_i-\hat a)^2$ 最小
- 回归直线一定过 $(\bar x,\bar y)$：$\hat y-\bar y=\hat b(x-\bar x)$（点斜式）；$x$ 每增加 1，$\hat y$ 平均增加 $\hat b$
- 相关系数 $r=\dfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2\sum(y_i-\bar y)^2}}$，$|r|\le 1$，$|r|$ 越接近 1 线性相关越强
- $r>0$ 正相关，$r<0$ 负相关；$|r|=1\iff$ 所有点都在回归直线上
- 拓展阅读：$r=\cos\langle\vec a,\vec b\rangle$，$\vec a=(x_1-\bar x,\cdots,x_n-\bar x)$，$\vec b=(y_1-\bar y,\cdots,y_n-\bar y)$
- 非线性回归：如 $y=b\sqrt{x}+a$，令 $u=\sqrt{x}$ 化成线性回归
~ 同见不等式大厦 R66：$|r|\le 1$ 由柯西不等式得到
~ ⚡ 第一反应：求回归方程 → 先算 $\bar x,\bar y$，再求 $\hat b$，最后 $\hat a=\bar y-\hat b\bar x$
E R49 P82 derive main | ▼ 加条件〔定义域〕：$x_i$ 不全相等
- 【配方】$Q(a,b)=\sum(y_i-bx_i-a)^2$：先对 $a$ 配方得 $a=\bar y-b\bar x$，再对 $b$ 配方
E P01 P82 premise |
- 【前提】二次式配方求最小值

N P80 orange prob | 〔结构前提〕$n$ 次独立重复试验，每次成功的概率为 $p$ | ★★ 二项分布
- $P(X=k)=C_n^kp^k(1-p)^{n-k}$（$k=0,1,\cdots,n$）
- $E(X)=np$，$D(X)=np(1-p)$
- 各概率之和 $=[p+(1-p)]^n=1$
- ✗ 不放回地抽取，各次不独立，不能用二项分布（用超几何分布）
~ ⚡ 第一反应：重复 $n$ 次、每次只有两种结果、互不影响 → 二项分布
E P78 P80 derive main | ▼ 加条件〔结构前提〕：独立重复
- 【独立 + 分类】指定 $k$ 次成功的一种情形概率为 $p^k(1-p)^{n-k}$（独立相乘），共 $C_n^k$ 种，互斥相加
E P34 P80 premise |
- 【前提】组合数 $C_n^k$
E R33 P80 premise |
- 【前提】二项式定理：$\sum P(X=k)=[p+(1-p)]^n$
E P36 P80 premise |
- 【前提】$kC_n^k=nC_{n-1}^{k-1}$，得 $E(X)=np$

N P81 lorange prob | 〔结构前提〕$N$ 件中有 $M$ 件次品，不放回地取 $n$ 件 | 超几何分布
- $P(X=k)=\dfrac{C_M^kC_{N-M}^{n-k}}{C_N^n}$
- $E(X)=\dfrac{nM}{N}$：与有放回（二项分布，$p=\dfrac{M}{N}$）的均值相同
- $k$ 的范围：$\max\{0,\ n-(N-M)\}\le k\le\min\{M,n\}$；记作 $X\sim H(N,n,M)$
~ ⚡ 第一反应：从有限个里不放回地取，问其中次品有几个 → 超几何分布
E S19 P81 derive main | ▼ 加条件〔结构前提〕：不放回
- 【古典概型】样本点总数 $C_N^n$，恰有 $k$ 件次品的有 $C_M^kC_{N-M}^{n-k}$ 种（分步计数）
E P34 P81 premise |
- 【前提】组合数

N Q97 problem prob | | 看到：“至少一个”“都不”的概率
- 路径：对立事件〔R47〕：$P(\text{至少一个})=1-P(\text{一个都没有})$；各事件独立时相乘〔P78〕
- 注意：先判断事件是否独立、是否互斥
E R47 Q97 apply |
- 【算对立事件】甲、乙独立投篮，命中率 0.6、0.5：至少一人命中 $=1-0.4\times 0.5=0.8$

N Q98 problem prob | | 看到：“在……的条件下”求概率
- 路径：$P(B|A)=\dfrac{P(AB)}{P(A)}$，古典概型直接在 $A$ 里数〔P78〕
- 注意：分清谁是条件；不放回抽取时样本空间会变
E P78 Q98 apply |
- 【缩小样本空间】10 件产品中 3 件次品，不放回取两次：第一次取到次品的条件下，第二次也是次品的概率 $\dfrac{2}{9}$

N Q99 problem prob | | 看到：结果有几种来源（全概率），或已知结果求来源（贝叶斯）
- 路径：① 按来源分成完备事件组 → ② 全概率相加 → ③ 反问来源时用贝叶斯〔P79〕
- 注意：各来源要两两互斥且覆盖全部
E P79 Q99 apply |
- 【分来源相加】甲、乙两厂产品占 60%、40%，次品率 2%、5%：$P(\text{次品})=0.012+0.020=0.032$；次品来自甲厂 $=\dfrac{0.012}{0.032}=\dfrac{3}{8}$

N Q100 problem prob | | 看到：求随机变量的均值、方差（含 $aX+b$）
- 路径：列分布列，按定义求〔S20〕；线性变换用性质〔R48〕
- 注意：先验分布列的概率和为 1
E R48 Q100 apply |
- 【线性性质】$E(X)=2$，$D(X)=3$：$E(2X-1)=3$，$D(2X-1)=12$

N Q101 problem prob | | 看到：独立重复试验，恰好发生 $k$ 次
- 路径：判断是二项分布，代入 $C_n^kp^k(1-p)^{n-k}$〔P80〕；均值 $np$，方差 $np(1-p)$
- 注意：“恰好 $k$ 次”要乘 $C_n^k$；“至少”用对立事件
E P80 Q101 apply |
- 【代入公式】投篮 3 次，命中率 0.6，恰中 2 次：$C_3^2\times 0.6^2\times 0.4=0.432$；$E(X)=1.8$，$D(X)=0.72$

N Q102 problem prob | | 看到：不放回地抽取，求次品个数的分布
- 路径：超几何分布〔P81〕
- 注意：$k$ 的取值范围受 $M$ 和 $n$ 限制
E P81 Q102 apply |
- 【组合计数】10 件中有 3 件次品，取 4 件恰有 1 件次品：$\dfrac{C_3^1C_7^3}{C_{10}^4}=\dfrac{105}{210}=\dfrac{1}{2}$；$E(X)=\dfrac{4\times 3}{10}=1.2$

N Q103 problem prob | | 看到：样本的平均数、方差（数据变换、两组合并）
- 路径：变换用 $a\bar x+b$、$a^2s^2$；两组合并用分层公式〔R49〕
- 注意：加上常数 $b$ 不改变方差
E R49 Q103 apply |
- 【变换、分层】平均数 5、方差 2 的数据乘 3 加 1：平均数 16，方差 18；男生 30 人平均 170、方差 16，女生 20 人平均 165、方差 25：总平均 168，总方差 $\dfrac{30\times 20+20\times 34}{50}=25.6$

N Q104 problem prob | | 看到：求回归直线方程，做预测
- 路径：求 $\bar x,\bar y$，代公式求 $\hat b$，再 $\hat a=\bar y-\hat b\bar x$〔P82〕
- 注意：回归直线过 $(\bar x,\bar y)$；预测值是估计值，不是确定值
E P82 Q104 apply |
- 【过样本中心】$\bar x=3$，$\bar y=10$，$\hat b=2$：$\hat a=4$，$\hat y=2x+4$，$x=6$ 时预测值 16

# ───────── v4 补：弧长与扇形、独立性检验、正态分布 ─────────
N P83 lorange tri | 〔结构前提〕圆心角 $\alpha$ 用弧度制 | ★ 弧长与扇形面积
- 弧度：$|\alpha|=\dfrac{l}{r}$（$l$ 为圆心角 $\alpha$ 所对的弧长）；换算 $180^\circ=\pi$ rad，$1^\circ=\dfrac{\pi}{180}$ rad
- 弧长 $l=|\alpha|r$；扇形面积 $S=\dfrac{1}{2}lr=\dfrac{1}{2}|\alpha|r^2$
- ✗ $\alpha=60^\circ$、$r=2$：直接代 $l=60\times 2=120$ 是错的，要先化成 $\dfrac{\pi}{3}$，$l=\dfrac{2\pi}{3}$
~ ⋯ 同源：三角形面积 $\dfrac{1}{2}\times$ 底 $\times$ 高〔S13〕：把扇形看成“底”为弧长、“高”为半径
~ ⚡ 第一反应：扇形的弧长、面积、周长 → 角先化成弧度，再用 $l=|\alpha|r$、$S=\dfrac{1}{2}lr$
E S04 P83 derive | ▼ 加条件〔结构前提〕：角用弧度制
- 【定义】弧度制：弧长与半径之比 $|\alpha|=\dfrac{l}{r}$
- 面积与圆心角成正比：$S=\dfrac{|\alpha|}{2\pi}\cdot\pi r^2=\dfrac{1}{2}|\alpha|r^2$
E S13 P83 premise |
- 【前提】圆的周长 $2\pi r$、面积 $\pi r^2$

N Q105 problem tri | | 看到：扇形的弧长、面积，或周长一定求面积最大
- 路径：角化弧度，代 $l=|\alpha|r$、$S=\dfrac{1}{2}lr$〔P83〕；周长一定时把 $S$ 写成 $r$ 的二次函数配方〔P01〕
- 注意：角度制要先化弧度；周长 $=l+2r$，别漏两条半径
E P83 Q105 apply |
- 【代公式、配方】$r=2$，$\alpha=\dfrac{\pi}{3}$：$l=\dfrac{2\pi}{3}$，$S=\dfrac{2\pi}{3}$；周长 8：$S=\dfrac{1}{2}(8-2r)r=-(r-2)^2+4$，$r=2$、$\alpha=2$ 时最大面积 4

N P84 lorange prob | 〔定义域〕$2\times 2$ 列联表各行和、列和都 $\ne 0$ | 独立性检验 $\chi^2$
- 列联表 $a,b,c,d$，$n=a+b+c+d$：$\chi^2=\dfrac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}$
- $\chi^2\ge$ 临界值 $x_\alpha$ 时，认为两个变量有关（犯错的概率不超过 $\alpha$）；否则不能认为有关
- $ad-bc=0$ 时样本中两个变量的频率完全符合独立
- 由来：四个格子各算 $\dfrac{(\text{实际频数}-\text{理论频数})^2}{\text{理论频数}}$ 再相加，理论频数如 $n\hat P(A)\hat P(B)=\dfrac{(a+b)(a+c)}{n}$，化简得上式
- ✗ $\chi^2<x_\alpha$ 不能说“两个变量无关”，只能说“没有足够证据认为有关”
~ ⚡ 第一反应：两个分类变量是否有关 → 列 $2\times 2$ 表算 $\chi^2$，与临界值比较（临界值见 T12）
E P78 P84 derive | ▼ 加条件〔定义域〕：行和、列和 $\ne 0$
- 【代入】若独立，$P(AB)=P(A)P(B)$，即 $\dfrac{a}{n}\approx\dfrac{a+b}{n}\cdot\dfrac{a+c}{n}$
- $an-(a+b)(a+c)=ad-bc$：$|ad-bc|$ 越大越偏离独立，$\chi^2$ 把它标准化（课本给出）

N Q106 problem prob | | 看到：根据列联表判断两个分类变量是否有关
- 路径：① 填 $2\times 2$ 列联表 → ② 算 $\chi^2$〔P84〕→ ③ 与临界值比较，下结论
- 注意：结论要带上“犯错误的概率不超过 $\alpha$”；$\chi^2$ 小时不能说“无关”
E P84 Q106 apply |
- 【算 $\chi^2$ 比临界值】$a=40$，$b=10$，$c=20$，$d=30$：$\chi^2=\dfrac{100\times(1200-200)^2}{50\times 50\times 60\times 40}\approx 16.67>6.635$，依据 $\alpha=0.01$ 认为有关

N P85 lorange prob | 〔结构前提〕$X\sim N(\mu,\sigma^2)$ | 正态分布的对称性
- 正态曲线关于直线 $x=\mu$ 对称，曲线与 $x$ 轴之间的面积为 1（由密度函数〔S23〕）
- $P(X\le\mu)=P(X\ge\mu)=\dfrac{1}{2}$；$P(X\le\mu-a)=P(X\ge\mu+a)$
- $P(X<\mu-a)=\dfrac{1-P(\mu-a\le X\le\mu+a)}{2}$；3σ 的概率见 T11
- ✗ $X\sim N(1,4)$：$\sigma=2$，不是 4；$P(-1\le X\le 3)\approx 0.6826$
~ ⚡ 第一反应：已知正态分布一侧的概率求另一侧 → 关于 $x=\mu$ 对称，总概率 1
E S20 P85 derive | ▼ 加条件〔结构前提〕：$X$ 服从正态分布
- 【对称】概率 = 曲线下的面积；关于 $x=\mu$ 对称的两块面积相等
E R47 P85 premise |
- 【前提】对立事件：$P(X>a)=1-P(X\le a)$

N Q107 problem prob | | 看到：正态分布求某区间的概率
- 路径：画出关于 $x=\mu$ 对称的曲线，用对称和总概率 1 转化〔P85〕；需要数值时用 3σ（T11）
- 注意：$N(\mu,\sigma^2)$ 第二个参数是方差，标准差要开方
E P85 Q107 apply |
- 【对称转化】$X\sim N(2,\sigma^2)$，$P(X<4)=0.8$：$P(X<0)=P(X>4)=0.2$，$P(0<X<2)=0.5-0.2=0.3$

# ═════════ v4 教材核对后补充（新教材逐章 + 老教材目录）═════════
# ───────── 向量：线性运算起点（由 S05 拆出）、旋转、角平分线 ─────────
N S21 start vec | | 【定义】向量的线性运算
- 加减（三角形法则）：$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$，$\vec a-\vec b=\vec a+(-\vec b)$，$\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$
- 运算律（课本给出）：$\vec a+\vec 0=\vec a$，$\vec a+\vec b=\vec b+\vec a$，$(\vec a+\vec b)+\vec c=\vec a+(\vec b+\vec c)$
- 数乘：$|\lambda\vec a|=|\lambda||\vec a|$，$\lambda(\mu\vec a)=(\lambda\mu)\vec a$，$(\lambda+\mu)\vec a=\lambda\vec a+\mu\vec a$，$\lambda(\vec a+\vec b)=\lambda\vec a+\lambda\vec b$
- 坐标：$\vec a=x\vec i+y\vec j$ 记作 $(x,y)$；共线：$\vec a\ne\vec 0$ 时 $\vec a\parallel\vec b\iff\vec b=\lambda\vec a$（课本给出）
E S01 S21 define |
- 【定义】向量的加法、数乘照搬实数运算律
E S21 S05 define |
- 【定义】数量积建立在向量与夹角之上

N R50 green vec | | ★ 旋转公式（向量、点绕原点旋转）
- $\overrightarrow{OP}=(a,b)$ 绕原点逆时针转 $\theta$：$(a\cos\theta-b\sin\theta,\ a\sin\theta+b\cos\theta)$
- 转 $\dfrac{\pi}{2}$：$(x,y)\to(-y,x)$；顺时针转 $\dfrac{\pi}{2}$：$(x,y)\to(y,-x)$
- 复数说法：乘 $\cos\theta+i\sin\theta$；乘 $i$ 即逆时针转 $\dfrac{\pi}{2}$
~ ⋯ 同源：三角形式乘法“辐角相加”〔R26〕
~ ⚡ 第一反应：点或向量绕原点转一个角 → 旋转公式（或乘 $\cos\theta+i\sin\theta$）
E R17 R50 derive |
- 【和角】设 $a=r\cos\varphi$，$b=r\sin\varphi$，转后为 $(r\cos(\varphi+\theta),\ r\sin(\varphi+\theta))$，用和角公式展开
E R41 R50 premise |
- 【前提】向量的坐标

N P86 lorange vec | 〔结构前提〕$AD$ 平分 $\angle BAC$，$D$ 在 $BC$ 上 | 角平分线定理
- $\dfrac{BD}{DC}=\dfrac{AB}{AC}$；外角平分线同样成立（必修四 9.1.1 例 6）
- 面积说法：$\dfrac{S_{\triangle ABD}}{S_{\triangle ACD}}=\dfrac{AB}{AC}=\dfrac{BD}{DC}$
~ ⚡ 第一反应：三角形中有角平分线 → 对边按两邻边之比分
E P21 P86 derive | ▼ 加条件〔结构前提〕：角平分线
- 【正弦定理】在 $\triangle ABD$、$\triangle ACD$ 中分别用正弦定理，$\sin\angle ADB=\sin\angle ADC$（互补）
E P20 P86 premise |
- 【面积法】两个三角形同高，面积比 = 底之比；又面积 $=\dfrac{1}{2}AB\cdot AD\sin\dfrac{A}{2}$

N Q108 problem vec | | 看到：点或向量绕原点旋转，求正方形、等边三角形的顶点
- 路径：旋转公式〔R50〕；或在复平面上乘 $\cos\theta+i\sin\theta$、乘 $i$〔R26〕
- 注意：分清逆时针、顺时针；绕的不是原点时先平移到原点
E R50 Q108 apply |
- 【套旋转公式】$(2,1)$ 逆时针转 $90^\circ$ 得 $(-1,2)$；转 $60^\circ$ 得 $\left(1-\dfrac{\sqrt{3}}{2},\ \sqrt{3}+\dfrac{1}{2}\right)$
E R26 Q108 apply |
- 【乘 $i$】正方形 $OABC$（逆时针），$A$ 对应 $1+2i$：$C$ 对应 $(1+2i)i=-2+i$

N Q109 problem vec | | 看到：三角形的角平分线，求边长或比值
- 路径：角平分线定理〔P86〕；或面积法、正弦定理
- 注意：对边分成的两段之比等于两邻边之比，不是两邻边之比的平方
E P86 Q109 apply |
- 【按邻边之比分】$AB=3$，$AC=2$，$BC=4$：$BD:DC=3:2$，$BD=\dfrac{12}{5}$

N Q110 problem vec | | 看到：已知三个顶点，求平行四边形第四个顶点或对称点
- 路径：$\overrightarrow{AB}=\overrightarrow{DC}$，坐标对应相等〔R41〕；对称点用中点反求
- 注意：只说“以这三点为顶点的平行四边形”时有三种情况
E R41 Q110 apply |
- 【向量相等】$ABCD$ 中 $A(1,2)$，$B(3,4)$，$C(5,1)$：$\overrightarrow{OD}=\overrightarrow{OA}+\overrightarrow{OC}-\overrightarrow{OB}=(3,-1)$

# ───────── 三角：已知值求角（反三角）、正割余割 ─────────
N P87 orange tri | 〔符号分支〕sin/cos 一个值对应两组角，tan 只有一组 | ★ 已知三角函数值求角
- $\sin x=a$（$-1\le a\le 1$）：$x=\arcsin a+2k\pi$ 或 $\pi-\arcsin a+2k\pi$（合写 $x=k\pi+(-1)^k\arcsin a$）；$a=\pm 1$ 时两组合并为一组
- $\cos x=a$（$-1\le a\le 1$）：$x=2k\pi\pm\arccos a$；$a=\pm 1$ 时两组合并为一组
- $\tan x=a$（$a$ 为任意实数）：$x=k\pi+\arctan a$（周期 $\pi$，每个周期只有一个角）
- 取值范围：$\arcsin a\in\left[-\dfrac{\pi}{2},\dfrac{\pi}{2}\right]$，$\arccos a\in[0,\pi]$，$\arctan a\in\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$
- 拓展（老教材）：$\arcsin(-x)=-\arcsin x$，$\arccos(-x)=\pi-\arccos x$，$\arcsin x+\arccos x=\dfrac{\pi}{2}$，$\sin(\arcsin x)=x$
- ✗ $\sin x=\dfrac{1}{2}$ 只写 $x=\dfrac{\pi}{6}+2k\pi$ 漏了 $\dfrac{5\pi}{6}+2k\pi$
~ ⚡ 第一反应：已知 sin、cos、tan 的值求角 → 先在一个周期里找全，再加周期
E R14 P87 derive main | ▼ 加条件〔符号分支〕：sin/cos 一个值两组角（端点合并），tan 只有一组
- 【对称】$\sin(\pi-\alpha)=\sin\alpha$ 给出 sin 的第二组角；$\cos(-\alpha)=\cos\alpha$ 给出 cos 的 $\pm$；$a=\pm 1$ 时 sin/cos 的两组角合并为一组
- 【推广】再加周期：sin/cos 加 $2k\pi$，tan 加 $k\pi$（tan 周期是 $\pi$，每个周期只有一个角）
E P13 P87 premise |
- 【前提】$\tan(\pi+\alpha)=\tan\alpha$

N R52 white tri ext | | 正割、余割、余切
- $\sec\alpha=\dfrac{r}{x}$，$\csc\alpha=\dfrac{r}{y}$，$\cot\alpha=\dfrac{x}{y}$
- $\cos\alpha\sec\alpha=1$，$\sin\alpha\csc\alpha=1$，$\tan\alpha\cot\alpha=1$
- $1+\tan^2\alpha=\sec^2\alpha$，$1+\cot^2\alpha=\csc^2\alpha$
~ 用于：读外文资料、大学课程（必修三拓展阅读）
~ ⚡ 第一反应：看到 sec、csc、cot → 化回 cos、sin、tan 的倒数
E S04 R52 derive |
- 【定义】终边上一点 $(x,y)$，$r=\sqrt{x^2+y^2}$，取倒数
E P12 R52 premise |
- 【前提】$1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$

N Q111 problem tri | | 看到：已知角终边上一点（或终边所在直线），求三角函数值
- 路径：求 $r=\sqrt{x^2+y^2}$，代 $\sin\alpha=\dfrac{y}{r}$ 等〔S04〕
- 注意：终边在直线上时有两条射线，分两种情况；点含参数时 $r$ 要带绝对值
E S04 Q111 apply |
- 【先求 $r$】终边过 $P(-3,4)$：$r=5$，$\sin\alpha=\dfrac{4}{5}$，$\cos\alpha=-\dfrac{3}{5}$，$\tan\alpha=-\dfrac{4}{3}$

N Q112 problem tri | | 看到：已知三角函数值求角，解简单三角方程
- 路径：在一个周期内找出全部角〔P87〕，再加周期；给定区间时逐个取 $k$
- 注意：sin、cos 一般两组解；$|a|>1$ 时 sin、cos 无解
E P87 Q112 apply |
- 【找全再加周期】$\sin x=\dfrac{1}{2}$：$x=\dfrac{\pi}{6}+2k\pi$ 或 $\dfrac{5\pi}{6}+2k\pi$；$\cos x=-\dfrac{1}{2}$，$x\in[0,2\pi)$：$x=\dfrac{2\pi}{3}$ 或 $\dfrac{4\pi}{3}$

# ───────── 函数：反函数、正切型函数 ─────────
N P88 orange fun | 〔结构前提〕$f$ 在定义域上一一对应（如单调） | ★ 反函数
- 求法：由 $y=f(x)$ 解出 $x$，再对调 $x,y$；$f^{-1}$ 的定义域 = $f$ 的值域
- $y=f(x)$ 与 $y=f^{-1}(x)$ 的图像关于直线 $y=x$ 对称；点 $(a,b)$ 在 $f$ 上 $\iff(b,a)$ 在 $f^{-1}$ 上
- $f[f^{-1}(x)]=x$，$f^{-1}[f(x)]=x$；单调函数一定有反函数，且单调性相同
- ✗ $y=x^2$（$x\in\mathbb{R}$）没有反函数：$y=4$ 对应 $x=\pm 2$
~ ⚡ 第一反应：求反函数 → 解出 $x$ 再对调；已知原函数过的点 → 反函数过对调后的点
E S15 P88 derive main | ▼ 加条件〔结构前提〕：一一对应
- 【对调】$(x,y)$ 与 $(y,x)$ 关于直线 $y=x$ 对称
E P88 P10 premise |
- 【特例】指数函数与对数函数互为反函数

N P89 lorange fun | 〔定义域〕$\omega\ne 0$，$\omega x+\varphi\ne\dfrac{\pi}{2}+k\pi$ | 正切型函数 $y=A\tan(\omega x+\varphi)$
- 周期 $T=\dfrac{\pi}{|\omega|}$；定义域 $\omega x+\varphi\ne\dfrac{\pi}{2}+k\pi$
- 对称中心：$\omega x+\varphi=\dfrac{k\pi}{2}$，纵坐标 0；没有对称轴
- $y=\tan x$：零点 $k\pi$，对称中心 $\left(\dfrac{k\pi}{2},0\right)$
- ✗ 正切型的周期不是 $\dfrac{2\pi}{|\omega|}$
~ ⚡ 第一反应：正切型函数 → 周期 $\dfrac{\pi}{|\omega|}$，把 $\omega x+\varphi$ 当整体
E P13 P89 derive | ▼ 加条件〔定义域〕：$\cos(\omega x+\varphi)\ne 0$
- 【整体代入】$\tan(\alpha+\pi)=\tan\alpha$，故 $\omega x$ 增加 $\pi$ 为一个周期
E S15 P89 premise |
- 【前提】周期的定义

N Q113 problem fun | | 看到：求反函数，或由原函数的点、性质推反函数
- 路径：解出 $x$ 再对调，写定义域（= 原函数值域）〔P88〕
- 注意：反函数的定义域不能漏写
E P88 Q113 apply |
- 【解出再对调】$y=2x+1\Rightarrow y=\dfrac{x-1}{2}$；$f(x)=2^x+1$ 过 $(1,3)$，则 $f^{-1}$ 过 $(3,1)$

N Q114 problem fun | | 看到：已知 $f(g(x))$ 的表达式，求 $f(x)$
- 路径：令 $t=g(x)$，把 $x$ 用 $t$ 表示后代入〔S15〕；或配凑成 $g(x)$ 的式子
- 注意：$t$ 的取值范围就是新函数的定义域
E S15 Q114 apply |
- 【换元】$f(x+1)=2x-3$：令 $t=x+1$，$f(t)=2(t-1)-3=2t-5$，即 $f(x)=2x-5$

E P89 Q84 apply |
- 【正切型整体代入】$y=\tan\left(2x+\dfrac{\pi}{4}\right)$：$T=\dfrac{\pi}{2}$，$x\ne\dfrac{\pi}{8}+\dfrac{k\pi}{2}$，对称中心 $\left(-\dfrac{\pi}{8}+\dfrac{k\pi}{4},0\right)$

# ───────── 地基：集合运算律 ─────────
N R51 white cnt | | 集合运算律
- $A\cap B=B\cap A$，$A\cap A=A$，$A\cap\varnothing=\varnothing$；$A\cup B=B\cup A$，$A\cup A=A$，$A\cup\varnothing=A$
- $A\subseteq B\iff A\cap B=A\iff A\cup B=B$
- $A\cup\complement_U A=U$，$A\cap\complement_U A=\varnothing$，$\complement_U(\complement_U A)=A$
- 分配律：$(A\cup B)\cap C=(A\cap C)\cup(B\cap C)$，$(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$
~ ⋯ 同源：实数的分配律〔S01〕；概率的事件运算〔S19〕
~ ⚡ 第一反应：看到 $A\cap B=A$、$A\cup B=B$ → 化成 $A\subseteq B$，别漏 $A=\varnothing$
E S14 R51 derive main |
- 【定义】按“且”“或”“非”逐个元素验证（维恩图）

N Q115 problem cnt | | 看到：由 $A\cap B=A$ 或 $A\cup B=B$ 求参数
- 路径：化成 $A\subseteq B$〔R51〕，先讨论 $A=\varnothing$，再列端点不等式
- 注意：端点能否取等要单独检验
E R51 Q115 apply |
- 【化成子集】$A=\{x\mid 2a\le x\le a+3\}$，$B=\{x\mid -1\le x\le 5\}$，$A\cap B=A$：$A=\varnothing$ 时 $a>3$；否则 $-\dfrac{1}{2}\le a\le 2$；故 $a\in\left[-\dfrac{1}{2},2\right]\cup(3,+\infty)$

# ───────── 代数：零积性质 ─────────
N R53 white alg | | 零积性质
- $ab=0\iff a=0$ 或 $b=0$
- 解方程的依据：因式分解后令每个因式为 0
- ✗ $x(x-1)=2$ 不能写成 $x=2$ 或 $x-1=2$：右边不是 0
~ ⚡ 第一反应：方程一边是乘积、另一边是 0 → 每个因式分别为 0
E S01 R53 derive |
- 【反证】若 $a\ne 0$，两边乘 $\dfrac{1}{a}$ 得 $b=0$
E R53 Q01 apply |
- 【令每个因式为 0】$(x-2)(x-3)=0\Rightarrow x=2$ 或 $x=3$

# ───────── 指数：增长模型 ─────────
N P90 lorange exp | 〔结构前提〕每期按相同百分比 $r$ 变化 | 指数增长模型与平均增长率
- 每期增长 $r$：$y=a(1+r)^x$；每期下降 $r$：$y=a(1-r)^x$
- 平均增长率：$(1+p_1)(1+p_2)\cdots(1+p_n)=(1+x)^n\Rightarrow x=\sqrt[n]{(1+p_1)\cdots(1+p_n)}-1$
~ ⋯ 同源：等比数列通项〔P29〕
~ ⚡ 第一反应：“每年增长 $r\%$”→ $a(1+r)^x$；求时间 → 两边取对数
E P05 P90 derive | ▼ 加条件〔结构前提〕：按相同百分比变化
- 【累乘】每过一期乘一次 $1+r$，$x$ 期乘 $(1+r)^x$
E P29 P90 premise |
- 【前提】等比数列：首项 $a$，公比 $1+r$

N Q116 problem exp | | 看到：增长率、复利、平均增长率
- 路径：写成 $a(1\pm r)^x$〔P90〕，求时间取对数〔P07〕
- 注意：平均增长率是几何平均，不是算术平均
E P90 Q116 apply |
- 【写指数式再取对数】$1000(1+10\%)^x=2000\Rightarrow x=\dfrac{\lg 2}{\lg 1.1}\approx 7.3$；两年分别增长 25%、80%：$(1+x)^2=1.25\times 1.8=2.25$，$x=50\%$

# ───────── 复数：n 次方根（拓展）─────────
N P91 lorange cpx ext | 〔定义域〕$z\ne 0$，$n$ 为正整数 | 复数的 $n$ 次方根
- $r(\cos\theta+i\sin\theta)$ 的 $n$ 次方根：$\sqrt[n]{r}\left(\cos\dfrac{\theta+2k\pi}{n}+i\sin\dfrac{\theta+2k\pi}{n}\right)$，$k=0,1,\cdots,n-1$
- 共 $n$ 个，在复平面上是正 $n$ 边形的顶点
~ ⚡ 第一反应：求复数的 $n$ 次方根 → 模开 $n$ 次方，辐角加 $2k\pi$ 后除以 $n$
E R27 P91 derive | ▼ 加条件〔定义域〕：$z\ne 0$
- 【逆用】设 $w^n=z$，按棣莫弗比较模和辐角，辐角相差 $2k\pi$

N Q117 problem cpx | | 看到：求复数的 $n$ 次方根（如 1 的立方根）
- 路径：化三角形式〔P24〕，按方根公式〔P91〕
- 注意：$k$ 取 $0$ 到 $n-1$，共 $n$ 个
E P91 Q117 apply |
- 【辐角加 $2k\pi$ 再除以 $n$】1 的立方根：$1$，$-\dfrac{1}{2}+\dfrac{\sqrt{3}}{2}i$，$-\dfrac{1}{2}-\dfrac{\sqrt{3}}{2}i$

# ───────── 数列：分期付款、无穷递缩等比、斐波那契 ─────────
N P92 lorange seq | 〔结构前提〕每期利率 $r$，按复利计算 | 分期付款（等额本息）、现值
- 现值：$A_0(1+r)^n=A\Rightarrow A_0=\dfrac{A}{(1+r)^n}$
- 等额本息：$\dfrac{x}{1+r}+\dfrac{x}{(1+r)^2}+\cdots+\dfrac{x}{(1+r)^m}=A_0\Rightarrow x=\dfrac{A_0r(1+r)^m}{(1+r)^m-1}$
- 等额本金：每期还 $\dfrac{A_0}{m}$ 加剩余本金的利息，各期还款额成递减的等差数列
~ ⚡ 第一反应：分期付款 → 把每期还款折算到同一时刻，用等比求和
E P31 P92 derive | ▼ 加条件〔结构前提〕：复利
- 【等比求和】各期还款的现值成等比数列，公比 $\dfrac{1}{1+r}$

N P93 lorange seq ext | 〔定义域〕$-1<q<1$ | 无穷递缩等比数列的和
- $S=\displaystyle\lim_{n\to\infty}S_n=\dfrac{a_1}{1-q}$（$|q|<1$）
- 循环小数化分数：$0.\dot 3=\dfrac{0.3}{1-0.1}=\dfrac{1}{3}$
- ✗ $q=2$：$1+2+4+\cdots$ 没有和，不能写 $\dfrac{1}{1-2}=-1$
~ ⚡ 第一反应：无限多项的等比求和、循环小数化分数 → $\dfrac{a_1}{1-q}$（先验 $|q|<1$）
E P31 P93 derive | ▼ 加条件〔定义域〕：$|q|<1$
- 【极限】$|q|<1$ 时 $q^n\to 0$（老教材数列极限）

N R54 white seq | | 斐波那契数列
- $F_1=F_2=1$，$F_n=F_{n-1}+F_{n-2}$（$n\ge 3$）：1，1，2，3，5，8，13，…
- 拓展：$F_n=\dfrac{1}{\sqrt{5}}\left[\left(\dfrac{1+\sqrt{5}}{2}\right)^n-\left(\dfrac{1-\sqrt{5}}{2}\right)^n\right]$，底数是 $x^2=x+1$ 的两根
~ 用于：递推数列的典型例子（选必三 5.1.2 例 2）
~ ⚡ 第一反应：后一项等于前两项之和 → 斐波那契数列
E S09 R54 derive |
- 【递推】每项由前两项相加
E P02 R54 premise |
- 【前提】通项的底数是 $x^2-x-1=0$ 的两根

N Q118 problem seq | | 看到：分期付款、贷款每期还多少
- 路径：每期还款折算到同一时刻（现值或终值），用等比求和〔P92〕〔P31〕
- 注意：分清还款期数 $m$ 和首次还款时间
E P92 Q118 apply |
- 【现值相加】贷款 10000 元，月利率 1%，分 2 个月等额还清：$x=\dfrac{10000\times 0.01\times 1.01^2}{1.01^2-1}\approx 5075.12$ 元

N Q119 problem seq | | 看到：循环小数化分数、无限等比求和
- 路径：写成首项、公比，用 $\dfrac{a_1}{1-q}$〔P93〕
- 注意：先验 $|q|<1$
E P93 Q119 apply |
- 【无穷等比求和】$0.\dot 1\dot 2=0.12+0.0012+\cdots=\dfrac{0.12}{1-0.01}=\dfrac{4}{33}$

# ───────── 计数：重复排列、不尽相异全排列、隔板法 ─────────
N P94 lorange cnt ext | 〔定义域〕$n_1+n_2+\cdots+n_k=n$ | 有重复排列与不尽相异元素的全排列
- 有重复排列：$n$ 种元素每次可重复取，排成 $m$ 位：$n^m$
- 不尽相异全排列：$n$ 个元素中有 $n_1$ 个相同、$n_2$ 个相同……：$\dfrac{n!}{n_1!\,n_2!\cdots n_k!}$
- ✗ 3 封信投 4 个信箱是 $4^3=64$，不是 $3^4$：每封信选信箱，信是“步”
~ ⚡ 第一反应：可重复选 → $n^m$（看谁是“步”）；有相同元素的全排列 → 除以相同元素的阶乘
E S07 P94 derive | ▼ 加条件〔定义域〕：个数之和为 $n$
- 【分步计数】每一位 $n$ 种，共 $m$ 步
E P33 P94 premise |
- 【前提】全排列 $n!$ 中，相同元素互换不产生新排列，除以 $n_1!\cdots n_k!$

N P95 lorange cnt ext | 〔定义域〕$n\ge r$（正整数解） | 隔板法：相同元素分给不同对象
- $x_1+x_2+\cdots+x_r=n$ 的正整数解：$C_{n-1}^{r-1}$
- 非负整数解：$C_{n+r-1}^{r-1}$（选必二拓展阅读）
~ ⚡ 第一反应：相同的东西分给不同的人 → 隔板法；允许为 0 时先每人借一个
E P34 P95 derive | ▼ 加条件〔定义域〕：$n\ge r$
- 【对应】$n$ 个元素排成一行，在 $n-1$ 个空中插 $r-1$ 块隔板；非负解令 $y_i=x_i+1$

N Q120 problem cnt | | 看到：有相同元素的排列、可重复的分配
- 路径：可重复选用 $n^m$，有相同元素除以阶乘〔P94〕；相同元素分组用隔板〔P95〕
- 注意：分清“元素相同”还是“对象相同”
E P94 Q120 apply |
- 【除以相同元素的阶乘】用 1，1，2，2，3 排五位数：$\dfrac{5!}{2!\,2!}=30$；3 封信投 4 个信箱：$4^3=64$
E P95 Q120 apply |
- 【隔板】8 个相同的球放进 4 个盒子：每盒至少一个 $C_7^3=35$；允许空盒 $C_{11}^3=165$

# ───────── 导数：平均变化率、线性近似 ─────────
N S22 start der | | 【定义】平均变化率
- $\dfrac{\Delta y}{\Delta x}=\dfrac{f(x_2)-f(x_1)}{x_2-x_1}=\dfrac{f(x_1+\Delta x)-f(x_1)}{\Delta x}$（$x_1\ne x_2$）：割线 $AB$ 的斜率
- 增函数 $\iff$ 区间内任意两点的 $\dfrac{\Delta y}{\Delta x}>0$；一次函数 $\iff$ 平均变化率恒为常数 $k$
~ ⋯ 同源：斜率公式〔P65〕、等差数列的公差 $d=\dfrac{a_n-a_m}{n-m}$〔P26〕
E S01 S22 define |
- 【定义】作差再相除
E S22 S08 define |
- 【极限】令 $\Delta x\to 0$，平均变化率的极限就是导数

N R55 white der | 〔定义域〕$f$ 在 $x_0$ 处可导 | 线性近似（以直代曲）
- $|\Delta x|$ 很小时：$f(x_0+\Delta x)\approx f(x_0)+f'(x_0)\Delta x$（近似公式，不是恒等式）
- 这是近似式，不是恒等式：用切线代替曲线
- 例：$\sqrt{9.05}\approx 3+\dfrac{0.05}{6}\approx 3.0083$
~ ⋯ 同源：二项式近似 $(1+x)^n\approx 1+nx$〔R33〕
~ ⚡ 第一反应：求接近已知点的函数值的近似值 → 线性近似
E S08 R55 derive |
- 【定义】$\Delta x$ 很小时差商 $\approx f'(x_0)$，两边乘 $\Delta x$

N Q121 problem der | | 看到：求平均速度、平均变化率
- 路径：$\dfrac{f(x_2)-f(x_1)}{x_2-x_1}$〔S22〕；瞬时速度再令 $\Delta x\to 0$〔S08〕
- 注意：平均变化率是区间上的量，导数是点上的量
E S22 Q121 apply |
- 【作差相除】$s=t^2$ 在 $[1,3]$ 上的平均速度：$\dfrac{9-1}{3-1}=4$

N Q122 problem der | | 看到：求 $\sqrt{9.05}$、$\dfrac{1}{2.03}$ 这类近似值
- 路径：取附近的整点 $x_0$，用 $f(x_0)+f'(x_0)\Delta x$〔R55〕
- 注意：$\Delta x$ 越小越准；结果是近似值
E R55 Q122 apply |
- 【以直代曲】$f(x)=\sqrt{x}$，$x_0=9$，$\Delta x=0.05$：$\sqrt{9.05}\approx 3+\dfrac{0.05}{6}\approx 3.0083$（精确值 3.00832）

# ───────── 解析几何：曲线系、第二定义、极坐标与参数方程 ─────────
N P96 lorange geo ext | 〔结构前提〕两条直线（两个圆）相交 | 直线系与圆系
- 过两直线交点的直线系：$A_1x+B_1y+C_1+\lambda(A_2x+B_2y+C_2)=0$（不含第二条直线本身）
- 过两圆交点的圆系：$x^2+y^2+D_1x+E_1y+F_1+\lambda(x^2+y^2+D_2x+E_2y+F_2)=0$（$\lambda\ne -1$）；$\lambda=-1$ 即公共弦
- 含参直线恒过定点：按参数整理成 $f(x,y)+\lambda g(x,y)=0$，解 $f=0$、$g=0$
~ ⚡ 第一反应：含参数的直线恒过定点、过两曲线交点的曲线 → 曲线系
E P69 P96 derive | ▼ 加条件〔结构前提〕：两曲线相交
- 【代入】交点同时满足两个方程，所以满足它们的任意组合

N P97 lorange geo ext | 〔结构前提〕椭圆、双曲线中心在原点，焦点在 $x$ 轴 | 准线与第二定义
- 准线 $x=\pm\dfrac{a^2}{c}$；到焦点的距离与到相应准线的距离之比为 $e$
- 椭圆 $0<e<1$，双曲线 $e>1$，抛物线 $e=1$：三种曲线统一
- 焦半径 $|PF_1|=a+ex_0$ 就是 $e$ 乘到左准线的距离 $x_0+\dfrac{a^2}{c}$
~ ⚡ 第一反应：圆锥曲线上的点到焦点的距离 → 换成 $e$ 乘到准线的距离
~ 用于：椭圆、双曲线上的点到焦点的距离（例 $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$ 上 $x_0=3$：$|PF_1|=5+\dfrac{4}{5}\times 3=\dfrac{37}{5}$）
E P70 P97 derive | ▼ 加条件〔结构前提〕：标准位置
- 【变形】$\sqrt{(x+c)^2+y^2}=a+\dfrac{c}{a}x=\dfrac{c}{a}\left(x+\dfrac{a^2}{c}\right)$
E P71 P97 premise |
- 【前提】抛物线：到焦点距离 = 到准线距离（$e=1$）

N P98 lorange geo ext | 〔定义域〕$\rho\ge 0$；化直角坐标时 $x\ne 0$ 才用 $\tan\theta=\dfrac{y}{x}$ | 极坐标与参数方程
- 互化：$x=\rho\cos\theta$，$y=\rho\sin\theta$；$\rho^2=x^2+y^2$
- 圆 $x=a+r\cos\theta$，$y=b+r\sin\theta$；椭圆 $x=a\cos\varphi$，$y=b\sin\varphi$
- 直线 $x=x_0+t\cos\alpha$，$y=y_0+t\sin\alpha$：$|t|$ 是到 $(x_0,y_0)$ 的距离
- 消参：用 $\sin^2\theta+\cos^2\theta=1$ 或代入消元
~ ⚡ 第一反应：椭圆、圆上的点求最值 → 设参数 $(a\cos\varphi,\ b\sin\varphi)$，化成辅助角
E S04 P98 derive |
- 【单位圆】单位圆上的点是 $(\cos\theta,\sin\theta)$，伸缩、平移得圆和椭圆
E R13 P98 premise |
- 【前提】消参用 $\sin^2\theta+\cos^2\theta=1$

N Q123 problem geo | | 看到：含参数的直线恒过定点，过两圆交点的圆
- 路径：按参数整理，令参数的系数和其余部分都为 0〔P96〕
- 注意：直线系 $l_1+\lambda l_2=0$ 不含 $l_2$ 本身
E P96 Q123 apply |
- 【按参数整理】$(2x+y-4)+\lambda(3x-2y+1)=0$：解 $2x+y=4$，$3x-2y=-1$ 得定点 $(1,2)$

N Q124 problem geo | | 看到：求点关于直线的对称点、光线反射
- 路径：设对称点，中点在直线上、连线与直线垂直〔P66〕，中点用〔R41〕
- 注意：关于 $y=\pm x+b$ 可直接代换：关于 $y=x+b$ 时 $(x_0,y_0)\to(y_0-b,\ x_0+b)$
E P66 Q124 apply |
- 【中点在线上、连线垂直】$A(3,0)$ 关于 $y=x+1$ 的对称点：$(0-1,\ 3+1)=(-1,4)$；中点 $(1,2)$ 在直线上，连线斜率 $-1$

N Q125 problem geo | | 看到：求动点的轨迹方程
- 路径：设动点 $(x,y)$ → 按条件列等式 → 化简配方〔P68〕→ 检验多余或遗漏的点
- 注意：到两定点距离之比为常数 $\lambda\ne 1$ 时是圆（阿波罗尼斯圆），$\lambda=1$ 时是垂直平分线
E P68 Q125 apply |
- 【列式再配方】$A(0,0)$，$B(3,0)$，$|PA|=2|PB|$：$x^2+y^2=4[(x-3)^2+y^2]\Rightarrow(x-4)^2+y^2=4$

N Q126 problem geo | | 看到：焦点三角形（$P$ 在椭圆、双曲线上，与两焦点构成三角形）
- 路径：定义 $|PF_1|\pm|PF_2|=2a$〔P70〕+ 余弦定理〔P22〕+ 面积公式〔P20〕
- 注意：椭圆焦点三角形面积 $S=b^2\tan\dfrac{\theta}{2}$，双曲线 $S=\dfrac{b^2}{\tan\frac{\theta}{2}}$（教材练习）
E P70 Q126 apply |
- 【定义 + 余弦定理】$\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$，$\angle F_1PF_2=60^\circ$：$S=9\tan 30^\circ=3\sqrt{3}$

N Q127 problem geo | | 看到：椭圆（圆）上的点到直线距离的最值
- 路径：设 $P(a\cos\varphi,\ b\sin\varphi)$〔P98〕，代点到直线距离〔P67〕，辅助角求最值〔P17〕
- 注意：也可以平移直线求切线；距离公式带绝对值
E P98 Q127 apply |
- 【设参数再辅助角】$\dfrac{x^2}{4}+y^2=1$ 上的点到 $x+y-4=0$：$d=\dfrac{|2\cos\varphi+\sin\varphi-4|}{\sqrt{2}}$，最小 $\dfrac{4-\sqrt{5}}{\sqrt{2}}$，最大 $\dfrac{4+\sqrt{5}}{\sqrt{2}}$

# ───────── 空间：基本定理与共面、三余弦与面积射影、球的截面、球冠球缺 ─────────
N P99 orange sp | 〔结构前提〕$\vec a,\vec b,\vec c$ 不共面（基本定理）；$A,B,C$ 不共线（共面） | ★ 空间向量基本定理与共面
- 基本定理：$\vec p=x\vec a+y\vec b+z\vec c$，$(x,y,z)$ 唯一；$x\vec a+y\vec b+z\vec c=\vec 0\iff x=y=z=0$
- 共面向量定理：$\vec a,\vec b$ 不共线时，$\vec a,\vec b,\vec c$ 共面 $\iff\vec c=x\vec a+y\vec b$
- 四点共面：$P\in$ 平面 $ABC\iff\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}\iff\overrightarrow{OP}=x\overrightarrow{OA}+y\overrightarrow{OB}+z\overrightarrow{OC}$，$x+y+z=1$
~ ⋯ 同源：平面向量基本定理、三点共线系数和为 1〔P56〕
~ ⚡ 第一反应：判断四点共面 → 系数和为 1；用基底表示空间向量 → 系数唯一
E S17 P99 derive main | ▼ 加条件〔结构前提〕：基底不共面
- 【推广】平面向量基本定理加一个不在平面内的方向 $\vec c$
E P56 P99 premise |
- 【前提】平面向量基本定理、三点共线

N P100 lorange sp | 〔结构前提〕$\theta_1$ 为斜线与平面所成角，$\theta_2$ 为射影与面内直线所成角 | 三余弦公式与面积射影
- 三余弦：$\cos\theta=\cos\theta_1\cos\theta_2$（$\theta$ 为斜线与面内直线所成角）
- 推论：线面角是斜线与平面内所有直线所成角中最小的
- 射影长 $A'B'=AB\cos\theta$；面积射影 $S'=S\cos\theta$（$\theta$ 为两平面所成的锐二面角）
- 拓展（老教材）：异面直线上两点距离 $EF=\sqrt{d^2+m^2+n^2\mp 2mn\cos\theta}$（由三向量和的模平方推出）
~ ⚡ 第一反应：已知射影面积和原面积 → 二面角的余弦是面积比
E P74 P100 derive | ▼ 加条件〔结构前提〕：斜线与射影
- 【射影】在两个直角三角形中各取余弦，相乘
E S13 P100 premise |
- 【前提】直角三角形中的余弦

N P101 lorange sp | 〔定义域〕$0\le d\le R$ | 球的截面
- 截面圆半径 $r=\sqrt{R^2-d^2}$（$d$ 为球心到截面的距离）；$d=0$ 时是大圆
- 北纬 $\varphi$ 的纬线长 $2\pi R\cos\varphi$
~ ⚡ 第一反应：球的截面 → 球心、截面圆心、截面圆上一点构成直角三角形
E S18 P101 derive | ▼ 加条件〔定义域〕：$d\le R$
- 【勾股】球心与截面圆心的连线垂直于截面
E S13 P101 premise |
- 【前提】勾股定理

N P102 lorange sp ext | 〔定义域〕$0<h\le 2R$ | 球冠与球缺
- 球冠面积 $S=2\pi Rh$（$h$ 为高）；球缺体积 $V=\pi h^2\left(R-\dfrac{h}{3}\right)$
- $h=2R$ 时即球面积 $4\pi R^2$、球体积 $\dfrac{4}{3}\pi R^3$
~ 用于：老教材立体几何（拓展）
~ ⚡ 第一反应：球被平面截下的一块 → 球冠面积 $2\pi Rh$
E S18 P102 derive | ▼ 加条件〔定义域〕：$0<h\le 2R$
- 【祖暅原理】与球体积同法（老教材给出）

N Q128 problem sp | | 看到：判断四点共面，或用基底表示空间向量
- 路径：$\overrightarrow{OP}=x\overrightarrow{OA}+y\overrightarrow{OB}+z\overrightarrow{OC}$，共面 $\iff x+y+z=1$〔P99〕
- 注意：$O$ 不在平面 $ABC$ 内时才能这样判断
E P99 Q128 apply |
- 【系数和为 1】$\overrightarrow{OP}=\dfrac{1}{2}\overrightarrow{OA}+\dfrac{1}{3}\overrightarrow{OB}+z\overrightarrow{OC}$，$P,A,B,C$ 共面：$z=1-\dfrac{1}{2}-\dfrac{1}{3}=\dfrac{1}{6}$

N Q129 problem sp | | 看到：已知射影面积与原面积求二面角，或用三余弦求角
- 路径：$\cos\theta=\dfrac{S'}{S}$；$\cos\theta=\cos\theta_1\cos\theta_2$〔P100〕
- 注意：面积射影求的是锐二面角
E P100 Q129 apply |
- 【面积比】三角形面积 4，在平面上的射影面积 2：$\cos\theta=\dfrac{1}{2}$，二面角 $60^\circ$

N Q130 problem sp | | 看到：球的截面面积、球心到截面的距离
- 路径：$r^2=R^2-d^2$〔P101〕
- 注意：截面圆的半径与球的半径不同
E P101 Q130 apply |
- 【勾股】$R=5$，$d=3$：$r=4$，截面面积 $16\pi$

# ───────── 概率统计：正态分布定义、标准化、两点分布、统计量 ─────────
N S23 start prob | | 【课本给出】正态分布
- 密度函数 $\varphi(x)=\dfrac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$，$x\in\mathbb{R}$；记作 $X\sim N(\mu,\sigma^2)$
- $\mu=E(X)$，$\sigma=\sqrt{D(X)}$（标准差），$\sigma^2$ 为方差
- $P(a\le X\le b)$ = 曲线在 $[a,b]$ 上与 $x$ 轴围成的面积
E S20 S23 define |
- 【定义】把离散的分布列推广到连续的密度曲线
E S23 P85 derive main |
- 【对称】密度函数中 $x-\mu$ 只以平方出现，曲线关于 $x=\mu$ 对称

N P103 lorange prob ext | 〔结构前提〕$Y\sim N(\mu,\sigma^2)$，$\sigma>0$ | 正态分布的标准化
- $X=\dfrac{Y-\mu}{\sigma}\sim N(0,1)$；$\Phi(a)=P(X<a)$
- $\Phi(-a)+\Phi(a)=1$；$P(a\le X<b)=\Phi(b)-\Phi(a)$；$P(|X|<a)=2\Phi(a)-1$
- $n$ 较大时二项分布 $B(n,p)$ 近似 $N(np,\ np(1-p))$
~ 用于：查标准正态分布表（选必二拓展阅读）
~ ⚡ 第一反应：一般正态分布查表 → 减均值、除以标准差
E S23 P103 derive | ▼ 加条件〔结构前提〕：$\sigma>0$
- 【代换】$E\left(\dfrac{Y-\mu}{\sigma}\right)=0$，$D\left(\dfrac{Y-\mu}{\sigma}\right)=1$
E R48 P103 premise |
- 【前提】$E(aX+b)=aE(X)+b$，$D(aX+b)=a^2D(X)$

N R56 white prob | | 两点分布
- $P(X=1)=p$，$P(X=0)=1-p$
- $E(X)=p$，$D(X)=p(1-p)$
- 二项分布是 $n$ 个独立两点分布之和：$E=np$，$D=np(1-p)$
~ ⚡ 第一反应：只有成功、失败两种结果的一次试验 → 两点分布
E S20 R56 derive |
- 【代入】$E(X)=1\cdot p+0\cdot(1-p)$；$D(X)=(1-p)^2p+(0-p)^2(1-p)=p(1-p)$
E R56 P80 premise |
- 【类比】教材由两点分布“类似地”得到 $np$、$np(1-p)$

N R57 white prob | | 统计量：位置量、直方图、加权平均、分层抽样
- 求和符号：$\sum(x_i+y_i)=\sum x_i+\sum y_i$，$\sum kx_i=k\sum x_i$，$\sum_{i=1}^n t=nt$；$\sum(x_i-\bar x)=0$
- 中位数：$2n+1$ 个数取第 $n+1$ 个，$2n$ 个数取中间两个的平均；众数；极差；标准差 $s=\sqrt{s^2}$
- $p\%$ 分位数：排序后算 $i=n\cdot p\%$；$i$ 不是整数取第 $\lceil i\rceil$ 个，是整数取第 $i$、$i+1$ 个的平均
- 按频率加权：$\bar x=\sum x_ip_i$，$s^2=\sum(x_i-\bar x)^2p_i$（与 $E(X)$、$D(X)$ 同形）
- 频率分布直方图：纵轴“频率/组距”，小矩形面积 = 频率，面积和 = 1；平均数 ≈ 各组中点 × 频率之和
- 分层抽样按比例：$\dfrac{n_i}{n}=\dfrac{N_i}{N}$
~ ⚡ 第一反应：直方图问题 → 面积 = 频率，面积和为 1；求百分位数 → 先排序，看 $np\%$ 是否为整数
E R49 R57 derive |
- 【分组】同值的数据合并，频率作权，就是加权平均
E S20 R57 premise |
- 【前提】与均值、方差的定义同形

N Q131 problem prob | | 看到：求中位数、百分位数，频率分布直方图估计
- 路径：排序后按位置取数；直方图用面积 = 频率、面积和为 1〔R57〕
- 注意：百分位数要先排序；直方图纵轴是“频率/组距”，不是频率
E R57 Q131 apply |
- 【按位置取数、面积和为 1】数据 1～10 的第 25 百分位数：$i=2.5$，取第 3 个数 3；组距 10，四组高 0.01、0.02、$a$、0.03：$a=0.04$，平均数 $\approx 55\times 0.1+65\times 0.2+75\times 0.4+85\times 0.3=74$

N Q132 problem prob | | 看到：几个独立事件中“恰好一个发生”
- 路径：拆成互斥事件之和〔R47〕，每项用独立相乘〔P78〕
- 注意：“恰好一个”与“至少一个”不同
E P78 Q132 apply |
- 【拆成互斥再相乘】甲、乙命中率 0.6、0.5：恰有一人命中 $=0.6\times 0.5+0.4\times 0.5=0.5$

'''

# 公式速查：(城市标题, [(编号, 公式)])；坐标由 build.py 填
FORMULAS = [
    ("代数", [("R02", r"$a^2-b^2=(a+b)(a-b)$"), ("R03", r"$(a\pm b)^2=a^2\pm 2ab+b^2$"),
             ("R04", r"$(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$"), ("R05", r"$(a\pm b)^3=a^3\pm 3a^2b+3ab^2\pm b^3$"),
             ("R06", r"$a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$"), ("R07", r"$a^2+b^2=(a+b)^2-2ab$，$a^3+b^3=(a+b)^3-3ab(a+b)$"),
             ("R08", r"$x^2+(p+q)x+pq=(x+p)(x+q)$"), ("P01", r"$ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}$"),
             ("P02", r"$x=\frac{-b\pm\sqrt{\Delta}}{2a}$，$\Delta=b^2-4ac$"), ("P03", r"$x_1+x_2=-\frac{b}{a}$，$x_1x_2=\frac{c}{a}$"),
             ("P45", r"$|x_1-x_2|=\frac{\sqrt{\Delta}}{|a|}$"), ("P42", r"$\frac{a}{b}\pm\frac{c}{d}=\frac{ad\pm bc}{bd}$"),
             ("P59", r"$f(a)=0\iff x-a$ 是 $f(x)$ 的因式"), ("R43", r"多项式恒等 $\iff$ 对应系数相等")]),
    ("指数、根式、对数", [("P41", r"$a^m\div a^n=a^{m-n}$，$a^{-n}=\frac{1}{a^n}$"), ("P05", r"$a^ra^s=a^{r+s}$，$(a^r)^s=a^{rs}$，$(ab)^r=a^rb^r$"), ("P90", r"$y=a(1+r)^x$"),
             ("P43", r"$\sqrt{a}\sqrt{b}=\sqrt{ab}$，$\sqrt{a^2}=|a|$"), ("P44", r"$\frac{1}{\sqrt{a}+\sqrt{b}}=\frac{\sqrt{a}-\sqrt{b}}{a-b}$"),
             ("P06", r"$a^{\log_a N}=N$，$\log_a 1=0$，$\log_a a=1$"), ("P07", r"$\log_a(MN)=\log_a M+\log_a N$，$\log_a M^n=n\log_a M$"),
             ("P08", r"$\log_a b=\frac{\log_c b}{\log_c a}$"), ("P09", r"$\log_a b\cdot\log_b a=1$，$\log_{a^m}b^n=\frac{n}{m}\log_a b$")]),
    ("三角", [("R13", r"$\sin^2\alpha+\cos^2\alpha=1$"), ("P11", r"$\tan\alpha=\frac{\sin\alpha}{\cos\alpha}$"),
             ("P12", r"$1+\tan^2\alpha=\frac{1}{\cos^2\alpha}$"), ("R14", r"$\sin(\pi-\alpha)=\sin\alpha$，$\cos\left(\frac{\pi}{2}-\alpha\right)=\sin\alpha$ 等六组"),
             ("R16", r"$\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$"), ("R17", r"$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$"),
             ("P14", r"$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$"), ("R18", r"$\sin 2\alpha=2\sin\alpha\cos\alpha$，$\cos 2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$"),
             ("R19", r"$\cos^2\alpha=\frac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\frac{1-\cos 2\alpha}{2}$"), ("P16", r"$\tan\frac{\alpha}{2}=\frac{\sin\alpha}{1+\cos\alpha}=\frac{1-\cos\alpha}{\sin\alpha}$"),
             ("R20", r"$\sin\alpha\cos\beta=\frac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$"), ("R21", r"$\sin\theta+\sin\varphi=2\sin\frac{\theta+\varphi}{2}\cos\frac{\theta-\varphi}{2}$"),
             ("P17", r"$a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\varphi)$"), ("P47", r"$\frac{a\sin\alpha+b\cos\alpha}{c\sin\alpha+d\cos\alpha}=\frac{a\tan\alpha+b}{c\tan\alpha+d}$"),
             ("R38", r"$(\sin\alpha\pm\cos\alpha)^2=1\pm\sin 2\alpha$"), ("R44", r"$\sin 3\alpha=3\sin\alpha-4\sin^3\alpha$，$\cos 3\alpha=4\cos^3\alpha-3\cos\alpha$"), ("P83", r"$l=|\alpha|r$，$S=\frac{1}{2}lr=\frac{1}{2}|\alpha|r^2$"),
             ("P87", r"$\sin x=a$：$x=k\pi+(-1)^k\arcsin a$；$\cos x=a$：$x=2k\pi\pm\arccos a$")]),
    ("向量与解三角形", [("R15", r"$\vec a\cdot\vec b=x_1x_2+y_1y_2$"), ("P49", r"$|\vec a\pm\vec b|^2=|\vec a|^2\pm 2\vec a\cdot\vec b+|\vec b|^2$"),
             ("P20", r"$S=\frac{1}{2}ab\sin C$"), ("P21", r"$\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R$"),
             ("P22", r"$a^2=b^2+c^2-2bc\cos A$，$\cos A=\frac{b^2+c^2-a^2}{2bc}$"), ("P86", r"$\frac{BD}{DC}=\frac{AB}{AC}$（角平分线）"),
             ("R50", r"$(a,b)$ 转 $\theta$：$(a\cos\theta-b\sin\theta,\ a\sin\theta+b\cos\theta)$"),
             ("R41", r"$\overrightarrow{AB}=(x_2-x_1,y_2-y_1)$，中点 $\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)$"),
             ("P56", r"$\overrightarrow{OP}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}$（三点共线）"),
             ("P57", r"投影 $\frac{\vec a\cdot\vec b}{|\vec b|}$，投影向量 $\frac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$"),
             ("R42", r"$\vec a\cdot\vec b=\frac{1}{4}\left(|\vec a+\vec b|^2-|\vec a-\vec b|^2\right)$"),
             ("P60", r"$\tan A+\tan B+\tan C=\tan A\tan B\tan C$")]),
    ("复数", [("R23", r"$z\bar z=|z|^2$"), ("P23", r"$\frac{a+bi}{c+di}=\frac{(ac+bd)+(bc-ad)i}{c^2+d^2}$"),
             ("R26", r"$r_1(\cos\theta_1+i\sin\theta_1)\cdot r_2(\cos\theta_2+i\sin\theta_2)=r_1r_2[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)]$"), ("R27", r"$[r(\cos\theta+i\sin\theta)]^n=r^n(\cos n\theta+i\sin n\theta)$"),
             ("P58", r"$x=\frac{-b\pm\sqrt{-\Delta}\,i}{2a}$（实系数，$\Delta<0$）"),
             ("P91", r"$\sqrt[n]{r}\left(\cos\frac{\theta+2k\pi}{n}+i\sin\frac{\theta+2k\pi}{n}\right)$")]),
    ("数列", [("P26", r"$a_n=a_1+(n-1)d$"), ("P28", r"$S_n=\frac{n(a_1+a_n)}{2}=na_1+\frac{n(n-1)}{2}d$"),
             ("P29", r"$a_n=a_1q^{n-1}$"), ("P31", r"$S_n=\frac{a_1(1-q^n)}{1-q}$（$q\ne 1$）"),
             ("P51", r"$2b=a+c$；$b^2=ac$"), ("P32", r"$a_n=S_n-S_{n-1}$（$n\ge 2$）"),
             ("R30", r"$\frac{1}{k(k+1)}=\frac{1}{k}-\frac{1}{k+1}$"), ("P53", r"$\frac{1}{k(k+d)}=\frac{1}{d}\left(\frac{1}{k}-\frac{1}{k+d}\right)$"),
             ("R31", r"$\sum k^2=\frac{n(n+1)(2n+1)}{6}$"), ("R32", r"$\sum k^3=\left[\frac{n(n+1)}{2}\right]^2$"),
             ("P92", r"$x=\frac{A_0r(1+r)^m}{(1+r)^m-1}$（等额本息）"), ("P93", r"$S=\frac{a_1}{1-q}$（$|q|<1$）")]),
    ("计数", [("P33", r"$A_n^m=\frac{n!}{(n-m)!}$"), ("P34", r"$C_n^m=\frac{n!}{m!(n-m)!}$"),
             ("P35", r"$C_n^m=C_n^{n-m}$，$C_{n+1}^m=C_n^m+C_n^{m-1}$"), ("R33", r"$(a+b)^n=\sum C_n^ka^{n-k}b^k$"),
             ("R34", r"$\sum C_n^k=2^n$"), ("R40", r"$\mathrm{card}(A\cup B)=\mathrm{card}(A)+\mathrm{card}(B)-\mathrm{card}(A\cap B)$"),
             ("P94", r"$n^m$；$\frac{n!}{n_1!n_2!\cdots n_k!}$"), ("P95", r"正整数解 $C_{n-1}^{r-1}$，非负整数解 $C_{n+r-1}^{r-1}$")]),
    ("导数", [("P37", r"$(uv)'=u'v+uv'$"), ("P38", r"$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$"),
             ("P55", r"$\left(\frac{1}{x}\right)'=-\frac{1}{x^2}$，$(\sqrt{x})'=\frac{1}{2\sqrt{x}}$"), ("S12", r"$y'_x=f'(u)\cdot g'(x)$（链式法则）")]),
    ("函数性质", [("P61", r"奇函数 $f(-x)=-f(x)$，偶函数 $f(-x)=f(x)$"), ("P62", r"$f(a+x)=f(b-x)\Rightarrow$ 对称轴 $x=\frac{a+b}{2}$"),
             ("P63", r"$f(x+a)=-f(x)\Rightarrow T=2a$"), ("R45", r"$y=f(x+h)$ 左移 $h$，$y=f(\omega x)$ 横坐标变为 $\frac{1}{\omega}$"),
             ("P64", r"$y=A\sin(\omega x+\varphi)$：$T=\frac{2\pi}{|\omega|}$"), ("P89", r"$y=A\tan(\omega x+\varphi)$：$T=\frac{\pi}{|\omega|}$"),
             ("P88", r"$f[f^{-1}(x)]=x$，图像关于 $y=x$ 对称")]),
    ("解析几何", [("P65", r"$k=\frac{y_2-y_1}{x_2-x_1}$，$y-y_0=k(x-x_0)$，$\frac{y-y_1}{y_2-y_1}=\frac{x-x_1}{x_2-x_1}$"), ("P66", r"$l_1\perp l_2\iff A_1A_2+B_1B_2=0$"),
             ("P67", r"$d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$"), ("P68", r"$r=\frac{1}{2}\sqrt{D^2+E^2-4F}$"),
             ("P69", r"弦长 $2\sqrt{r^2-d^2}$"), ("P70", r"椭圆 $a^2=b^2+c^2$，双曲线 $c^2=a^2+b^2$，$e=\frac{c}{a}$"),
             ("P71", r"$|PF|=x_0+\frac{p}{2}$，$|AB|=x_1+x_2+p$"), ("P72", r"$|AB|=\sqrt{1+k^2}\,|x_1-x_2|$"),
             ("P73", r"$k_{AB}\cdot k_{OM}=-\frac{b^2}{a^2}$（椭圆）"), ("P96", r"$l_1+\lambda l_2=0$ 过两直线交点"),
             ("P97", r"准线 $x=\pm\frac{a^2}{c}$，$\frac{|PF|}{d}=e$"), ("P98", r"$x=\rho\cos\theta$，$y=\rho\sin\theta$；$x=a\cos\varphi$，$y=b\sin\varphi$")]),
    ("空间向量与立体几何", [("R46", r"$\vec a\cdot\vec b=x_1x_2+y_1y_2+z_1z_2$"), ("P74", r"线面角 $\sin\theta=|\cos\langle\vec u,\vec n\rangle|$"),
             ("P75", r"$d=\frac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}$"), ("P76", r"$V_台=\frac{1}{3}h\left(S+\sqrt{SS'}+S'\right)$"),
             ("P77", r"$2R=\sqrt{a^2+b^2+c^2}$"), ("P99", r"$\overrightarrow{OP}=x\overrightarrow{OA}+y\overrightarrow{OB}+z\overrightarrow{OC}$，$x+y+z=1$（共面）"),
             ("P100", r"$\cos\theta=\cos\theta_1\cos\theta_2$，$S'=S\cos\theta$"), ("P101", r"$r=\sqrt{R^2-d^2}$"), ("P102", r"$S_{冠}=2\pi Rh$")]),
    ("概率统计", [("R47", r"$P(A\cup B)=P(A)+P(B)-P(AB)$，$P(\bar A)=1-P(A)$"), ("P78", r"$P(AB)=P(A)P(B|A)$"),
             ("P79", r"$P(B)=\sum P(A_i)P(B|A_i)$"), ("R48", r"$E(aX+b)=aE(X)+b$，$D(aX+b)=a^2D(X)$"),
             ("P80", r"$P(X=k)=C_n^kp^k(1-p)^{n-k}$，$E=np$，$D=np(1-p)$"), ("P81", r"$P(X=k)=\frac{C_M^kC_{N-M}^{n-k}}{C_N^n}$"),
             ("R49", r"$s^2=\frac{1}{n}\sum x_i^2-\bar x^2$"), ("P82", r"$\hat b=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}$，$\hat a=\bar y-\hat b\bar x$"),
             ("P84", r"$\chi^2=\frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}$"), ("P85", r"$P(X\le\mu-a)=P(X\ge\mu+a)$"), ("R56", r"两点分布 $E=p$，$D=p(1-p)$"),
             ("P103", r"$X=\frac{Y-\mu}{\sigma}\sim N(0,1)$"), ("R57", r"直方图面积 = 频率；$p\%$ 分位数 $i=np\%$")]),
]

TOOLS = [
    ("T1", "特殊角三角函数值", [
        r"$\alpha$：$0$，$\frac{\pi}{6}$，$\frac{\pi}{4}$，$\frac{\pi}{3}$，$\frac{\pi}{2}$",
        r"$\sin$：$0$，$\frac{1}{2}$，$\frac{\sqrt{2}}{2}$，$\frac{\sqrt{3}}{2}$，$1$",
        r"$\cos$：$1$，$\frac{\sqrt{3}}{2}$，$\frac{\sqrt{2}}{2}$，$\frac{1}{2}$，$0$",
        r"$\tan$：$0$，$\frac{\sqrt{3}}{3}$，$1$，$\sqrt{3}$，不存在",
        r"$\sin 15^\circ=\cos 75^\circ=\frac{\sqrt{6}-\sqrt{2}}{4}$，$\cos 15^\circ=\sin 75^\circ=\frac{\sqrt{6}+\sqrt{2}}{4}$",
        r"$\tan 15^\circ=2-\sqrt{3}$，$\tan 75^\circ=2+\sqrt{3}$"]),
    ("T2", "杨辉三角 n=0～6", ["1 ｜ 1 1 ｜ 1 2 1 ｜ 1 3 3 1", "1 4 6 4 1 ｜ 1 5 10 10 5 1", "1 6 15 20 15 6 1"]),
    ("T3", "常用对数", [r"$\lg 2\approx 0.3010$，$\lg 3\approx 0.4771$，$\lg 5\approx 0.6990$", r"$\ln 2\approx 0.693$，$\ln 3\approx 1.099$"]),
    ("T4", "诱导公式口诀", ["“奇变偶不变，符号看象限”", r"把 $\alpha$ 看作锐角定符号；记忆口诀，不是条件"]),
    ("T5", "平方 11～20", ["121，144，169，196，225", "256，289，324，361，400"]),
    ("T6", "立方 1～10", ["1，8，27，64，125", "216，343，512，729，1000"]),
    ("T7", r"$2^1$～$2^{10}$", ["2，4，8，16，32", "64，128，256，512，1024"]),
    ("T8", "常见勾股数", ["(3,4,5)　(5,12,13)　(8,15,17)", "(7,24,25)　(20,21,29)　(9,40,41)"]),
    ("T9", "常用近似值", [r"$\sqrt{2}\approx 1.414$，$\sqrt{3}\approx 1.732$，$\sqrt{5}\approx 2.236$", r"$\pi\approx 3.1416$，$e\approx 2.718$"]),
    ("T10", "基本导数表", [r"$C'=0$，$(x^n)'=nx^{n-1}$", r"$(\sin x)'=\cos x$，$(\cos x)'=-\sin x$", r"$(e^x)'=e^x$，$(\ln x)'=\frac{1}{x}$（$x>0$）"]),
    ("T11", "正态分布 3σ（教材取值）", [r"$P(\mu-\sigma\le X\le\mu+\sigma)\approx 0.6826$", r"$2\sigma$：$\approx 0.9544$；$3\sigma$：$\approx 0.9974$"]),
    ("T12", "独立性检验临界值", [r"$\alpha$：0.1，0.05，0.01，0.005，0.001", r"$x_\alpha$：2.706，3.841，6.635，7.879，10.828"]),
]

# v3：原 27 个题型入口已并入问题节点 Q01–Q67（对照表见节点清单第 14 节）；
# 左栏“问题目录”由 build.py 从问题节点自动生成：看到什么 → 先查（节点的“注意”）→ Q 编号〔坐标〕。
ENTRIES = []
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚"


def parse():
    secs, nodes, edges = {}, [], []
    cur = None
    for raw in RAW.split("\n"):
        line = raw.rstrip()
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("SEC "):
            k, t = line[4:].split(" | ", 1)
            secs[k.strip()] = t.strip()
            cur = None
        elif line.startswith("N "):
            assert line.count("|") == 2, "节点行的条件、标题里不能有 |（用 \\lvert 或改写）：" + line
            head, cond, title = (x.strip() for x in line[2:].split("|", 2))
            f = head.split()
            cur = dict(id=f[0], type=f[1], sec=f[2], ext="ext" in f[3:], cond=cond.strip() or None,
                       title=title.strip(), lines=[], notes=[])
            nodes.append(cur)
        elif line.startswith("E "):
            head, mark = line[2:].split(" |", 1)
            f = head.split()
            cur = dict(s=f[0], t=f[1], kind=f[2], main="main" in f[3:], mark=mark.strip() or None, lines=[])
            edges.append(cur)
        elif line.startswith("- "):
            cur["lines"].append(line[2:])
        elif line.startswith("~ "):
            cur["notes"].append(line[2:])
        else:
            raise ValueError("无法识别：" + line)
    ids = {n["id"] for n in nodes}
    for e in edges:
        assert e["s"] in ids and e["t"] in ids, (e["s"], e["t"])
    assert len(ids) == len(nodes), "编号重复"
    return secs, nodes, edges


SECS, NODES, EDGES = parse()

# ── 方法（往哪走）：运算逻辑、变换方式，本身不是公式。名称与不等式大厦 v47 对齐（配凑、代换、数形结合、分类讨论、归纳、反证）──
# (编号, 线上名, 名称（细分）, 方向, 依据, 信号, 范例（推导链）, ⚠ 陷阱, 归入的原方法名)
METHODS = [
    ("M1", "展开分解", "展开分解（展开、提公因式、因式分解、逆用公式）",
     "要合并、比较系数、验证恒等 → 展开成和；要约分、解方程、定正负 → 分解成积",
     "分配律〔S01〕；乘法公式从左往右是展开，从右往左是分解",
     "括号相乘要合并；二次式、高次式要拆；方程一边是 0",
     r"分配律 → $(a\pm b)^2$、$a^2-b^2$ → 十字相乘、因式定理 → 零积性质解方程；$(x+\Delta x)^n$ 展开 → $(x^n)'=nx^{n-1}$",
     "分解要分到不能再分；约掉的因式不能为 0",
     ["展开", "展开验证", "逆用", "提取", "因式分解", "合并", "相乘", "分解", "去括号", "对比"]),
    ("M2", "配凑", "配凑（配方、补项、加一项减一项、待定系数）",
     "二次式求最值、找对称轴、化标准方程 → 凑成“平方 + 常数”；差一项就补上再减去",
     "完全平方公式〔R03〕；恒等的多项式对应系数相等〔R43〕",
     "二次式求最值或值域；$x^2+y^2+Dx+Ey+F=0$；两式相乘差一个交叉项",
     r"$(a+b)^2$ → $a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}$ → 求根公式 → 圆的一般方程 → 最小二乘回归；积的求导：加一项减一项",
     "配方时先提出二次项系数；补上的项要减回去",
     ["配方", "配方法", "配凑", "平方"]),
    ("M3", "代换", "代换（换元、整体代入、字母代换、拆角配角、平移伸缩）",
     "已有一个公式，想要它的“兄弟公式” → 把字母换成别的式子；式子复杂 → 把一块看成整体、换成新变量",
     "恒等式对字母的一切取值成立，代入什么都成立",
     "结构与已知公式相似；同一块反复出现；复合函数；角能写成已知角的和差",
     r"$\cos(\alpha-\beta)$ →（$\beta\to-\beta$）和角 →（$\beta=\alpha$）倍角 → 降幂 →（$\alpha\to\frac{\alpha}{2}$）半角；$t=2^x$ 化二次；复合函数求导",
     "换元后新变量的范围要随之改变",
     ["代入", "代换", "设", "整体代入", "拆角", "平移", "平移、伸缩", "变形", "伸缩"]),
    ("M4", "特例", "特例与推广（取特殊值、赋值、由特殊到一般）",
     "一般结论里取特殊值 → 得到常用特例、求系数和；特殊情形成立 → 推广到一般",
     "一般式对所有取值成立，自然对特殊值成立",
     "求展开式系数和；和角里令两角相等；整数指数想推到实数指数",
     r"和角 →（$\beta=\alpha$）倍角；二项式定理 →（$x=1,-1,0$）系数和；整数指数 →（推广）实数指数；累加法 →（$f(n)=d$）等差通项",
     "推广后要重新核对条件（如底数 $>0$）",
     ["特例", "赋值", "推广", "类比"]),
    ("M5", "作差相消", "作差相消（两式相减、累加、累乘、错位相减、倒序相加）",
     "相邻项、两个式子结构相似 → 相减或倒序相加，中间项抵消，只剩首尾",
     "等式两边同加减仍相等〔S01〕",
     "相邻项相减有规律；$S_n$ 与 $a_n$ 混在一起；等差 × 等比；两点都在同一曲线上",
     r"相邻项相减 → 累加相消 → 等差通项、裂项、平方和；$S-qS$ → 等比求和 → 错位相减；$a_n=S_n-S_{n-1}$；两点代入相减 → 点差法",
     "看清首尾剩几项；$n=1$ 要单独验证",
     ["作差", "相减", "相加减", "移项", "累加相消", "累加", "累乘", "错位相减", "倒序相加", "作比", "相加", "相消"]),
    ("M6", "同除", "同除与通分（同除、同乘共轭、通分、齐次化）",
     "分子分母次数相同、要化成单一变量 → 同除一个非零式；分母麻烦 → 通分或同乘共轭",
     "分式的基本性质：分子分母同乘除一个非零式，值不变〔P42〕",
     "sin、cos 的齐次式；分母含根式、含 $i$；求离心率要化 $a,c$ 齐次式",
     r"同除 $\cos\alpha$：切化弦 ⇄ 弦化切 → 正切和角；同乘共轭 → 分母有理化、复数除法；差商通分 → 商的求导法则",
     "同除的式子不能为 0（如 $\\cos\\alpha\\ne 0$）",
     ["同除", "相除", "通分", "通分验证", "同乘", "分母实数化", "约分"]),
    ("M7", "对称", "对称（终边对称、函数图像对称、下标对称）",
     "角或图形关于某点、某线对称 → 写出对称点的坐标关系，一个结论变两个",
     "单位圆上对称点的坐标关系〔S04〕；$f(-x)=\\pm f(x)$〔S15〕",
     "$\\pi\\pm\\alpha$、$-\\alpha$；$f(a+x)=f(b-x)$；下标和相等；正态曲线",
     r"单位圆上终边对称 → 诱导公式 → 已知值求角有两组解；$f(-x)=\pm f(x)$ → 对称轴、对称中心 → 周期；正态曲线关于 $x=\mu$ 对称",
     "区分一个函数自身对称与两个函数图像互相对称",
     ["对称", "对调"]),
    ("M8", "数形结合", "数形结合（向量化、坐标化、几何意义）",
     "几何关系难直接算 → 化成坐标或向量运算；代数式有几何意义 → 画出来看",
     "数量积〔S05〕、坐标法〔S16〕：几何量都能写成坐标的式子",
     "角、长度、垂直、距离；$|z-z_0|$；$\\overrightarrow{PA}\\cdot\\overrightarrow{PB}$；能建坐标系",
     r"数量积坐标式 → 两角差余弦 → 和角；$|\vec a-\vec b|^2$ → 余弦定理；投影 → 点到直线、点到平面的距离 → 空间角",
     "图只作引导，结论要能用代数说清",
     ["向量", "取点"]),
    ("M9", "分类讨论", "分类讨论（分类、分步、按情况分开）",
     "情况不止一种 → 分成互不重叠的几类分别处理；一件事要几步完成 → 各步相乘",
     "分类加法原理、分步乘法原理〔S07〕",
     "含参数；绝对值；“至少”“恰好”；计数；完备事件组",
     r"分步 → 排列 → 组合 → 二项式定理；“选或不选” → 子集 $2^n$；重叠部分 → 容斥 → 概率加法公式；独立 + 分类 → 二项分布",
     "分类标准统一，不重不漏",
     ["双计数", "对应", "数个数", "拆成互斥", "分组", "分类讨论", "分类", "分步计数", "分类计数"]),
    ("M10", "归纳", "归纳与递推",
     "对一切正整数 $n$ 成立 → 奠基 + 由 $n=k$ 推 $n=k+1$；后项由前项决定 → 构造成等差、等比",
     "数学归纳法〔S10〕",
     "含正整数 $n$ 的恒等式；递推关系",
     r"$n=k\to n=k+1$：棣莫弗公式、立方和；递推 $a_{n+1}=pa_n+q$ → 构造等比；斐波那契",
     "递推那一步必须用上归纳假设",
     ["归纳法", "递推", "归纳"]),
    ("M11", "补形", "补形与面积法",
     "图形不规则 → 补成熟悉的图形再减；同一个面积（体积）用两种方法算 → 列等式",
     "面积公式〔S13〕、体积公式与祖暅原理〔S18〕",
     "台体、三棱锥外接球；三角形里有高、有角平分线",
     r"三个面积公式相等 → 正弦定理；面积比 → 角平分线定理；台体 = 大锥 − 小锥；外接球补成长方体",
     "补上的部分要算对、减干净",
     ["补形", "补形相减", "面积法", "作垂线"]),
    ("M12", "回到定义", "回到定义与取极限",
     "现成公式用不上 → 回到定义直接算；从平均到瞬时、从有限到无限 → 取极限",
     "各个定义（三角函数、对数、导数、条件概率……）就是最底层的工具",
     "新函数求导；圆锥曲线上的点到焦点的距离；求轨迹；无限项求和",
     r"平均变化率 →（$\Delta x\to 0$）导数 → 求导法则 → 线性近似；等比求和 →（$n\to\infty$）无穷递缩；对数、三角函数都由定义推出",
     "定义里的条件（如 $x\\ne 0$、$P(A)>0$）一并带上",
     ["定义", "按定义", "极限", "取极限", "求导"]),
    ("M13", "互逆", "互逆（逆运算、逆向使用）",
     "正着做不出 → 换成逆运算或反面",
     "指数与对数、乘方与开方、原函数与反函数互为逆运算",
     "指数方程、对数方程；求反函数；“至少一个”算反面",
     r"指数 ⇄ 对数；原函数 ⇄ 反函数；积化和差 ⇄ 和差化积；乘法 ⇄ 除法（复数三角形式）；对立事件",
     "逆运算有条件（真数 $>0$、一一对应）",
     ["逆运算", "开平方", "取对数", "取倒数"]),
    ("M14", "反证", "反证",
     "直接证明困难 → 假设结论不成立，推出矛盾",
     "排中律：结论成立与不成立必有一个",
     "“唯一”“至多”“至少”；系数对应相等；零积性质",
     r"若 $a\ne 0$，乘 $\frac{1}{a}$ 得 $b=0$（零积性质）；两多项式之差不是零多项式则根有限（系数对应相等）",
     "要否定整个结论",
     ["反证"]),
]
METHOD_OF = {old: (m[0], m[1]) for m in METHODS for old in m[-1]}
# 推导线上写成工具名的标签：工具（公式、定理、公理）不是方法，线上改写成【方法】⇐ 工具 X
TOOL_LABELS = {   # 线上写成工具名的标签：只是套用工具，写成“由 工具名〔编号〕：”，不加【】
    "数量积": ("数量积坐标式", "R15"), "单位圆": ("单位圆定义", "S04"), "共线": ("共线向量定理", "S21"),
    "投影": ("投影", "P57"), "夹角": ("夹角公式", "R46"), "勾股": ("勾股定理", "S13"), "射影": ("直角三角形中的余弦", "S13"),
    "和角": ("和角公式", "R17"), "链式法则": ("链式法则", "S12"), "正弦定理": ("正弦定理", "P21"), "等比求和": ("等比求和公式", "P31"),
    "结合律": ("结合律", "S01"), "二项式展开": ("二项式定理", "R33"), "带余除法": ("带余除法", "R01"),
    "独立 + 分类": ("独立事件概率相乘", "S19"), "古典概型": ("古典概型", "S19"), "祖暅原理": ("祖暅原理", "S18"),
    "商法则": ("商的求导法则", "P38"), "分步计数": ("分步乘法原理", "S07"), "分类计数": ("分类加法原理", "S07"),
}

# ── 题型入口的“方向”（方法）：每个问题节点先用哪种方法定方向；路径里的公式是工具 ──
DIRECTION = {
    "Q01": ("展开分解", "化成两个一次因式的积，令每个因式为 0；分解不开再配方"),
    "Q02": ("展开分解", "化成因式的积，按每个因式的正负分区间"),
    "Q03": ("展开分解", "化成交点式，零点直接读出"),
    "Q04": ("分类讨论", "把参数拆进因式，按两根的大小分类"),
    "Q05": ("互逆", "由根倒推因式：交点式反过来用"),
    "Q06": ("展开分解", "试根降次，化成低次因式的积"),
    "Q07": ("配凑", "配成“平方 + 常数”：开口向上且最小值不小于 0"),
    "Q08": ("配凑", "配成“平方 + 常数”，读出顶点"),
    "Q09": ("代换", "把所求式化成 $x_1+x_2$、$x_1x_2$ 的式子再整体代入"),
    "Q10": ("代换", "把所求式化成已知的 $a+b$、$ab$ 再代入"),
    "Q11": ("展开分解", "先分解，再约分、通分"),
    "Q12": ("展开分解", "凑成乘法公式的形状，整体代入"),
    "Q13": ("展开分解", "两边化到同一形式，或作差化为 0"),
    "Q14": ("作差相消", "作差，化成积或平方再定正负"),
    "Q15": ("代换", "把根的条件翻译成两根之和、积与判别式"),
    "Q16": ("代换", "设而不求：联立后用两根之和、积整体代入"),
    "Q17": ("代换", "根式化成分数指数，统一底数"),
    "Q18": ("代换", "把已知式整体平方，整体代入"),
    "Q19": ("代换", "换成同底，再合并"),
    "Q20": ("代换", "换元 $t=a^x$，化成二次方程"),
    "Q21": ("互逆", "合并成一个对数后化成指数式"),
    "Q22": ("代换", "化成同底看单调性，或找中间值 0、1"),
    "Q23": ("同除", "分子、分母同乘共轭（有理化）；开方要定号"),
    "Q24": ("互逆", "指数式化成对数式，再用倒数关系"),
    "Q25": ("代换", "用平方关系开方求其余，按象限定号"),
    "Q26": ("同除", "分子、分母同除 $\\cos^n\\alpha$，化成 $\\tan\\alpha$"),
    "Q27": ("配凑", "两边平方，把 $\\sin\\alpha\\pm\\cos\\alpha$ 与 $\\sin\\alpha\\cos\\alpha$ 联系起来"),
    "Q28": ("对称", "用对称（诱导公式）把任意角化成锐角"),
    "Q29": ("代换", "拆成特殊角的和差"),
    "Q30": ("代换", "配角：把所求角写成已知角的和差"),
    "Q31": ("代换", "降幂、辅助角，化成一个 $A\\sin(\\omega x+\\varphi)+k$，再整体看"),
    "Q32": ("配凑", "根号里配成完全平方，开方加绝对值"),
    "Q33": ("互逆", "把正切和角公式变形后逆用"),
    "Q34": ("互逆", "积与和互化"),
    "Q35": ("代换", "$\\alpha\\to\\dfrac{\\alpha}{2}$ 代入半角公式"),
    "Q36": ("代换", "直接代入余弦定理"),
    "Q37": ("代换", "边角互化：边换成角或角换成边"),
    "Q38": ("补形", "用两边及夹角算面积，或分割、补形"),
    "Q39": ("代换", "边角互化，统一成只含边或只含角"),
    "Q40": ("代换", "把 $A+B$ 换成 $\\pi-C$"),
    "Q41": ("数形结合", "模先平方化成数量积；有坐标就坐标化"),
    "Q42": ("代换", "边化角，化成一个三角函数，再由角的范围求最值"),
    "Q43": ("同除", "除法：分子、分母同乘分母的共轭"),
    "Q44": ("数形结合", "用模、共轭的几何意义：长度、距离"),
    "Q45": ("特例", "先用 $i^4=1$、$(1\\pm i)^2=\\pm 2i$ 降次"),
    "Q46": ("数形结合", "化成三角形式：模相乘、辐角相加"),
    "Q47": ("作差相消", "累加、累乘，让中间项抵消"),
    "Q48": ("作差相消", "$S_n$ 与 $S_{n-1}$ 两式相减"),
    "Q49": ("回到定义", "回到首项与公差（公比），列方程"),
    "Q50": ("对称", "下标和相等（对称）就用下标性质"),
    "Q51": ("作差相消", "乘公比后错位相减"),
    "Q52": ("作差相消", "裂成两项之差，中间相消"),
    "Q53": ("展开分解", "拆成几部分，分别求和"),
    "Q54": ("代换", "把每段的和看成新数列的项"),
    "Q55": ("作差相消", "先放缩成可裂项的形式，再相消"),
    "Q56": ("回到定义", "写出通项，令 $x$ 的次数满足条件"),
    "Q57": ("特例", "赋值 $x=1$、$-1$、$0$"),
    "Q58": ("分类讨论", "按“选或不选某个元素”分类（组合意义）"),
    "Q59": ("分类讨论", "先分类，再分步；特殊元素优先"),
    "Q60": ("展开分解", "写成“整数 + 小量”，二项式展开取前几项"),
    "Q61": ("代换", "识别结构；复合函数把内层看成整体"),
    "Q62": ("回到定义", "导数的几何意义：切线斜率"),
    "Q63": ("展开分解", "导数分解因式，看正负"),
    "Q64": ("作差相消", "移项作差构造函数，看单调性和最值"),
    "Q65": ("展开分解", "提公因式，再十字相乘；不行就求根写成交点式"),
    "Q66": ("代换", "一看角（拆角配角）、二看名（切化弦）、三看次数（降幂）"),
    "Q67": ("代换", "切化弦，“1”换成 $\\sin^2\\alpha+\\cos^2\\alpha$，统一成 sin、cos"),
    "Q68": ("代换", "构造新数列：加常数成等比，或取倒数成等差"),
    "Q69": ("作差相消", "写出 $n-1$ 时的同式，两式相减"),
    "Q70": ("分类讨论", "按导数零点的有无、大小分类讨论"),
    "Q71": ("代换", "先设切点，再把已知点代入切线"),
    "Q72": ("分类讨论", "按是否重叠分类：多数的减去"),
    "Q73": ("数形结合", "选两个不共线的向量作基底，沿图形“走路”"),
    "Q74": ("数形结合", "坐标化：终点减起点，代坐标条件"),
    "Q75": ("数形结合", "极化：数量积化成距离的平方，看几何最值"),
    "Q76": ("数形结合", "向量往另一方向上投影"),
    "Q77": ("回到定义", "回到复数相等的定义：实部、虚部分别相等"),
    "Q78": ("配凑", "$S_n$ 配方看对称轴；或看 $a_n$ 何时变号"),
    "Q79": ("展开分解", "展开后比较系数；或赋特殊值"),
    "Q80": ("对称", "比较 $f(-x)$ 与 $f(x)$"),
    "Q81": ("对称", "取两个自变量的中点作对称轴"),
    "Q82": ("代换", "关系式连用两次，推出周期"),
    "Q83": ("代换", "平移、伸缩都是对 $x$ 本身代换"),
    "Q84": ("代换", "把 $\\omega x+\\varphi$ 当整体"),
    "Q85": ("代换", "按平行、垂直的关系设方程，再代点求参数"),
    "Q86": ("数形结合", "距离 = 向量在法向量上投影的长度"),
    "Q87": ("配凑", "配成标准方程"),
    "Q88": ("数形结合", "几何法：圆心到直线的距离与半径比较"),
    "Q89": ("同除", "列 $a,c$ 的齐次式，同除 $a$ 的幂得 $e$"),
    "Q90": ("回到定义", "回到定义：到焦点的距离 = 到准线的距离"),
    "Q91": ("代换", "设而不求：联立后韦达整体代入"),
    "Q92": ("作差相消", "两点代入方程后相减（点差）"),
    "Q93": ("数形结合", "建系坐标化，用方向向量、法向量的夹角"),
    "Q94": ("数形结合", "向法向量投影；或补形用等体积"),
    "Q95": ("补形", "不规则的补成柱、锥、长方体"),
    "Q96": ("数形结合", "看方向向量与法向量的关系"),
    "Q97": ("互逆", "正面情况多，先算反面（对立事件）"),
    "Q98": ("回到定义", "回到条件概率的定义，缩小样本空间"),
    "Q99": ("分类讨论", "按来源分类，各类相加"),
    "Q100": ("回到定义", "按定义列分布列再求"),
    "Q101": ("分类讨论", "恰好 $k$ 次：选出哪 $k$ 次（分类），每类独立相乘"),
    "Q102": ("分类讨论", "分步计数：次品里选几件，正品里选几件"),
    "Q103": ("代换", "数据整体乘加，跟着变换平均数、方差"),
    "Q104": ("回到定义", "按最小二乘的公式代入，过样本中心"),
    "Q105": ("配凑", "化成半径的二次函数，配方"),
    "Q106": ("回到定义", "按公式算 $\\chi^2$，与临界值比较"),
    "Q107": ("对称", "曲线关于 $x=\\mu$ 对称，总概率为 1"),
    "Q108": ("数形结合", "旋转：坐标公式，或复数乘 $\\cos\\theta+i\\sin\\theta$"),
    "Q109": ("补形", "面积法：两个三角形同高，面积比 = 底之比"),
    "Q110": ("数形结合", "向量相等：坐标对应相等"),
    "Q111": ("回到定义", "回到任意角三角函数的定义"),
    "Q112": ("对称", "在一个周期内用对称找全，再加周期"),
    "Q113": ("互逆", "解出 $x$ 再对调 $x,y$"),
    "Q114": ("代换", "换元 $t=g(x)$"),
    "Q115": ("分类讨论", "先讨论空集，再讨论非空"),
    "Q116": ("互逆", "写成指数式，两边取对数解出时间"),
    "Q117": ("互逆", "开方是乘方的逆：辐角加 $2k\\pi$ 再除以 $n$"),
    "Q118": ("代换", "折算到同一时刻，化成等比求和"),
    "Q119": ("回到定义", "无限项求和：取极限"),
    "Q120": ("分类讨论", "分清元素相同还是对象相同，再选计数方式"),
    "Q121": ("回到定义", "回到平均变化率的定义：作差再相除"),
    "Q122": ("回到定义", "以直代曲：用切线近似"),
    "Q123": ("特例", "对任意参数都成立：参数的系数和其余部分分别为 0"),
    "Q124": ("数形结合", "中点在直线上、连线与直线垂直"),
    "Q125": ("回到定义", "按条件直接列等式（定义法），再化简"),
    "Q126": ("回到定义", "回到定义 $|PF_1|\\pm|PF_2|=2a$，配合余弦定理"),
    "Q127": ("代换", "参数换元，化成一个三角函数求最值"),
    "Q128": ("数形结合", "用三个向量表示，看系数和"),
    "Q129": ("数形结合", "射影：面积比、余弦相乘"),
    "Q130": ("数形结合", "构造直角三角形：球心、截面圆心、截面上一点"),
    "Q131": ("回到定义", "按位置的定义取数；直方图面积 = 频率"),
    "Q132": ("分类讨论", "拆成互斥的几类，每类独立相乘"),
}

# 写不成一个公式、由几种方法配合工具组成的流程：节点加棕色“解法”标记（照不等式大厦 v47）
JIEFA = ["R08"]

# ── 推导线补全过程（只增不删）：(起, 止) → (加在前面的行, 加在后面的行) ──
EDGE_DETAIL = {
    ("P62", "P63"): ([r"由对称轴 $x=a$：$f(x)=f(2a-x)$；再用对称轴 $x=b$，把 $2a-x$ 当自变量换进去"], [r"所以周期 $T=2|b-a|$"]),
    ("P70", "P97"): ([r"椭圆标准方程推导中，平方整理后得到："], [r"即 $|PF_1|=e\cdot$（$P$ 到直线 $x=-\dfrac{a^2}{c}$ 的距离）"]),
    ("R22", "R23"): ([r"$z=a+bi$ 与共轭 $\bar z=a-bi$ 相乘："], [r"所以 $z\bar z=|z|^2$；$z+\bar z=2a$，$z-\bar z=2bi$ 直接相加减"]),
    ("S04", "P11"): ([], [r"终边与单位圆的交点 $(x,y)=(\cos\alpha,\sin\alpha)$，所以 $\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$（要求 $\cos\alpha\ne 0$）"]),
    ("S06", "R24"): ([r"由 $i^2=-1$ 依次乘 $i$：$i^3=-i$"], [r"$i^{n+4}=i^n\cdot i^4=i^n$：4 个一循环"]),
    ("S09", "P32"): ([r"$S_n=a_1+\cdots+a_{n-1}+a_n$，$S_{n-1}=a_1+\cdots+a_{n-1}$"], [r"相减只剩 $a_n$（$S_{n-1}$ 要有意义，所以 $n\ge 2$）；$n=1$ 时 $a_1=S_1$"]),
    ("P01", "P02"): ([r"由配方，$ax^2+bx+c=0$ 化为"], [r"$\Delta\ge 0$ 时两边开平方：$x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{\Delta}}{2a}$，移项得求根公式"]),
    ("R29", "R32"): ([r"$n=1$ 时 $1=1$；设 $n=k$ 时 $1^3+\cdots+k^3=\left[\dfrac{k(k+1)}{2}\right]^2$，两边加 $(k+1)^3$："], [r"右边正是 $n=k+1$ 时的形式"]),
    ("P14", "P15"): ([], [r"$\tan 2\alpha=\dfrac{\tan\alpha+\tan\alpha}{1-\tan\alpha\tan\alpha}=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$"]),
    ("P28", "R29"): ([], [r"$S_n=n\cdot 1+\dfrac{n(n-1)}{2}\cdot 1=\dfrac{n(n+1)}{2}$"]),
    ("P45", "P72"): ([r"两交点都在直线 $y=kx+m$ 上："], [r"$|AB|=\sqrt{(1+k^2)(x_1-x_2)^2}=\sqrt{1+k^2}\,|x_1-x_2|$，$|x_1-x_2|$ 用韦达表示"]),
    ("R04", "R07"): ([], [r"$(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)$ 移项：$a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$"]),
    ("R05", "R07"): ([], [r"$(a+b)^3=a^3+b^3+3ab(a+b)$ 移项：$a^3+b^3=(a+b)^3-3ab(a+b)$"]),
    ("R03", "R07"): ([], [r"$(a+b)^2=a^2+2ab+b^2$ 移项：$a^2+b^2=(a+b)^2-2ab$；$(a+b)^2$ 与 $(a-b)^2$ 相减：$(a-b)^2=(a+b)^2-4ab$"]),
    ("R17", "R18"): ([], [r"$\sin 2\alpha=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha$；$\cos 2\alpha=\cos^2\alpha-\sin^2\alpha$"]),
    ("R33", "R39"): ([r"$f(x)=a_0+a_1x+\cdots+a_nx^n$ 对一切 $x$ 成立："], [r"$x=1$ 得各项系数和，$x=-1$ 得交错和，两式相加、相减再除以 2 得偶次、奇次项系数和；$x=0$ 得常数项"]),
    ("S09", "P51"): ([r"成等差：相邻两项的差相等；成等比：相邻两项的比相等"], [r"整理得 $2b=a+c$；$b^2=ac$"]),
    ("S20", "R56"): ([r"$X$ 只取 1、0，概率 $p$、$1-p$，代入均值、方差的定义："], []),
    ("S23", "P103"): ([r"$X=\dfrac{Y-\mu}{\sigma}=\dfrac{1}{\sigma}Y-\dfrac{\mu}{\sigma}$，用 $E(aY+b)$、$D(aY+b)$："], [r"均值 0、方差 1，所以 $X\sim N(0,1)$"]),
    ("P08", "P40"): ([], [r"$(\log_a x)'=\dfrac{1}{\ln a}(\ln x)'=\dfrac{1}{x\ln a}$"]),
    ("R30", "P53"): ([r"仿 $\dfrac{1}{k(k+1)}$：两个因式相差 $d$ 时"], [r"右边通分：$\dfrac{1}{d}\cdot\dfrac{(k+d)-k}{k(k+d)}=\dfrac{1}{k(k+d)}$；根式型用分母有理化"]),
    ("R33", "R35"): ([], [r"$(x+\Delta x)^n=x^n+C_n^1x^{n-1}\Delta x+C_n^2x^{n-2}(\Delta x)^2+\cdots$，减去 $x^n$ 再除以 $\Delta x$"]),
    ("R01", "R04"): ([r"$(a+b+c)^2=(a+b+c)(a+b+c)$，每项乘每项共 9 项"], [r"平方项 3 个；$ab$、$bc$、$ca$ 各出现 2 次"]),
    ("R13", "P46"): ([r"$\sin^2\alpha+\cos^2\alpha=1$ 移项：$\sin^2\alpha=1-\cos^2\alpha$"], [r"开平方：$\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，符号由 $\alpha$ 所在象限定"]),
    ("R20", "R21"): ([], [r"则 $\alpha=\dfrac{\theta+\varphi}{2}$，$\beta=\dfrac{\theta-\varphi}{2}$，代入积化和差，左右互换即和差化积"]),
    ("R23", "R25"): ([], [r"即 $|z_1z_2|=|z_1||z_2|$"]),
    ("S15", "P63"): ([r"$f(x+a)=-f(x)$ 中把 $x$ 换成 $x+a$："], [r"所以 $T=2a$；$f(x+a)=\dfrac{1}{f(x)}$ 同理"]),
    ("R01", "R11"): ([r"左边 $(a^2+b^2)(c^2+d^2)$ 展开；右边 $(ac+bd)^2+(ad-bc)^2$ 展开，交叉项 $+2abcd$、$-2abcd$ 抵消"], []),
    ("R03", "P68"): ([r"把 $x^2+y^2+Dx+Ey+F=0$ 中 $x$、$y$ 两组分别配方："], [r"得 $\left(x+\dfrac{D}{2}\right)^2+\left(y+\dfrac{E}{2}\right)^2=\dfrac{D^2+E^2-4F}{4}$，右边 $>0$ 才是圆"]),
    ("R13", "P12"): ([r"$\sin^2\alpha+\cos^2\alpha=1$"], [r"$\dfrac{\sin^2\alpha}{\cos^2\alpha}+1=\dfrac{1}{\cos^2\alpha}$，即 $1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$"]),
    ("R18", "P18"): ([r"倍角写成分式：分母补上 $1=\sin^2\dfrac{\alpha}{2}+\cos^2\dfrac{\alpha}{2}$"], [r"全部化成 $t=\tan\dfrac{\alpha}{2}$；$\cos\alpha$ 同理"]),
    ("R28", "P50"): ([], [r"累加：$a_2-a_1=f(1)$，…，$a_n-a_{n-1}=f(n-1)$，$n-1$ 个式子相加，中间项抵消：$a_n=a_1+\sum_{k=1}^{n-1}f(k)$",
                          r"累乘：$\dfrac{a_2}{a_1}\cdot\dfrac{a_3}{a_2}\cdots\dfrac{a_n}{a_{n-1}}=\prod_{k=1}^{n-1}g(k)$，中间项约掉"]),
    ("S01", "R01"): ([], [r"$(a+b)(c+d)=a(c+d)+b(c+d)=ac+ad+bc+bd$"]),
    ("S01", "R28"): ([], [r"去括号后 $b_2$ 与 $-b_2$、$b_3$ 与 $-b_3$……两两抵消，只剩 $b_{n+1}-b_1$"]),
    ("S06", "R22"): ([r"$(a+bi)(c+di)$ 按多项式展开：$ac+adi+bci+bdi^2$"], [r"实部 $ac-bd$、虚部 $ad+bc$ 分别合并"]),
    ("P03", "P45"): ([], [r"如 $x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2=\dfrac{b^2}{a^2}-\dfrac{2c}{a}$"]),
    ("P05", "P40"): ([], [r"$(a^x)'=e^{x\ln a}\cdot\ln a=a^x\ln a$"]),
    ("P26", "P27"): ([r"用通项写出 $a_m+a_n$ 与 $a_p+a_q$："], [r"$m+n=p+q$ 时两边相等"]),
    ("P29", "P30"): ([r"用通项写出 $a_ma_n$ 与 $a_pa_q$："], [r"$m+n=p+q$ 时两边相等"]),
    ("R18", "R19"): ([r"由 $\cos 2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$"], [r"得 $\cos^2\alpha=\dfrac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\dfrac{1-\cos 2\alpha}{2}$"]),
    ("R01", "R02"): ([r"$(a+b)(a-b)=a^2-ab+ab-b^2$"], []),
    ("R18", "R38"): ([r"$(\sin\alpha\pm\cos\alpha)^2=\sin^2\alpha\pm 2\sin\alpha\cos\alpha+\cos^2\alpha$"], []),
    ("S03", "P06"): ([], [r"得 $a^{\log_a N}=N$；把 $N=a^b$ 代入 $b=\log_a N$ 得 $\log_a a^b=b$"]),
    ("S06", "P24"): ([r"$z=a+bi\ne 0$，$r=|z|=\sqrt{a^2+b^2}$"], [r"所以有角 $\theta$ 使 $\cos\theta=\dfrac{a}{r}$，$\sin\theta=\dfrac{b}{r}$，即 $z=r(\cos\theta+i\sin\theta)$"]),
    ("S09", "P26"): ([r"$a_2-a_1=d$，…，$a_n-a_{n-1}=d$ 相加："], [r"$a_n-a_1=(n-1)d$"]),
    ("S09", "P29"): ([r"$\dfrac{a_2}{a_1}=q$，…，$\dfrac{a_n}{a_{n-1}}=q$ 相乘："], [r"$\dfrac{a_n}{a_1}=q^{n-1}$"]),
    ("P08", "P09"): ([], [r"$\log_a b\cdot\log_b a=\dfrac{\lg b}{\lg a}\cdot\dfrac{\lg a}{\lg b}=1$；$\log_{a^m}b^n=\dfrac{n\lg b}{m\lg a}=\dfrac{n}{m}\log_a b$"]),
    ("P24", "R26"): ([r"两个三角形式按多项式相乘，用 $i^2=-1$"], []),
    ("P43", "P44"): ([], [r"分母 $(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})=a-b$"]),
    ("R01", "R09"): ([r"右边 $(x-y)(x^{n-1}+x^{n-2}y+\cdots+y^{n-1})$ 展开"], [r"只剩 $x^n-y^n$"]),
    ("R17", "P14"): ([r"$\tan(\alpha+\beta)=\dfrac{\sin(\alpha+\beta)}{\cos(\alpha+\beta)}$，代入和角公式"], [r"得 $\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$；$\beta\to-\beta$ 得差角"]),
    ("R17", "R26"): ([r"相乘后实部 $\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2$，虚部 $\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2$"], []),
    ("P06", "P10"): ([], [r"$y=a^x\iff x=\log_a y$，交换 $x,y$ 得 $y=\log_a x$，图像关于 $y=x$ 对称"]),
    ("P28", "P54"): ([], [r"$(S_{2m}-S_m)-S_m$：对应项都相差 $md$，共 $m$ 项，差为 $m^2d$"]),
    ("R12", "P41"): ([], [r"$a^m\div a^n=a^m\cdot a^{-n}=a^{m-n}$，正整数指数的运算律照样成立"]),
    ("R26", "P25"): ([], [r"$\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]$ 乘 $z_2$ 得 $z_1$，所以它就是商"]),
    ("R26", "R27"): ([r"$n=1$ 成立；设 $z^k=r^k(\cos k\theta+i\sin k\theta)$"], [r"$z^{k+1}=z^k\cdot z$：模相乘、辐角相加，得 $r^{k+1}[\cos(k+1)\theta+i\sin(k+1)\theta]$"]),
    ("S04", "R13"): ([], [r"代入得 $\cos^2\alpha+\sin^2\alpha=1$"]),
    ("P05", "P43"): ([], [r"$\sqrt{a}=a^{\frac{1}{2}}$：$\sqrt{a}\sqrt{b}=a^{\frac{1}{2}}b^{\frac{1}{2}}=(ab)^{\frac{1}{2}}=\sqrt{ab}$"]),
    ("P03", "P04"): ([r"右边 $a(x-x_1)(x-x_2)=a[x^2-(x_1+x_2)x+x_1x_2]$"], [r"代入 $x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$，得 $ax^2+bx+c$"]),
    ("R23", "P23"): ([], [r"分母变成 $(c+di)(c-di)=c^2+d^2$（实数），分子展开"]),
    ("P02", "P03"): ([r"$x_{1,2}=\dfrac{-b\pm\sqrt{\Delta}}{2a}$"], [r"和 $=\dfrac{-2b}{2a}=-\dfrac{b}{a}$；积 $=\dfrac{b^2-\Delta}{4a^2}=\dfrac{4ac}{4a^2}=\dfrac{c}{a}$"]),
    ("R14", "P13"): ([], [r"如 $\tan(\pi+\alpha)=\dfrac{-\sin\alpha}{-\cos\alpha}=\tan\alpha$"]),
    ("R17", "R20"): ([r"$\sin(\alpha+\beta)+\sin(\alpha-\beta)=2\sin\alpha\cos\beta$"], [r"两边除以 2 得积化和差；$\cos$ 的两式同理"]),
}
for _e in EDGES:
    _k = (_e["s"], _e["t"])
    if _e["kind"] == "derive" and _k in EDGE_DETAIL:
        _b, _a = EDGE_DETAIL[_k]
        _e["lines"] = list(_b) + _e["lines"] + list(_a)
