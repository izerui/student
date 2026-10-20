# 恒等式大厦 · 拓扑图

> 从 23 个起点出发，不跳步推出高中全部恒等式与公式。S 起点（公理与定义）→ R 结论 → P 带条件结论，共 183 个知识节点。

---

## 页面设置

- 标题：恒等式大厦
- 编号写法：[SRPQ]\d{2,3}
- 保存键：identity-tree-learned

| 区域 | 颜色 | 位置 | 说明 |
|---|---|---|---|
| 地基 | #795548 | 0.5 | 地基：实数运算律 · 初中几何 · 计数原理 · 数学归纳法（直接承认，不依赖别的起点） |
| 代数 | #1565C0 | 0.15 | ① 代数：运算律 → 分配律展开 → 乘法公式、因式分解 → 配方、求根公式、韦达定理 |
| 指数与对数 | #6A1B9A | 0.3 | ② 指数、根式与对数：指数运算律 → 整数、实数指数 → 根式；对数（逆运算）→ 运算律、换底 |
| 三角 | #C62828 | 0.45 | ③ 三角：单位圆 → 勾股、诱导；数量积 → 和差角 → 倍角、降幂、半角、辅助角；解三角形 |
| 向量 | #AD1457 | 0.55 | ③a 向量与解三角形：数量积 → 运算公式 → 余弦定理；面积 → 正弦定理 |
| 复数 | #4527A0 | 0.65 | ③b 复数：$i^2=-1$ → 乘法、共轭与模 → 三角形式：模相乘、辐角相加 → 棣莫弗 |
| 数列 | #00695C | 0.2 | ④ 数列：累加相消 → 等差、等比的通项与求和 → 裂项、自然数幂和 |
| 计数 | #E65100 | 0.8 | ⑤ 计数：两个计数原理 → 排列 → 组合 → 二项式定理 |
| 导数 | #2E7D32 | 0.35 | ⑥ 导数：导数定义 → 求导法则；导数表的由来 |
| 函数性质 | #0277BD | 0.1 | ⑦ 函数性质：奇偶、周期、图像的定义 → 对称、周期的恒等关系 → 图像变换 → 正弦型函数 |
| 解析几何 | #BF360C | 0.75 | ⑧ 解析几何：斜率 → 直线方程 → 平行垂直、距离（投影）→ 圆（配方）→ 圆锥曲线 → 联立（韦 |
| 空间 | #37474F | 0.6 | ③c 空间向量与立体几何：空间坐标数量积 → 空间角、距离（投影）；体积：台 = 大锥 − 小锥 |
| 概率统计 | #00838F | 0.9 | ⑨ 概率统计：事件与概率 → 加法、乘法、全概率、贝叶斯 → 期望与方差 → 二项、超几何；统计：方 |

---

## 主干链

1. **代数主干**
   运算律 S01 → 多项式乘法 R01 → 完全平方 R03 → 配方 P01 → 求根公式 P02 → 韦达定理 P03
2. **三角主干（勾股）**
   单位圆 S04 → 勾股恒等式 R13
3. **三角主干（和角）**
   数量积 S05 → 坐标式 R15 → 两角差余弦 R16 → 和角公式 R17 → 倍角 R18 → 降幂 R19
4. **向量到余弦定理**
   数量积 S05 → 向量模的平方 P49 → 余弦定理 P22
5. **等差数列**
   等差定义 S09 → 等差通项 P26 → 下标性质 P27 → 等差求和 P28
6. **等比数列**
   等比定义 S09 → 等比通项 P29 → 等比求和 P31

---

## 第 0 层　地基：公理、定义与起点

### S01 运算律、等式性质与绝对值
- 标志：交换律、结合律；分配律 $a(b+c)=ab+ac$
- 区域：地基
- 类型：起点
- 标签：公理
- 是什么：等式两边同加、同乘一个数仍相等；同除一个非零数仍相等；减 $b$ 即加 $-b$；除以 $b$（$b\ne 0$）即乘 $\dfrac{1}{b}$；绝对值：$a\ge 0$ 时 $|a|=a$，$a<0$ 时 $|a|=-a$
- 注释：
  - 实数运算的基本规定，所有恒等式的地基

### S02 乘方与指数幂
- 标志：$a^n$：$n$ 个 $a$ 相乘（$n$ 为正整数）
- 区域：指数与对数
- 类型：起点
- 标签：定义
- 是什么：$a^0=1$，$a^{-n}=\dfrac{1}{a^n}$（$a\ne 0$）；$a^{\frac{m}{n}}=\sqrt[n]{a^m}$（$a>0$；$m,n$ 为正整数，$n>1$）；$a^{-\frac{m}{n}}=\dfrac{1}{a^{\frac{m}{n}}}$（$a>0$）；无理数指数幂（$a>0$）课本承认

### S03 对数
- 标志：$a>0$，$a\ne 1$，$N>0$ 时：$a^b=N\iff b=\log_a N$
- 区域：指数与对数
- 类型：起点
- 标签：定义
- 是什么：$\lg N=\log_{10}N$，$\ln N=\log_e N$

### S04 三角函数（单位圆）
- 标志：角 $\alpha$ 终边与单位圆交于 $P(x,y)$
- 区域：三角
- 类型：起点
- 标签：定义
- 是什么：$\sin\alpha=y$，$\cos\alpha=x$，$\tan\alpha=\dfrac{y}{x}$（$x\ne 0$）；终边上任一点 $P(x,y)$（非原点），$r=\sqrt{x^2+y^2}$：$\sin\alpha=\dfrac{y}{r}$，$\cos\alpha=\dfrac{x}{r}$，$\tan\alpha=\dfrac{y}{x}$；单位圆是 $r=1$ 的特例（相似三角形）；终边相同的角 $\alpha+2k\pi$（$k\in\mathbb{Z}$）三角函数值相同

### S05 向量数量积
- 标志：$\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$（$\theta\in[0,\pi]$ 为夹角）
- 区域：向量
- 类型：起点
- 标签：定义
- 是什么：交换律、数乘结合律、分配律（课本给出）；单位正交基：$\vec i\cdot\vec i=\vec j\cdot\vec j=1$，$\vec i\cdot\vec j=0$；线性运算（加减、数乘、坐标、共线）见起点〔S21〕；B 版先学线性运算（必修二），再学数量积（必修三）；$\vec a\cdot\vec a=|\vec a|^2$；$\vec e$ 为单位向量时 $\vec a\cdot\vec e=|\vec a|\cos\langle\vec a,\vec e\rangle$

### S06 复数
- 标志：$i^2=-1$；$z=a+bi$（$a,b\in\mathbb{R}$）；$a+bi=c+di\iff a=c$ 且 $b=d$
- 区域：复数
- 类型：起点
- 标签：定义
- 是什么：$z$ ↔ 点 $(a,b)$ ↔ 向量；模 $|z|=\sqrt{a^2+b^2}$，共轭 $\bar z=a-bi$；加、乘按多项式运算，运算律照常成立；相反数 $-z=-a-bi$，减法 $z_1-z_2=(a-c)+(b-d)i$；乘法公式照常成立：$(z_1+z_2)^2=z_1^2+2z_1z_2+z_2^2$，$z_1^2-z_2^2=(z_1+z_2)(z_1-z_2)$
- 反例：
  - $\sqrt{a}$ 只用于 $a\ge 0$：$\sqrt{-1}\times\sqrt{-4}=\sqrt{4}=2$ 是错的（应为 $i\cdot 2i=-2$）

### S11 欧拉公式
- 标志：$e^{i\theta}=\cos\theta+i\sin\theta$；$\theta=\pi$ 时 $e^{i\pi}+1=0$
- 区域：复数
- 类型：起点
- 标签：承认；拓展
- 是什么：要用级数或复变函数才能证明，高中只承认
- 注释：
  - 同源：三角形式乘法“辐角相加”与 $e^ae^b=e^{a+b}$ 是同一件事〔R26〕
  - 拓展——复数的乘方、三角恒等式的另一种推法

### S09 数列
- 标志：$S_n=a_1+a_2+\cdots+a_n$
- 区域：数列
- 类型：起点
- 标签：定义
- 是什么：等差：$a_{n+1}-a_n=d$（常数）；等比：$\dfrac{a_{n+1}}{a_n}=q$（常数，$a_n\ne 0$，$q\ne 0$）

### S10 数学归纳法
- 标志：$n=n_0$ 成立；$n=k$ 成立 $\Rightarrow n=k+1$ 成立
- 区域：地基
- 类型：起点
- 标签：公理
- 是什么：$\Rightarrow$ 对一切 $n\ge n_0$ 成立
- 注释：
  - 同见不等式大厦 P23（伯努利归纳步）

### S07 两个计数原理
- 标志：分类加法：各类方法数相加
- 区域：地基
- 类型：起点
- 标签：原理
- 是什么：分步乘法：各步方法数相乘

### S08 导数
- 标志：$f'(x_0)=\displaystyle\lim_{\Delta x\to 0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
- 区域：导数
- 类型：起点
- 标签：定义
- 是什么：$f'(x_0)=\displaystyle\lim_{\Delta x\to 0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$

### S12 导数表与链式法则
- 标志：$C'=0$；$(\sin x)'=\cos x$，$(\cos x)'=-\sin x$；$(e^x)'=e^x$（$x\in\mathbb{R}$）
- 区域：导数
- 类型：起点
- 标签：课本给出
- 是什么：$(x^\alpha)'=\alpha x^{\alpha-1}$（$\alpha$ 为任意实数时取 $x>0$；$\alpha$ 为正整数时 $x\in\mathbb{R}$）；$(a^x)'=a^x\ln a$（$a>0$，$x\in\mathbb{R}$）；$(\log_a x)'=\dfrac{1}{x\ln a}$（$a>0,\ a\ne 1,\ x>0$）；$(\ln x)'=\dfrac{1}{x}$（$x>0$）；有定义不等于可导：$\sqrt{x}$ 在 $x=0$ 有定义，但没有有限导数；链式法则：$g$ 在 $x$ 处可导、$f$ 在 $u=g(x)$ 处可导 $\Rightarrow y'_x=f'(u)\cdot g'(x)$
- 注释：
  - 课本直接给出（链式法则课本写“可以证明”）；B 版先给 $(a^x)'$、$(\log_a x)'$，再令 $a=e$；下面的 R35、P39、P40 只说明由来（拓展）
  - 求基本初等函数的导数 → 查表；复合函数 → 链式法则

### S13 平面几何基础
- 标志：勾股定理 $a^2+b^2=c^2$（直角三角形，$c$ 为斜边）；两点距离 $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$（B 版另用向量 $\overrightarrow{AB}$ 的模重新推出〔R41〕〔R15〕）
- 区域：地基
- 类型：起点
- 标签：初中定理
- 是什么：三角形面积 $=\dfrac{1}{2}\times$ 底 $\times$ 高；圆周角定理：同弧所对的圆周角相等；直径所对的圆周角是直角（课本承认）；垂径定理：圆心到弦的垂线平分弦；圆的切线垂直于过切点的半径

### S14 集合的运算
- 标志：$A\cap B=\{x\mid x\in A$ 且 $x\in B\}$，$A\cup B=\{x\mid x\in A$ 或 $x\in B\}$
- 区域：地基
- 类型：起点
- 标签：定义
- 是什么：补集 $\complement_U A=\{x\mid x\in U$ 且 $x\notin A\}$；$\mathrm{card}(A)$：有限集 $A$ 的元素个数

### S15 函数的图像、奇偶性、周期性
- 标志：图像：点 $(x,y)$ 在 $y=f(x)$ 的图像上 $\iff y=f(x)$
- 区域：函数性质
- 类型：起点
- 标签：定义
- 是什么：定义域关于原点对称，对每个 $x$：$f(-x)=f(x)$ 为偶函数，$f(-x)=-f(x)$ 为奇函数；存在非零常数 $T$，对定义域内每个 $x$ 有 $f(x+T)=f(x)$：周期函数；最小的正周期叫最小正周期

### S16 坐标法：倾斜角与斜率，曲线与方程
- 标志：倾斜角 $\alpha\in[0,\pi)$；$\alpha\ne\dfrac{\pi}{2}$ 时斜率 $k=\tan\alpha$
- 区域：解析几何
- 类型：起点
- 标签：定义
- 是什么：曲线上点的坐标都是方程的解，以方程的解为坐标的点都在曲线上；圆：到定点距离为定长；椭圆：到两定点距离之和为 $2a$（$2a>|F_1F_2|$）；双曲线：到两定点距离之差的绝对值为 $2a$（$0<2a<|F_1F_2|$）；抛物线：到定点与定直线距离相等（定点不在定直线上）

### S17 空间向量与空间直角坐标系
- 标志：单位正交基 $\vec i,\vec j,\vec k$ 两两垂直、长度为 1；$\vec a=x\vec i+y\vec j+z\vec k$ 记作 $(x,y,z)$
- 区域：空间
- 类型：起点
- 标签：定义
- 是什么：直线的方向向量 $\vec u$；平面的法向量 $\vec n$：与平面垂直的非零向量；运算律与平面向量相同（课本给出）；直线：$B\in l\iff\overrightarrow{AB}=\lambda\vec u$；平面：$B\in\alpha\iff\overrightarrow{AB}\cdot\vec n=0$

### S18 祖暅原理，柱、锥、球的体积与面积
- 标志：祖暅原理：夹在两个平行平面间的两个几何体，被平行于这两个平面的任意平面所截，截面积总相等，则体积相等
- 区域：空间
- 类型：起点
- 标签：课本给出
- 是什么：柱体 $V=Sh$；锥体 $V=\dfrac{1}{3}Sh$；球 $V=\dfrac{4}{3}\pi R^3$，$S=4\pi R^2$；圆柱侧面积 $2\pi rl$；圆锥侧面积 $\pi rl$（由侧面展开图得出：矩形、扇形〔P83〕）

### S19 古典概型、事件的关系、独立与条件概率
- 标志：古典概型：$P(A)=\dfrac{k}{n}$（$n$ 为样本点总数，$k$ 为 $A$ 包含的样本点数）
- 区域：概率统计
- 类型：起点
- 标签：定义
- 是什么：互斥：$A\cap B=\varnothing$；对立：互斥且 $A\cup B=\Omega$；性质（课本给出）：$0\le P(A)\le 1$，$P(\Omega)=1$；$A,B$ 互斥时 $P(A\cup B)=P(A)+P(B)$；独立：$P(AB)=P(A)P(B)$；条件概率：$P(B|A)=\dfrac{P(AB)}{P(A)}$（$P(A)>0$）

### S20 离散型随机变量的分布列、均值与方差
- 标志：分布列 $P(X=x_i)=p_i$，$p_i\ge 0$，$p_1+p_2+\cdots+p_n=1$
- 区域：概率统计
- 类型：起点
- 标签：定义
- 是什么：均值 $E(X)=\sum x_ip_i$；方差 $D(X)=\sum\left[x_i-E(X)\right]^2p_i$；$P(X\le a)+P(X>a)=1$；$Y=aX+b$（$a\ne 0$）时 $P(X=t)=P(Y=at+b)$，两个分布列的概率行相同

### S21 向量的线性运算
- 标志：加减（三角形法则）：$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$，$\vec a-\vec b=\vec a+(-\vec b)$，$\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$
- 区域：向量
- 类型：起点
- 标签：定义
- 是什么：运算律（课本给出）：$\vec a+\vec 0=\vec a$，$\vec a+\vec b=\vec b+\vec a$，$(\vec a+\vec b)+\vec c=\vec a+(\vec b+\vec c)$；数乘：$|\lambda\vec a|=|\lambda||\vec a|$，$\lambda(\mu\vec a)=(\lambda\mu)\vec a$，$(\lambda+\mu)\vec a=\lambda\vec a+\mu\vec a$，$\lambda(\vec a+\vec b)=\lambda\vec a+\lambda\vec b$；坐标：$\vec a=x\vec i+y\vec j$ 记作 $(x,y)$；共线：$\vec a\ne\vec 0$ 时 $\vec a\parallel\vec b\iff\vec b=\lambda\vec a$（课本给出）

### S22 平均变化率
- 标志：$\dfrac{\Delta y}{\Delta x}=\dfrac{f(x_2)-f(x_1)}{x_2-x_1}=\dfrac{f(x_1+\Delta x)-f(x_1)}{\Delta x}$（$x_1\ne x_2$）：割线 $AB$ 的斜率
- 区域：导数
- 类型：起点
- 标签：定义
- 是什么：增函数 $\iff$ 区间内任意两点的 $\dfrac{\Delta y}{\Delta x}>0$；一次函数 $\iff$ 平均变化率恒为常数 $k$
- 注释：
  - 同源：斜率公式〔P65〕、等差数列的公差 $d=\dfrac{a_n-a_m}{n-m}$〔P26〕

### S23 正态分布
- 标志：密度函数 $\varphi(x)=\dfrac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$，$x\in\mathbb{R}$；记作 $X\sim N(\mu,\sigma^2)$
- 区域：概率统计
- 类型：起点
- 标签：课本给出
- 是什么：$\mu=E(X)$，$\sigma=\sqrt{D(X)}$（标准差），$\sigma^2$ 为方差；$P(a\le X\le b)$ = 曲线在 $[a,b]$ 上与 $x$ 轴围成的面积

## 第 1 层　推导第 1 层

### R01 多项式乘法
- 标志：$(a+b)(c+d)=ac+ad+bc+bd$
- 区域：代数
- 类型：结论
- 重要度：3
- 是什么：$(a+b)(c+d)=ac+ad+bc+bd$
- 注释：
  - 本图所有“展开”都从这里出发
  - 看到括号相乘 → 逐项展开
- 依赖：
  - 来源：S01
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】「分配律」$(a+b)(c+d)=a(c+d)+b(c+d)$
      2. 【展开】「分配律」$a(c+d)+b(c+d)=ac+ad+bc+bd$（分配律用两次）

### R36 去括号与合并同类项
- 标志：$a-(b-c)=a-b+c$，$-(a+b)=-a-b$
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$ma+na=(m+n)a$
- 注释：
  - 一切化简、解方程
  - 括号前是负号 → 去括号全变号
- 依赖：
  - 来源：S01
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】「分配律」乘 $-1$ 去括号：$-(a+b)=(-1)a+(-1)b=-a-b$；$a-(b-c)=a+(-1)(b-c)=a-b+c$（减 $b$ 即加 $-b$）
      2. 【逆用】「分配律」合并同类项：$ma+na=(m+n)a$

### R37 绝对值运算
- 标志：$|ab|=|a||b|$，$|a|^2=a^2$；$\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$（$b\ne 0$）
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$|ab|=|a||b|$，$|a|^2=a^2$；$\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$（$b\ne 0$）
- 注释：
  - 不等式大厦 R09（绝对值界）
  - 同源：复数模的乘法〔R25〕
  - 看到含绝对值的乘除、平方 → $|ab|=|a||b|$，$|a|^2=a^2$；去绝对值按正负分类
- 依赖：
  - 来源：S01
    种类：推出
    方法：分类讨论
    步骤：
      1. 【分类】按 $a,b$ 正负分四种情况，用「绝对值定义」逐一验证

### P42 分式运算
- 标志：约分 $\dfrac{ac}{bc}=\dfrac{a}{b}$（$c\ne 0$）；$\dfrac{a}{b}\pm\dfrac{c}{d}=\dfrac{ad\pm bc}{bd}$
- 区域：代数
- 类型：结论
- 重要度：1
- 条件：定义域分母 $\ne 0$
- 是什么：$\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd}$，$\dfrac{a}{b}\div\dfrac{c}{d}=\dfrac{ad}{bc}$（$c\ne 0$）
- 反例：
  - $\dfrac{x^2-1}{x-1}=x+1$ 只在 $x\ne 1$ 时成立：约掉的因式不能为 0
- 注释：
  - 裂项、复数除法、商的求导、弦化切
  - 看到分式 → 先因式分解，再约分、通分
- 依赖：
  - 来源：S01
    种类：推出
    方法：同除
    条件：▼ 加条件〔定义域〕：分母 $\ne 0$
    步骤：
      1. 【定义】除以 $b$ 即乘 $\dfrac{1}{b}$：$\dfrac{a}{b}=a\cdot\dfrac{1}{b}$
      2. 【约分】分子、分母同除非零式 $c$：$\dfrac{ac}{bc}\Rightarrow\dfrac{a}{b}$

### R12 指数运算律（正整数指数）
- 标志：$a^m\cdot a^n=a^{m+n}$，$(a^m)^n=a^{mn}$，$(ab)^n=a^nb^n$
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 是什么：$a^m\cdot a^n=a^{m+n}$，$(a^m)^n=a^{mn}$，$(ab)^n=a^nb^n$
- 注释：
  - 指数函数性质、比大小（不等式大厦 P04）
  - 看到同底数幂相乘除、幂的乘方 → 先化成同底，再用指数运算律
- 依赖：
  - 来源：S02
    种类：推出
    方法：回到定义
    步骤：
      1. 【定义】「乘方定义」$a^m\cdot a^n$：$m$ 个 $a$ 再乘 $n$ 个 $a$，共 $m+n$ 个 $\Rightarrow a^{m+n}$
  - 来源：S01
    种类：前提
    步骤：
      1. 【前提】结合律、交换律重排

### P06 对数恒等式
- 标志：$a^{\log_a N}=N$，$\log_a a^b=b$
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域$a>0,\ a\ne 1,\ N>0$
- 是什么：$\log_a 1=0$，$\log_a a=1$
- 反例：
  - $N=-2$ 时 $\log_a N$ 无意义
- 注释：
  - 看到 $a^{\log_a N}$ 或 $\log_a a^b$ → 直接等于 $N$、$b$
- 依赖：
  - 来源：S03
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$a>0,\ a\ne 1,\ N>0$
    步骤：
      1. 【代入】$b=\log_a N$ 代回 $a^b=N$：$a^{\log_a N}=N$
      2. 【代入】$N=a^b$ 代入 $b=\log_a N$：$\log_a a^b=b$

### R13 勾股恒等式
- 标志：$\sin^2\alpha+\cos^2\alpha=1$
- 区域：三角
- 类型：结论
- 重要度：3
- 是什么：$\sin^2\alpha+\cos^2\alpha=1$
- 注释：
  - 同见不等式大厦 R01、R02、R03
  - 看到 $\sin^2$、$\cos^2$ 同时出现，或已知一个求另一个 → 勾股恒等式
- 依赖：
  - 来源：S04
    种类：推出
    方法：代换
    步骤：
      1. 【代入】$P(\cos\alpha,\sin\alpha)$ 在单位圆 $x^2+y^2=1$ 上 $\Rightarrow\cos^2\alpha+\sin^2\alpha=1$（「三角函数定义」）
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】单位圆方程由勾股定理得到

### P11 商数关系
- 标志：$\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- 区域：三角
- 类型：结论
- 条件：定义域$\cos\alpha\ne 0$
- 是什么：$\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- 反例：
  - $\alpha=\dfrac{\pi}{2}$：$\cos\alpha=0$，两边都无意义
- 注释：
  - 看到 tan 与 sin、cos 混在一起 → 切化弦
- 依赖：
  - 来源：S04
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$\cos\alpha\ne 0$
    步骤：
      1. 【定义】$\tan\alpha=\dfrac{y}{x}$（「三角函数定义」）
      2. 【代入】交点 $(x,y)=(\cos\alpha,\sin\alpha)\Rightarrow\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$（要求 $\cos\alpha\ne 0$）

### R14 诱导公式（sin、cos 对任意实数 $\alpha$ 成立）
- 标志：① $\alpha+2k\pi$：值不变
- 区域：三角
- 类型：结论
- 重要度：2
- 是什么：② $\sin(\pi+\alpha)=-\sin\alpha$，$\cos(\pi+\alpha)=-\cos\alpha$；③ $\sin(-\alpha)=-\sin\alpha$，$\cos(-\alpha)=\cos\alpha$；④ $\sin(\pi-\alpha)=\sin\alpha$，$\cos(\pi-\alpha)=-\cos\alpha$；⑤ $\sin\left(\dfrac{\pi}{2}-\alpha\right)=\cos\alpha$，$\cos\left(\dfrac{\pi}{2}-\alpha\right)=\sin\alpha$；⑥ $\sin\left(\dfrac{\pi}{2}+\alpha\right)=\cos\alpha$，$\cos\left(\dfrac{\pi}{2}+\alpha\right)=-\sin\alpha$；⑦ $\sin\left(\dfrac{3\pi}{2}-\alpha\right)=-\cos\alpha$，$\cos\left(\dfrac{3\pi}{2}-\alpha\right)=-\sin\alpha$；⑧ $\sin\left(\dfrac{3\pi}{2}+\alpha\right)=-\cos\alpha$，$\cos\left(\dfrac{3\pi}{2}+\alpha\right)=\sin\alpha$（B 版：①～⑧都称诱导公式）
- 注释：
  - 口诀“奇变偶不变，符号看象限”（把 $\alpha$ 看作锐角定符号）只用于记忆，不是条件
  - 看到 $\pi\pm\alpha$、$\dfrac{\pi}{2}\pm\alpha$、$-\alpha$ → 诱导公式化成锐角
- 依赖：
  - 来源：S04
    种类：推出
    方法：代换
    步骤：
      1. 【对称】终边关于原点、$x$ 轴、$y$ 轴、$y=x$ 对称：交点 $(x,y)$ 变为 $(-x,-y)$、$(x,-y)$、$(-x,y)$、$(y,x)$（「三角函数定义」）
      2. 【代换】⑥：⑤ 中 $\alpha\to-\alpha$，再用「诱导公式③」
      3. 【拆角】⑦⑧：$\dfrac{3\pi}{2}\pm\alpha=\pi+\left(\dfrac{\pi}{2}\pm\alpha\right)$，用「诱导公式②」再用「诱导公式⑤⑥」

### P24 三角形式
- 标志：$z=a+bi=r(\cos\theta+i\sin\theta)$，$r=|z|$
- 区域：复数
- 类型：结论
- 重要度：1
- 条件：定义域$z\ne 0$；符号分支$\theta$ 由 $a,b$ 正负定
- 是什么：$\cos\theta=\dfrac{a}{r}$，$\sin\theta=\dfrac{b}{r}$；$\theta$ 可加 $2k\pi$；辐角主值取 $[0,2\pi)$；$\bar z=r[\cos(-\theta)+i\sin(-\theta)]$，$\dfrac{1}{z}=\dfrac{1}{r}[\cos(-\theta)+i\sin(-\theta)]$
- 反例：
  - $z=-1-i$：只看 $\tan\theta=1$ 取 $\dfrac{\pi}{4}$，得 $1+i\ne z$
- 注释：
  - 复数化三角形式 → 求 $r$，按 $a,b$ 正负定辐角
- 依赖：
  - 来源：S06
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕〔符号分支〕：$z\ne 0$；$\theta$ 看 $a,b$ 正负
    步骤：
      1. 【定义】$z=a+bi\ne 0$，$r=|z|=\sqrt{a^2+b^2}$
      2. 【代入】$\left(\dfrac{a}{r}\right)^2+\left(\dfrac{b}{r}\right)^2=1\Rightarrow\left(\dfrac{a}{r},\dfrac{b}{r}\right)$ 在单位圆上（「三角函数定义」）
      3. 【代换】有角 $\theta$ 使 $\cos\theta=\dfrac{a}{r}$，$\sin\theta=\dfrac{b}{r}\Rightarrow z=r(\cos\theta+i\sin\theta)$
  - 来源：S04
    种类：前提
    步骤：
      1. 【前提】单位圆定义

### R28 累加相消
- 标志：$(b_2-b_1)+(b_3-b_2)+\cdots+(b_{n+1}-b_n)=b_{n+1}-b_1$
- 区域：数列
- 类型：结论
- 重要度：1
- 是什么：$(b_2-b_1)+(b_3-b_2)+\cdots+(b_{n+1}-b_n)=b_{n+1}-b_1$
- 注释：
  - 看到“相邻项相减”的和 → 累加相消
- 依赖：
  - 来源：S01
    种类：推出
    方法：作差相消
    步骤：
      1. 【去括号】$(b_2-b_1)+(b_3-b_2)+\cdots+(b_{n+1}-b_n)\Rightarrow -b_1+b_2-b_2+b_3-b_3+\cdots+b_{n+1}$（「结合律」）
      2. 【相消】$b_2$ 与 $-b_2$、$b_3$ 与 $-b_3$……两两抵消 $\Rightarrow b_{n+1}-b_1$

### P51 等差中项、等比中项
- 标志：$a,b,c$ 成等差 $\iff 2b=a+c$
- 区域：数列
- 类型：结论
- 条件：结构前提等差、等比
- 是什么：$a,b,c$ 成等比 $\Rightarrow b^2=ac$（反过来还要 $a,b,c\ne 0$）；$x,y$ 的等比中项 $G=\pm\sqrt{xy}$（$xy>0$）
- 反例：
  - $0,0,0$ 满足 $b^2=ac$，但不是等比数列
- 注释：
  - 三个数成等差或等比 → 中项（等比中项 $G^2=ab$，要求 $ab>0$）
- 依赖：
  - 来源：S09
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔结构前提〕：等差、等比
    步骤：
      1. 【定义】成等差：相邻两项的差相等 $\Rightarrow b-a=c-b$
      2. 【移项】$2b=a+c$
      3. 【定义】成等比：相邻两项的比相等 $\Rightarrow\dfrac{b}{a}=\dfrac{c}{b}$
      4. 【同乘】$b^2=ac$

### P32 $a_n$ 与 $S_n$
- 标志：$a_1=S_1$；$n\ge 2$ 时 $a_n=S_n-S_{n-1}$
- 区域：数列
- 类型：结论
- 条件：定义域$n\ge 2$
- 是什么：$a_1=S_1$；$n\ge 2$ 时 $a_n=S_n-S_{n-1}$
- 反例：
  - $S_n=n^2+1$：$a_1=2$，而 $2n-1$ 在 $n=1$ 时得 1
- 注释：
  - 已知 $S_n$ 求 $a_n$
  - 给出 $S_n$ 求 $a_n$ → 作差，$n=1$ 单独验证
- 依赖：
  - 来源：S09
    种类：推出
    方法：特例
    条件：▼ 加条件〔定义域〕：$n\ge 2$（$S_n$ 公式代入 $n=0$ 不为 0 时，$n=1$ 不能合并）
    步骤：
      1. 【定义】$S_n=a_1+\cdots+a_{n-1}+a_n$，$S_{n-1}=a_1+\cdots+a_{n-1}$
      2. 【作差】$S_n-S_{n-1}=a_n$（$S_{n-1}$ 要有意义，所以 $n\ge 2$）
      3. 【特例】$n=1$：$a_1=S_1$

### P33 排列数
- 标志：$A_n^m=n(n-1)\cdots(n-m+1)=\dfrac{n!}{(n-m)!}$（$0!=1$；约定 $A_n^0=C_n^0=1$）
- 区域：计数
- 类型：结论
- 条件：定义域$m\le n$（自然数）
- 是什么：$A_n^m+mA_n^{m-1}=A_{n+1}^m$（教材例题：按是否含某个元素分类）
- 注释：
  - 从 $n$ 个中选 $m$ 个排成一列（有序）→ 排列数
- 依赖：
  - 来源：S07
    种类：推出
    方法：分类讨论
    条件：▼ 加条件〔定义域〕：$m\le n$
    步骤：
      1. 【分步计数】第 1 位 $n$ 种，第 2 位 $n-1$ 种……第 $m$ 位 $n-m+1$ 种，相乘（「分步乘法原理」）

### P37 和、差、积的求导法则
- 标志：$(u\pm v)'=u'\pm v'$
- 区域：导数
- 类型：结论
- 重要度：2
- 条件：定义域$u,v$ 在该点可导
- 是什么：$(uv)'=u'v+uv'$；$(Cu)'=Cu'$（积法则加 $C'=0$）
- 反例：
  - $u=|x|$，$v=-|x|$，$x=0$：$(u+v)'=0$，右边 $u'$、$v'$ 不存在
- 注释：
  - 切线、单调性、极值
  - 看到函数的和、差、积 → 和差积法则
- 依赖：
  - 来源：S08
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕：$u,v$ 在该点可导
    步骤：
      1. 【配凑】$u(x+\Delta x)v(x+\Delta x)-u(x)v(x)=[u(x+\Delta x)-u(x)]v(x+\Delta x)+u(x)[v(x+\Delta x)-v(x)]$
      2. 【取极限】同除 $\Delta x$，令 $\Delta x\to 0$；$v$ 可导 $\Rightarrow v$ 连续（课本承认）

### R40 子集个数与容斥原理
- 标志：$n$ 元集合的子集有 $2^n$ 个，真子集有 $2^n-1$ 个
- 区域：计数
- 类型：中间步
- 是什么：容斥：$\mathrm{card}(A\cup B)=\mathrm{card}(A)+\mathrm{card}(B)-\mathrm{card}(A\cap B)$；德摩根律 $\complement_U(A\cup B)=(\complement_U A)\cap(\complement_U B)$，$\complement_U(A\cap B)=(\complement_U A)\cup(\complement_U B)$（必修一例题、习题）
- 反例：
  - 50 人中 30 人会英语、25 人会日语：直接相加得 55 > 50，两种都会的人数了两次
- 注释：
  - 同源：二项式系数和 $2^n$〔R34〕；概率的加法公式〔R47〕
  - 两类有重叠的计数 → 相加再减去重叠部分；求子集个数 → $2^n$
- 依赖：
  - 来源：S14
    种类：推出
    方法：作差相消
    步骤：
      1. 【分类计数】$A\cup B$ 分成“只在 $A$”“只在 $B$”“在 $A\cap B$”三类（「分类加法原理」）
      2. 【相减】$\mathrm{card}(A)+\mathrm{card}(B)$ 把 $A\cap B$ 数了两次，减去一次
  - 来源：S07
    种类：前提
    步骤：
      1. 【前提】分步乘法：每个元素“选或不选”2 种，共 $2^n$ 种

### R41 线性运算的坐标、中点与重心
- 标志：$\vec a\pm\vec b=(x_1\pm x_2,\ y_1\pm y_2)$，$\lambda\vec a=(\lambda x_1,\ \lambda y_1)$
- 区域：向量
- 类型：结论
- 重要度：1
- 是什么：$\overrightarrow{AB}=(x_2-x_1,\ y_2-y_1)$：终点坐标减起点坐标；中点：$\overrightarrow{OM}=\dfrac{1}{2}(\overrightarrow{OA}+\overrightarrow{OB})$，$M\left(\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\right)$；重心：$G\left(\dfrac{x_1+x_2+x_3}{3},\dfrac{y_1+y_2+y_3}{3}\right)$，$\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}=\vec 0$；两向量相等 $\iff$ 坐标对应相等；与 $\vec a$ 同向的单位向量 $\dfrac{\vec a}{|\vec a|}$；数轴上两点距离 $|a-b|$、中点 $\dfrac{a+b}{2}$
- 注释：
  - 已知点的坐标求向量 → 终点减起点；中点 → 坐标取平均
- 依赖：
  - 来源：S21
    种类：推出
    方法：展开分解
    步骤：
      1. 【分解】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$
      2. 【合并】「分配律」$\vec a\pm\vec b=(x_1\pm x_2)\vec i+(y_1\pm y_2)\vec j$，$\lambda\vec a=\lambda x_1\vec i+\lambda y_1\vec j$
      3. 【移项】中点：$\overrightarrow{AM}=\overrightarrow{MB}\Rightarrow\overrightarrow{OM}-\overrightarrow{OA}=\overrightarrow{OB}-\overrightarrow{OM}\Rightarrow\overrightarrow{OM}=\dfrac{1}{2}(\overrightarrow{OA}+\overrightarrow{OB})$

### P61 奇偶函数的性质
- 标志：偶函数图像关于 $y$ 轴对称，奇函数图像关于原点对称
- 区域：函数性质
- 类型：结论
- 重要度：1
- 条件：定义域定义域关于原点对称
- 是什么：奇函数在 $x=0$ 处有定义 $\Rightarrow f(0)=0$；两个奇函数或两个偶函数之积为偶函数；奇函数与偶函数之积为奇函数（在公共定义域上）；奇函数在两个对称区间上单调性相同，偶函数相反；$x^{2n}$ 为偶函数，$x^{2n-1}$ 为奇函数（$n$ 为正整数）：只含奇次项的多项式是奇函数
- 反例：
  - $f(x)=x^2$，$x\in[-1,2]$：定义域不关于原点对称，不是偶函数
- 注释：
  - 同源：$\sin(-\alpha)=-\sin\alpha$、$\cos(-\alpha)=\cos\alpha$〔R14〕：正弦是奇函数，余弦是偶函数
  - 已知函数在一侧的式子求另一侧，或 $f(a)$ 求 $f(-a)$ → 奇偶性
- 依赖：
  - 来源：S15
    种类：推出
    方法：对称
    条件：▼ 加条件〔定义域〕：定义域关于原点对称
    步骤：
      1. 【代入】奇函数 $f(-x)=-f(x)$ 中令 $x=0$：$f(0)=-f(0)\Rightarrow f(0)=0$
      2. 【相乘】$f,g$ 同为奇函数：$f(-x)g(-x)=[-f(x)][-g(x)]=f(x)g(x)$
      3. 【对称】点 $(x,y)$ 与 $(-x,y)$ 或 $(-x,-y)$ 同在图像上

### R45 图像变换：平移、伸缩、对称
- 标志：平移：$y=f(x+h)$ 由 $y=f(x)$ 向左平移 $h$（$h>0$）；$y=f(x)+k$ 向上平移 $k$（$k>0$）
- 区域：函数性质
- 类型：中间步
- 是什么：伸缩：$y=f(\omega x)$（$\omega>0$）横坐标变为原来的 $\dfrac{1}{\omega}$；$y=Af(x)$（$A>0$）纵坐标变为原来的 $A$ 倍；对称：$y=f(-x)$ 与 $y=f(x)$ 关于 $y$ 轴，$y=-f(x)$ 关于 $x$ 轴，$y=-f(-x)$ 关于原点；拓展（老教材）：坐标轴平移 $x=x'+h$，$y=y'+k$：曲线方程中把 $x$ 换成 $x'+h$，$y$ 换成 $y'+k$
- 反例：
  - $y=\sin 2x$ 向左平移 $\dfrac{\pi}{6}$ 得 $y=\sin 2\left(x+\dfrac{\pi}{6}\right)=\sin\left(2x+\dfrac{\pi}{3}\right)$，不是 $\sin\left(2x+\dfrac{\pi}{6}\right)$
- 注释：
  - 问图像怎么变 → 平移、伸缩都只对 $x$ 本身操作（先提出 $\omega$）
- 依赖：
  - 来源：S15
    种类：推出
    方法：代换
    步骤：
      1. 【代入】$(x_0,y_0)$ 在 $y=f(x)$ 上 $\iff(x_0-h,\ y_0)$ 在 $y=f(x+h)$ 上（向左平移 $h$）
      2. 【代入】$(x_0,y_0)$ 在 $y=f(x)$ 上 $\iff\left(\dfrac{x_0}{\omega},\ y_0\right)$ 在 $y=f(\omega x)$ 上（横坐标变为 $\dfrac{1}{\omega}$）

### P65 斜率公式与直线方程
- 标志：斜率 $k=\dfrac{y_2-y_1}{x_2-x_1}$
- 区域：解析几何
- 类型：结论
- 重要度：1
- 条件：定义域$x_1\ne x_2$
- 是什么：点斜式 $y-y_0=k(x-x_0)$；斜截式 $y=kx+b$；截距式 $\dfrac{x}{a}+\dfrac{y}{b}=1$（$a,b\ne 0$）；两点式 $\dfrac{y-y_1}{y_2-y_1}=\dfrac{x-x_1}{x_2-x_1}$（$x_1\ne x_2$，$y_1\ne y_2$）；一般式 $Ax+By+C=0$（$A,B$ 不全为 0）：法向量 $(A,B)$，方向向量 $(B,-A)$；$B\ne 0$ 时 $k=-\dfrac{A}{B}$；方向向量 $(\cos\theta,\sin\theta)$，斜率存在时 $(1,k)$；方向向量 $(u,v)$、$u\ne 0$ 时 $k=\dfrac{v}{u}$；点法式 $A(x-x_0)+B(y-y_0)=0$；两点式的整式形式 $(x-x_1)(y_2-y_1)=(x_2-x_1)(y-y_1)$ 对任意两点都成立；三点共线 $\iff$ 任两点连线的斜率都相等（或都不存在）
- 反例：
  - 点斜式、斜截式表示不了竖直线 $x=x_0$；两点式表示不了与坐标轴平行的直线；截距式表示不了过原点或与坐标轴平行的直线
- 注释：
  - 已知一点和斜率 → 点斜式；设直线时先想斜率是否存在
- 依赖：
  - 来源：S16
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕：$x_1\ne x_2$
    步骤：
      1. 【定义】$k=\tan\alpha=\dfrac{y_2-y_1}{x_2-x_1}$
      2. 【定义】直线上任一点 $(x,y)$ 与 $(x_0,y_0)$ 连线的斜率都是 $k$：$\dfrac{y-y_0}{x-x_0}=k$
      3. 【同乘】$x-x_0$：$y-y_0=k(x-x_0)$

### P83 弧长与扇形面积
- 标志：弧度：$|\alpha|=\dfrac{l}{r}$（$l$ 为圆心角 $\alpha$ 所对的弧长）；换算 $180^\circ=\pi$ rad，$1^\circ=\dfrac{\pi}{180}$ rad
- 区域：三角
- 类型：结论
- 重要度：1
- 条件：结构前提圆心角 $\alpha$ 用弧度制
- 是什么：弧长 $l=|\alpha|r$；扇形面积 $S=\dfrac{1}{2}lr=\dfrac{1}{2}|\alpha|r^2$
- 反例：
  - $\alpha=60^\circ$、$r=2$：直接代 $l=60\times 2=120$ 是错的，要先化成 $\dfrac{\pi}{3}$，$l=\dfrac{2\pi}{3}$
- 注释：
  - 同源：三角形面积 $\dfrac{1}{2}\times$ 底 $\times$ 高〔S13〕：把扇形看成“底”为弧长、“高”为半径
  - 扇形的弧长、面积、周长 → 角先化成弧度，再用 $l=|\alpha|r$、$S=\dfrac{1}{2}lr$
- 依赖：
  - 来源：S04
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔结构前提〕：角用弧度制
    步骤：
      1. 【定义】弧度制：弧长与半径之比 $|\alpha|=\dfrac{l}{r}\Rightarrow l=|\alpha|r$
      2. 【作比】面积与圆心角成正比：$S=\dfrac{|\alpha|}{2\pi}\cdot\pi r^2=\dfrac{1}{2}|\alpha|r^2$
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】圆的周长 $2\pi r$、面积 $\pi r^2$

### P88 反函数
- 标志：求法：由 $y=f(x)$ 解出 $x$，再对调 $x,y$；$f^{-1}$ 的定义域 = $f$ 的值域
- 区域：函数性质
- 类型：结论
- 重要度：1
- 条件：结构前提$f$ 在定义域上一一对应（如单调）
- 是什么：$y=f(x)$ 与 $y=f^{-1}(x)$ 的图像关于直线 $y=x$ 对称；点 $(a,b)$ 在 $f$ 上 $\iff(b,a)$ 在 $f^{-1}$ 上；$f[f^{-1}(x)]=x$，$f^{-1}[f(x)]=x$；单调函数一定有反函数，且单调性相同
- 反例：
  - $y=x^2$（$x\in\mathbb{R}$）没有反函数：$y=4$ 对应 $x=\pm 2$
- 注释：
  - 求反函数 → 解出 $x$ 再对调；已知原函数过的点 → 反函数过对调后的点
- 依赖：
  - 来源：S15
    种类：推出
    方法：对称
    条件：▼ 加条件〔结构前提〕：一一对应
    步骤：
      1. 【对调】$y=f(x)$ 解出 $x=f^{-1}(y)$，对调 $x,y$：$y=f^{-1}(x)$
      2. 【对称】$(x,y)$ 与 $(y,x)$ 关于直线 $y=x$ 对称：$(a,b)$ 在 $f$ 上 $\iff(b,a)$ 在 $f^{-1}$ 上

### R51 集合运算律
- 标志：$A\cap B=B\cap A$，$A\cap A=A$，$A\cap\varnothing=\varnothing$；$A\cup B=B\cup A$，$A\cup A=A$，$A\cup\varnothing=A$
- 区域：计数
- 类型：中间步
- 是什么：$A\subseteq B\iff A\cap B=A\iff A\cup B=B$；$A\cup\complement_U A=U$，$A\cap\complement_U A=\varnothing$，$\complement_U(\complement_U A)=A$；分配律：$(A\cup B)\cap C=(A\cap C)\cup(B\cap C)$，$(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$
- 注释：
  - 同源：实数的分配律〔S01〕；概率的事件运算〔S19〕
  - 看到 $A\cap B=A$、$A\cup B=B$ → 化成 $A\subseteq B$，别漏 $A=\varnothing$
- 依赖：
  - 来源：S14
    种类：推出
    方法：回到定义
    步骤：
      1. 【定义】按“且”“或”“非”逐个元素验证（维恩图）

### R53 零积性质
- 标志：$ab=0\iff a=0$ 或 $b=0$
- 区域：代数
- 类型：中间步
- 是什么：解方程的依据：因式分解后令每个因式为 0
- 反例：
  - $x(x-1)=2$ 不能写成 $x=2$ 或 $x-1=2$：右边不是 0
- 注释：
  - 方程一边是乘积、另一边是 0 → 每个因式分别为 0
- 依赖：
  - 来源：S01
    种类：推出
    方法：同除
    步骤：
      1. 【同乘】若 $a\ne 0$，两边乘 $\dfrac{1}{a}$：$ab=0\Rightarrow\dfrac{1}{a}\cdot ab=\dfrac{1}{a}\cdot 0\Rightarrow b=0$

### R55 线性近似（以直代曲）
- 标志：$|\Delta x|$ 很小时：$f(x_0+\Delta x)\approx f(x_0)+f'(x_0)\Delta x$（近似公式，不是恒等式）
- 区域：导数
- 类型：中间步
- 条件：定义域$f$ 在 $x_0$ 处可导
- 是什么：这是近似式，不是恒等式：用切线代替曲线；例：$\sqrt{9.05}\approx 3+\dfrac{0.05}{6}\approx 3.0083$
- 注释：
  - 同源：二项式近似 $(1+x)^n\approx 1+nx$〔R33〕
  - 求接近已知点的函数值的近似值 → 线性近似
- 依赖：
  - 来源：S08
    种类：推出
    方法：回到定义
    步骤：
      1. 【定义】$\Delta x$ 很小时差商 $\approx f'(x_0)$
      2. 【同乘】两边乘 $\Delta x$

### P101 球的截面
- 标志：截面圆半径 $r=\sqrt{R^2-d^2}$（$d$ 为球心到截面的距离）；$d=0$ 时是大圆
- 区域：空间
- 类型：结论
- 条件：定义域$0\le d\le R$
- 是什么：北纬 $\varphi$ 的纬线长 $2\pi R\cos\varphi$
- 注释：
  - 球的截面 → 球心、截面圆心、截面圆上一点构成直角三角形
- 依赖：
  - 来源：S18
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$d\le R$
    步骤：
      1. 【作垂线】球心 $O$ 与截面圆心 $O'$ 的连线垂直于截面，$OO'=d$
      2. 【开平方】「勾股定理」$r^2+d^2=R^2\Rightarrow r=\sqrt{R^2-d^2}$
      3. 【代入】北纬 $\varphi$：$d=R\sin\varphi$，$r=R\cos\varphi$，纬线长 $2\pi R\cos\varphi$
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】勾股定理

### P102 球冠与球缺
- 标志：球冠面积 $S=2\pi Rh$（$h$ 为高）；球缺体积 $V=\pi h^2\left(R-\dfrac{h}{3}\right)$
- 区域：空间
- 类型：结论
- 标签：拓展
- 条件：定义域$0<h\le 2R$
- 是什么：$h=2R$ 时即球面积 $4\pi R^2$、球体积 $\dfrac{4}{3}\pi R^3$
- 注释：
  - 老教材立体几何（拓展）
  - 球被平面截下的一块 → 球冠面积 $2\pi Rh$
- 依赖：
  - 来源：S18
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$0<h\le 2R$
    步骤：
      1. 【对比】「祖暅原理」与球体积同法（老教材给出）：距球心 $t$ 的截面积 $\pi(R^2-t^2)$ = 圆柱截面 $\pi R^2$ − 圆锥截面 $\pi t^2$
      2. 【相减】$t$ 从 $R-h$ 到 $R$（$h\le R$）：球缺体积 = 圆柱段 − 圆台段 $=\pi R^2h-\dfrac{\pi}{3}\left[R^3-(R-h)^3\right]$
      3. 【展开】$=\pi R^2h-\dfrac{\pi}{3}\left(3R^2h-3Rh^2+h^3\right)=\pi h^2\left(R-\dfrac{h}{3}\right)$（$h>R$ 时用球体积减去高 $2R-h$ 的球缺，结果同式）

### R56 两点分布
- 标志：$P(X=1)=p$，$P(X=0)=1-p$
- 区域：概率统计
- 类型：中间步
- 是什么：$E(X)=p$，$D(X)=p(1-p)$；二项分布是 $n$ 个独立两点分布之和：$E=np$，$D=np(1-p)$
- 注释：
  - 只有成功、失败两种结果的一次试验 → 两点分布
- 依赖：
  - 来源：S20
    种类：推出
    方法：代换
    步骤：
      1. 【代入】$X$ 只取 1、0，概率 $p$、$1-p$，代入均值、方差的定义
      2. 【代入】$E(X)=1\cdot p+0\cdot(1-p)$；$D(X)=(1-p)^2p+(0-p)^2(1-p)=p(1-p)$

## 第 2 层　推导第 2 层

### R02 平方差
- 标志：$a^2-b^2=(a+b)(a-b)$
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$a^2-b^2=(a+b)(a-b)$
- 注释：
  - 同见不等式大厦 P03、P25
  - 配合：分母有理化〔P44〕、共轭〔R23〕
  - 看到两个平方相减，或“和×差” → 平方差
- 依赖：
  - 来源：R01
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】「多项式乘法」$(a+b)(a-b)=a^2-ab+ab-b^2$
      2. 【合并】交叉项 $-ab+ab$ 抵消：$a^2-ab+ab-b^2=a^2-b^2$

### R03 完全平方
- 标志：$(a\pm b)^2=a^2\pm 2ab+b^2$
- 区域：代数
- 类型：结论
- 重要度：2
- 是什么：$(a\pm b)^2=a^2\pm 2ab+b^2$
- 注释：
  - 同见不等式大厦 R37、R49
  - 配合：配方〔P01〕、$(\sin\alpha\pm\cos\alpha)^2$〔R38〕
  - 看到 $a^2\pm 2ab+b^2$ 三项 → 写成完全平方
- 依赖：
  - 来源：R01
    种类：推出
    方法：代换
    步骤：
      1. 【展开】「多项式乘法」$(a+b)^2=(a+b)(a+b)=a^2+ab+ab+b^2$
      2. 【合并】两个交叉项合并成 $2ab$：$=a^2+2ab+b^2$
      3. 【代换】$b\to -b$：$(a-b)^2=a^2-2ab+b^2$

### R04 三数和的平方
- 标志：$(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$
- 区域：代数
- 类型：中间步
- 是什么：$(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$
- 注释：
  - 同见不等式大厦 R64
- 依赖：
  - 来源：R01
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】「多项式乘法」$(a+b+c)^2=(a+b+c)(a+b+c)$，每项乘每项共 9 项
      2. 【合并】平方项 3 个；$ab$、$bc$、$ca$ 各出现 2 次：$=a^2+b^2+c^2+2ab+2bc+2ca$

### R06 立方和（差）
- 标志：$a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$
- 注释：
  - 同见不等式大厦 P27、R25
  - 高次式分解
  - 看到两个立方相加减 → 立方公式
- 依赖：
  - 来源：R01
    种类：推出
    方法：代换
    步骤：
      1. 【展开】右边 $(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3$
      2. 【合并】中间项抵消：$=a^3+b^3$
      3. 【代换】$b\to -b$：$a^3-b^3=(a-b)(a^2+ab+b^2)$

### R08 因式分解
- 标志：提公因式：分配律倒用
- 区域：代数
- 类型：中间步
- 是什么：公式法：平方差、完全平方、立方和（差）倒用；十字相乘：$acx^2+(ad+bc)x+bd=(ax+b)(cx+d)$；特例 $x^2+(p+q)x+pq=(x+p)(x+q)$：找两数乘得常数项、加得一次项系数；分组分解；顺序：一提、二套、三检查；十字相乘不行时，用求根公式〔P02〕求两根，写成交点式〔P04〕
- 注释：
  - 解一元二次、高次方程；不等式大厦 R25（穿根法）
  - 配合：约分〔P42〕
  - 看到二次式要拆开 → 先试十字相乘
- 依赖：
  - 来源：R01
    种类：推出
    方法：展开分解
    步骤：
      1. 【逆用】「多项式乘法」与乘法公式从右往左读：$ac+ad+bc+bd\Rightarrow(a+b)(c+d)$

### R09 $x^n-y^n$ 的分解
- 标志：$x^n-y^n=(x-y)(x^{n-1}+x^{n-2}y+\cdots+y^{n-1})$（$n$ 为正整数）
- 区域：代数
- 类型：中间步
- 标签：拓展
- 是什么：$n=2,3$ 即平方差、立方差
- 注释：
  - 高次式分解
  - 看到 $x^n-1$ → 提出 $x-1$
- 依赖：
  - 来源：R01
    种类：推出
    方法：作差相消
    步骤：
      1. 【展开】右边 $(x-y)(x^{n-1}+x^{n-2}y+\cdots+y^{n-1})=(x^n+x^{n-1}y+\cdots+xy^{n-1})-(x^{n-1}y+\cdots+xy^{n-1}+y^n)$
      2. 【相减】相邻项错位抵消，只剩 $x^n-y^n$

### R10 三元立方和
- 标志：$a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$
- 区域：代数
- 类型：中间步
- 标签：拓展
- 是什么：$=\dfrac{1}{2}(a+b+c)\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$；推论：$a+b+c=0\Rightarrow a^3+b^3+c^3=3abc$
- 注释：
  - 已知 $a+b+c=0$ 的求值
  - 看到 $a+b+c=0$ 和立方和 → 等于 $3abc$
- 依赖：
  - 来源：R01
    种类：推出
    方法：配凑
    步骤：
      1. 【展开】右边 $(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$，中间项抵消 $\Rightarrow a^3+b^3+c^3-3abc$
      2. 【配方】「完全平方」$a^2+b^2+c^2-ab-bc-ca=\dfrac{1}{2}\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$

### R11 拉格朗日恒等式
- 标志：$(a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2$
- 区域：代数
- 类型：中间步
- 标签：拓展
- 是什么：$(a^2+b^2)(c^2+d^2)=(ac+bd)^2+(ad-bc)^2$
- 注释：
  - 同见不等式大厦 R66：由 $(ad-bc)^2\ge 0$ 得柯西不等式
  - 同源：模的乘法 $|z_1z_2|=|z_1||z_2|$〔R25〕
  - 不等式大厦 R66（柯西不等式）
  - 看到两个平方和相乘 → 拆成两个平方和（柯西）
- 依赖：
  - 来源：R01
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】左边 $(a^2+b^2)(c^2+d^2)=a^2c^2+a^2d^2+b^2c^2+b^2d^2$
      2. 【展开】右边 $(ac+bd)^2+(ad-bc)^2=a^2c^2+2abcd+b^2d^2+a^2d^2-2abcd+b^2c^2$
      3. 【合并】交叉项 $+2abcd$、$-2abcd$ 抵消：两边都是 $a^2c^2+a^2d^2+b^2c^2+b^2d^2$

### P41 整数指数幂运算律
- 标志：$a^m\div a^n=a^{m-n}$，$\left(\dfrac{a}{b}\right)^n=\dfrac{a^n}{b^n}$
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域$a\ne 0,\ b\ne 0$
- 是什么：$m,n$ 为整数时，正整数指数的三条运算律仍成立
- 反例：
  - $a=0$：$0^{-1}$ 无意义
- 注释：
  - 看到负指数、零指数 → $a^{-n}=\dfrac{1}{a^n}$，$a^0=1$
- 依赖：
  - 来源：R12
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$a\ne 0,\ b\ne 0$
    步骤：
      1. 【代入】「零指数、负指数的定义」$a^m\div a^n=a^m\cdot\dfrac{1}{a^n}=a^m\cdot a^{-n}$
      2. 【合并】$a^m\cdot a^{-n}=a^{m-n}$（正整数指数的运算律照样成立）
  - 来源：S02
    种类：前提
    步骤：
      1. 【前提】$a^0=1$，$a^{-n}=\dfrac{1}{a^n}$

### P10 指数函数与对数函数互为反函数
- 标志：$y=a^x$ 与 $y=\log_a x$ 的图像关于 $y=x$ 对称
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域$a>0,\ a\ne 1$
- 是什么：$\log_a(a^x)=x$（$x\in\mathbb{R}$），$a^{\log_a x}=x$（$x>0$）；特例：$e^x$ 与 $\ln x$
- 注释：
  - 互逆：指数式 ⟷ 对数式
  - 指数、对数函数的图像与性质
  - 指数式和对数式要互相转化 → 指对互化
- 依赖：
  - 来源：P06
    种类：推出
    方法：对称
    步骤：
      1. 【定义】指数式与对数式互化：$y=a^x\iff x=\log_a y$
      2. 【对称】交换 $x,y$：$y=\log_a x$，图像关于 $y=x$ 对称
  - 来源：P88
    种类：前提
    步骤：
      1. 【特例】指数函数与对数函数互为反函数

### P12 正切与余弦
- 标志：$1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$
- 区域：三角
- 类型：结论
- 条件：定义域$\cos\alpha\ne 0$
- 是什么：$1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$
- 注释：
  - 同见不等式大厦 P16
  - 已知 $\tan\alpha$ 求 $\cos^2\alpha$；不等式大厦 P16
  - 看到 $1+\tan^2\alpha$ 或 $\dfrac{1}{\cos^2\alpha}$ → 互化
- 依赖：
  - 来源：R13
    种类：推出
    方法：代换
    步骤：
      1. 【同除】$\sin^2\alpha+\cos^2\alpha=1$ 两边 $\div\cos^2\alpha\Rightarrow\dfrac{\sin^2\alpha}{\cos^2\alpha}+1=\dfrac{1}{\cos^2\alpha}$
      2. 【代换】$\dfrac{\sin^2\alpha}{\cos^2\alpha}=\tan^2\alpha\Rightarrow 1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$（「商数关系」）
  - 来源：P11
    种类：前提
    步骤：
      1. 【前提】$\dfrac{\sin\alpha}{\cos\alpha}=\tan\alpha$

### P13 tan 的诱导公式
- 标志：$\tan(\pi+\alpha)=\tan\alpha$，$\tan(-\alpha)=-\tan\alpha$，$\tan(\pi-\alpha)=-\tan\alpha$
- 区域：三角
- 类型：结论
- 条件：定义域两边的 tan 都有定义
- 是什么：$\tan\left(\dfrac{\pi}{2}-\alpha\right)=\dfrac{1}{\tan\alpha}$（$\alpha\ne\dfrac{k\pi}{2}$）
- 注释：
  - 含 tan 的化简求值
  - 看到 $\tan(\pi\pm\alpha)$ 等 → tan 的诱导公式
- 依赖：
  - 来源：R14
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：两边的 tan 都有定义
    步骤：
      1. 【相除】sin 式 $\div$ cos 式（「商数关系」）
      2. 【代入】如 $\tan(\pi+\alpha)=\dfrac{\sin(\pi+\alpha)}{\cos(\pi+\alpha)}=\dfrac{-\sin\alpha}{-\cos\alpha}=\tan\alpha$（「诱导公式②」）

### P47 弦化切（齐次式）
- 标志：$\dfrac{a\sin\alpha+b\cos\alpha}{c\sin\alpha+d\cos\alpha}=\dfrac{a\tan\alpha+b}{c\tan\alpha+d}$
- 区域：三角
- 类型：结论
- 条件：定义域$\cos\alpha\ne 0$，分母 $\ne 0$
- 是什么：$\sin\alpha\cos\alpha=\dfrac{\tan\alpha}{1+\tan^2\alpha}$，$\sin^2\alpha=\dfrac{\tan^2\alpha}{1+\tan^2\alpha}$
- 反例：
  - $\alpha=\dfrac{\pi}{2}$ 时 $\cos\alpha=0$，不能同除
- 注释：
  - 已知 $\tan\alpha$ 求 sin、cos 的齐次式 → 弦化切
- 依赖：
  - 来源：P11
    种类：推出
    方法：同除
    条件：▼ 加条件〔定义域〕：$\cos\alpha\ne 0$
    步骤：
      1. 【同除】一次式：分子、分母 $\div\cos\alpha\Rightarrow\dfrac{a\tan\alpha+b}{c\tan\alpha+d}$
      2. 【代换】二次式：先用“1”的代换 $1=\sin^2\alpha+\cos^2\alpha$，如 $\sin\alpha\cos\alpha=\dfrac{\sin\alpha\cos\alpha}{\sin^2\alpha+\cos^2\alpha}$
      3. 【同除】再 $\div\cos^2\alpha\Rightarrow\dfrac{\tan\alpha}{1+\tan^2\alpha}$；$\sin^2\alpha=\dfrac{\tan^2\alpha}{1+\tan^2\alpha}$ 同理
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】$1=\sin^2\alpha+\cos^2\alpha$
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】分子、分母同除非零式

### R15 数量积坐标式
- 标志：$\vec a=(x_1,y_1)$，$\vec b=(x_2,y_2)\Rightarrow\vec a\cdot\vec b=x_1x_2+y_1y_2$
- 区域：向量
- 类型：结论
- 重要度：2
- 是什么：$|\vec a|^2=x_1^2+y_1^2$
- 注释：
  - 同见不等式大厦 R16
  - 已知坐标求数量积 → 坐标式
- 依赖：
  - 来源：S05
    种类：推出
    方法：代换
    步骤：
      1. 【分解】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$
      2. 【展开】「分配律」$\vec a\cdot\vec b=x_1x_2\,\vec i\cdot\vec i+(x_1y_2+x_2y_1)\,\vec i\cdot\vec j+y_1y_2\,\vec j\cdot\vec j$
      3. 【代入】$\vec i\cdot\vec i=\vec j\cdot\vec j=1$，$\vec i\cdot\vec j=0\Rightarrow\vec a\cdot\vec b=x_1x_2+y_1y_2$
  - 来源：R01
    种类：前提
    步骤：
      1. 【前提】与多项式乘法同样逐项展开

### P19 三角形内角关系
- 标志：$\sin(A+B)=\sin C$，$\cos(A+B)=-\cos C$
- 区域：向量
- 类型：结论
- 条件：结构前提$A+B+C=\pi$
- 是什么：$\sin\dfrac{A+B}{2}=\cos\dfrac{C}{2}$；$\cos\dfrac{A+B}{2}=\sin\dfrac{C}{2}$；$\tan(A+B)=-\tan C$（$C\ne\dfrac{\pi}{2}$）；教材例题：$\sin A+\sin B+\sin C=4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\cos\dfrac{C}{2}$（和差化积 + $\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$）
- 注释：
  - 三角形中的化简
  - 三角形中出现 $A+B$ → 换成 $\pi-C$
- 依赖：
  - 来源：R14
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：$A+B+C=\pi$
    步骤：
      1. 【代换】$A+B=\pi-C$：$\sin(A+B)=\sin C$，$\cos(A+B)=-\cos C$（「诱导公式④」）
      2. 【相除】$\tan(A+B)=-\tan C$（$C\ne\dfrac{\pi}{2}$）
      3. 【代换】$\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$：$\sin\dfrac{A+B}{2}=\cos\dfrac{C}{2}$，$\cos\dfrac{A+B}{2}=\sin\dfrac{C}{2}$（「诱导公式⑤」）

### P20 三角形面积
- 标志：$S=\dfrac{1}{2}ab\sin C=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B$
- 区域：向量
- 类型：结论
- 条件：结构前提$a,b$ 夹角 $C$
- 是什么：拓展：$\overrightarrow{OA}=(x_1,y_1)$，$\overrightarrow{OB}=(x_2,y_2)$：$S_{\triangle OAB}=\dfrac{1}{2}|x_1y_2-x_2y_1|$（必修三拓展阅读）
- 反例：
  - 直角边 $a=b=1$、$C=90^\circ$：$S=\dfrac{1}{2}$；误用非夹角 $A=45^\circ$ 得 $\dfrac{\sqrt{2}}{4}$
- 注释：
  - 求三角形面积 → $\dfrac{1}{2}ab\sin C$
- 依赖：
  - 来源：S04
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：$a,b$ 夹角 $C$
    步骤：
      1. 【定义】以 $a$ 为底，高 $h=b\sin C\Rightarrow S=\dfrac{1}{2}ah=\dfrac{1}{2}ab\sin C$（「三角函数定义」）
      2. 【代换】$C$ 为钝角：$h=b\sin(\pi-C)=b\sin C$（「诱导公式④」）
  - 来源：R14
    种类：前提
    步骤：
      1. 【前提】诱导公式 ④
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】面积 $=\dfrac{1}{2}\times$ 底 $\times$ 高

### R22 复数乘法
- 标志：$(a+bi)(c+di)=(ac-bd)+(ad+bc)i$
- 区域：复数
- 类型：中间步
- 是什么：$(a+bi)(c+di)=(ac-bd)+(ad+bc)i$
- 注释：
  - 复数相乘 → 展开，用 $i^2=-1$
- 依赖：
  - 来源：S06
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】$(a+bi)(c+di)=ac+adi+bci+bdi^2$
      2. 【代入】$i^2=-1\Rightarrow ac+adi+bci-bd$
      3. 【合并】实部 $ac-bd$、虚部 $ad+bc\Rightarrow(ac-bd)+(ad+bc)i$
  - 来源：R01
    种类：前提
    步骤：
      1. 【前提】多项式乘法展开

### R24 $i^n$ 以 4 为周期
- 标志：$i^1=i$，$i^2=-1$，$i^3=-i$，$i^4=1$；$i^{n+4}=i^n$
- 区域：复数
- 类型：中间步
- 是什么：复数乘方：$z^mz^n=z^{m+n}$，$(z^m)^n=z^{mn}$，$(z_1z_2)^n=z_1^nz_2^n$；$z\ne 0$ 时 $z^0=1$，$z^{-n}=\dfrac{1}{z^n}$；$(1+i)^2=2i$，$(1-i)^2=-2i$，$\dfrac{1+i}{1-i}=i$（教材例题）
- 注释：
  - 复数的高次幂
  - 看到 $i$ 的高次幂 → 指数除以 4 看余数
- 依赖：
  - 来源：S06
    种类：推出
    方法：展开分解
    步骤：
      1. 【相乘】由 $i^2=-1$ 依次乘 $i$：$i^3=i^2\cdot i=-i$
      2. 【代入】$i^4=(i^2)^2=(-1)^2=1$
      3. 【相乘】$i^{n+4}=i^n\cdot i^4=i^n$：4 个一循环
  - 来源：R12
    种类：前提
    步骤：
      1. 【前提】指数运算律

### P50 累加法、累乘法（求通项）
- 标志：$a_{n+1}-a_n=f(n)\Rightarrow a_n=a_1+\displaystyle\sum_{k=1}^{n-1}f(k)$
- 区域：数列
- 类型：结论
- 重要度：2
- 条件：定义域$n\ge 2$，$n=1$ 单独验证
- 是什么：$\dfrac{a_{n+1}}{a_n}=g(n)\Rightarrow a_n=a_1\displaystyle\prod_{k=1}^{n-1}g(k)$（$a_n\ne 0$）；等差、等比的通项是 $f(n)=d$、$g(n)=q$ 的特例
- 注释：
  - 看到 $a_{n+1}-a_n=f(n)$ → 累加；$\dfrac{a_{n+1}}{a_n}=g(n)$ → 累乘
- 依赖：
  - 来源：R28
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔定义域〕：$n\ge 2$
    步骤：
      1. 【累加】$a_2-a_1=f(1)$，…，$a_n-a_{n-1}=f(n-1)$，$n-1$ 个式子相加，中间项抵消 $\Rightarrow a_n=a_1+\sum_{k=1}^{n-1}f(k)$（「累加相消」）
      2. 【累乘】$\dfrac{a_2}{a_1}\cdot\dfrac{a_3}{a_2}\cdots\dfrac{a_n}{a_{n-1}}=\prod_{k=1}^{n-1}g(k)$，中间项约掉 $\Rightarrow a_n=a_1\prod_{k=1}^{n-1}g(k)$

### R30 裂项
- 标志：$\dfrac{1}{k(k+1)}=\dfrac{1}{k}-\dfrac{1}{k+1}$（$k$ 为正整数）
- 区域：数列
- 类型：结论
- 重要度：1
- 是什么：$\displaystyle\sum_{k=1}^{n}\dfrac{1}{k(k+1)}=1-\dfrac{1}{n+1}$
- 注释：
  - 同见不等式大厦 P24
  - 配合：累加相消〔R28〕
  - 通项是 $\dfrac{1}{k(k+1)}$ → 裂项相消
- 依赖：
  - 来源：R28
    种类：推出
    方法：作差相消
    步骤：
      1. 【通分】$\dfrac{1}{k}-\dfrac{1}{k+1}=\dfrac{(k+1)-k}{k(k+1)}=\dfrac{1}{k(k+1)}$
      2. 【累加】$\displaystyle\sum_{k=1}^{n}\left(\dfrac{1}{k}-\dfrac{1}{k+1}\right)=1-\dfrac{1}{n+1}$（「累加相消」）
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】通分

### P34 组合数
- 标志：$C_n^m=\dfrac{A_n^m}{m!}=\dfrac{n!}{m!(n-m)!}$
- 区域：计数
- 类型：结论
- 重要度：2
- 条件：定义域$0\le m\le n$
- 是什么：$C_n^m=\dfrac{A_n^m}{m!}=\dfrac{n!}{m!(n-m)!}$
- 注释：
  - 只选不排（无序）→ 组合数
- 依赖：
  - 来源：P33
    种类：推出
    方法：同除
    步骤：
      1. 【分步计数】先选 $m$ 个再排列：$A_n^m=C_n^m\cdot m!$（「分步乘法原理」）
      2. 【同除】$C_n^m=\dfrac{A_n^m}{m!}$

### P38 商的求导法则
- 标志：$\left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^2}$（同时得出 $\dfrac{u}{v}$ 可导）
- 区域：导数
- 类型：结论
- 重要度：1
- 条件：定义域$u,v$ 可导，$v(x)\ne 0$
- 是什么：特例：$\left(\dfrac{1}{g}\right)'=-\dfrac{g'}{g^2}$
- 反例：
  - $v(x)=0$ 时 $\dfrac{u}{v}$ 在该点无定义
- 注释：
  - 不等式大厦 P05（构造函数判单调）；切线、单调性、极值
  - 看到分式函数 → 商法则
- 依赖：
  - 来源：S08
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕：$v(x)\ne 0$
    步骤：
      1. 【通分】【配凑】差商 $=\dfrac{\frac{u(x+\Delta x)-u(x)}{\Delta x}v(x)-u(x)\frac{v(x+\Delta x)-v(x)}{\Delta x}}{v(x+\Delta x)v(x)}$
      2. 【取极限】$v$ 连续且 $v(x)\ne 0$：$\Delta x$ 足够小时 $v(x+\Delta x)\ne 0$；令 $\Delta x\to 0$
  - 来源：P37
    种类：前提
    步骤：
      1. 【前提】$u,v$ 可导，配凑手法同积法则
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】分式化简（分母 $\ne 0$）

### P59 余数定理与因式定理
- 标志：$f(x)$ 除以 $x-a$ 的余数等于 $f(a)$
- 区域：代数
- 类型：结论
- 标签：拓展
- 条件：结构前提$f(x)$ 是多项式
- 是什么：因式定理：$f(a)=0\iff x-a$ 是 $f(x)$ 的因式；例：$f(x)=x^3-6x^2+11x-6$，$f(1)=0\Rightarrow f(x)=(x-1)(x^2-5x+6)$
- 注释：
  - 高次式分解 → 试根，$f(a)=0$ 就提出 $x-a$
- 依赖：
  - 来源：R01
    种类：推出
    方法：特例
    条件：▼ 加条件〔结构前提〕：$f(x)$ 是多项式
    步骤：
      1. 【设】「带余除法」$f(x)=(x-a)q(x)+r$
      2. 【赋值】令 $x=a$：$f(a)=0\cdot q(a)+r\Rightarrow r=f(a)$

### P56 平面向量基本定理与三点共线
- 标志：$\vec e_1,\vec e_2$ 不共线 $\Rightarrow$ 平面内任一 $\vec a=\lambda_1\vec e_1+\lambda_2\vec e_2$，且 $\lambda_1,\lambda_2$ 唯一（课本给出）
- 区域：向量
- 类型：结论
- 重要度：1
- 条件：结构前提$\vec e_1,\vec e_2$ 不共线；$A,B$ 不重合
- 是什么：唯一 $\Rightarrow$ 对应系数相等：$\lambda_1\vec e_1+\lambda_2\vec e_2=\mu_1\vec e_1+\mu_2\vec e_2\Rightarrow\lambda_1=\mu_1$，$\lambda_2=\mu_2$；$P$ 在直线 $AB$ 上 $\iff\overrightarrow{OP}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}$（系数和为 1，$O$ 任取）；拓展（老教材）：定比分点 $\overrightarrow{AP}=\lambda\overrightarrow{PB}$（$\lambda\ne -1$）$\Rightarrow x=\dfrac{x_1+\lambda x_2}{1+\lambda}$，$y=\dfrac{y_1+\lambda y_2}{1+\lambda}$
- 反例：
  - $\vec e_1=(1,0)$，$\vec e_2=(2,0)$ 共线：$(0,1)$ 无法用它们表示
- 注释：
  - 图形中用两个不共线向量表示其他向量 → 选基底；三点共线 → 系数和为 1
- 依赖：
  - 来源：S21
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：基底不共线
    步骤：
      1. 【代换】「共线」$\overrightarrow{AP}=t\overrightarrow{AB}\Rightarrow\overrightarrow{OP}-\overrightarrow{OA}=t(\overrightarrow{OB}-\overrightarrow{OA})$
      2. 【移项】$\overrightarrow{OP}=(1-t)\overrightarrow{OA}+t\overrightarrow{OB}$
  - 来源：R41
    种类：前提
    步骤：
      1. 【前提】向量的加减与数乘

### P62 对称轴与对称中心
- 标志：$f(a+x)=f(a-x)\iff$ 图像关于直线 $x=a$ 对称；一般 $f(a+x)=f(b-x)$：对称轴 $x=\dfrac{a+b}{2}$
- 区域：函数性质
- 类型：结论
- 重要度：2
- 条件：结构前提关系式对定义域内每个 $x$ 都成立
- 是什么：$f(a+x)+f(a-x)=2b\iff$ 图像关于点 $(a,b)$ 对称；偶函数、奇函数是 $a=0$（$b=0$）的特例
- 反例：
  - $y=f(1+x)$ 与 $y=f(1-x)$ 是两个函数，它们的图像关于直线 $x=0$ 对称，不是 $x=1$
- 注释：
  - 看到 $f(a+x)=f(b-x)$ → 对称轴取中点 $x=\dfrac{a+b}{2}$
- 依赖：
  - 来源：P61
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：关系式对每个 $x$ 成立
    步骤：
      1. 【平移】令 $g(x)=f(x+a)$：$g$ 为偶函数 $\iff g(-x)=g(x)\iff f(a+x)=f(a-x)$
      2. 【平移】令 $g(x)=f(x+a)-b$：$g$ 为奇函数 $\iff f(a-x)-b=-[f(a+x)-b]\iff f(a+x)+f(a-x)=2b$

### R47 概率的加法公式、对立事件
- 标志：对立事件：$P(\bar A)=1-P(A)$
- 区域：概率统计
- 类型：结论
- 重要度：2
- 是什么：一般：$P(A\cup B)=P(A)+P(B)-P(A\cap B)$（必修二 5.3 探究题；B 版记作 $P(A+B)$、$P(AB)$）
- 反例：
  - 掷骰子，$A$=偶数点，$B$=点数 $\le 3$：$P(A)+P(B)=1$，但 $A,B$ 不对立，$P(A\cup B)=\dfrac{5}{6}$
- 注释：
  - 同源：容斥原理〔R40〕
  - “至少一个”“不都是” → 先算对立事件，再用 1 减
- 依赖：
  - 来源：S19
    种类：推出
    方法：分类讨论
    步骤：
      1. 【分解】$A\cup B=A\cup(\bar AB)$，$B=AB\cup(\bar AB)$，均为互斥并
      2. 【相减】两式用「互斥加法」后相减：$P(A\cup B)=P(A)+P(B)-P(A\cap B)$
      3. 【特例】对立：$A\cup\bar A=\Omega$，$P(A)+P(\bar A)=1$
  - 来源：R40
    种类：前提
    步骤：
      1. 【前提】与容斥原理同型：重叠部分减一次

### P94 有重复排列与不尽相异元素的全排列
- 标志：有重复排列：$n$ 种元素每次可重复取，排成 $m$ 位：$n^m$
- 区域：计数
- 类型：结论
- 标签：拓展
- 条件：定义域$n_1+n_2+\cdots+n_k=n$
- 是什么：不尽相异全排列：$n$ 个元素中有 $n_1$ 个相同、$n_2$ 个相同……：$\dfrac{n!}{n_1!\,n_2!\cdots n_k!}$
- 反例：
  - 3 封信投 4 个信箱是 $4^3=64$，不是 $3^4$：每封信选信箱，信是“步”
- 注释：
  - 可重复选 → $n^m$（看谁是“步”）；有相同元素的全排列 → 除以相同元素的阶乘
- 依赖：
  - 来源：S07
    种类：推出
    方法：分类讨论
    条件：▼ 加条件〔定义域〕：个数之和为 $n$
    步骤：
      1. 【分步计数】每一位 $n$ 种，共 $m$ 步（「分步乘法原理」）
  - 来源：P33
    种类：前提
    步骤：
      1. 【前提】全排列 $n!$ 中，相同元素互换不产生新排列，除以 $n_1!\cdots n_k!$

### P98 极坐标与参数方程
- 标志：互化：$x=\rho\cos\theta$，$y=\rho\sin\theta$；$\rho^2=x^2+y^2$
- 区域：解析几何
- 类型：结论
- 标签：拓展
- 条件：定义域$\rho\ge 0$；化直角坐标时 $x\ne 0$ 才用 $\tan\theta=\dfrac{y}{x}$
- 是什么：圆 $x=a+r\cos\theta$，$y=b+r\sin\theta$；椭圆 $x=a\cos\varphi$，$y=b\sin\varphi$；直线 $x=x_0+t\cos\alpha$，$y=y_0+t\sin\alpha$：$|t|$ 是到 $(x_0,y_0)$ 的距离；消参：用 $\sin^2\theta+\cos^2\theta=1$ 或代入消元
- 注释：
  - 椭圆、圆上的点求最值 → 设参数 $(a\cos\varphi,\ b\sin\varphi)$，化成辅助角
- 依赖：
  - 来源：S04
    种类：推出
    方法：代换
    步骤：
      1. 【代入】「三角函数定义」$\cos\theta=\dfrac{x}{\rho}$，$\sin\theta=\dfrac{y}{\rho}$：$x=\rho\cos\theta$，$y=\rho\sin\theta$
      2. 【定义】「单位圆」上的点是 $(\cos\theta,\sin\theta)$
      3. 【伸缩】横、纵坐标都乘 $r$：$(r\cos\theta,r\sin\theta)$；横乘 $a$、纵乘 $b$：$x=a\cos\varphi$，$y=b\sin\varphi$（椭圆）
      4. 【平移】$(r\cos\theta,r\sin\theta)$ 平移到圆心 $(a,b)$：$x=a+r\cos\theta$，$y=b+r\sin\theta$（圆）
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】消参用 $\sin^2\theta+\cos^2\theta=1$

## 第 3 层　推导第 3 层

### P01 配方
- 标志：$ax^2+bx+c=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$
- 区域：代数
- 类型：结论
- 重要度：2
- 条件：定义域$a\ne 0$
- 是什么：$ax^2+bx+c=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$
- 反例：
  - $a=0$ 时 $\dfrac{b}{2a}$ 无意义
- 注释：
  - 同见不等式大厦 R17；同见二次函数大厦 R01
  - 求二次式的最值；不等式大厦 R23
  - 看到求二次式的最值、值域 → 配方
- 依赖：
  - 来源：R03
    种类：推出
    方法：配凑
    条件：▼ 加条件〔定义域〕：$a\ne 0$
    步骤：
      1. 【提取】$ax^2+bx+c\Rightarrow a\left(x^2+\dfrac{b}{a}x\right)+c$
      2. 【配方】「完全平方」补上 $\left(\dfrac{b}{2a}\right)^2$ 再减去：$a\left[\left(x+\dfrac{b}{2a}\right)^2-\dfrac{b^2}{4a^2}\right]+c$
      3. 【合并】$=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$

### P05 实数指数运算律
- 标志：$a^ra^s=a^{r+s}$，$(a^r)^s=a^{rs}$，$(ab)^r=a^rb^r$，$\dfrac{a^r}{a^s}=a^{r-s}$（$r,s\in\mathbb{R}$）
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域$a>0,\ b>0$
- 是什么：$a^ra^s=a^{r+s}$，$(a^r)^s=a^{rs}$，$(ab)^r=a^rb^r$，$\dfrac{a^r}{a^s}=a^{r-s}$（$r,s\in\mathbb{R}$）
- 反例：
  - 若允许负底数：$(-8)^{\frac{2}{6}}=\sqrt[6]{64}=2$，而 $(-8)^{\frac{1}{3}}=-2$，同一个数得出两个值
- 注释：
  - 看到分数、实数指数 → 先化成同底（底数 $>0$），再用指数运算律
- 依赖：
  - 来源：P41
    种类：推出
    方法：特例
    条件：▼ 加条件〔定义域〕：$a>0,\ b>0$
    步骤：
      1. 【推广】由整数指数推广到有理、实数指数（课本说明运算律仍成立）

### R16 两角差的余弦
- 标志：$\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
- 区域：三角
- 类型：结论
- 重要度：3
- 是什么：$\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
- 注释：
  - 看到两角差的余弦，或能把角拆成已知角的差 → 两角差余弦
- 依赖：
  - 来源：R15
    种类：推出
    方法：数形结合
    步骤：
      1. 【设】$\overrightarrow{OA}=(\cos\alpha,\sin\alpha)$，$\overrightarrow{OB}=(\cos\beta,\sin\beta)$（单位向量）
      2. 【代入】「数量积坐标式」$\overrightarrow{OA}\cdot\overrightarrow{OB}=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
      3. 【定义】「数量积定义」$\overrightarrow{OA}\cdot\overrightarrow{OB}=1\cdot 1\cdot\cos\theta=\cos\theta$（$\theta$ 为夹角）
      4. 【代换】$\alpha-\beta=\pm\theta+2k\pi\Rightarrow\cos(\alpha-\beta)=\cos\theta$（「诱导公式①③」）
  - 来源：R14
    种类：前提
    步骤：
      1. 【前提】$\alpha-\beta=\pm\theta+2k\pi$，由 ①③ 得 $\cos(\alpha-\beta)=\cos\theta$
  - 来源：S04
    种类：前提
    步骤：
      1. 【前提】单位圆上的点 $(\cos\alpha,\sin\alpha)$

### P21 正弦定理
- 标志：$\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$（$R$ 为外接圆半径；“$=2R$”是教材探索题）
- 区域：向量
- 类型：结论
- 重要度：2
- 条件：结构前提同一三角形的边与对角
- 是什么：推论：$a=2R\sin A$，$a:b:c=\sin A:\sin B:\sin C$（边角互化）；推论：$a>b\iff A>B\iff\sin A>\sin B$（大边对大角）；拓展：$S=\dfrac{abc}{4R}$
- 反例：
  - $a=2$，$b=1$，$A=B=60^\circ$ 不来自同一三角形：$\dfrac{a}{\sin A}\ne\dfrac{b}{\sin B}$
- 注释：
  - 不等式大厦 R13（三角形中求最值）
  - 配合：余弦定理〔P22〕做边角互化
  - 已知两角一边，或边角混在一起（各项中边的次数相同）→ 正弦定理边角互化
- 依赖：
  - 来源：P20
    种类：推出
    方法：补形
    步骤：
      1. 【同除】$\dfrac{1}{2}ab\sin C=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B$ 同除 $\dfrac{1}{2}abc\Rightarrow\dfrac{\sin C}{c}=\dfrac{\sin A}{a}=\dfrac{\sin B}{b}$
      2. 【取倒数】$\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}$
      3. 【补形】$=2R$：作直径 $BD$，$\angle BCD=90^\circ$，$\angle BDC$ 与 $A$ 相等或互补（「圆周角定理」）
      4. 【定义】$a=BD\sin\angle BDC=2R\sin\angle BDC=2R\sin A$（「诱导公式④」）
      5. 【特例】$A=90^\circ$：$BC$ 就是直径，$a=2R$ 直接成立
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】圆周角定理：$\angle BDC$ 与 $A$ 相等或互补

### P49 数量积的运算公式
- 标志：$|\vec a\pm\vec b|^2=|\vec a|^2\pm 2\vec a\cdot\vec b+|\vec b|^2$；$(\vec a+\vec b)\cdot(\vec a-\vec b)=|\vec a|^2-|\vec b|^2$
- 区域：向量
- 类型：结论
- 重要度：2
- 条件：定义域夹角公式要求 $\vec a,\vec b\ne\vec 0$
- 是什么：$\vec a\perp\vec b\iff\vec a\cdot\vec b=0$（规定零向量与任意向量垂直）；$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；坐标：$\vec a\parallel\vec b\iff x_1y_2-x_2y_1=0$；$\vec a\perp\vec b\iff x_1x_2+y_1y_2=0$；$\cos\theta=\dfrac{x_1x_2+y_1y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}$
- 反例：
  - $\vec b=\vec 0$ 时夹角无定义，$\cos\theta$ 的分母为 0
- 注释：
  - 同见不等式大厦 R16、R27
  - 解析几何中的垂直、夹角
  - 同源：完全平方〔R03〕、平方差〔R02〕
  - 模 → 平方；夹角 → $\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；垂直 → $\vec a\cdot\vec b=0$
- 依赖：
  - 来源：S05
    种类：推出
    方法：数形结合
    条件：▼ 加条件〔定义域〕：夹角公式要求非零向量
    步骤：
      1. 【展开】「分配律」$|\vec a\pm\vec b|^2=(\vec a\pm\vec b)\cdot(\vec a\pm\vec b)$，$(\vec a+\vec b)\cdot(\vec a-\vec b)$，与「完全平方」「平方差」同型
      2. 【定义】垂直、夹角：由「数量积定义」变形，$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$
  - 来源：R15
    种类：前提
    步骤：
      1. 【前提】坐标运算

### R23 共轭与模
- 标志：$z\bar z=|z|^2=a^2+b^2$；$z+\bar z=2a$，$z-\bar z=2bi$
- 区域：复数
- 类型：结论
- 重要度：1
- 是什么：$\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$，$\overline{z_1z_2}=\bar z_1\bar z_2$，$\overline{\left(\dfrac{z_1}{z_2}\right)}=\dfrac{\bar z_1}{\bar z_2}$；$z\ne 0$ 时 $\dfrac{1}{z}=\dfrac{\bar z}{|z|^2}$
- 注释：
  - 求 $|z|$、$z\bar z$ → 共轭相乘
- 依赖：
  - 来源：R22
    种类：推出
    方法：作差相消
    步骤：
      1. 【展开】$z\bar z=(a+bi)(a-bi)=a^2-(bi)^2=a^2+b^2$（「平方差」）
      2. 【代换】$a^2+b^2=|z|^2\Rightarrow z\bar z=|z|^2$
      3. 【相加】$z+\bar z=2a$
      4. 【相减】$z-\bar z=2bi$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】与平方差同型

### P26 等差通项
- 标志：$a_n=a_1+(n-1)d$，$a_n=a_m+(n-m)d$
- 区域：数列
- 类型：结论
- 重要度：1
- 条件：结构前提等差数列
- 是什么：$d=\dfrac{a_n-a_m}{n-m}$（$n\ne m$）：点 $(n,a_n)$ 连线的斜率；$\{a_n\}$ 等差 $\iff a_n=kn+b$（$k=d$）
- 注释：
  - 已知等差数列的两项 → $a_n=a_m+(n-m)d$ 求公差
- 依赖：
  - 来源：S09
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：等差数列
    步骤：
      1. 【定义】「等差定义」$a_2-a_1=d$，…，$a_n-a_{n-1}=d$
      2. 【累加】$(n-1)$ 个 $d$ 相加 $\Rightarrow a_n-a_1=(n-1)d$
      3. 【移项】$a_n=a_1+(n-1)d$
  - 来源：P50
    种类：前提
    步骤：
      1. 【特例】$f(n)=d$

### P29 等比通项
- 标志：$a_n=a_1q^{n-1}$
- 区域：数列
- 类型：结论
- 重要度：1
- 条件：结构前提等比数列
- 是什么：$a_n=a_mq^{n-m}$（$n<m$ 时用整数指数）；$\{a_n\}$ 等比 $\iff a_n=kq^n$（$k,q$ 为非零常数）；$a_n>0$ 时 $\{\lg a_n\}$ 是等差数列（公差 $\lg q$）
- 注释：
  - 已知等比数列的两项 → $a_n=a_mq^{n-m}$ 求公比
- 依赖：
  - 来源：S09
    种类：推出
    方法：同除
    条件：▼ 加条件〔结构前提〕：等比数列
    步骤：
      1. 【定义】「等比定义」$\dfrac{a_2}{a_1}=q$，…，$\dfrac{a_n}{a_{n-1}}=q$
      2. 【累乘】$(n-1)$ 个 $q$ 相乘 $\Rightarrow\dfrac{a_n}{a_1}=q^{n-1}$
      3. 【同乘】$a_n=a_1q^{n-1}$
  - 来源：P50
    种类：前提
    步骤：
      1. 【特例】$g(n)=q$
  - 来源：P41
    种类：前提
    步骤：
      1. 【前提】$q^0=1$，$q\cdot q^{n-2}=q^{n-1}$

### P35 组合数性质
- 标志：$C_n^m=C_n^{n-m}$（$0\le m\le n$）
- 区域：计数
- 类型：结论
- 条件：定义域下标范围见各式
- 是什么：$C_{n+1}^m=C_n^m+C_n^{m-1}$（$1\le m\le n$，杨辉三角的递推）
- 注释：
  - 组合数化简、证明
  - 组合数化简 → 对称性、杨辉三角递推
- 依赖：
  - 来源：P34
    种类：推出
    方法：分类讨论
    步骤：
      1. 【对称】选出 $m$ 个 ⟺ 留下 $n-m$ 个：$C_n^m=C_n^{n-m}$
      2. 【分类计数】某个指定元素选或不选：$C_{n+1}^m=C_n^m+C_n^{m-1}$（「分类加法原理」）

### R33 二项式定理
- 标志：$(a+b)^n=\displaystyle\sum_{k=0}^{n}C_n^k a^{n-k}b^k$（$n$ 为正整数）
- 区域：计数
- 类型：结论
- 重要度：3
- 是什么：通项 $T_{k+1}=C_n^k a^{n-k}b^k$
- 注释：
  - 同见不等式大厦 P26（伯努利不等式）
  - 配合：区分二项式系数〔R34〕与项的系数〔R39〕
  - 看到 $(a+b)^n$ 展开、求某一项 → 通项 $T_{k+1}$
- 依赖：
  - 来源：P34
    种类：推出
    方法：分类讨论
    步骤：
      1. 【展开】$n$ 个 $(a+b)$ 相乘，每个括号选 $a$ 或 $b$（「分步乘法原理」）
      2. 【分类计数】恰好选 $k$ 个 $b$ 有 $C_n^k$ 种，得项 $C_n^ka^{n-k}b^k$
  - 来源：R01
    种类：前提
    步骤：
      1. 【前提】多项式乘法逐项展开

### P36 组合数的提取
- 标志：$kC_n^k=nC_{n-1}^{k-1}$
- 区域：计数
- 类型：结论
- 标签：拓展
- 条件：定义域$1\le k\le n$
- 是什么：$kC_n^k=nC_{n-1}^{k-1}$
- 注释：
  - 组合数求和
  - 看到 $kC_n^k$ → 提取成 $nC_{n-1}^{k-1}$
- 依赖：
  - 来源：P34
    种类：推出
    方法：分类讨论
    步骤：
      1. 【代入】$kC_n^k=k\cdot\dfrac{n!}{k!(n-k)!}=n\cdot\dfrac{(n-1)!}{(k-1)!(n-k)!}=nC_{n-1}^{k-1}$
      2. 【分步计数】（另一路）选 $k$ 人委员会再选主席 $=$ 先选主席再选其余 $k-1$ 人

### P39 $(\ln x)'$ 的由来
- 标志：$(\ln x)'=\dfrac{1}{x}$
- 区域：导数
- 类型：结论
- 标签：拓展
- 条件：定义域$x>0$
- 是什么：$(\ln x)'=\dfrac{1}{x}$
- 依赖：
  - 来源：P10
    种类：推出
    方法：代换
    步骤：
      1. 【求导】对 $\ln(e^x)=x$ 两边求导：$(\ln)'(e^x)\cdot e^x=1$（「链式法则」）
      2. 【代换】令 $u=e^x$：$(\ln u)'=\dfrac{1}{u}$，$u$ 取遍 $(0,+\infty)$
  - 来源：S12
    种类：前提
    步骤：
      1. 【前提】链式法则；$\ln x$ 可导由导数表给出

### P55 常用导数
- 标志：$\left(\dfrac{1}{x}\right)'=-\dfrac{1}{x^2}$（$x\ne 0$）；$(\sqrt{x})'=\dfrac{1}{2\sqrt{x}}$（$x>0$）
- 区域：导数
- 类型：结论
- 重要度：1
- 条件：定义域各式括号内
- 是什么：$(e^{ax+b})'=ae^{ax+b}$；$[\ln(ax+b)]'=\dfrac{a}{ax+b}$（$ax+b>0$）；$(\tan x)'=\dfrac{1}{\cos^2x}$（$\cos x\ne 0$；教材例题：商法则 + $\sin^2x+\cos^2x=1$）
- 反例：
  - $(\sqrt{x})'$ 在 $x=0$ 处不存在
- 注释：
  - 看到 $\dfrac{1}{x}$、$\sqrt{x}$、$e^{ax+b}$、$\ln(ax+b)$ → 常用导数
- 依赖：
  - 来源：S12
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：各式括号内
    步骤：
      1. 【特例】$(x^\alpha)'$ 取 $\alpha=-1,\ \dfrac{1}{2}$
      2. 【代换】$u=ax+b$（「链式法则」）
  - 来源：P38
    种类：前提
    步骤：
      1. 【商法则】$\left(\dfrac{1}{x}\right)'=\dfrac{0\cdot x-1}{x^2}$，$x<0$ 时同样成立

### R43 恒等的多项式：系数对应相等（待定系数法）
- 标志：待定系数法本身是教材方法（必修一 3.1.1 例 7：过三点设 $y=ax^2+bx+c$）；“系数对应相等”这条定理教材没给，属拓展
- 区域：代数
- 类型：中间步
- 标签：拓展
- 是什么：$a_nx^n+\cdots+a_1x+a_0=b_nx^n+\cdots+b_1x+b_0$ 对一切 $x$ 成立 $\iff a_k=b_k$（$k=0,1,\cdots,n$）；例：$x^2+3x+5=(x+1)^2+m(x+1)+n$：展开比较得 $m=1$，$n=3$
- 反例：
  - 只对某个 $x$ 成立的等式不能比较系数：$x^2=x$ 在 $x=1$ 时成立，但两边系数不同
- 注释：
  - 同源：复数相等实部、虚部分别相等〔S06〕；平面向量基本定理的系数唯一〔P56〕
  - 两个多项式恒等、要求未知系数 → 展开后对应系数相等
- 依赖：
  - 来源：P59
    种类：推出
    方法：反证
    步骤：
      1. 【相减】两边之差 $(a_n-b_n)x^n+\cdots+(a_1-b_1)x+(a_0-b_0)$ 对一切 $x$ 为 $0$
      2. 【反证】若不是零多项式，最多有 $n$ 个根（每个根提出一个因式，「因式定理」），与“对一切 $x$ 成立”矛盾 $\Rightarrow a_k=b_k$
  - 来源：R01
    种类：前提
    步骤：
      1. 【前提】展开后合并同类项

### P63 周期的常用判定
- 标志：$f(x+a)=-f(x)\Rightarrow T=2a$；$f(x+a)=\dfrac{1}{f(x)}$（$f(x)\ne 0$）$\Rightarrow T=2a$
- 区域：函数性质
- 类型：结论
- 标签：拓展
- 条件：结构前提关系式对每个 $x$ 成立，$a\ne 0$
- 是什么：图像有两条对称轴 $x=a$、$x=b$（$a\ne b$）$\Rightarrow T=2|a-b|$；有对称中心 $(a,0)$ 和对称轴 $x=b$（$a\ne b$）$\Rightarrow T=4|a-b|$
- 反例：
  - $f(x)=\sin 2\pi x$ 满足 $f(x+2)=f(x)$，但最小正周期是 1：推出的 $T$ 是周期，不一定是最小正周期
- 注释：
  - 看到 $f(x+a)=-f(x)$ 或两条对称轴 → 先求周期，再把大自变量化小
- 依赖：
  - 来源：S15
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：关系式对每个 $x$ 成立
    步骤：
      1. 【代换】$f(x+a)=-f(x)$ 中 $x\to x+a$：$f(x+2a)=-f(x+a)$
      2. 【代入】用两次：$f(x+2a)=-f(x+a)=f(x)\Rightarrow T=2a$
      3. 【代换】$f(x+a)=\dfrac{1}{f(x)}$ 同理：$f(x+2a)=\dfrac{1}{f(x+a)}=f(x)\Rightarrow T=2a$
  - 来源：P62
    种类：推出
    方法：回到定义
    步骤：
      1. 【代换】对称轴 $x=a$：$f(a+x)=f(a-x)$ 中 $x\to x-a$：$f(x)=f(2a-x)$
      2. 【代换】再用对称轴 $x=b$，把 $2a-x$ 当自变量：$f(x)=f(2a-x)=f[2b-(2a-x)]=f(x+2b-2a)$
      3. 【定义】「周期函数」周期 $T=2|b-a|$

### P68 圆的方程（配方）
- 标志：标准方程 $(x-a)^2+(y-b)^2=r^2$
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：定义域$D^2+E^2-4F>0$
- 是什么：一般方程 $x^2+y^2+Dx+Ey+F=0$ 配方：$\left(x+\dfrac{D}{2}\right)^2+\left(y+\dfrac{E}{2}\right)^2=\dfrac{D^2+E^2-4F}{4}$；圆心 $\left(-\dfrac{D}{2},-\dfrac{E}{2}\right)$，半径 $\dfrac{1}{2}\sqrt{D^2+E^2-4F}$；二元二次方程表示圆：$x^2$、$y^2$ 系数相等且不含 $xy$ 项，再验 $D^2+E^2-4F>0$；点 $(x_1,y_1)$ 与圆：$(x_1-a)^2+(y_1-b)^2$ 大于、等于、小于 $r^2$ 分别为圆外、圆上、圆内；以 $A(x_1,y_1)$、$B(x_2,y_2)$ 为直径的圆：$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0$（由 $\overrightarrow{PA}\cdot\overrightarrow{PB}=0$）
- 反例：
  - $x^2+y^2+2x+2=0$：$D^2+E^2-4F=4-8<0$，不表示任何图形
- 注释：
  - 看到 $x^2+y^2+Dx+Ey+F=0$ → 配方读圆心、半径
- 依赖：
  - 来源：S16
    种类：推出
    方法：回到定义
    步骤：
      1. 【定义】到圆心 $(a,b)$ 距离为 $r$：$\sqrt{(x-a)^2+(y-b)^2}=r$（「两点距离公式」）
      2. 【平方】$(x-a)^2+(y-b)^2=r^2$
  - 来源：R03
    种类：推出
    方法：配凑
    条件：▼ 加条件〔定义域〕：$D^2+E^2-4F>0$
    步骤：
      1. 【配方】「完全平方」$x^2+Dx=\left(x+\dfrac{D}{2}\right)^2-\dfrac{D^2}{4}$，$y^2+Ey=\left(y+\dfrac{E}{2}\right)^2-\dfrac{E^2}{4}$
      2. 【移项】$x^2+y^2+Dx+Ey+F=0\Rightarrow\left(x+\dfrac{D}{2}\right)^2+\left(y+\dfrac{E}{2}\right)^2=\dfrac{D^2+E^2-4F}{4}$
      3. 【定义】右边 $>0$ 才是圆

### P70 椭圆、双曲线的基本量
- 标志：椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$：$a^2=b^2+c^2$，$e=\dfrac{c}{a}\in(0,1)$，$e^2=1-\dfrac{b^2}{a^2}$
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：结构前提椭圆 $a>b>0$，双曲线 $a>0,b>0$，中心在原点、焦点在坐标轴上
- 是什么：双曲线 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$：$c^2=a^2+b^2$，$e=\dfrac{c}{a}>1$，$e^2=1+\dfrac{b^2}{a^2}$，渐近线 $y=\pm\dfrac{b}{a}x$；椭圆上的点 $P$：$|PF_1|+|PF_2|=2a$；双曲线上的点：$|PF_1|$ 与 $|PF_2|$ 之差的绝对值为 $2a$；焦点在 $y$ 轴：椭圆 $\dfrac{y^2}{a^2}+\dfrac{x^2}{b^2}=1$；双曲线 $\dfrac{y^2}{a^2}-\dfrac{x^2}{b^2}=1$，渐近线 $y=\pm\dfrac{a}{b}x$（不是 $\dfrac{b}{a}$）；顶点：椭圆 $(\pm a,0)$、$(0,\pm b)$，长轴 $2a$、短轴 $2b$；双曲线 $(\pm a,0)$，实轴 $2a$、虚轴 $2b$；等轴双曲线 $a=b$，$e=\sqrt{2}$，渐近线 $y=\pm x$；焦半径（标准方程推导中的式子）：椭圆 $|PF_1|=a+ex_0$，$|PF_2|=a-ex_0$；双曲线 $|PF_1|=|ex_0+a|$；椭圆上点到焦点的距离最小 $a-c$、最大 $a+c$（长轴端点）；双曲线上点到焦点的距离最小 $c-a$；设方程：两点定椭圆设 $mx^2+ny^2=1$；共渐近线的双曲线设 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=\lambda$（$\lambda\ne 0$）
- 反例：
  - 椭圆 $\dfrac{x^2}{4}+\dfrac{y^2}{9}=1$ 焦点在 $y$ 轴：$a^2=9$，$c=\sqrt{5}$；误取 $a^2=4$ 得 $c^2=4-9<0$
- 注释：
  - 已知 $a,b,c,e$ 中的两个 → 椭圆用 $a^2=b^2+c^2$，双曲线用 $c^2=a^2+b^2$；求 $e$ 列 $a,c$ 的齐次式
- 依赖：
  - 来源：S16
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：标准位置
    步骤：
      1. 【定义】$|PF_1|+|PF_2|=2a$：$\sqrt{(x+c)^2+y^2}+\sqrt{(x-c)^2+y^2}=2a$
      2. 【移项】$\sqrt{(x+c)^2+y^2}=2a-\sqrt{(x-c)^2+y^2}$
      3. 【平方】两次：$a^2-cx=a\sqrt{(x-c)^2+y^2}\Rightarrow(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$
      4. 【代换】令 $b^2=a^2-c^2$：$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$
      5. 【代换】双曲线同理，令 $b^2=c^2-a^2$：$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$
  - 来源：R03
    种类：前提
    步骤：
      1. 【前提】两边平方用完全平方展开

### R46 空间向量的坐标运算
- 标志：$\vec a\cdot\vec b=x_1x_2+y_1y_2+z_1z_2$，$|\vec a|=\sqrt{x_1^2+y_1^2+z_1^2}$
- 区域：空间
- 类型：结论
- 重要度：2
- 是什么：$\vec a\perp\vec b\iff x_1x_2+y_1y_2+z_1z_2=0$；非零向量 $\cos\langle\vec a,\vec b\rangle=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$；两点距离 $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2}$；长方体对角线 $l^2=a^2+b^2+c^2$；线性运算：$\vec a\pm\vec b$、$\lambda\vec a$ 按分量；$\overrightarrow{AB}$ = 终点减起点；中点坐标取平均；平行：$\vec a\ne\vec 0$ 时 $\vec a\parallel\vec b\iff\vec b=\lambda\vec a$；分量都不为 0 时 $\dfrac{x_2}{x_1}=\dfrac{y_2}{y_1}=\dfrac{z_2}{z_1}$；基底法求长：$|\vec a+\vec b+\vec c|^2=|\vec a|^2+|\vec b|^2+|\vec c|^2+2(\vec a\cdot\vec b+\vec b\cdot\vec c+\vec c\cdot\vec a)$（与三数和的平方同型）
- 注释：
  - 立体几何能建系 → 写出点的坐标，用坐标数量积
- 依赖：
  - 来源：S17
    种类：推出
    方法：代换
    步骤：
      1. 【展开】$\vec a\cdot\vec b=(x_1\vec i+y_1\vec j+z_1\vec k)\cdot(x_2\vec i+y_2\vec j+z_2\vec k)=x_1x_2+y_1y_2+z_1z_2$（$\vec i^2=\vec j^2=\vec k^2=1$，交叉项为 0；与平面坐标式相同，多一项 $z_1z_2$）
      2. 【代入】$\vec b=\vec a$：$|\vec a|=\sqrt{\vec a\cdot\vec a}=\sqrt{x_1^2+y_1^2+z_1^2}$
  - 来源：R15
    种类：前提
    步骤：
      1. 【前提】平面数量积坐标式的推法

### P76 台体的体积与侧面积
- 标志：$V=\dfrac{1}{3}h\left(S+\sqrt{SS'}+S'\right)$（$S$、$S'$ 为下、上底面积）
- 区域：空间
- 类型：结论
- 条件：结构前提台体：上下底平行且相似，截面积之比为对应边之比的平方
- 是什么：$S'=S$ 时即柱体 $Sh$，$S'=0$ 时即锥体 $\dfrac{1}{3}Sh$；圆台侧面积 $\pi(r+r')l$；全面积：圆柱 $2\pi r(r+l)$，圆锥 $\pi r(r+l)$，圆台 $\pi(r'^2+r^2+r'l+rl)$；侧面积：直棱柱 $ch$，正棱锥 $\dfrac{1}{2}ch'$，正棱台 $\dfrac{1}{2}(c+c')h'$（$c$ 底面周长，$h'$ 斜高；$c'=c$、$c'=0$ 时得前两式）；拓展（老教材）：拟柱体 $V=\dfrac{h}{6}(S+4S_0+S')$（$S_0$ 为中截面面积），柱、锥、台、球都适用
- 注释：
  - 台体 → 补成大锥再减去小锥
- 依赖：
  - 来源：S18
    种类：推出
    方法：补形
    条件：▼ 加条件〔结构前提〕：台体
    步骤：
      1. 【补形】台体 = 大锥 − 小锥；小锥高 $x$ 满足 $\dfrac{x}{x+h}=\dfrac{\sqrt{S'}}{\sqrt{S}}$（面积比 = 相似比的平方）
      2. 【移项】$x\sqrt{S}=(x+h)\sqrt{S'}\Rightarrow x=\dfrac{h\sqrt{S'}}{\sqrt{S}-\sqrt{S'}}$
      3. 【相减】「锥体体积」$V=\dfrac{1}{3}S(x+h)-\dfrac{1}{3}S'x=\dfrac{1}{3}\left[Sh+x(S-S')\right]$
      4. 【代入】「平方差」$x(S-S')=\dfrac{h\sqrt{S'}(\sqrt{S}-\sqrt{S'})(\sqrt{S}+\sqrt{S'})}{\sqrt{S}-\sqrt{S'}}=h\left(\sqrt{SS'}+S'\right)$
      5. 【合并】$V=\dfrac{1}{3}h\left(S+\sqrt{SS'}+S'\right)$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】$S-S'=(\sqrt{S}-\sqrt{S'})(\sqrt{S}+\sqrt{S'})$

### P78 条件概率与乘法公式、独立的判断
- 标志：乘法公式：$P(AB)=P(A)P(B|A)$
- 区域：概率统计
- 类型：结论
- 重要度：2
- 条件：定义域$P(A)>0$
- 是什么：古典概型中 $P(B|A)=\dfrac{n(AB)}{n(A)}$：在 $A$ 里数 $B$；$A,B$ 独立 $\iff P(B|A)=P(B)$；$A,B$ 独立则 $A$ 与 $\bar B$、$\bar A$ 与 $\bar B$ 也独立；推广：$P(A_1A_2A_3)=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)$；$A,B,C$ 相互独立时 $P(ABC)=P(A)P(B)P(C)$；条件概率也满足概率的性质：$P(\bar B|A)=1-P(B|A)$；$B,C$ 互斥时 $P(B\cup C|A)=P(B|A)+P(C|A)$
- 反例：
  - $P(B|A)$ 与 $P(A|B)$ 不同：掷骰子，$A$=点数为 2，$B$=偶数点：$P(B|A)=1$，$P(A|B)=\dfrac{1}{3}$
- 注释：
  - “在……发生的条件下” → 条件概率，缩小样本空间；“相互独立” → 概率相乘
- 依赖：
  - 来源：S19
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔定义域〕：$P(A)>0$
    步骤：
      1. 【同乘】「条件概率定义」两边乘 $P(A)$：$P(AB)=P(A)P(B|A)$
      2. 【同除】古典概型分子、分母同除 $n(\Omega)$：$P(B|A)=\dfrac{n(AB)}{n(A)}$
      3. 【相减】$P(A\bar B)=P(A)-P(AB)=P(A)[1-P(B)]$
  - 来源：R47
    种类：前提
    步骤：
      1. 【前提】对立事件 $P(\bar B)=1-P(B)$

### R48 均值与方差的性质
- 标志：$E(aX+b)=aE(X)+b$；$D(aX+b)=a^2D(X)$
- 区域：概率统计
- 类型：结论
- 重要度：2
- 是什么：$D(X)=E(X^2)-[E(X)]^2$
- 反例：
  - $D(2X+1)\ne 2D(X)+1$：$X$ 取 0、1 各 $\dfrac{1}{2}$，$D(X)=\dfrac{1}{4}$，$D(2X+1)=1$
- 注释：
  - 已知 $X$ 的均值、方差，求 $aX+b$ 的 → 线性性质；方差难算 → $E(X^2)-[E(X)]^2$
- 依赖：
  - 来源：S20
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】$\sum(ax_i+b)p_i=a\sum x_ip_i+b\sum p_i$
      2. 【展开】$D(X)=\sum\left[x_i^2-2x_iE(X)+E(X)^2\right]p_i$
      3. 【合并】逐项求和
  - 来源：R03
    种类：前提
    步骤：
      1. 【前提】完全平方展开

### P81 超几何分布
- 标志：$P(X=k)=\dfrac{C_M^kC_{N-M}^{n-k}}{C_N^n}$
- 区域：概率统计
- 类型：结论
- 条件：结构前提$N$ 件中有 $M$ 件次品，不放回地取 $n$ 件
- 是什么：$E(X)=\dfrac{nM}{N}$：与有放回（二项分布，$p=\dfrac{M}{N}$）的均值相同；$k$ 的范围：$\max\{0,\ n-(N-M)\}\le k\le\min\{M,n\}$；记作 $X\sim H(N,n,M)$
- 注释：
  - 从有限个里不放回地取，问其中次品有几个 → 超几何分布
- 依赖：
  - 来源：S19
    种类：推出
    方法：分类讨论
    条件：▼ 加条件〔结构前提〕：不放回
    步骤：
      1. 【分步计数】样本点总数 $C_N^n$，恰有 $k$ 件次品的有 $C_M^kC_{N-M}^{n-k}$ 种（「古典概型」）
  - 来源：P34
    种类：前提
    步骤：
      1. 【前提】组合数

### P85 正态分布的对称性
- 标志：正态曲线关于直线 $x=\mu$ 对称，曲线与 $x$ 轴之间的面积为 1（由密度函数〔S23〕）
- 区域：概率统计
- 类型：结论
- 条件：结构前提$X\sim N(\mu,\sigma^2)$
- 是什么：$P(X\le\mu)=P(X\ge\mu)=\dfrac{1}{2}$；$P(X\le\mu-a)=P(X\ge\mu+a)$；$P(X<\mu-a)=\dfrac{1-P(\mu-a\le X\le\mu+a)}{2}$；3σ 的概率见 T11
- 反例：
  - $X\sim N(1,4)$：$\sigma=2$，不是 4；$P(-1\le X\le 3)\approx 0.6826$
- 注释：
  - 已知正态分布一侧的概率求另一侧 → 关于 $x=\mu$ 对称，总概率 1
- 依赖：
  - 来源：S20
    种类：推出
    方法：对称
    条件：▼ 加条件〔结构前提〕：$X$ 服从正态分布
    步骤：
      1. 【对称】概率 = 曲线下的面积；关于 $x=\mu$ 对称的两块面积相等
  - 来源：S23
    种类：推出
    方法：对称
    步骤：
      1. 【对称】密度函数中 $x-\mu$ 只以平方出现，曲线关于 $x=\mu$ 对称
  - 来源：R47
    种类：前提
    步骤：
      1. 【前提】对立事件：$P(X>a)=1-P(X\le a)$

### P87 已知三角函数值求角
- 标志：$\sin x=a$（$-1\le a\le 1$）：$x=\arcsin a+2k\pi$ 或 $\pi-\arcsin a+2k\pi$（合写 $x=k\pi+(-1)^k\arcsin a$）；$a=\pm 1$ 时两组合并为一组
- 区域：三角
- 类型：结论
- 重要度：1
- 条件：符号分支sin/cos 一个值对应两组角，tan 只有一组
- 是什么：$\cos x=a$（$-1\le a\le 1$）：$x=2k\pi\pm\arccos a$；$a=\pm 1$ 时两组合并为一组；$\tan x=a$（$a$ 为任意实数）：$x=k\pi+\arctan a$（周期 $\pi$，每个周期只有一个角）；取值范围：$\arcsin a\in\left[-\dfrac{\pi}{2},\dfrac{\pi}{2}\right]$，$\arccos a\in[0,\pi]$，$\arctan a\in\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$；拓展（老教材）：$\arcsin(-x)=-\arcsin x$，$\arccos(-x)=\pi-\arccos x$，$\arcsin x+\arccos x=\dfrac{\pi}{2}$，$\sin(\arcsin x)=x$
- 反例：
  - $\sin x=\dfrac{1}{2}$ 只写 $x=\dfrac{\pi}{6}+2k\pi$ 漏了 $\dfrac{5\pi}{6}+2k\pi$
- 注释：
  - 已知 sin、cos、tan 的值求角 → 先在一个周期里找全，再加周期
- 依赖：
  - 来源：R14
    种类：推出
    方法：特例
    条件：▼ 加条件〔符号分支〕：sin/cos 一个值两组角（端点合并），tan 只有一组
    步骤：
      1. 【对称】「诱导公式④」$\sin(\pi-\alpha)=\sin\alpha$ 给出 sin 的第二组角；$a=\pm 1$ 时两组合并
      2. 【对称】「诱导公式③」$\cos(-\alpha)=\cos\alpha$ 给出 cos 的 $\pm$；$a=\pm 1$ 时两组合并
      3. 【推广】再加周期：sin/cos 加 $2k\pi$，tan 加 $k\pi$（tan 周期 $\pi$，每个周期只有一个角）
  - 来源：P13
    种类：前提
    步骤：
      1. 【前提】$\tan(\pi+\alpha)=\tan\alpha$

### R52 正割、余割、余切
- 标志：$\sec\alpha=\dfrac{r}{x}$，$\csc\alpha=\dfrac{r}{y}$，$\cot\alpha=\dfrac{x}{y}$
- 区域：三角
- 类型：中间步
- 标签：拓展
- 是什么：$\cos\alpha\sec\alpha=1$，$\sin\alpha\csc\alpha=1$，$\tan\alpha\cot\alpha=1$；$1+\tan^2\alpha=\sec^2\alpha$，$1+\cot^2\alpha=\csc^2\alpha$
- 注释：
  - 读外文资料、大学课程（必修三拓展阅读）
  - 看到 sec、csc、cot → 化回 cos、sin、tan 的倒数
- 依赖：
  - 来源：S04
    种类：推出
    方法：互逆
    步骤：
      1. 【定义】终边上一点 $(x,y)$，$r=\sqrt{x^2+y^2}$
      2. 【取倒数】$\sec\alpha=\dfrac{r}{x}$，$\csc\alpha=\dfrac{r}{y}$，$\cot\alpha=\dfrac{x}{y}$
  - 来源：P12
    种类：前提
    步骤：
      1. 【前提】$1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$

### P89 正切型函数 $y=A\tan(\omega x+\varphi)$
- 标志：周期 $T=\dfrac{\pi}{|\omega|}$；定义域 $\omega x+\varphi\ne\dfrac{\pi}{2}+k\pi$
- 区域：函数性质
- 类型：结论
- 条件：定义域$\omega\ne 0$，$\omega x+\varphi\ne\dfrac{\pi}{2}+k\pi$
- 是什么：对称中心：$\omega x+\varphi=\dfrac{k\pi}{2}$，纵坐标 0；没有对称轴；$y=\tan x$：零点 $k\pi$，对称中心 $\left(\dfrac{k\pi}{2},0\right)$
- 反例：
  - 正切型的周期不是 $\dfrac{2\pi}{|\omega|}$
- 注释：
  - 正切型函数 → 周期 $\dfrac{\pi}{|\omega|}$，把 $\omega x+\varphi$ 当整体
- 依赖：
  - 来源：P13
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕：$\cos(\omega x+\varphi)\ne 0$
    步骤：
      1. 【代入】「tan 的诱导公式」$\tan(\alpha+\pi)=\tan\alpha$，$\alpha=\omega x+\varphi$：$A\tan\left[\omega\left(x+\dfrac{\pi}{\omega}\right)+\varphi\right]=A\tan(\omega x+\varphi+\pi)=A\tan(\omega x+\varphi)$（$\omega x$ 增加 $\pi$ 为一个周期）
      2. 【定义】「周期函数」$T=\dfrac{\pi}{|\omega|}$
  - 来源：S15
    种类：前提
    步骤：
      1. 【前提】周期的定义

### P95 隔板法：相同元素分给不同对象
- 标志：$x_1+x_2+\cdots+x_r=n$ 的正整数解：$C_{n-1}^{r-1}$
- 区域：计数
- 类型：结论
- 标签：拓展
- 条件：定义域$n\ge r$（正整数解）
- 是什么：非负整数解：$C_{n+r-1}^{r-1}$（选必二拓展阅读）
- 注释：
  - 相同的东西分给不同的人 → 隔板法；允许为 0 时先每人借一个
- 依赖：
  - 来源：P34
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$n\ge r$
    步骤：
      1. 【对应】$n$ 个元素排成一行，在 $n-1$ 个空中插 $r-1$ 块隔板
      2. 【代换】非负解令 $y_i=x_i+1$

### P99 空间向量基本定理与共面
- 标志：基本定理：$\vec p=x\vec a+y\vec b+z\vec c$，$(x,y,z)$ 唯一；$x\vec a+y\vec b+z\vec c=\vec 0\iff x=y=z=0$
- 区域：空间
- 类型：结论
- 重要度：1
- 条件：结构前提$\vec a,\vec b,\vec c$ 不共面（基本定理）；$A,B,C$ 不共线（共面）
- 是什么：共面向量定理：$\vec a,\vec b$ 不共线时，$\vec a,\vec b,\vec c$ 共面 $\iff\vec c=x\vec a+y\vec b$；四点共面：$P\in$ 平面 $ABC\iff\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}\iff\overrightarrow{OP}=x\overrightarrow{OA}+y\overrightarrow{OB}+z\overrightarrow{OC}$，$x+y+z=1$
- 注释：
  - 同源：平面向量基本定理、三点共线系数和为 1〔P56〕
  - 判断四点共面 → 系数和为 1；用基底表示空间向量 → 系数唯一
- 依赖：
  - 来源：S17
    种类：推出
    方法：特例
    条件：▼ 加条件〔结构前提〕：基底不共面
    步骤：
      1. 【推广】「平面向量基本定理」加一个不在平面内的方向 $\vec c$：$\vec p=x\vec a+y\vec b+z\vec c$，$(x,y,z)$ 唯一
  - 来源：P56
    种类：前提
    步骤：
      1. 【前提】平面向量基本定理、三点共线

## 第 4 层　推导第 4 层

### R05 两数和（差）的立方
- 标志：$(a\pm b)^3=a^3\pm 3a^2b+3ab^2\pm b^3$
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$(a\pm b)^3=a^3\pm 3a^2b+3ab^2\pm b^3$
- 依赖：
  - 来源：R03
    种类：推出
    方法：代换
    步骤：
      1. 【展开】「完全平方」$(a+b)^3=(a+b)^2(a+b)=(a^2+2ab+b^2)(a+b)$
      2. 【合并】$=a^3+a^2b+2a^2b+2ab^2+ab^2+b^3=a^3+3a^2b+3ab^2+b^3$
      3. 【代换】$b\to -b$：$(a-b)^3=a^3-3a^2b+3ab^2-b^3$
  - 来源：R33
    种类：前提
    步骤：
      1. 【特例】$n=3$（另一路）

### P43 根式运算
- 标志：$\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}$（$a,b\ge 0$）；$\dfrac{\sqrt{a}}{\sqrt{b}}=\sqrt{\dfrac{a}{b}}$（$a\ge 0$，$b>0$）
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域被开方数 $\ge 0$；符号分支开方要定号
- 是什么：$(\sqrt{a})^2=a$（$a\ge 0$）；$\sqrt{a^2}=|a|$；$n$ 次根式：$(\sqrt[n]{a})^n=a$；$\sqrt[n]{a^n}=a$（$n$ 奇），$\sqrt[n]{a^n}=|a|$（$n$ 偶）；例 $\sqrt[4]{(-3)^4}=3$
- 反例：
  - $a=-3$：$\sqrt{(-3)^2}=3\ne -3$；$\sqrt{(-2)(-8)}=4$，但 $\sqrt{-2}$ 无意义
- 注释：
  - 复数的模；含根式的化简
  - 配合：已知一值求其余〔P46〕、升幂后开方〔R19〕都要定号
  - 看到根号 → 化成分数指数幂；开偶次方要带绝对值
- 依赖：
  - 来源：P05
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕〔符号分支〕：被开方数 $\ge 0$；$\sqrt{a^2}=|a|$
    步骤：
      1. 【特例】取 $r=\dfrac{1}{2}$：$\sqrt{a}=a^{\frac{1}{2}}$
      2. 【代入】「实数指数运算律」$\sqrt{a}\sqrt{b}=a^{\frac{1}{2}}b^{\frac{1}{2}}=(ab)^{\frac{1}{2}}=\sqrt{ab}$
      3. 【定义】算术平方根非负：$\sqrt{a^2}=|a|$

### P07 对数运算律
- 标志：$\log_a(MN)=\log_a M+\log_a N$
- 区域：指数与对数
- 类型：结论
- 重要度：2
- 条件：定义域$M>0,\ N>0$
- 是什么：$\log_a\dfrac{M}{N}=\log_a M-\log_a N$；$\log_a M^n=n\log_a M$（$n\in\mathbb{R}$）
- 反例：
  - $\log_2[(-2)(-4)]=3$ 有意义，$\log_2(-2)$ 无意义；$\log_a x^2=2\log_a|x|$（$x\ne 0$）
- 注释：
  - 同见不等式大厦 P21、P04
  - 看到同底对数相加减 → 合成积、商的对数
- 依赖：
  - 来源：P05
    种类：推出
    方法：互逆
    步骤：
      1. 【设】$M=a^p$，$N=a^q$，即 $p=\log_a M$，$q=\log_a N$
      2. 【代入】「实数指数运算律」积 $MN=a^pa^q=a^{p+q}$；商 $\dfrac{M}{N}=a^p\div a^q=a^{p-q}$；幂 $M^n=(a^p)^n=a^{pn}$
      3. 【取对数】$\log_a(MN)=p+q$，$\log_a\dfrac{M}{N}=p-q$，$\log_a M^n=np$（「对数定义」）
  - 来源：P06
    种类：前提
    步骤：
      1. 【前提】指数式与对数式互化

### R17 其余和差角
- 标志：$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$
- 区域：三角
- 类型：结论
- 重要度：2
- 是什么：$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
- 注释：
  - 看到两角和差，或角能拆成已知角的和差 → 和差角公式（拆角配角）
- 依赖：
  - 来源：R16
    种类：推出
    方法：代换
    步骤：
      1. 【代换】$\beta\to-\beta$：$\cos(\alpha+\beta)=\cos\alpha\cos(-\beta)+\sin\alpha\sin(-\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$（「诱导公式③」）
      2. 【代换】$\sin(\alpha+\beta)=\cos\left[\dfrac{\pi}{2}-(\alpha+\beta)\right]=\cos\left[\left(\dfrac{\pi}{2}-\alpha\right)-\beta\right]$（「诱导公式⑤」）
      3. 【展开】$=\cos\left(\dfrac{\pi}{2}-\alpha\right)\cos\beta+\sin\left(\dfrac{\pi}{2}-\alpha\right)\sin\beta=\sin\alpha\cos\beta+\cos\alpha\sin\beta$
      4. 【代换】$\beta\to-\beta$：$\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$（「诱导公式③」）
  - 来源：R14
    种类：前提
    步骤：
      1. 【前提】诱导公式 ③⑤

### P22 余弦定理
- 标志：$a^2=b^2+c^2-2bc\cos A$（其余两式同理）
- 区域：向量
- 类型：结论
- 重要度：2
- 条件：结构前提$a$ 为 $A$ 的对边，$b,c$ 夹 $A$
- 是什么：推论 $\cos A=\dfrac{b^2+c^2-a^2}{2bc}$（已知三边求角）；$A=90^\circ$ 时即勾股定理；射影定理 $a=b\cos C+c\cos B$（必修四 9.1.2 例 5，可反推余弦定理）
- 反例：
  - 3、4、5 的直角三角形 $A=90^\circ$，误把 $a$ 取成 3（不是 $A$ 的对边）：右边 $=4^2+5^2-0=41$，左边 $=9$
- 注释：
  - 同源：勾股恒等式〔R13〕
  - 已知三边，或两边及夹角 → 余弦定理
- 依赖：
  - 来源：P49
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔结构前提〕：$a$ 为 $A$ 的对边
    步骤：
      1. 【代换】$\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$
      2. 【展开】「$|\vec a-\vec b|^2$」$|\overrightarrow{BC}|^2=|\overrightarrow{AC}|^2-2\overrightarrow{AC}\cdot\overrightarrow{AB}+|\overrightarrow{AB}|^2=b^2+c^2-2bc\cos A$

### P23 复数除法
- 标志：$\dfrac{a+bi}{c+di}=\dfrac{(ac+bd)+(bc-ad)i}{c^2+d^2}$
- 区域：复数
- 类型：结论
- 条件：定义域$c+di\ne 0$
- 是什么：$\dfrac{a+bi}{c+di}=\dfrac{(ac+bd)+(bc-ad)i}{c^2+d^2}$
- 反例：
  - $c=d=0$ 时分母为 0
- 注释：
  - 复数计算
  - 复数除法 → 分母实数化
- 依赖：
  - 来源：R23
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$c+di\ne 0$
    步骤：
      1. 【同乘】分子、分母同乘 $c-di$（「共轭」）
      2. 【展开】分母 $(c+di)(c-di)=c^2+d^2$（实数）；分子 $(a+bi)(c-di)=(ac+bd)+(bc-ad)i$
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】分式化简（分母 $\ne 0$）

### R25 模的乘法
- 标志：$|z_1z_2|=|z_1||z_2|$
- 区域：复数
- 类型：中间步
- 是什么：$|\bar z|=|z|$；$|z_1-z_2|$ = 复平面上两点间的距离（$|z-z_0|=r$ 表示圆）
- 注释：
  - 同源：拉格朗日恒等式〔R11〕
  - 复数求模
  - 求积的模 → 模相乘；看到 $|z-z_0|$ → 两点距离
- 依赖：
  - 来源：R23
    种类：推出
    方法：互逆
    步骤：
      1. 【代入】$|z_1z_2|^2=z_1z_2\cdot\overline{z_1z_2}=z_1z_2\cdot\bar z_1\bar z_2=(z_1\bar z_1)(z_2\bar z_2)=|z_1|^2|z_2|^2$（「$z\bar z=|z|^2$」「$\overline{z_1z_2}=\bar z_1\bar z_2$」）
      2. 【开平方】$|z_1z_2|=|z_1||z_2|$

### P27 等差下标性质
- 标志：$m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$
- 区域：数列
- 类型：结论
- 条件：结构前提等差数列
- 是什么：$m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$
- 反例：
  - 1, 2, 4, 7 不是等差：$a_1+a_4=8$，$a_2+a_3=6$
- 注释：
  - 等差数列中下标和相等 → 两项之和相等
- 依赖：
  - 来源：P26
    种类：推出
    方法：代换
    步骤：
      1. 【代入】「等差通项」$a_m+a_n=2a_1+(m+n-2)d$，$a_p+a_q=2a_1+(p+q-2)d$
      2. 【代换】$m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$

### P30 等比下标性质
- 标志：$m+n=p+q\Rightarrow a_ma_n=a_pa_q$
- 区域：数列
- 类型：结论
- 条件：结构前提等比数列
- 是什么：$m+n=p+q\Rightarrow a_ma_n=a_pa_q$
- 反例：
  - 1, 2, 4, 7：$a_1a_4=7$，$a_2a_3=8$
- 注释：
  - 等比数列的性质速算
  - 等比数列中下标和相等 → 两项之积相等
- 依赖：
  - 来源：P29
    种类：推出
    方法：代换
    步骤：
      1. 【代入】「等比通项」$a_ma_n=a_1^2q^{m+n-2}$，$a_pa_q=a_1^2q^{p+q-2}$
      2. 【代换】$m+n=p+q\Rightarrow a_ma_n=a_pa_q$

### P31 等比求和
- 标志：$q\ne 1$：$S_n=\dfrac{a_1(1-q^n)}{1-q}$；$q=1$：$S_n=na_1$
- 区域：数列
- 类型：结论
- 重要度：2
- 条件：结构前提等比数列；定义域$q\ne 1$
- 是什么：$q\ne 1$ 时 $S_n=Aq^n-A$，$A=\dfrac{a_1}{q-1}$；另一形式：$q\ne 1$ 时 $S_n=\dfrac{a_1-a_nq}{1-q}$（已知 $a_1,q,a_n$ 时直接用）
- 反例：
  - $q=1$ 时分母为 0
- 注释：
  - 同见不等式大厦 P13
  - 差比数列求和
  - 等比求和 → 先看 $q$ 是否为 1
- 依赖：
  - 来源：P29
    种类：推出
    方法：同除
    条件：▼ 加条件〔定义域〕：$q\ne 1$
    步骤：
      1. 【错位相减】$S_n-qS_n=a_1-a_1q^n$
      2. 【同除】两边除以 $1-q$：$S_n=\dfrac{a_1(1-q^n)}{1-q}$
  - 来源：R09
    种类：前提
    步骤：
      1. 【因式分解】$1-q^n=(1-q)(1+q+\cdots+q^{n-1})$（另一路）
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】两边除以 $1-q$

### R34 二项式系数性质
- 标志：$C_n^0+C_n^1+\cdots+C_n^n=2^n$
- 区域：计数
- 类型：中间步
- 是什么：奇数项的二项式系数和 = 偶数项的二项式系数和 $=2^{n-1}$（$n\ge 1$）；注意：二项式系数 $C_n^k$ 不等于项的系数〔R39〕
- 注释：
  - 求二项式系数和 → $2^n$
- 依赖：
  - 来源：R33
    种类：推出
    方法：特例
    步骤：
      1. 【赋值】令 $a=b=1$：$C_n^0+C_n^1+\cdots+C_n^n=2^n$
      2. 【赋值】令 $a=1,\ b=-1$：交错和为 0
  - 来源：R40
    种类：前提
    步骤：
      1. 【双计数】子集共 $2^n$ 个，按元素个数分类为 $\sum C_n^k$（另一路）

### R39 展开式的各项系数和
- 标志：$f(x)=a_0+a_1x+\cdots+a_nx^n$：$a_0+a_1+\cdots+a_n=f(1)$，$a_0-a_1+a_2-\cdots=f(-1)$
- 区域：计数
- 类型：结论
- 重要度：1
- 是什么：偶次项系数和 $=\dfrac{f(1)+f(-1)}{2}$，奇次项 $=\dfrac{f(1)-f(-1)}{2}$，常数项 $a_0=f(0)$；例 $(2x-1)^5$：各项系数和 $=1$，二项式系数和 $=2^5=32$
- 注释：
  - 求展开式各项系数和 → 赋值 $x=1$、$-1$、$0$
- 依赖：
  - 来源：R33
    种类：推出
    方法：特例
    步骤：
      1. 【赋值】$f(x)=a_0+a_1x+\cdots+a_nx^n$ 对一切 $x$ 成立，令 $x=1$：各项系数和；$x=-1$：交错和
      2. 【相加】【相减】两式相加、相减再除以 2：偶次、奇次项系数和
      3. 【赋值】$x=0$：常数项

### R35 正整数幂求导的由来
- 标志：$(x^n)'=nx^{n-1}$（$n$ 为正整数，$x\in\mathbb{R}$）
- 区域：导数
- 类型：中间步
- 标签：拓展
- 是什么：$(x^n)'=nx^{n-1}$（$n$ 为正整数，$x\in\mathbb{R}$）
- 注释：
  - 多项式函数求导
- 依赖：
  - 来源：S08
    种类：推出
    方法：回到定义
    步骤：
      1. 【定义】「导数定义」$\dfrac{(x+\Delta x)^n-x^n}{\Delta x}=nx^{n-1}+C_n^2x^{n-2}\Delta x+\cdots$
      2. 【取极限】令 $\Delta x\to 0$：$(x^n)'=nx^{n-1}$
  - 来源：R33
    种类：推出
    方法：同除
    步骤：
      1. 【展开】$(x+\Delta x)^n=x^n+C_n^1x^{n-1}\Delta x+C_n^2x^{n-2}(\Delta x)^2+\cdots$（「二项式定理」）
      2. 【相减】减去 $x^n$
      3. 【同除】除以 $\Delta x$

### P57 投影向量与投影的数量
- 标志：投影的数量（$\vec a$ 在 $\vec b$ 方向上）：$|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}$，可正可负
- 区域：向量
- 类型：结论
- 重要度：1
- 条件：定义域$\vec b\ne\vec 0$
- 是什么：投影向量（B 版也简称“投影”）：$\dfrac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$；几何意义：$\vec a\cdot\vec b$ 等于 $|\vec b|$ 乘 $\vec a$ 在 $\vec b$ 方向上投影的数量；正交分解：$\vec a=(\vec a\cdot\vec e_1)\vec e_1+(\vec a\cdot\vec e_2)\vec e_2$：坐标就是在基向量上投影的数量；叫法：B 版“投影” = 投影向量，“投影的数量” = $|\vec a|\cos\theta$；有的教材把后者叫“投影”
- 注释：
  - 一个向量在另一个方向上的“影子”、到直线或平面的距离 → 投影 $\dfrac{\vec a\cdot\vec b}{|\vec b|}$
- 依赖：
  - 来源：P49
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$\vec b\ne\vec 0$
    步骤：
      1. 【代入】$|\vec a|\cos\theta$，$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}\Rightarrow|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}$（「夹角公式」）
      2. 【相乘】投影向量 = 投影 × 单位向量 $\dfrac{\vec b}{|\vec b|}\Rightarrow\dfrac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$

### P73 点差法（中点弦；选必一复习题 B13、B23）
- 标志：椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$：$k_{AB}\cdot k_{OM}=-\dfrac{b^2}{a^2}$
- 区域：解析几何
- 类型：结论
- 条件：结构前提弦 $AB$ 的中点 $M(x_0,y_0)$，$x_1\ne x_2$，$x_0\ne 0$
- 是什么：双曲线 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$：$k_{AB}\cdot k_{OM}=\dfrac{b^2}{a^2}$；抛物线 $y^2=2px$：$k_{AB}=\dfrac{p}{y_0}$（$y_0\ne 0$）
- 反例：
  - 双曲线 $x^2-\dfrac{y^2}{2}=1$ 以 $(1,1)$ 为中点：点差得 $y=2x-1$，代回 $\Delta=16-24<0$，这样的弦不存在
- 注释：
  - 已知弦的中点求斜率 → 点差法，求完要回代验 $\Delta>0$
- 依赖：
  - 来源：P70
    种类：推出
    方法：同除
    条件：▼ 加条件〔结构前提〕：已知中点
    步骤：
      1. 【代入】$A(x_1,y_1)$、$B(x_2,y_2)$ 分别代入：$\dfrac{x_1^2}{a^2}+\dfrac{y_1^2}{b^2}=1$，$\dfrac{x_2^2}{a^2}+\dfrac{y_2^2}{b^2}=1$
      2. 【相减】「平方差」$\dfrac{(x_1+x_2)(x_1-x_2)}{a^2}+\dfrac{(y_1+y_2)(y_1-y_2)}{b^2}=0$
      3. 【同除】$(x_1+x_2)(x_1-x_2)$（$x_1\ne x_2$，$x_1+x_2\ne 0$）：$\dfrac{y_1+y_2}{x_1+x_2}\cdot\dfrac{y_1-y_2}{x_1-x_2}=-\dfrac{b^2}{a^2}$，即 $k_{OM}\cdot k_{AB}=-\dfrac{b^2}{a^2}$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】平方差

### P74 法向量与空间角
- 标志：求 $\vec n$：设 $\vec n=(x,y,z)$，令 $\vec n\cdot\overrightarrow{AB}=0$，$\vec n\cdot\overrightarrow{AC}=0$（$\overrightarrow{AB},\overrightarrow{AC}$ 不共线），取一组非零解
- 区域：空间
- 类型：结论
- 重要度：2
- 条件：定义域$\vec n\ne\vec 0$；符号分支二面角是锐角还是钝角看图
- 是什么：线线角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\cos\theta=|\cos\langle\vec u_1,\vec u_2\rangle|$；线面角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\sin\theta=|\cos\langle\vec u,\vec n\rangle|$；二面角 $\theta\in[0,\pi]$：$|\cos\theta|=|\cos\langle\vec n_1,\vec n_2\rangle|$，锐角还是钝角由图形判断；两平面所成角 $\theta\in\left[0,\dfrac{\pi}{2}\right]$：$\cos\theta=|\cos\langle\vec n_1,\vec n_2\rangle|$，$\sin\theta=\sin\langle\vec n_1,\vec n_2\rangle$，不用判断锐钝；平行、垂直：$l\perp\alpha\iff\vec u\parallel\vec n$；$l\parallel\alpha$ 或 $l\subset\alpha\iff\vec u\cdot\vec n=0$；$\vec n_1\perp\vec n_2\Rightarrow\alpha_1\perp\alpha_2$，$\vec n_1\parallel\vec n_2\Rightarrow\alpha_1\parallel\alpha_2$ 或重合
- 反例：
  - 线面角写成 $\cos\theta=|\cos\langle\vec u,\vec n\rangle|$ 是错的：法向量与平面垂直，两角互余
- 注释：
  - 求空间角 → 方向向量、法向量的夹角；线面角取正弦
- 依赖：
  - 来源：R46
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕〔符号分支〕：$\vec n\ne\vec 0$；二面角看图
    步骤：
      1. 【定义】「夹角公式」线线角取不超过 $\dfrac{\pi}{2}$ 的那个，加绝对值：$\cos\theta=|\cos\langle\vec u_1,\vec u_2\rangle|$
      2. 【代换】线面角 $\theta$ 与 $\langle\vec u,\vec n\rangle$ 互余（或差 $\dfrac{\pi}{2}$）：$\theta=\dfrac{\pi}{2}-\langle\vec u,\vec n\rangle$ 或 $\theta=\langle\vec u,\vec n\rangle-\dfrac{\pi}{2}$
      3. 【代入】「诱导公式」化成正弦：$\sin\theta=|\cos\langle\vec u,\vec n\rangle|$
  - 来源：R14
    种类：前提
    步骤：
      1. 【前提】诱导公式 ⑤⑥：$\cos\left(\dfrac{\pi}{2}\pm\theta\right)=\mp\sin\theta$

### P77 外接球半径（补形）
- 标志：长方体棱长 $a,b,c$：外接球直径 $2R=\sqrt{a^2+b^2+c^2}$
- 区域：空间
- 类型：结论
- 标签：拓展
- 条件：结构前提长方体，或能补成长方体的几何体
- 是什么：正方体棱长 $a$：外接球 $R=\dfrac{\sqrt{3}}{2}a$，内切球 $r=\dfrac{a}{2}$；三条侧棱两两垂直的三棱锥：补成长方体
- 注释：
  - 求外接球 → 能补成长方体就用体对角线
- 依赖：
  - 来源：R46
    种类：推出
    方法：补形
    条件：▼ 加条件〔结构前提〕：能补成长方体
    步骤：
      1. 【补形】长方体的体对角线就是外接球的直径：$2R=\sqrt{a^2+b^2+c^2}$（「长方体对角线」$l^2=a^2+b^2+c^2$）
      2. 【特例】正方体 $a=b=c$：$R=\dfrac{\sqrt{3}}{2}a$

### P79 全概率公式与贝叶斯公式
- 标志：全概率：$P(B)=\displaystyle\sum_{i=1}^{n}P(A_i)P(B|A_i)$
- 区域：概率统计
- 类型：结论
- 重要度：1
- 条件：结构前提$A_1,\cdots,A_n$ 两两互斥、并为 $\Omega$，$P(A_i)>0$
- 是什么：贝叶斯：$P(A_i|B)=\dfrac{P(A_i)P(B|A_i)}{P(B)}$（$P(B)>0$）
- 反例：
  - 掷骰子，$A_1$=点数 $\le 4$，$A_2$=点数 $\ge 3$ 有重叠，$B$=点数为 3：套公式得 $\dfrac{1}{3}$，而 $P(B)=\dfrac{1}{6}$
- 注释：
  - 结果由几种“来源”造成 → 全概率（分来源相加）；已知结果反问来源 → 贝叶斯
- 依赖：
  - 来源：P78
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：完备事件组
    步骤：
      1. 【分解】$B=A_1B\cup\cdots\cup A_nB$，各项两两互斥
      2. 【代入】每项用「乘法公式」，互斥相加
      3. 【作比】贝叶斯：$P(A_iB)$ 用两种「乘法公式」表示，相等后相除
  - 来源：S19
    种类：前提
    步骤：
      1. 【前提】互斥事件的加法

### R49 样本的平均数与方差（含分层）
- 标志：$\bar x=\dfrac{1}{n}\sum x_i$，$s^2=\dfrac{1}{n}\sum(x_i-\bar x)^2=\dfrac{1}{n}\sum x_i^2-\bar x^2$
- 区域：概率统计
- 类型：中间步
- 是什么：数据 $ax_i+b$：平均数 $a\bar x+b$，方差 $a^2s^2$；分层：两层各 $m$、$n$ 个，平均数 $\bar x$、$\bar y$，方差 $s_1^2$、$s_2^2$：总平均数 $\bar w=\dfrac{m\bar x+n\bar y}{m+n}$；总方差 $=\dfrac{m\left[s_1^2+(\bar x-\bar w)^2\right]+n\left[s_2^2+(\bar y-\bar w)^2\right]}{m+n}$
- 注释：
  - 数据整体乘加 → 平均数跟着变，方差只乘 $a^2$；两组合并 → 分层公式
- 依赖：
  - 来源：R48
    种类：推出
    方法：展开分解
    步骤：
      1. 【特例】把每个数据看作取值概率为 $\dfrac{1}{n}$
      2. 【展开】分层：$\sum(x_i-\bar w)^2=\sum(x_i-\bar x)^2+m(\bar x-\bar w)^2$（交叉项 $\sum(x_i-\bar x)=0$）

### P80 二项分布
- 标志：$P(X=k)=C_n^kp^k(1-p)^{n-k}$（$k=0,1,\cdots,n$）
- 区域：概率统计
- 类型：结论
- 重要度：2
- 条件：结构前提$n$ 次独立重复试验，每次成功的概率为 $p$
- 是什么：$E(X)=np$，$D(X)=np(1-p)$；各概率之和 $=[p+(1-p)]^n=1$
- 反例：
  - 不放回地抽取，各次不独立，不能用二项分布（用超几何分布）
- 注释：
  - 重复 $n$ 次、每次只有两种结果、互不影响 → 二项分布
- 依赖：
  - 来源：P78
    种类：推出
    方法：分类讨论
    条件：▼ 加条件〔结构前提〕：独立重复
    步骤：
      1. 【相乘】指定 $k$ 次成功的一种情形概率为 $p^k(1-p)^{n-k}$（「独立事件乘法」）
      2. 【分类计数】共 $C_n^k$ 种，互斥相加
  - 来源：P34
    种类：前提
    步骤：
      1. 【前提】组合数 $C_n^k$
  - 来源：R33
    种类：前提
    步骤：
      1. 【前提】二项式定理：$\sum P(X=k)=[p+(1-p)]^n$
  - 来源：P36
    种类：前提
    步骤：
      1. 【前提】$kC_n^k=nC_{n-1}^{k-1}$，得 $E(X)=np$
  - 来源：R56
    种类：前提
    步骤：
      1. 【类比】教材由两点分布“类似地”得到 $np$、$np(1-p)$

### P84 独立性检验 $\chi^2$
- 标志：列联表 $a,b,c,d$，$n=a+b+c+d$：$\chi^2=\dfrac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}$
- 区域：概率统计
- 类型：结论
- 条件：定义域$2\times 2$ 列联表各行和、列和都 $\ne 0$
- 是什么：$\chi^2\ge$ 临界值 $x_\alpha$ 时，认为两个变量有关（犯错的概率不超过 $\alpha$）；否则不能认为有关；$ad-bc=0$ 时样本中两个变量的频率完全符合独立；由来：四个格子各算 $\dfrac{(\text{实际频数}-\text{理论频数})^2}{\text{理论频数}}$ 再相加，理论频数如 $n\hat P(A)\hat P(B)=\dfrac{(a+b)(a+c)}{n}$，化简得上式
- 反例：
  - $\chi^2<x_\alpha$ 不能说“两个变量无关”，只能说“没有足够证据认为有关”
- 注释：
  - 两个分类变量是否有关 → 列 $2\times 2$ 表算 $\chi^2$，与临界值比较（临界值见 T12）
- 依赖：
  - 来源：P78
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔定义域〕：行和、列和 $\ne 0$
    步骤：
      1. 【代入】若独立，$P(AB)=P(A)P(B)$，即 $\dfrac{a}{n}\approx\dfrac{a+b}{n}\cdot\dfrac{a+c}{n}$
      2. 【作差】$an-(a+b)(a+c)=ad-bc$：$|ad-bc|$ 越大越偏离独立，$\chi^2$ 把它标准化（课本给出）

### P86 角平分线定理
- 标志：$\dfrac{BD}{DC}=\dfrac{AB}{AC}$；外角平分线同样成立（必修四 9.1.1 例 6）
- 区域：向量
- 类型：结论
- 条件：结构前提$AD$ 平分 $\angle BAC$，$D$ 在 $BC$ 上
- 是什么：面积说法：$\dfrac{S_{\triangle ABD}}{S_{\triangle ACD}}=\dfrac{AB}{AC}=\dfrac{BD}{DC}$
- 注释：
  - 三角形中有角平分线 → 对边按两邻边之比分
- 依赖：
  - 来源：P21
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：角平分线
    步骤：
      1. 【代入】「正弦定理」$\triangle ABD$：$\dfrac{BD}{\sin\angle BAD}=\dfrac{AB}{\sin\angle ADB}$；$\triangle ACD$：$\dfrac{DC}{\sin\angle CAD}=\dfrac{AC}{\sin\angle ADC}$
      2. 【作比】$\angle BAD=\angle CAD$，$\sin\angle ADB=\sin\angle ADC$（互补，「诱导公式④」）$\Rightarrow\dfrac{BD}{DC}=\dfrac{AB}{AC}$
  - 来源：P20
    种类：前提
    步骤：
      1. 【面积法】两个三角形同高，面积比 = 底之比；又面积 $=\dfrac{1}{2}AB\cdot AD\sin\dfrac{A}{2}$

### P90 指数增长模型与平均增长率
- 标志：每期增长 $r$：$y=a(1+r)^x$；每期下降 $r$：$y=a(1-r)^x$
- 区域：指数与对数
- 类型：结论
- 条件：结构前提每期按相同百分比 $r$ 变化
- 是什么：平均增长率：$(1+p_1)(1+p_2)\cdots(1+p_n)=(1+x)^n\Rightarrow x=\sqrt[n]{(1+p_1)\cdots(1+p_n)}-1$
- 注释：
  - 同源：等比数列通项〔P29〕
  - “每年增长 $r\%$”→ $a(1+r)^x$；求时间 → 两边取对数
- 依赖：
  - 来源：P05
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：按相同百分比变化
    步骤：
      1. 【累乘】每过一期乘一次 $1+r$：$a\Rightarrow a(1+r)\Rightarrow a(1+r)^2\Rightarrow\cdots\Rightarrow a(1+r)^x$
  - 来源：P29
    种类：前提
    步骤：
      1. 【前提】等比数列：首项 $a$，公比 $1+r$

### P103 正态分布的标准化
- 标志：$X=\dfrac{Y-\mu}{\sigma}\sim N(0,1)$；$\Phi(a)=P(X<a)$
- 区域：概率统计
- 类型：结论
- 标签：拓展
- 条件：结构前提$Y\sim N(\mu,\sigma^2)$，$\sigma>0$
- 是什么：$\Phi(-a)+\Phi(a)=1$；$P(a\le X<b)=\Phi(b)-\Phi(a)$；$P(|X|<a)=2\Phi(a)-1$；$n$ 较大时二项分布 $B(n,p)$ 近似 $N(np,\ np(1-p))$
- 注释：
  - 查标准正态分布表（选必二拓展阅读）
  - 一般正态分布查表 → 减均值、除以标准差
- 依赖：
  - 来源：S23
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔结构前提〕：$\sigma>0$
    步骤：
      1. 【展开】$X=\dfrac{Y-\mu}{\sigma}=\dfrac{1}{\sigma}Y-\dfrac{\mu}{\sigma}$
      2. 【代入】用 $E(aY+b)$、$D(aY+b)$：$E\left(\dfrac{Y-\mu}{\sigma}\right)=0$，$D\left(\dfrac{Y-\mu}{\sigma}\right)=1$
      3. 【定义】均值 0、方差 1，所以 $X\sim N(0,1)$（正态变量作线性变换后仍服从正态分布，课本承认）
  - 来源：R48
    种类：前提
    步骤：
      1. 【前提】$E(aX+b)=aE(X)+b$，$D(aX+b)=a^2D(X)$

## 第 5 层　推导第 5 层

### R07 互换式
- 标志：$a^2+b^2=(a+b)^2-2ab$
- 区域：代数
- 类型：结论
- 重要度：1
- 是什么：$(a-b)^2=(a+b)^2-4ab$；$a^3+b^3=(a+b)^3-3ab(a+b)$；$a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$
- 注释：
  - 同见不等式大厦 R60、R52
  - 配合：韦达〔P03〕→ 两根的对称式〔P45〕
  - 看到平方和 $a^2+b^2$、对称式（交换 $a,b$ 不变）→ 化成 $a+b$ 与 $ab$
- 依赖：
  - 来源：R03
    种类：推出
    方法：作差相消
    步骤：
      1. 【移项】$(a+b)^2=a^2+2ab+b^2\Rightarrow a^2+b^2=(a+b)^2-2ab$
      2. 【相减】$(a+b)^2-(a-b)^2=4ab\Rightarrow(a-b)^2=(a+b)^2-4ab$
  - 来源：R05
    种类：推出
    方法：作差相消
    步骤：
      1. 【提取】$(a+b)^3=a^3+3a^2b+3ab^2+b^3=a^3+b^3+3ab(a+b)$
      2. 【移项】$a^3+b^3=(a+b)^3-3ab(a+b)$
  - 来源：R04
    种类：推出
    方法：作差相消
    步骤：
      1. 【提取】$(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)$
      2. 【移项】$a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$

### P02 求根公式
- 标志：$ax^2+bx+c=0$（$a\ne 0$）的根 $x=\dfrac{-b\pm\sqrt{\Delta}}{2a}$，$\Delta=b^2-4ac$
- 区域：代数
- 类型：结论
- 条件：定义域$\Delta\ge 0$
- 是什么：$\Delta>0$ 两个不等实根，$\Delta=0$ 两个相等的实根（重根），$\Delta<0$ 无实根
- 反例：
  - $\Delta<0$ 时 $\sqrt{\Delta}$ 在实数范围内无意义
- 注释：
  - 同见二次函数大厦 J05
  - 解方程、二次函数零点
  - 十字相乘拆不开 → 求根公式（先看 $\Delta$）
- 依赖：
  - 来源：P01
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔定义域〕：$\Delta\ge 0$
    步骤：
      1. 【配方】$ax^2+bx+c=0\Rightarrow\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}$
      2. 【开平方】$\Delta\ge 0$：$x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{\Delta}}{2a}$
      3. 【移项】$x=\dfrac{-b\pm\sqrt{\Delta}}{2a}$
  - 来源：P43
    种类：前提
    步骤：
      1. 【前提】开平方

### P44 分母有理化
- 标志：$\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{a-b}$
- 区域：指数与对数
- 类型：结论
- 条件：定义域$a,b\ge 0,\ a\ne b$
- 是什么：$\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{a-b}$
- 注释：
  - 同见不等式大厦 P25、P54（根式裂项）
  - 分母是根式的和或差 → 乘它的“共轭”，用平方差
- 依赖：
  - 来源：P43
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$a,b\ge 0,\ a\ne b$
    步骤：
      1. 【同乘】分子、分母同乘 $\sqrt{a}-\sqrt{b}$：$\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})}$（$a\ne b$）
      2. 【展开】「平方差」分母 $(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})=a-b$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】分母用平方差

### P08 换底公式
- 标志：$\log_a b=\dfrac{\log_c b}{\log_c a}$
- 区域：指数与对数
- 类型：结论
- 重要度：1
- 条件：定义域$a,c>0$ 且 $\ne 1$，$b>0$
- 是什么：$\log_a b=\dfrac{\log_c b}{\log_c a}$
- 注释：
  - 对数式化简
  - 看到底数不同的对数 → 换成同底（常换成 lg 或 ln）
- 依赖：
  - 来源：P07
    种类：推出
    方法：同除
    步骤：
      1. 【设】$\log_a b=x\Rightarrow a^x=b$
      2. 【取对数】两边取 $\log_c$：$\log_c a^x=\log_c b\Rightarrow x\log_c a=\log_c b$（「对数运算律」）
      3. 【同除】$x=\dfrac{\log_c b}{\log_c a}$（$a\ne 1\Rightarrow\log_c a\ne 0$）

### P46 已知一个三角函数值求其余
- 标志：$\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，$\cos\alpha=\pm\sqrt{1-\sin^2\alpha}$，再 $\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- 区域：三角
- 类型：结论
- 重要度：1
- 条件：符号分支± 由 $\alpha$ 所在象限定
- 是什么：$\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，$\cos\alpha=\pm\sqrt{1-\sin^2\alpha}$，再 $\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$
- 反例：
  - $\cos\alpha=\dfrac{3}{5}$ 且 $\alpha$ 在第四象限：$\sin\alpha=-\dfrac{4}{5}$，取 $+\dfrac{4}{5}$ 就错
- 注释：
  - 已知一个三角函数值求其余 → 勾股开方，按象限定号
- 依赖：
  - 来源：R13
    种类：推出
    方法：互逆
    条件：▼ 加条件〔符号分支〕：± 按象限定
    步骤：
      1. 【移项】$\sin^2\alpha+\cos^2\alpha=1\Rightarrow\sin^2\alpha=1-\cos^2\alpha$
      2. 【开平方】$\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，符号由 $\alpha$ 所在象限定
  - 来源：P43
    种类：前提
    步骤：
      1. 【前提】$\sqrt{a^2}=|a|$，开方要定号

### P14 两角和差的正切
- 标志：$\tan(\alpha\pm\beta)=\dfrac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$
- 区域：三角
- 类型：结论
- 条件：定义域三个 tan 都有定义
- 是什么：变形：$\tan\alpha+\tan\beta=\tan(\alpha+\beta)(1-\tan\alpha\tan\beta)$；$\tan\left(\dfrac{\pi}{4}\pm\theta\right)=\dfrac{1\pm\tan\theta}{1\mp\tan\theta}=\dfrac{\cos\theta\pm\sin\theta}{\cos\theta\mp\sin\theta}$（教材例题）
- 反例：
  - $\alpha=\beta=\dfrac{\pi}{4}$：$\tan(\alpha+\beta)$ 无定义，右边分母 $1-1=0$
- 注释：
  - 解析几何——两直线夹角 $\tan\theta=\left|\dfrac{k_2-k_1}{1+k_1k_2}\right|$
  - 看到 tan 的和差，或 $\tan\alpha+\tan\beta$ 与 $\tan\alpha\tan\beta$ 同时出现 → 正切和角
- 依赖：
  - 来源：R17
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：三个 tan 都有定义
    步骤：
      1. 【代入】$\tan(\alpha+\beta)=\dfrac{\sin(\alpha+\beta)}{\cos(\alpha+\beta)}=\dfrac{\sin\alpha\cos\beta+\cos\alpha\sin\beta}{\cos\alpha\cos\beta-\sin\alpha\sin\beta}$（「商数关系」「和角公式」）
      2. 【同除】分子、分母 $\div\cos\alpha\cos\beta\Rightarrow\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$
      3. 【代换】$\beta\to-\beta$ 得差角（「tan 的诱导公式」$\tan(-\beta)=-\tan\beta$）
  - 来源：P42
    种类：前提
    步骤：
      1. 【前提】分子、分母同除非零式

### R18 倍角
- 标志：$\sin 2\alpha=2\sin\alpha\cos\alpha$
- 区域：三角
- 类型：结论
- 重要度：2
- 是什么：$\cos 2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$
- 注释：
  - 同见不等式大厦 R02
  - 三角函数的图像与性质
  - 看到 $2\alpha$ 与 $\alpha$ 同时出现 → 倍角
- 依赖：
  - 来源：R17
    种类：推出
    方法：代换
    步骤：
      1. 【特例】令 $\beta=\alpha$：$\sin 2\alpha=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha$
      2. 【特例】令 $\beta=\alpha$：$\cos 2\alpha=\cos\alpha\cos\alpha-\sin\alpha\sin\alpha=\cos^2\alpha-\sin^2\alpha$
      3. 【代换】「勾股恒等式」$\sin^2\alpha=1-\cos^2\alpha$ 或 $\cos^2\alpha=1-\sin^2\alpha\Rightarrow\cos 2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】用 $\sin^2\alpha+\cos^2\alpha=1$ 换成单一函数

### R20 积化和差
- 标志：$\sin\alpha\cos\beta=\dfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$
- 区域：三角
- 类型：中间步
- 是什么：$\cos\alpha\cos\beta=\dfrac{1}{2}[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$；$\cos\alpha\sin\beta=\dfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)]$；$\sin\alpha\sin\beta=-\dfrac{1}{2}[\cos(\alpha+\beta)-\cos(\alpha-\beta)]$
- 注释：
  - 三角式的积和互化、证明
  - 看到两个三角函数相乘要化成和 → 积化和差
- 依赖：
  - 来源：R17
    种类：推出
    方法：作差相消
    步骤：
      1. 【相加】「和差角公式」$\sin(\alpha+\beta)+\sin(\alpha-\beta)=2\sin\alpha\cos\beta$；相减得 $\sin(\alpha+\beta)-\sin(\alpha-\beta)=2\cos\alpha\sin\beta$
      2. 【同除】两边 $\div 2$ 得积化和差
      3. 【相加】$\cos$ 的两式同理：$\cos(\alpha+\beta)+\cos(\alpha-\beta)=2\cos\alpha\cos\beta$，$\cos(\alpha+\beta)-\cos(\alpha-\beta)=-2\sin\alpha\sin\beta$

### P17 辅助角
- 标志：$a\sin x+b\cos x=\sqrt{a^2+b^2}\,\sin(x+\varphi)$
- 区域：三角
- 类型：结论
- 重要度：2
- 条件：定义域$a,b$ 不全为 0；符号分支$\varphi$ 由 $a,b$ 正负定
- 是什么：$\cos\varphi=\dfrac{a}{\sqrt{a^2+b^2}}$，$\sin\varphi=\dfrac{b}{\sqrt{a^2+b^2}}$
- 反例：
  - $a=b=-1$ 应取 $\varphi=\dfrac{5\pi}{4}$；只看 $\tan\varphi=1$ 取 $\dfrac{\pi}{4}$，得 $\sin x+\cos x$，错
- 注释：
  - 同见不等式大厦 R13
  - 配合：先降幂〔R19〕、倍角〔R18〕，再辅助角
  - 看到同角的 $a\sin\omega x+b\cos\omega x$ → 辅助角化成一个正弦
- 依赖：
  - 来源：R17
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕〔符号分支〕：$a,b$ 不全为 0；$\varphi$ 看 $a,b$ 正负
    步骤：
      1. 【提取】提出 $r=\sqrt{a^2+b^2}$：$a\sin x+b\cos x=r\left(\dfrac{a}{r}\sin x+\dfrac{b}{r}\cos x\right)$
      2. 【代换】$\cos\varphi=\dfrac{a}{r}$，$\sin\varphi=\dfrac{b}{r}\Rightarrow=r(\sin x\cos\varphi+\cos x\sin\varphi)$
      3. 【逆用】「sin 和角公式」$=r\sin(x+\varphi)$
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】$\left(\dfrac{a}{r}\right)^2+\left(\dfrac{b}{r}\right)^2=1$，故有 $\varphi$

### P48 海伦公式
- 标志：$S=\sqrt{p(p-a)(p-b)(p-c)}$，$p=\dfrac{a+b+c}{2}$
- 区域：向量
- 类型：结论
- 标签：拓展
- 条件：结构前提$a,b,c$ 为三角形三边
- 是什么：秦九韶三斜求积：$S=\sqrt{\dfrac{1}{4}\left[c^2a^2-\left(\dfrac{c^2+a^2-b^2}{2}\right)^2\right]}$（必修四拓展阅读，与海伦公式等价）
- 注释：
  - 已知三边求面积 → 海伦公式（拓展）
- 依赖：
  - 来源：P20
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔结构前提〕：$a,b,c$ 为三边
    步骤：
      1. 【平方】$S^2=\dfrac{1}{4}a^2b^2\sin^2C=\dfrac{1}{4}a^2b^2(1-\cos^2C)$（「勾股恒等式」）
      2. 【代入】$\cos C=\dfrac{a^2+b^2-c^2}{2ab}$（「余弦定理推论」）
      3. 【分解】两次「平方差」：$S^2=\dfrac{1}{16}[(a+b)^2-c^2][c^2-(a-b)^2]=\dfrac{(a+b+c)(a+b-c)(c+a-b)(c-a+b)}{16}=p(p-a)(p-b)(p-c)$
  - 来源：P22
    种类：前提
    步骤：
      1. 【前提】$\cos C=\dfrac{a^2+b^2-c^2}{2ab}$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】平方差分解

### R26 三角形式乘法
- 标志：$r_1(\cos\theta_1+i\sin\theta_1)\cdot r_2(\cos\theta_2+i\sin\theta_2)$
- 区域：复数
- 类型：结论
- 重要度：2
- 是什么：$=r_1r_2[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)]$；模相乘，辐角相加；几何意义：乘 $r_2(\cos\theta_2+i\sin\theta_2)$ = 把 $\overrightarrow{OZ_1}$ 绕原点逆时针转 $\theta_2$、模变为 $r_2$ 倍；乘 $i$ 即逆时针转 $\dfrac{\pi}{2}$
- 反例：
  - 辐角主值不能直接相加：$z_1=z_2=-1$，主值都是 $\pi$，相加得 $2\pi$，而 $\arg(1)=0$
- 注释：
  - 三角形式相乘 → 模相乘、辐角相加
- 依赖：
  - 来源：P24
    种类：推出
    方法：展开分解
    步骤：
      1. 【展开】两个三角形式按多项式相乘，用 $i^2=-1$：$r_1r_2[(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)+i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)]$
      2. 【合并】实部、虚部分别合并
  - 来源：R17
    种类：推出
    方法：展开分解
    步骤：
      1. 【相乘】实部 $\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2$，虚部 $\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2$
      2. 【逆用】「和角公式」实部 $=\cos(\theta_1+\theta_2)$，虚部 $=\sin(\theta_1+\theta_2)$

### P28 等差求和
- 标志：$S_n=\dfrac{n(a_1+a_n)}{2}=na_1+\dfrac{n(n-1)}{2}d$
- 区域：数列
- 类型：结论
- 重要度：2
- 条件：结构前提等差数列
- 是什么：$S_n=\dfrac{d}{2}n^2+\left(a_1-\dfrac{d}{2}\right)n$；反过来 $S_n=An^2+Bn\iff\{a_n\}$ 等差；$S_{2n-1}=(2n-1)a_n$；两等差数列 $\dfrac{a_n}{b_n}=\dfrac{S_{2n-1}}{T_{2n-1}}$；拓展：$\left\{\dfrac{S_n}{n}\right\}$ 也是等差数列，公差 $\dfrac{d}{2}$
- 反例：
  - $S_n=n^2+1$ 常数项不为 0：$a_1=2$，$a_2=3$，$a_3=5$，不是等差
  - 1, 2, 4, 7：$S_4=14$，而 $\dfrac{4\times(1+7)}{2}=16$
- 注释：
  - 等差求和：知首末项用 $\dfrac{n(a_1+a_n)}{2}$；项数为奇数的前 $n$ 项和（如 $S_9=9a_5$）想到 $S_{2n-1}=(2n-1)a_n$
- 依赖：
  - 来源：P27
    种类：推出
    方法：同除
    步骤：
      1. 【倒序相加】$S_n=a_1+a_2+\cdots+a_n$，$S_n=a_n+a_{n-1}+\cdots+a_1$，对应项和都等于 $a_1+a_n$（「等差下标性质」）
      2. 【同除】$2S_n=n(a_1+a_n)\Rightarrow S_n=\dfrac{n(a_1+a_n)}{2}$

### P52 差比数列求和（错位相减）
- 标志：例：$\displaystyle\sum_{k=1}^{n}k\,q^{k-1}=\dfrac{1-(n+1)q^n+nq^{n+1}}{(1-q)^2}$
- 区域：数列
- 类型：结论
- 重要度：1
- 条件：结构前提$c_n=a_nb_n$，等差×等比；定义域$q\ne 1$
- 是什么：核对 $n=1$：$\dfrac{1-2q+q^2}{(1-q)^2}=1$
- 反例：
  - $q=1$ 时分母为 0，应为 $\sum k=\dfrac{n(n+1)}{2}$
- 注释：
  - 配合：等比求和〔P31〕
  - 通项是“等差 × 等比” → 错位相减
- 依赖：
  - 来源：P31
    种类：推出
    方法：同除
    条件：▼ 加条件〔结构前提〕〔定义域〕：等差×等比；$q\ne 1$
    步骤：
      1. 【错位相减】$S-qS=\sum q^{k-1}-nq^n$
      2. 【代入】「等比求和」$(1-q)S=\dfrac{1-q^n}{1-q}-nq^n$
      3. 【同除】$S=\dfrac{1-(n+1)q^n+nq^{n+1}}{(1-q)^2}$

### R42 平行四边形恒等式、中线长与极化恒等式
- 标志：$|\vec a+\vec b|^2+|\vec a-\vec b|^2=2\left(|\vec a|^2+|\vec b|^2\right)$：平行四边形对角线平方和 = 四边平方和（选必一 2.1 正文）
- 区域：向量
- 类型：中间步
- 是什么：$\vec a\cdot\vec b=\dfrac{1}{2}\left(|\vec a+\vec b|^2-|\vec a|^2-|\vec b|^2\right)$（教材练习）；拓展：极化恒等式 $\vec a\cdot\vec b=\dfrac{1}{4}\left(|\vec a+\vec b|^2-|\vec a-\vec b|^2\right)$；$M$ 为 $BC$ 中点：$\overrightarrow{AB}\cdot\overrightarrow{AC}=|AM|^2-|BM|^2$；中线长：$|AM|^2=\dfrac{1}{4}(2b^2+2c^2-a^2)$
- 注释：
  - 数量积的两个向量共起点、且能找到中点 → 化成“中线平方 − 半边平方”
- 依赖：
  - 来源：P49
    种类：推出
    方法：展开分解
    步骤：
      1. 【相减】$|\vec a+\vec b|^2-|\vec a-\vec b|^2=4\vec a\cdot\vec b$（「完全平方」）
      2. 【分解】$\overrightarrow{AB}=\overrightarrow{AM}+\overrightarrow{MB}$，$\overrightarrow{AC}=\overrightarrow{AM}-\overrightarrow{MB}$
      3. 【相乘】「和×差」$\overrightarrow{AB}\cdot\overrightarrow{AC}=|AM|^2-|BM|^2$
  - 来源：R41
    种类：前提
    步骤：
      1. 【前提】中点：$\overrightarrow{AM}=\dfrac{1}{2}(\overrightarrow{AB}+\overrightarrow{AC})$，平方后用余弦定理推论
  - 来源：P22
    种类：前提
    步骤：
      1. 【前提】$2bc\cos A=b^2+c^2-a^2$

### P67 点到直线、两平行线间的距离
- 标志：点 $P(x_0,y_0)$ 到 $Ax+By+C=0$：$d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：定义域$A,B$ 不全为 0
- 是什么：平行线 $Ax+By+C_1=0$ 与 $Ax+By+C_2=0$：$d=\dfrac{|C_1-C_2|}{\sqrt{A^2+B^2}}$
- 反例：
  - $3x+4y-5=0$ 与 $6x+8y+1=0$：要先化成 $6x+8y-10=0$，$d=\dfrac{11}{10}$；直接用 $\dfrac{|-5-1|}{5}$ 错
- 注释：
  - 点到直线距离 → 代入 $|Ax_0+By_0+C|$，再除以 $\sqrt{A^2+B^2}$
- 依赖：
  - 来源：P57
    种类：推出
    方法：展开分解
    步骤：
      1. 【取点】在直线上取一点 $Q(x_1,y_1)$：$Ax_1+By_1=-C$；法向量 $\vec n=(A,B)$
      2. 【代入】「投影的数量」$d=\dfrac{|\overrightarrow{QP}\cdot\vec n|}{|\vec n|}$
      3. 【展开】$\overrightarrow{QP}\cdot\vec n=A(x_0-x_1)+B(y_0-y_1)=Ax_0+By_0+C\Rightarrow d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$
  - 来源：P65
    种类：前提
    步骤：
      1. 【前提】一般式的法向量 $(A,B)$

### P75 点到平面的距离
- 标志：$d=\dfrac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}$（$A$ 为平面内任一点）
- 区域：空间
- 类型：结论
- 重要度：1
- 条件：定义域$\vec n\ne\vec 0$
- 是什么：直线到平行平面、两平行平面间的距离：都化成点到平面的距离
- 注释：
  - 同源：点到直线的距离〔P67〕，都是向量在法向量上的投影
  - 点到平面的距离 → 平面内任取一点连向该点，求在法向量上的投影
- 依赖：
  - 来源：P57
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$\vec n\ne\vec 0$
    步骤：
      1. 【代入】「投影的数量」$\overrightarrow{AP}$ 在法向量 $\vec n$ 方向上投影的绝对值：$d=\dfrac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}$
  - 来源：P74
    种类：前提
    步骤：
      1. 【前提】先求法向量

### P82 回归直线（最小二乘法）与相关系数
- 标志：$\hat y=\hat bx+\hat a$：$\hat b=\dfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}=\dfrac{\sum x_iy_i-n\bar x\bar y}{\sum x_i^2-n\bar x^2}$，$\hat a=\bar y-\hat b\bar x$
- 区域：概率统计
- 类型：结论
- 条件：定义域$\sum(x_i-\bar x)^2\ne 0$
- 是什么：最小二乘：使残差 $e_i=y_i-\hat y_i$ 的平方和 $\sum(y_i-\hat bx_i-\hat a)^2$ 最小；回归直线一定过 $(\bar x,\bar y)$：$\hat y-\bar y=\hat b(x-\bar x)$（点斜式）；$x$ 每增加 1，$\hat y$ 平均增加 $\hat b$；相关系数 $r=\dfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2\sum(y_i-\bar y)^2}}$，$|r|\le 1$，$|r|$ 越接近 1 线性相关越强；$r>0$ 正相关，$r<0$ 负相关；$|r|=1\iff$ 所有点都在回归直线上；拓展阅读：$r=\cos\langle\vec a,\vec b\rangle$，$\vec a=(x_1-\bar x,\cdots,x_n-\bar x)$，$\vec b=(y_1-\bar y,\cdots,y_n-\bar y)$；非线性回归：如 $y=b\sqrt{x}+a$，令 $u=\sqrt{x}$ 化成线性回归
- 注释：
  - 同见不等式大厦 R66：$|r|\le 1$ 由柯西不等式得到
  - 求回归方程 → 先算 $\bar x,\bar y$，再求 $\hat b$，最后 $\hat a=\bar y-\hat b\bar x$
- 依赖：
  - 来源：R49
    种类：推出
    方法：配凑
    条件：▼ 加条件〔定义域〕：$x_i$ 不全相等
    步骤：
      1. 【配方】$Q(a,b)=\sum(y_i-bx_i-a)^2$ 先对 $a$ 配方 $\Rightarrow a=\bar y-b\bar x$
      2. 【配方】再对 $b$ 配方
  - 来源：P01
    种类：前提
    步骤：
      1. 【前提】二次式配方求最小值

### R50 旋转公式（向量、点绕原点旋转）
- 标志：$\overrightarrow{OP}=(a,b)$ 绕原点逆时针转 $\theta$：$(a\cos\theta-b\sin\theta,\ a\sin\theta+b\cos\theta)$
- 区域：向量
- 类型：结论
- 重要度：1
- 是什么：转 $\dfrac{\pi}{2}$：$(x,y)\to(-y,x)$；顺时针转 $\dfrac{\pi}{2}$：$(x,y)\to(y,-x)$；复数说法：乘 $\cos\theta+i\sin\theta$；乘 $i$ 即逆时针转 $\dfrac{\pi}{2}$
- 注释：
  - 同源：三角形式乘法“辐角相加”〔R26〕
  - 点或向量绕原点转一个角 → 旋转公式（或乘 $\cos\theta+i\sin\theta$）
- 依赖：
  - 来源：R17
    种类：推出
    方法：展开分解
    步骤：
      1. 【设】$a=r\cos\varphi$，$b=r\sin\varphi$，转后为 $(r\cos(\varphi+\theta),\ r\sin(\varphi+\theta))$
      2. 【展开】「和角公式」$r\cos(\varphi+\theta)=a\cos\theta-b\sin\theta$，$r\sin(\varphi+\theta)=a\sin\theta+b\cos\theta$
  - 来源：R41
    种类：前提
    步骤：
      1. 【前提】向量的坐标

### P92 分期付款（等额本息）、现值
- 标志：现值：$A_0(1+r)^n=A\Rightarrow A_0=\dfrac{A}{(1+r)^n}$
- 区域：数列
- 类型：结论
- 条件：结构前提每期利率 $r$，按复利计算
- 是什么：等额本息：$\dfrac{x}{1+r}+\dfrac{x}{(1+r)^2}+\cdots+\dfrac{x}{(1+r)^m}=A_0\Rightarrow x=\dfrac{A_0r(1+r)^m}{(1+r)^m-1}$；等额本金：每期还 $\dfrac{A_0}{m}$ 加剩余本金的利息，各期还款额成递减的等差数列
- 注释：
  - 分期付款 → 把每期还款折算到同一时刻，用等比求和
- 依赖：
  - 来源：P31
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：复利
    步骤：
      1. 【代换】各期还款的现值成等比数列，公比 $\dfrac{1}{1+r}$
      2. 【代入】「等比求和」

### P93 无穷递缩等比数列的和
- 标志：$S=\displaystyle\lim_{n\to\infty}S_n=\dfrac{a_1}{1-q}$（$|q|<1$）
- 区域：数列
- 类型：结论
- 标签：拓展
- 条件：定义域$-1<q<1$
- 是什么：循环小数化分数：$0.\dot 3=\dfrac{0.3}{1-0.1}=\dfrac{1}{3}$
- 反例：
  - $q=2$：$1+2+4+\cdots$ 没有和，不能写 $\dfrac{1}{1-2}=-1$
- 注释：
  - 无限多项的等比求和、循环小数化分数 → $\dfrac{a_1}{1-q}$（先验 $|q|<1$）
- 依赖：
  - 来源：P31
    种类：推出
    方法：回到定义
    条件：▼ 加条件〔定义域〕：$|q|<1$
    步骤：
      1. 【取极限】$|q|<1$ 时 $q^n\to 0$（老教材数列极限）

### P100 三余弦公式与面积射影
- 标志：三余弦：$\cos\theta=\cos\theta_1\cos\theta_2$（$\theta$ 为斜线与面内直线所成角）
- 区域：空间
- 类型：结论
- 条件：结构前提$\theta_1$ 为斜线与平面所成角，$\theta_2$ 为射影与面内直线所成角
- 是什么：推论：线面角是斜线与平面内所有直线所成角中最小的；射影长 $A'B'=AB\cos\theta$；面积射影 $S'=S\cos\theta$（$\theta$ 为两平面所成的锐二面角）；拓展（老教材）：异面直线上两点距离 $EF=\sqrt{d^2+m^2+n^2\mp 2mn\cos\theta}$（由三向量和的模平方推出）
- 注释：
  - 已知射影面积和原面积 → 二面角的余弦是面积比
- 依赖：
  - 来源：P74
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔结构前提〕：斜线与射影
    步骤：
      1. 【作垂线】斜线 $PA$ 交平面于 $A$，$PO\perp$ 平面于 $O$，$AO$ 为射影；面内直线 $l$ 过 $A$，作 $OB\perp l$ 于 $B$，连 $PB$
      2. 【定义】「线面垂直判定」$l\perp PO$，$l\perp OB\Rightarrow l\perp$ 平面 $POB\Rightarrow l\perp PB$
      3. 【作比】$\mathrm{Rt}\triangle PAO$：$\cos\theta_1=\dfrac{AO}{PA}$；$\mathrm{Rt}\triangle AOB$：$\cos\theta_2=\dfrac{AB}{AO}$（$\theta_1$ 斜线与射影所成角，$\theta_2$ 射影与 $l$ 所成角）
      4. 【相乘】$\cos\theta_1\cos\theta_2=\dfrac{AB}{PA}=\cos\theta$（$\mathrm{Rt}\triangle PBA$）
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】直角三角形中的余弦

### R57 统计量：位置量、直方图、加权平均、分层抽样
- 标志：求和符号：$\sum(x_i+y_i)=\sum x_i+\sum y_i$，$\sum kx_i=k\sum x_i$，$\sum_{i=1}^n t=nt$；$\sum(x_i-\bar x)=0$
- 区域：概率统计
- 类型：中间步
- 是什么：中位数：$2n+1$ 个数取第 $n+1$ 个，$2n$ 个数取中间两个的平均；众数；极差；标准差 $s=\sqrt{s^2}$；$p\%$ 分位数：排序后算 $i=n\cdot p\%$；$i$ 不是整数取第 $\lceil i\rceil$ 个，是整数取第 $i$、$i+1$ 个的平均；按频率加权：$\bar x=\sum x_ip_i$，$s^2=\sum(x_i-\bar x)^2p_i$（与 $E(X)$、$D(X)$ 同形）；频率分布直方图：纵轴“频率/组距”，小矩形面积 = 频率，面积和 = 1；平均数 ≈ 各组中点 × 频率之和；分层抽样按比例：$\dfrac{n_i}{n}=\dfrac{N_i}{N}$
- 注释：
  - 直方图问题 → 面积 = 频率，面积和为 1；求百分位数 → 先排序，看 $np\%$ 是否为整数
- 依赖：
  - 来源：R49
    种类：推出
    方法：展开分解
    步骤：
      1. 【合并】同值的数据合并，频率作权，就是加权平均
  - 来源：S20
    种类：前提
    步骤：
      1. 【前提】与均值、方差的定义同形

## 第 6 层　推导第 6 层

### P03 韦达定理
- 标志：$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$（重根算两个）
- 区域：代数
- 类型：结论
- 重要度：2
- 条件：定义域$a\ne 0$，$x_1,x_2$ 为两实根（$\Delta\ge 0$）
- 是什么：$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$（重根算两个）
- 反例：
  - $x^2+x+1=0$：$\Delta=-3<0$，照公式得 $x_1+x_2=-1$，但实根不存在
- 注释：
  - 同见不等式大厦 R52；同见二次函数大厦 J06
  - 二次函数大厦 R11（根的符号）；不等式大厦 R34
  - 配合：互换式〔R07〕
  - 不解方程求两根的式子 → 韦达
- 依赖：
  - 来源：P02
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$x_1,x_2$ 为两实根（$\Delta\ge 0$）
    步骤：
      1. 【代入】$x_{1,2}=\dfrac{-b\pm\sqrt{\Delta}}{2a}$
      2. 【相加】$x_1+x_2=\dfrac{-2b}{2a}=-\dfrac{b}{a}$
      3. 【相乘】「平方差」$x_1x_2=\dfrac{b^2-\Delta}{4a^2}=\dfrac{4ac}{4a^2}=\dfrac{c}{a}$
  - 来源：R02
    种类：前提
    步骤：
      1. 【前提】$\dfrac{(-b)^2-\Delta}{4a^2}=\dfrac{c}{a}$

### P09 换底推论
- 标志：$\log_a b\cdot\log_b a=1$（$a,b>0$ 且 $\ne 1$）
- 区域：指数与对数
- 类型：结论
- 条件：定义域底数 $>0$ 且 $\ne 1$
- 是什么：$\log_{a^m}b^n=\dfrac{n}{m}\log_a b$（$m\ne 0$）；链式：$\log_a b\cdot\log_b c=\log_a c$（$c>0$）；例 $\log_2 3\cdot\log_3 8=\log_2 8=3$
- 注释：
  - 对数式化简求值
  - 看到 $\log_a b\cdot\log_b c$ 连乘 → 链式相消
- 依赖：
  - 来源：P08
    种类：推出
    方法：代换
    步骤：
      1. 【代换】「换底公式」都换成以 $c$ 为底（取 $c=10$）：$\log_a b\cdot\log_b a=\dfrac{\lg b}{\lg a}\cdot\dfrac{\lg a}{\lg b}=1$
      2. 【代换】「换底公式」$\log_{a^m}b^n=\dfrac{\lg b^n}{\lg a^m}=\dfrac{n\lg b}{m\lg a}=\dfrac{n}{m}\log_a b$（「对数运算律」）

### R38 同角关系的常用变形
- 标志：$(\sin\alpha\pm\cos\alpha)^2=1\pm 2\sin\alpha\cos\alpha=1\pm\sin 2\alpha$
- 区域：三角
- 类型：结论
- 重要度：1
- 是什么：“1”的代换：$1=\sin^2\alpha+\cos^2\alpha$
- 注释：
  - 看到 $\sin\alpha\pm\cos\alpha$ 与 $\sin\alpha\cos\alpha$ → 两边平方互求
- 依赖：
  - 来源：R18
    种类：推出
    方法：代换
    步骤：
      1. 【展开】「完全平方」$(\sin\alpha\pm\cos\alpha)^2=\sin^2\alpha\pm 2\sin\alpha\cos\alpha+\cos^2\alpha$
      2. 【代换】$\sin^2\alpha+\cos^2\alpha=1$（「勾股恒等式」），$2\sin\alpha\cos\alpha=\sin 2\alpha$（「倍角」）$\Rightarrow 1\pm 2\sin\alpha\cos\alpha=1\pm\sin 2\alpha$
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】$\sin^2\alpha+\cos^2\alpha=1$ 合并
  - 来源：R03
    种类：前提
    步骤：
      1. 【前提】完全平方

### P15 正切倍角
- 标志：$\tan 2\alpha=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$
- 区域：三角
- 类型：结论
- 条件：定义域$\tan\alpha$、$\tan 2\alpha$ 有定义
- 是什么：即 $\alpha\ne\dfrac{\pi}{2}+k\pi$ 且 $\alpha\ne\dfrac{\pi}{4}+\dfrac{k\pi}{2}$
- 注释：
  - 已知 $\tan\alpha$ 求 $\tan 2\alpha$
  - 已知 $\tan\alpha$ 求 $\tan 2\alpha$ → 正切倍角
- 依赖：
  - 来源：P14
    种类：推出
    方法：特例
    步骤：
      1. 【特例】令 $\beta=\alpha$：$\tan 2\alpha=\dfrac{\tan\alpha+\tan\alpha}{1-\tan\alpha\tan\alpha}=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$

### R19 降幂
- 标志：$\cos^2\alpha=\dfrac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\dfrac{1-\cos 2\alpha}{2}$
- 区域：三角
- 类型：中间步
- 是什么：$\sin\alpha\cos\alpha=\dfrac{1}{2}\sin 2\alpha$；升幂：$1+\cos 2\alpha=2\cos^2\alpha$，$1-\cos 2\alpha=2\sin^2\alpha$
- 注释：
  - 配合：$\sqrt{1+\cos 2\alpha}=\sqrt{2}|\cos\alpha|$，开方要用〔P43〕定号
  - 求周期、最值、单调性时看到 $\sin^2$、$\cos^2$ → 降幂；看到 $1\pm\cos 2\alpha$ → 升幂
- 依赖：
  - 来源：R18
    种类：推出
    方法：同除
    步骤：
      1. 【移项】$\cos 2\alpha=2\cos^2\alpha-1\Rightarrow 2\cos^2\alpha=1+\cos 2\alpha$；$\cos 2\alpha=1-2\sin^2\alpha\Rightarrow 2\sin^2\alpha=1-\cos 2\alpha$
      2. 【同除】两边 $\div 2\Rightarrow\cos^2\alpha=\dfrac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\dfrac{1-\cos 2\alpha}{2}$

### R21 和差化积
- 标志：$\sin\theta+\sin\varphi=2\sin\dfrac{\theta+\varphi}{2}\cos\dfrac{\theta-\varphi}{2}$
- 区域：三角
- 类型：中间步
- 是什么：$\sin\theta-\sin\varphi=2\cos\dfrac{\theta+\varphi}{2}\sin\dfrac{\theta-\varphi}{2}$；$\cos\theta+\cos\varphi=2\cos\dfrac{\theta+\varphi}{2}\cos\dfrac{\theta-\varphi}{2}$；$\cos\theta-\cos\varphi=-2\sin\dfrac{\theta+\varphi}{2}\sin\dfrac{\theta-\varphi}{2}$
- 注释：
  - 互逆：积化和差〔R20〕
  - 三角式的积和互化、证明
  - 看到两个三角函数相加减要化成积 → 和差化积
- 依赖：
  - 来源：R20
    种类：推出
    方法：代换
    步骤：
      1. 【代换】令 $\alpha+\beta=\theta$，$\alpha-\beta=\varphi\Rightarrow\alpha=\dfrac{\theta+\varphi}{2}$，$\beta=\dfrac{\theta-\varphi}{2}$
      2. 【代入】代入积化和差，左右互换即和差化积

### P18 万能公式
- 标志：令 $t=\tan\dfrac{\alpha}{2}$：$\sin\alpha=\dfrac{2t}{1+t^2}$，$\cos\alpha=\dfrac{1-t^2}{1+t^2}$
- 区域：三角
- 类型：结论
- 标签：拓展
- 条件：定义域$\alpha\ne\pi+2k\pi$
- 是什么：$\tan\alpha=\dfrac{2t}{1-t^2}$（还要 $t^2\ne 1$）
- 注释：
  - 三角式化成有理式（换元）
  - 要把三角式化成 $\tan\dfrac{\alpha}{2}$ 的有理式 → 万能公式（拓展）
- 依赖：
  - 来源：R18
    种类：推出
    方法：同除
    条件：▼ 加条件〔定义域〕：$\alpha\ne\pi+2k\pi$
    步骤：
      1. 【补形】倍角写成分式，分母补上 $1=\sin^2\dfrac{\alpha}{2}+\cos^2\dfrac{\alpha}{2}$（「勾股恒等式」）：$\sin\alpha=\dfrac{2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}}{\sin^2\frac{\alpha}{2}+\cos^2\frac{\alpha}{2}}$
      2. 【同除】分子、分母 $\div\cos^2\dfrac{\alpha}{2}\Rightarrow\sin\alpha=\dfrac{2t}{1+t^2}$（$t=\tan\dfrac{\alpha}{2}$）
      3. 【同除】$\cos\alpha$ 同理：$\cos\alpha=\dfrac{\cos^2\frac{\alpha}{2}-\sin^2\frac{\alpha}{2}}{\sin^2\frac{\alpha}{2}+\cos^2\frac{\alpha}{2}}=\dfrac{1-t^2}{1+t^2}$

### P25 三角形式除法
- 标志：$\dfrac{z_1}{z_2}=\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]$
- 区域：复数
- 类型：结论
- 条件：定义域$z_2\ne 0$
- 是什么：$\dfrac{z_1}{z_2}=\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]$
- 注释：
  - 复数计算
- 依赖：
  - 来源：R26
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$z_2\ne 0$
    步骤：
      1. 【相乘】$\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]\cdot r_2(\cos\theta_2+i\sin\theta_2)=r_1(\cos\theta_1+i\sin\theta_1)=z_1$（「三角形式乘法」）
      2. 【逆用】「除法是乘法的逆运算」：商乘 $z_2$ 等于 $z_1$，所以它就是 $\dfrac{z_1}{z_2}$

### R27 棣莫弗公式
- 标志：$[r(\cos\theta+i\sin\theta)]^n=r^n(\cos n\theta+i\sin n\theta)$（$n$ 为正整数；教材习题推广到一切整数 $n$，$z\ne 0$）
- 区域：复数
- 类型：结论
- 重要度：1
- 是什么：$[r(\cos\theta+i\sin\theta)]^n=r^n(\cos n\theta+i\sin n\theta)$（$n$ 为正整数；教材习题推广到一切整数 $n$，$z\ne 0$）
- 注释：
  - 教材必修四 10.3
  - 复数的乘方、方根
  - 复数的高次幂 → 先看能否用 $(1\pm i)^2=\pm 2i$ 或 $i^n$ 的周期；不行再化三角形式用棣莫弗
- 依赖：
  - 来源：R26
    种类：推出
    方法：归纳
    步骤：
      1. 【特例】$n=1$ 成立
      2. 【归纳】「数学归纳法」设 $n=k$ 成立：$z^k=r^k(\cos k\theta+i\sin k\theta)$
      3. 【相乘】$z^{k+1}=z^k\cdot z$：模相乘、辐角相加（「三角形式乘法」）$\Rightarrow r^{k+1}[\cos(k+1)\theta+i\sin(k+1)\theta]$
  - 来源：S10
    种类：前提
    步骤：
      1. 【前提】数学归纳法

### R29 自然数求和
- 标志：$1+2+\cdots+n=\dfrac{n(n+1)}{2}$
- 区域：数列
- 类型：中间步
- 是什么：$a_k=k$ 本身是等差数列，无需另加条件
- 注释：
  - 看到 $1+2+\cdots+n$ → $\dfrac{n(n+1)}{2}$
- 依赖：
  - 来源：P28
    种类：推出
    方法：代换
    步骤：
      1. 【特例】$a_1=1$，$d=1$
      2. 【代入】$S_n=n\cdot 1+\dfrac{n(n-1)}{2}\cdot 1=\dfrac{n(n+1)}{2}$

### P54 片段和（选必三复习题）
- 标志：等差：$S_m,\ S_{2m}-S_m,\ S_{3m}-S_{2m}$ 成等差（公差 $m^2d$）
- 区域：数列
- 类型：结论
- 条件：结构前提等差、等比
- 是什么：等比：片段和都不为 0 时成等比（公比 $q^m$）
- 反例：
  - $q=-1$，$m=2$：片段和都是 0，$0,0,0$ 不是等比数列
- 注释：
  - 等差、等比的前 $m$、$2m$、$3m$ 项和 → 片段和
- 依赖：
  - 来源：P28
    种类：推出
    方法：分类讨论
    步骤：
      1. 【作差】等差：相邻片段和相减 $(S_{2m}-S_m)-S_m$
      2. 【分组】对应项都相差 $md$，共 $m$ 项 $\Rightarrow$ 差为 $m^2d$
  - 来源：P29
    种类：前提
    步骤：
      1. 等比：【作比】$S_{2m}-S_m=q^mS_m$（每项乘 $q^m$）

### P53 裂项的其他形式
- 标志：$\dfrac{1}{k(k+d)}=\dfrac{1}{d}\left(\dfrac{1}{k}-\dfrac{1}{k+d}\right)$
- 区域：数列
- 类型：结论
- 重要度：1
- 条件：定义域$d\ne 0$；根式形 $k\ge 0$
- 是什么：$\dfrac{1}{\sqrt{k}+\sqrt{k+1}}=\sqrt{k+1}-\sqrt{k}$；一般：$\{a_n\}$ 等差、$d\ne 0$、各项 $\ne 0$：$\dfrac{1}{a_ka_{k+1}}=\dfrac{1}{d}\left(\dfrac{1}{a_k}-\dfrac{1}{a_{k+1}}\right)$；例 $\dfrac{1}{(2k-1)(2k+1)}=\dfrac{1}{2}\left(\dfrac{1}{2k-1}-\dfrac{1}{2k+1}\right)$
- 注释：
  - 同见不等式大厦 P25、P54、P55
  - 通项是 $\dfrac{1}{a_ka_{k+1}}$ 或 $\dfrac{1}{\sqrt{k}+\sqrt{k+1}}$ → 裂项
- 依赖：
  - 来源：R30
    种类：推出
    方法：同除
    条件：▼ 加条件〔定义域〕：$d\ne 0$
    步骤：
      1. 【推广】仿 $\dfrac{1}{k(k+1)}$：两个因式相差 $d$ 时
      2. 【通分】右边 $\dfrac{1}{d}\cdot\dfrac{(k+d)-k}{k(k+d)}=\dfrac{1}{k(k+d)}$
      3. 【同乘】根式型：分子分母同乘 $\sqrt{k+1}-\sqrt{k}$（分母有理化，「平方差」）
  - 来源：P44
    种类：前提
    步骤：
      1. 【同乘】根式形用分母有理化

### P40 一般指数、对数求导的由来
- 标志：$(a^x)'=a^x\ln a$，$(\log_a x)'=\dfrac{1}{x\ln a}$
- 区域：导数
- 类型：结论
- 标签：拓展
- 条件：定义域$a>0,\ a\ne 1$；对数式 $x>0$
- 是什么：$(a^x)'=a^x\ln a$，$(\log_a x)'=\dfrac{1}{x\ln a}$
- 注释：
  - 一般指数、对数函数求导
  - 底数不是 $e$ 的指数、对数 → $a^x\ln a$、$\dfrac{1}{x\ln a}$
- 依赖：
  - 来源：P05
    种类：推出
    方法：回到定义
    步骤：
      1. 【代换】$a^x=e^{x\ln a}$
      2. 【求导】$(a^x)'=e^{x\ln a}\cdot\ln a=a^x\ln a$（「链式法则」）
  - 来源：P08
    种类：推出
    方法：回到定义
    步骤：
      1. 【代换】$\log_a x=\dfrac{\ln x}{\ln a}$（「换底公式」）
      2. 【求导】$(\log_a x)'=\dfrac{1}{\ln a}(\ln x)'=\dfrac{1}{x\ln a}$
  - 来源：P39
    种类：前提
    步骤：
      1. 【前提】$(\ln x)'=\dfrac{1}{x}$
  - 来源：P06
    种类：前提
    步骤：
      1. 【前提】$a=e^{\ln a}$
  - 来源：S12
    种类：前提
    步骤：
      1. 【前提】链式法则；$(e^x)'=e^x$

### R44 三倍角
- 标志：$\sin 3\alpha=3\sin\alpha-4\sin^3\alpha$
- 区域：三角
- 类型：中间步
- 标签：拓展
- 是什么：$\cos 3\alpha=4\cos^3\alpha-3\cos\alpha$
- 注释：
  - 看到 $3\alpha$ 与 $\alpha$ 同时出现 → 拆成 $2\alpha+\alpha$，或直接用三倍角（拓展）
- 依赖：
  - 来源：R17
    种类：推出
    方法：代换
    步骤：
      1. 【拆角】$\sin 3\alpha=\sin(2\alpha+\alpha)=\sin 2\alpha\cos\alpha+\cos 2\alpha\sin\alpha$（「和角公式」）
      2. 【代换】「倍角」「勾股恒等式」化成只含 $\sin\alpha$：$=2\sin\alpha(1-\sin^2\alpha)+(1-2\sin^2\alpha)\sin\alpha=3\sin\alpha-4\sin^3\alpha$
      3. 【代换】$\cos 3\alpha$ 同理：$=(2\cos^2\alpha-1)\cos\alpha-2\sin^2\alpha\cos\alpha=4\cos^3\alpha-3\cos\alpha$
  - 来源：R18
    种类：前提
    步骤：
      1. 【前提】倍角
  - 来源：R13
    种类：前提
    步骤：
      1. 【前提】$\cos^2\alpha=1-\sin^2\alpha$

### P60 三角形中的正切恒等式
- 标志：$\tan A+\tan B+\tan C=\tan A\tan B\tan C$
- 区域：向量
- 类型：结论
- 标签：拓展
- 条件：结构前提$A+B+C=\pi$，且都不是直角
- 是什么：$\tan A+\tan B+\tan C=\tan A\tan B\tan C$
- 注释：
  - 三角形中三个正切的和与积同时出现 → 正切恒等式
- 依赖：
  - 来源：P19
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：三个角都不是直角
    步骤：
      1. 【代入】$\tan(A+B)=-\tan C$ 代入「正切和角变形」$\tan A+\tan B=\tan(A+B)(1-\tan A\tan B)\Rightarrow\tan A+\tan B=-\tan C+\tan A\tan B\tan C$
      2. 【移项】$\tan A+\tan B+\tan C=\tan A\tan B\tan C$
  - 来源：P14
    种类：前提
    步骤：
      1. 【前提】正切和角的变形

### P64 正弦型函数 $y=A\sin(\omega x+\varphi)$
- 标志：周期 $T=\dfrac{2\pi}{|\omega|}$，频率 $f=\dfrac{1}{T}$；振幅 $A$、初相 $\varphi$；最大值 $|A|$，最小值 $-|A|$
- 区域：函数性质
- 类型：结论
- 重要度：2
- 条件：定义域$\omega\ne 0$，$A\ne 0$
- 是什么：余弦曲线：对称轴 $x=k\pi$，对称中心 $\left(\dfrac{\pi}{2}+k\pi,0\right)$；正弦曲线：对称轴 $x=\dfrac{\pi}{2}+k\pi$，对称中心 $(k\pi,0)$；由 $y=\sin x$：向左（$\varphi>0$）或向右平移 $|\varphi|$ → 横坐标变为 $\dfrac{1}{\omega}$ 倍 → 纵坐标变为 $A$ 倍（$\omega>0$，$A>0$）；对称轴：$\omega x+\varphi=\dfrac{\pi}{2}+k\pi$；对称中心：$\omega x+\varphi=k\pi$，纵坐标 0；增区间（$\omega>0$，$A>0$）：$-\dfrac{\pi}{2}+2k\pi\le\omega x+\varphi\le\dfrac{\pi}{2}+2k\pi$
- 反例：
  - $y=\sin(-2x)$ 的周期是 $\pi$，不是 $-\pi$：周期要用 $|\omega|$
- 注释：
  - 化成 $A\sin(\omega x+\varphi)$ 之后 → 把 $\omega x+\varphi$ 当整体，代入 $\sin$ 的性质
- 依赖：
  - 来源：R45
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：$\omega\ne 0$，$A\ne 0$
    步骤：
      1. 【平移】$x\to x+\varphi$：$y=\sin x\Rightarrow y=\sin(x+\varphi)$
      2. 【伸缩】$x\to\omega x$：$y=\sin(x+\varphi)\Rightarrow y=\sin(\omega x+\varphi)$
      3. 【同乘】乘 $A$：$y=\sin(\omega x+\varphi)\Rightarrow y=A\sin(\omega x+\varphi)$
  - 来源：S15
    种类：前提
    步骤：
      1. 【前提】周期定义：$\sin\left[\omega\left(x+\dfrac{2\pi}{\omega}\right)+\varphi\right]=\sin(\omega x+\varphi+2\pi)$
  - 来源：R14
    种类：前提
    步骤：
      1. 【前提】诱导公式 ①：$\sin(\alpha+2\pi)=\sin\alpha$
  - 来源：P17
    种类：前提
    步骤：
      1. 【前提】辅助角把 $a\sin\omega x+b\cos\omega x$ 化成一个正弦

### P66 两直线平行与垂直
- 标志：$l_1\parallel l_2\iff k_1=k_2$ 且 $b_1\ne b_2$；$l_1\perp l_2\iff k_1k_2=-1$
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：定义域斜率式要求两条斜率都存在
- 是什么：一般式：$l_1\perp l_2\iff A_1A_2+B_1B_2=0$；$l_1\parallel l_2\Rightarrow A_1B_2-A_2B_1=0$（还要排除重合）；重合 $\iff$ 有 $\lambda$ 使 $A_1=\lambda A_2$，$B_1=\lambda B_2$，$C_1=\lambda C_2$；$Ax+By+C_1=0$ 与 $Ax+By+C_2=0$ 平行 $\iff C_1\ne C_2$；相交 $\iff A_1B_2\ne A_2B_1$；与 $Ax+By+C=0$ 平行的设 $Ax+By+m=0$，垂直的设 $Bx-Ay+m=0$；拓展：夹角 $\tan\theta=\left|\dfrac{k_2-k_1}{1+k_1k_2}\right|$（$1+k_1k_2\ne 0$）；到角（老教材，有方向）$\tan\theta=\dfrac{k_2-k_1}{1+k_1k_2}$
- 反例：
  - $x=1$ 与 $y=2$ 垂直，但 $x=1$ 没有斜率，$k_1k_2=-1$ 用不上
- 注释：
  - 两直线垂直 → 一般式 $A_1A_2+B_1B_2=0$，不用讨论斜率
- 依赖：
  - 来源：P49
    种类：推出
    方法：代换
    步骤：
      1. 【定义】法向量 $\vec n_1=(A_1,B_1)$，$\vec n_2=(A_2,B_2)$
      2. 【代入】「垂直的坐标条件」两直线垂直 $\iff(A_1,B_1)\perp(A_2,B_2)\iff A_1A_2+B_1B_2=0$
      3. 【代入】「共线的坐标条件」平行或重合 $\iff$ 法向量共线（平行还要排除重合）
  - 来源：P65
    种类：前提
    步骤：
      1. 【前提】法向量 $(A,B)$；$k=-\dfrac{A}{B}$，$k_1k_2=-1\iff A_1A_2=-B_1B_2$
  - 来源：P14
    种类：前提
    步骤：
      1. 【前提】夹角：$\tan(\alpha_2-\alpha_1)$ 用正切差角

### P69 直线与圆：位置关系、弦长、切线
- 标志：$d<r$ 相交，$d=r$ 相切，$d>r$ 相离
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：结构前提$d$ 为圆心到直线的距离，$r$ 为半径
- 是什么：弦长 $|AB|=2\sqrt{r^2-d^2}$；圆 $x^2+y^2=r^2$ 上一点 $(x_0,y_0)$ 处的切线：$x_0x+y_0y=r^2$；两圆：圆心距 $d$ 与 $r_1+r_2$、$|r_1-r_2|$ 比较；两圆相交时，两方程相减得公共弦所在直线；外离 $d>r_1+r_2$，外切 $d=r_1+r_2$，相交 $|r_1-r_2|<d<r_1+r_2$，内切 $d=|r_1-r_2|$，内含 $d<|r_1-r_2|$
- 注释：
  - 直线与圆的问题 → 先算圆心到直线的距离 $d$，再与 $r$ 比
- 依赖：
  - 来源：P67
    种类：推出
    方法：互逆
    步骤：
      1. 【作垂线】圆心到弦作垂线，平分弦（「垂径定理」）：半弦长、$d$、$r$ 构成直角三角形
      2. 【开平方】「勾股定理」$\left(\dfrac{|AB|}{2}\right)^2+d^2=r^2\Rightarrow|AB|=2\sqrt{r^2-d^2}$
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】垂径定理、勾股定理
  - 来源：P49
    种类：前提
    步骤：
      1. 【前提】切线垂直于半径：$(x-x_0,\ y-y_0)\cdot(x_0,y_0)=0$，展开用 $x_0^2+y_0^2=r^2$

### R54 斐波那契数列
- 标志：$F_1=F_2=1$，$F_n=F_{n-1}+F_{n-2}$（$n\ge 3$）：1，1，2，3，5，8，13，…
- 区域：数列
- 类型：中间步
- 是什么：拓展：$F_n=\dfrac{1}{\sqrt{5}}\left[\left(\dfrac{1+\sqrt{5}}{2}\right)^n-\left(\dfrac{1-\sqrt{5}}{2}\right)^n\right]$，底数是 $x^2=x+1$ 的两根
- 注释：
  - 递推数列的典型例子（选必三 5.1.2 例 2）
  - 后一项等于前两项之和 → 斐波那契数列
- 依赖：
  - 来源：S09
    种类：推出
    方法：作差相消
    步骤：
      1. 【相加】每项由前两项相加
  - 来源：P02
    种类：前提
    步骤：
      1. 【前提】通项的底数是 $x^2-x-1=0$ 的两根

## 第 7 层　推导第 7 层

### P04 交点式
- 标志：$ax^2+bx+c=a(x-x_1)(x-x_2)$
- 区域：代数
- 类型：结论
- 条件：定义域$\Delta\ge 0$（实根存在）
- 是什么：$ax^2+bx+c=a(x-x_1)(x-x_2)$
- 注释：
  - 同见二次函数大厦 P01
  - 不等式大厦 R34（三个二次）
  - 已知两根或两个零点 → 交点式
- 依赖：
  - 来源：P03
    种类：推出
    方法：代换
    步骤：
      1. 【展开】右边 $a(x-x_1)(x-x_2)=a[x^2-(x_1+x_2)x+x_1x_2]$
      2. 【代入】「韦达定理」$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$：$=a\left(x^2+\dfrac{b}{a}x+\dfrac{c}{a}\right)=ax^2+bx+c$（对比系数）
  - 来源：P02
    种类：前提
    步骤：
      1. 【因式分解】求出两根后写成 $a(x-x_1)(x-x_2)$（另一路）

### P45 两根的对称式
- 标志：$x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2$；$\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{x_1+x_2}{x_1x_2}$（$c\ne 0$）
- 区域：代数
- 类型：结论
- 重要度：2
- 条件：定义域$x_1,x_2$ 为两实根（$\Delta\ge 0$）
- 是什么：$|x_1-x_2|=\sqrt{(x_1+x_2)^2-4x_1x_2}=\dfrac{\sqrt{\Delta}}{|a|}$
- 反例：
  - $x^2+x+1=0$ 无实根，硬套得 $x_1^2+x_2^2=(-1)^2-2=-1$，实数平方和不可能为负
- 注释：
  - 解析几何——联立消元后求弦长、中点
  - 配合：弦长 $|AB|=\sqrt{1+k^2}\,|x_1-x_2|$
  - 看到 $x_1^2+x_2^2$、$|x_1-x_2|$ → 韦达代入互换式
- 依赖：
  - 来源：P03
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：两实根，$\Delta\ge 0$
    步骤：
      1. 【代入】「韦达定理」代入「互换式」，如 $x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2=\dfrac{b^2}{a^2}-\dfrac{2c}{a}$
  - 来源：R07
    种类：前提
    步骤：
      1. 【前提】互换式

### P16 半角
- 标志：$\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$，$\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$
- 区域：三角
- 类型：结论
- 重要度：1
- 条件：符号分支± 由 $\frac{\alpha}{2}$ 所在象限定
- 是什么：$\tan\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{1+\cos\alpha}}$（$\cos\alpha\ne -1$，± 同样按象限定）；$\tan\dfrac{\alpha}{2}=\dfrac{\sin\alpha}{1+\cos\alpha}=\dfrac{1-\cos\alpha}{\sin\alpha}$（无 ±；前式 $\cos\alpha\ne -1$，后式 $\sin\alpha\ne 0$）
- 反例：
  - $\alpha=300^\circ$：$\cos 150^\circ=-\dfrac{\sqrt{3}}{2}$，取正号得 $+\dfrac{\sqrt{3}}{2}$，错
- 注释：
  - 求 $15^\circ$、$22.5^\circ$ 等的值
  - 求 $\dfrac{\alpha}{2}$ 的三角函数值 → 半角（定号）
- 依赖：
  - 来源：R19
    种类：推出
    方法：同除
    条件：▼ 加条件〔符号分支〕：± 由 $\frac{\alpha}{2}$ 所在象限定
    步骤：
      1. 【代换】$\alpha\to\dfrac{\alpha}{2}$：$\sin^2\dfrac{\alpha}{2}=\dfrac{1-\cos\alpha}{2}$，$\cos^2\dfrac{\alpha}{2}=\dfrac{1+\cos\alpha}{2}$
      2. 【开平方】$\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$，$\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$
      3. 【同乘】tan 式：$\tan\dfrac{\alpha}{2}=\dfrac{\sin\frac{\alpha}{2}}{\cos\frac{\alpha}{2}}$，前式分子、分母同乘 $2\cos\dfrac{\alpha}{2}\Rightarrow\dfrac{\sin\alpha}{1+\cos\alpha}$（「倍角」「升幂」）
      4. 【同乘】后式分子、分母同乘 $2\sin\dfrac{\alpha}{2}\Rightarrow\dfrac{1-\cos\alpha}{\sin\alpha}$
  - 来源：P43
    种类：前提
    步骤：
      1. 【前提】开平方要定号

### R31 平方和
- 标志：$1^2+2^2+\cdots+n^2=\dfrac{n(n+1)(2n+1)}{6}$
- 区域：数列
- 类型：结论
- 重要度：1
- 是什么：$1^2+2^2+\cdots+n^2=\dfrac{n(n+1)(2n+1)}{6}$
- 注释：
  - 数列求和、放缩估计
  - 看到 $1^2+2^2+\cdots$ → 平方和公式
- 依赖：
  - 来源：R05
    种类：推出
    方法：作差相消
    步骤：
      1. 【展开】$(k+1)^3-k^3=3k^2+3k+1$（「两数和的立方」）
      2. 【累加】$k$ 从 1 加到 $n$：$(n+1)^3-1=3\sum k^2+\dfrac{3n(n+1)}{2}+n$（「累加相消」）
      3. 【移项】解出 $\sum k^2=\dfrac{n(n+1)(2n+1)}{6}$
  - 来源：R28
    种类：前提
    步骤：
      1. 【前提】累加相消
  - 来源：R29
    种类：前提
    步骤：
      1. 【前提】$\sum k=\dfrac{n(n+1)}{2}$

### R32 立方和
- 标志：$1^3+2^3+\cdots+n^3=\left[\dfrac{n(n+1)}{2}\right]^2=(1+2+\cdots+n)^2$
- 区域：数列
- 类型：中间步
- 是什么：$1^3+2^3+\cdots+n^3=\left[\dfrac{n(n+1)}{2}\right]^2=(1+2+\cdots+n)^2$
- 注释：
  - 同源：平方和〔R31〕
  - 数列求和
  - 看到 $1^3+2^3+\cdots$ → 立方和公式
- 依赖：
  - 来源：R29
    种类：推出
    方法：归纳
    步骤：
      1. 【特例】$n=1$：$1=1$
      2. 【归纳】设 $n=k$ 时 $1^3+\cdots+k^3=\left[\dfrac{k(k+1)}{2}\right]^2$
      3. 【相加】两边加 $(k+1)^3$：$\left[\dfrac{k(k+1)}{2}\right]^2+(k+1)^3=\dfrac{(k+1)^2(k+2)^2}{4}$
      4. 【归纳】右边正是 $n=k+1$ 时的形式
  - 来源：S10
    种类：前提
    步骤：
      1. 【前提】数学归纳法

### P58 实系数方程的虚根
- 标志：$ax^2+bx+c=0$（$a,b,c\in\mathbb{R}$，$a\ne 0$，$\Delta<0$）：$x=\dfrac{-b\pm\sqrt{-\Delta}\,i}{2a}$，两根互为共轭
- 区域：复数
- 类型：结论
- 条件：结构前提实系数一元二次方程，$\Delta<0$
- 是什么：韦达定理仍成立：$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$；特例：$a>0$ 时 $x^2=-a$ 的解为 $\pm\sqrt{a}\,i$；注意写 $\sqrt{-\Delta}\,i$，不写 $\sqrt{\Delta}$（$\Delta<0$）
- 反例：
  - 系数不全是实数时虚根不一定成对：$x^2-ix=0$ 的根是 $0$、$i$
- 注释：
  - 实系数二次方程有一个虚根 $p+qi$ → 另一根是 $p-qi$，再用韦达
- 依赖：
  - 来源：S06
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：实系数，$\Delta<0$
    步骤：
      1. 【代入】$\left(\pm\sqrt{-\Delta}\,i\right)^2=(-\Delta)i^2=\Delta\Rightarrow x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{-\Delta}\,i}{2a}$
  - 来源：P01
    种类：推出
    方法：互逆
    步骤：
      1. 【配方】$ax^2+bx+c=0\Rightarrow\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}<0$
      2. 【开平方】在复数范围内开方
  - 来源：P03
    种类：前提
    步骤：
      1. 【前提】两根相加、相乘的算法与实根时相同

### P71 抛物线：四种标准方程、焦半径与焦点弦
- 标志：$y^2=2px$：焦点 $\left(\dfrac{p}{2},0\right)$，准线 $x=-\dfrac{p}{2}$；$y^2=-2px$：焦点 $\left(-\dfrac{p}{2},0\right)$，准线 $x=\dfrac{p}{2}$
- 区域：解析几何
- 类型：结论
- 条件：结构前提抛物线标准方程（$p>0$）
- 是什么：$x^2=2py$：焦点 $\left(0,\dfrac{p}{2}\right)$，准线 $y=-\dfrac{p}{2}$；$x^2=-2py$：焦点 $\left(0,-\dfrac{p}{2}\right)$，准线 $y=\dfrac{p}{2}$；$y=ax^2$ 先化成 $x^2=\dfrac{1}{a}y$；焦半径 $|PF|=x_0+\dfrac{p}{2}$（$y^2=2px$）：到焦点的距离 = 到准线的距离；$x^2=2py$ 时 $|PF|=y_0+\dfrac{p}{2}$；过焦点的弦 $|AB|=x_1+x_2+p$（两段焦半径相加；教材习题中使用）；过焦点的弦 $y_1y_2=-p^2$（选必一练习 A）；拓展：$x_1x_2=\dfrac{p^2}{4}$
- 注释：
  - 抛物线上的点到焦点的距离 → 换成到准线的距离
- 依赖：
  - 来源：S16
    种类：推出
    方法：作差相消
    条件：▼ 加条件〔结构前提〕：标准位置
    步骤：
      1. 【定义】到焦点 $\left(\dfrac{p}{2},0\right)$ 的距离 = 到准线 $x=-\dfrac{p}{2}$ 的距离：$|PF|=x_0+\dfrac{p}{2}$
      2. 【相加】焦点弦 = 两段焦半径之和：$|AB|=\left(x_1+\dfrac{p}{2}\right)+\left(x_2+\dfrac{p}{2}\right)=x_1+x_2+p$
  - 来源：P03
    种类：前提
    步骤：
      1. 【前提】韦达：设 $x=my+\dfrac{p}{2}$ 代入得 $y^2-2pmy-p^2=0$，$y_1y_2=-p^2$

### P91 复数的 $n$ 次方根
- 标志：$r(\cos\theta+i\sin\theta)$ 的 $n$ 次方根：$\sqrt[n]{r}\left(\cos\dfrac{\theta+2k\pi}{n}+i\sin\dfrac{\theta+2k\pi}{n}\right)$，$k=0,1,\cdots,n-1$
- 区域：复数
- 类型：结论
- 标签：拓展
- 条件：定义域$z\ne 0$，$n$ 为正整数
- 是什么：共 $n$ 个，在复平面上是正 $n$ 边形的顶点
- 注释：
  - 求复数的 $n$ 次方根 → 模开 $n$ 次方，辐角加 $2k\pi$ 后除以 $n$
- 依赖：
  - 来源：R27
    种类：推出
    方法：展开分解
    条件：▼ 加条件〔定义域〕：$z\ne 0$
    步骤：
      1. 【设】$w^n=z$，$w=\rho(\cos\varphi+i\sin\varphi)$
      2. 【逆用】「棣莫弗公式」比较模和辐角：$\rho^n=r$，$n\varphi=\theta+2k\pi$（辐角相差 $2k\pi$）

### P96 直线系与圆系
- 标志：过两直线交点的直线系：$A_1x+B_1y+C_1+\lambda(A_2x+B_2y+C_2)=0$（不含第二条直线本身）
- 区域：解析几何
- 类型：结论
- 标签：拓展
- 条件：结构前提两条直线（两个圆）相交
- 是什么：过两圆交点的圆系：$x^2+y^2+D_1x+E_1y+F_1+\lambda(x^2+y^2+D_2x+E_2y+F_2)=0$（$\lambda\ne -1$）；$\lambda=-1$ 即公共弦；含参直线恒过定点：按参数整理成 $f(x,y)+\lambda g(x,y)=0$，解 $f=0$、$g=0$
- 注释：
  - 含参数的直线恒过定点、过两曲线交点的曲线 → 曲线系
- 依赖：
  - 来源：P69
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：两曲线相交
    步骤：
      1. 【代入】交点同时满足两个方程，所以满足它们的任意组合：$f(x_0,y_0)=0$，$g(x_0,y_0)=0\Rightarrow f(x_0,y_0)+\lambda g(x_0,y_0)=0$
      2. 【赋值】圆系中 $\lambda=-1$：$x^2+y^2$ 项消去，得公共弦所在直线

## 第 8 层　推导第 8 层

### P72 直线与圆锥曲线：联立、弦长、中点
- 标志：联立消 $y$ 得 $Ax^2+Bx+C=0$：$x_1+x_2=-\dfrac{B}{A}$，$x_1x_2=\dfrac{C}{A}$
- 区域：解析几何
- 类型：结论
- 重要度：2
- 条件：定义域联立后二次项系数 $\ne 0$，且 $\Delta>0$
- 是什么：弦长 $|AB|=\sqrt{1+k^2}\,|x_1-x_2|=\sqrt{1+\dfrac{1}{k^2}}\,|y_1-y_2|$（后式 $k\ne 0$）；中点 $\left(\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\right)$；相切 $\iff$ 消元后的一元二次方程 $\Delta=0$；与抛物线只有一个公共点还可能是平行于对称轴的直线（不是相切）
- 反例：
  - $x^2-y^2=1$ 与 $y=x+1$：消元后二次项系数为 0（直线平行于渐近线），只有一个交点 $(-1,0)$
- 注释：
  - 直线与曲线交于两点 → 设而不求：联立、判别式、韦达、整体代入
- 依赖：
  - 来源：P45
    种类：推出
    方法：代换
    条件：▼ 加条件〔定义域〕：二次项系数 $\ne 0$，$\Delta>0$
    步骤：
      1. 【代入】两交点都在直线 $y=kx+m$ 上：$y_1-y_2=k(x_1-x_2)$
      2. 【代入】「两点距离公式」$|AB|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}=\sqrt{(1+k^2)(x_1-x_2)^2}$
      3. 【开平方】$|AB|=\sqrt{1+k^2}\,|x_1-x_2|$
      4. 【代入】「韦达定理」$|x_1-x_2|=\sqrt{(x_1+x_2)^2-4x_1x_2}$
  - 来源：S13
    种类：前提
    步骤：
      1. 【前提】两点距离公式
  - 来源：P65
    种类：前提
    步骤：
      1. 【前提】设直线 $y=kx+m$（斜率不存在时另算）

### P97 准线与第二定义
- 标志：准线 $x=\pm\dfrac{a^2}{c}$；到焦点的距离与到相应准线的距离之比为 $e$
- 区域：解析几何
- 类型：结论
- 标签：拓展
- 条件：结构前提椭圆、双曲线中心在原点，焦点在 $x$ 轴
- 是什么：椭圆 $0<e<1$，双曲线 $e>1$，抛物线 $e=1$：三种曲线统一；焦半径 $|PF_1|=a+ex_0$ 就是 $e$ 乘到左准线的距离 $x_0+\dfrac{a^2}{c}$
- 注释：
  - 圆锥曲线上的点到焦点的距离 → 换成 $e$ 乘到准线的距离
  - 椭圆、双曲线上的点到焦点的距离（例 $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$ 上 $x_0=3$：$|PF_1|=5+\dfrac{4}{5}\times 3=\dfrac{37}{5}$）
- 依赖：
  - 来源：P70
    种类：推出
    方法：代换
    条件：▼ 加条件〔结构前提〕：标准位置
    步骤：
      1. 【平方】椭圆标准方程推导中平方整理：$\sqrt{(x+c)^2+y^2}=a+\dfrac{c}{a}x$
      2. 【提取】$a+\dfrac{c}{a}x=\dfrac{c}{a}\left(x+\dfrac{a^2}{c}\right)$
      3. 【代换】$e=\dfrac{c}{a}$：$|PF_1|=e\cdot$（$P$ 到直线 $x=-\dfrac{a^2}{c}$ 的距离）
  - 来源：P71
    种类：前提
    步骤：
      1. 【前提】抛物线：到焦点距离 = 到准线距离（$e=1$）

## 思想方法

### 展开分解
- 说明：展开分解（展开、提公因式、因式分解、逆用公式）
- 方向：要合并、比较系数、验证恒等 → 展开成和；要约分、解方程、定正负 → 分解成积
- 依据：分配律〔S01〕；乘法公式从左往右是展开，从右往左是分解
- 信号：括号相乘要合并；二次式、高次式要拆；方程一边是 0
- 出现在：P03、P100、P102、P17、P22、P23、P25、P41、P44、P48、P57、P67、P91、R01、R02、R04、R08、R11、R22、R24、R26、R36、R41、R42、R48、R49、R50、R57
- 标签：展开；展开验证；逆用；提取；因式分解；合并；相乘；分解；去括号；对比
- 例子：
  - 分配律 → $(a\pm b)^2$、$a^2-b^2$ → 十字相乘、因式定理 → 零积性质解方程；$(x+\Delta x)^n$ 展开 → $(x^n)'=nx^{n-1}$
- 易错：
  - 分解要分到不能再分；约掉的因式不能为 0

### 配凑
- 说明：配凑（配方、补项、加一项减一项、待定系数）
- 方向：二次式求最值、找对称轴、化标准方程 → 凑成“平方 + 常数”；差一项就补上再减去
- 依据：完全平方公式〔R03〕；恒等的多项式对应系数相等〔R43〕
- 信号：二次式求最值或值域；$x^2+y^2+Dx+Ey+F=0$；两式相乘差一个交叉项
- 出现在：P01、P68、P82、R10
- 标签：配方；配方法；配凑；平方
- 例子：
  - $(a+b)^2$ → $a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a}$ → 求根公式 → 圆的一般方程 → 最小二乘回归；积的求导：加一项减一项
- 易错：
  - 配方时先提出二次项系数；补上的项要减回去

### 代换
- 说明：代换（换元、整体代入、字母代换、拆角配角、平移伸缩）
- 方向：已有一个公式，想要它的“兄弟公式” → 把字母换成别的式子；式子复杂 → 把一块看成整体、换成新变量
- 依据：恒等式对字母的一切取值成立，代入什么都成立
- 信号：结构与已知公式相似；同一块反复出现；复合函数；角能写成已知角的和差
- 出现在：P04、P06、P09、P101、P11、P12、P13、P14、P19、P20、P24、P27、P30、P39、P45、P55、P58、P62、P63、P64、P66、P70、P72、P74、P75、P92、P95、P96、P97、P98、R03、R05、R06、R13、R14、R15、R17、R18、R21、R29、R38、R44、R45、R46、R56
- 标签：代入；代换；设；整体代入；拆角；平移；平移、伸缩；变形；伸缩
- 例子：
  - $\cos(\alpha-\beta)$ →（$\beta\to-\beta$）和角 →（$\beta=\alpha$）倍角 → 降幂 →（$\alpha\to\frac{\alpha}{2}$）半角；$t=2^x$ 化二次；复合函数求导
- 易错：
  - 换元后新变量的范围要随之改变

### 特例
- 说明：特例与推广（取特殊值、赋值、由特殊到一般）
- 方向：一般结论里取特殊值 → 得到常用特例、求系数和；特殊情形成立 → 推广到一般
- 依据：一般式对所有取值成立，自然对特殊值成立
- 信号：求展开式系数和；和角里令两角相等；整数指数想推到实数指数
- 出现在：P05、P15、P32、P59、P87、P99、R34、R39
- 标签：特例；赋值；推广；类比
- 例子：
  - 和角 →（$\beta=\alpha$）倍角；二项式定理 →（$x=1,-1,0$）系数和；整数指数 →（推广）实数指数；累加法 →（$f(n)=d$）等差通项
- 易错：
  - 推广后要重新核对条件（如底数 $>0$）

### 作差相消
- 说明：作差相消（两式相减、累加、累乘、错位相减、倒序相加）
- 方向：相邻项、两个式子结构相似 → 相减或倒序相加，中间项抵消，只剩首尾
- 依据：等式两边同加减仍相等〔S01〕
- 信号：相邻项相减有规律；$S_n$ 与 $a_n$ 混在一起；等差 × 等比；两点都在同一曲线上
- 出现在：P02、P26、P50、P56、P60、P71、P78、P79、P84、P86、P90、R07、R09、R20、R23、R28、R30、R31、R40、R54
- 标签：作差；相减；相加减；移项；累加相消；累加；累乘；错位相减；倒序相加；作比；相加；相消
- 例子：
  - 相邻项相减 → 累加相消 → 等差通项、裂项、平方和；$S-qS$ → 等比求和 → 错位相减；$a_n=S_n-S_{n-1}$；两点代入相减 → 点差法
- 易错：
  - 看清首尾剩几项；$n=1$ 要单独验证

### 同除
- 说明：同除与通分（同除、同乘共轭、通分、齐次化）
- 方向：分子分母次数相同、要化成单一变量 → 同除一个非零式；分母麻烦 → 通分或同乘共轭
- 依据：分式的基本性质：分子分母同乘除一个非零式，值不变〔P42〕
- 信号：sin、cos 的齐次式；分母含根式、含 $i$；求离心率要化 $a,c$ 齐次式
- 出现在：P08、P16、P18、P28、P29、P31、P34、P42、P47、P52、P53、P73、R19、R35、R53
- 标签：同除；相除；通分；通分验证；同乘；分母实数化；约分
- 例子：
  - 同除 $\cos\alpha$：切化弦 ⇄ 弦化切 → 正切和角；同乘共轭 → 分母有理化、复数除法；差商通分 → 商的求导法则
- 易错：
  - 同除的式子不能为 0（如 $\cos\alpha\ne 0$）

### 对称
- 说明：对称（终边对称、函数图像对称、下标对称）
- 方向：角或图形关于某点、某线对称 → 写出对称点的坐标关系，一个结论变两个
- 依据：单位圆上对称点的坐标关系〔S04〕；$f(-x)=\pm f(x)$〔S15〕
- 信号：$\pi\pm\alpha$、$-\alpha$；$f(a+x)=f(b-x)$；下标和相等；正态曲线
- 出现在：P10、P61、P85、P88
- 标签：对称；对调
- 例子：
  - 单位圆上终边对称 → 诱导公式 → 已知值求角有两组解；$f(-x)=\pm f(x)$ → 对称轴、对称中心 → 周期；正态曲线关于 $x=\mu$ 对称
- 易错：
  - 区分一个函数自身对称与两个函数图像互相对称

### 数形结合
- 说明：数形结合（向量化、坐标化、几何意义）
- 方向：几何关系难直接算 → 化成坐标或向量运算；代数式有几何意义 → 画出来看
- 依据：数量积〔S05〕、坐标法〔S16〕：几何量都能写成坐标的式子
- 信号：角、长度、垂直、距离；$|z-z_0|$；$\overrightarrow{PA}\cdot\overrightarrow{PB}$；能建坐标系
- 出现在：P49、R16
- 标签：向量；取点
- 例子：
  - 数量积坐标式 → 两角差余弦 → 和角；$|\vec a-\vec b|^2$ → 余弦定理；投影 → 点到直线、点到平面的距离 → 空间角
- 易错：
  - 图只作引导，结论要能用代数说清

### 分类讨论
- 说明：分类讨论（分类、分步、按情况分开）
- 方向：情况不止一种 → 分成互不重叠的几类分别处理；一件事要几步完成 → 各步相乘
- 依据：分类加法原理、分步乘法原理〔S07〕
- 信号：含参数；绝对值；“至少”“恰好”；计数；完备事件组
- 出现在：P33、P35、P36、P54、P80、P81、P94、R33、R37、R47
- 标签：双计数；对应；数个数；拆成互斥；分组；分类讨论；分类；分步计数；分类计数
- 例子：
  - 分步 → 排列 → 组合 → 二项式定理；“选或不选” → 子集 $2^n$；重叠部分 → 容斥 → 概率加法公式；独立 + 分类 → 二项分布
- 易错：
  - 分类标准统一，不重不漏

### 归纳
- 说明：归纳与递推
- 方向：对一切正整数 $n$ 成立 → 奠基 + 由 $n=k$ 推 $n=k+1$；后项由前项决定 → 构造成等差、等比
- 依据：数学归纳法〔S10〕
- 信号：含正整数 $n$ 的恒等式；递推关系
- 出现在：R27、R32
- 标签：归纳法；递推；归纳
- 例子：
  - $n=k\to n=k+1$：棣莫弗公式、立方和；递推 $a_{n+1}=pa_n+q$ → 构造等比；斐波那契
- 易错：
  - 递推那一步必须用上归纳假设

### 补形
- 说明：补形与面积法
- 方向：图形不规则 → 补成熟悉的图形再减；同一个面积（体积）用两种方法算 → 列等式
- 依据：面积公式〔S13〕、体积公式与祖暅原理〔S18〕
- 信号：台体、三棱锥外接球；三角形里有高、有角平分线
- 出现在：P21、P76、P77
- 标签：补形；补形相减；面积法；作垂线
- 例子：
  - 三个面积公式相等 → 正弦定理；面积比 → 角平分线定理；台体 = 大锥 − 小锥；外接球补成长方体
- 易错：
  - 补上的部分要算对、减干净

### 回到定义
- 说明：回到定义与取极限
- 方向：现成公式用不上 → 回到定义直接算；从平均到瞬时、从有限到无限 → 取极限
- 依据：各个定义（三角函数、对数、导数、条件概率……）就是最底层的工具
- 信号：新函数求导；圆锥曲线上的点到焦点的距离；求轨迹；无限项求和
- 出现在：P103、P37、P38、P40、P43、P51、P63、P65、P68、P83、P89、P93、R12、R35、R51、R55
- 标签：定义；按定义；极限；取极限；求导
- 例子：
  - 平均变化率 →（$\Delta x\to 0$）导数 → 求导法则 → 线性近似；等比求和 →（$n\to\infty$）无穷递缩；对数、三角函数都由定义推出
- 易错：
  - 定义里的条件（如 $x\ne 0$、$P(A)>0$）一并带上

### 互逆
- 说明：互逆（逆运算、逆向使用）
- 方向：正着做不出 → 换成逆运算或反面
- 依据：指数与对数、乘方与开方、原函数与反函数互为逆运算
- 信号：指数方程、对数方程；求反函数；“至少一个”算反面
- 出现在：P07、P46、P58、P69、R25、R52
- 标签：逆运算；开平方；取对数；取倒数
- 例子：
  - 指数 ⇄ 对数；原函数 ⇄ 反函数；积化和差 ⇄ 和差化积；乘法 ⇄ 除法（复数三角形式）；对立事件
- 易错：
  - 逆运算有条件（真数 $>0$、一一对应）

### 反证
- 说明：反证
- 方向：直接证明困难 → 假设结论不成立，推出矛盾
- 依据：排中律：结论成立与不成立必有一个
- 信号：“唯一”“至多”“至少”；系数对应相等；零积性质
- 出现在：R43
- 标签：反证
- 例子：
  - 若 $a\ne 0$，乘 $\frac{1}{a}$ 得 $b=0$（零积性质）；两多项式之差不是零多项式则根有限（系数对应相等）
- 易错：
  - 要否定整个结论

