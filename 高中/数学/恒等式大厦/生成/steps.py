"""推导线一步一行的写法（照不等式大厦 v48）：每行【动作】+ 这一步的式子，工具写「工具名」。
build.py 用它替换推导线上的文字；data.py 里的原文不动（只增不删）。键 = (起点, 终点)。"""

STEPS = {
    ('S01', 'R01'): [
        r"【展开】「分配律」$(a+b)(c+d)=a(c+d)+b(c+d)$",
        r"【展开】「分配律」$a(c+d)+b(c+d)=ac+ad+bc+bd$（分配律用两次）",
    ],
    ('R01', 'R02'): [
        r"【展开】「多项式乘法」$(a+b)(a-b)=a^2-ab+ab-b^2$",
        r"【合并】交叉项 $-ab+ab$ 抵消：$a^2-ab+ab-b^2=a^2-b^2$",
    ],
    ('R01', 'R03'): [
        r"【展开】「多项式乘法」$(a+b)^2=(a+b)(a+b)=a^2+ab+ab+b^2$",
        r"【合并】两个交叉项合并成 $2ab$：$=a^2+2ab+b^2$",
        r"【代换】$b\to -b$：$(a-b)^2=a^2-2ab+b^2$",
    ],
    ('R01', 'R04'): [
        r"【展开】「多项式乘法」$(a+b+c)^2=(a+b+c)(a+b+c)$，每项乘每项共 9 项",
        r"【合并】平方项 3 个；$ab$、$bc$、$ca$ 各出现 2 次：$=a^2+b^2+c^2+2ab+2bc+2ca$",
    ],
    ('R03', 'R05'): [
        r"【展开】「完全平方」$(a+b)^3=(a+b)^2(a+b)=(a^2+2ab+b^2)(a+b)$",
        r"【合并】$=a^3+a^2b+2a^2b+2ab^2+ab^2+b^3=a^3+3a^2b+3ab^2+b^3$",
        r"【代换】$b\to -b$：$(a-b)^3=a^3-3a^2b+3ab^2-b^3$",
    ],
    ('R01', 'R06'): [
        r"【展开】右边 $(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3$",
        r"【合并】中间项抵消：$=a^3+b^3$",
        r"【代换】$b\to -b$：$a^3-b^3=(a-b)(a^2+ab+b^2)$",
    ],
    ('R03', 'R07'): [
        r"【移项】$(a+b)^2=a^2+2ab+b^2\Rightarrow a^2+b^2=(a+b)^2-2ab$",
        r"【相减】$(a+b)^2-(a-b)^2=4ab\Rightarrow(a-b)^2=(a+b)^2-4ab$",
    ],
    ('R05', 'R07'): [
        r"【提取】$(a+b)^3=a^3+3a^2b+3ab^2+b^3=a^3+b^3+3ab(a+b)$",
        r"【移项】$a^3+b^3=(a+b)^3-3ab(a+b)$",
    ],
    ('R04', 'R07'): [
        r"【提取】$(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)$",
        r"【移项】$a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)$",
    ],
    ('R01', 'R08'): [
        r"【逆用】「多项式乘法」与乘法公式从右往左读：$ac+ad+bc+bd\Rightarrow(a+b)(c+d)$",
    ],
    ('R03', 'P01'): [
        r"【提取】$ax^2+bx+c\Rightarrow a\left(x^2+\dfrac{b}{a}x\right)+c$",
        r"【配方】「完全平方」补上 $\left(\dfrac{b}{2a}\right)^2$ 再减去：$a\left[\left(x+\dfrac{b}{2a}\right)^2-\dfrac{b^2}{4a^2}\right]+c$",
        r"【合并】$=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$",
    ],
    ('P01', 'P02'): [
        r"【配方】$ax^2+bx+c=0\Rightarrow\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}$",
        r"【开平方】$\Delta\ge 0$：$x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{\Delta}}{2a}$",
        r"【移项】$x=\dfrac{-b\pm\sqrt{\Delta}}{2a}$",
    ],
    ('P02', 'P03'): [
        r"【代入】$x_{1,2}=\dfrac{-b\pm\sqrt{\Delta}}{2a}$",
        r"【相加】$x_1+x_2=\dfrac{-2b}{2a}=-\dfrac{b}{a}$",
        r"【相乘】「平方差」$x_1x_2=\dfrac{b^2-\Delta}{4a^2}=\dfrac{4ac}{4a^2}=\dfrac{c}{a}$",
    ],
    ('P03', 'P04'): [
        r"【展开】右边 $a(x-x_1)(x-x_2)=a[x^2-(x_1+x_2)x+x_1x_2]$",
        r"【代入】「韦达定理」$x_1+x_2=-\dfrac{b}{a}$，$x_1x_2=\dfrac{c}{a}$：$=a\left(x^2+\dfrac{b}{a}x+\dfrac{c}{a}\right)=ax^2+bx+c$（对比系数）",
    ],
    ('R01', 'R09'): [
        r"【展开】右边 $(x-y)(x^{n-1}+x^{n-2}y+\cdots+y^{n-1})=(x^n+x^{n-1}y+\cdots+xy^{n-1})-(x^{n-1}y+\cdots+xy^{n-1}+y^n)$",
        r"【相减】相邻项错位抵消，只剩 $x^n-y^n$",
    ],
    ('R01', 'R10'): [
        r"【展开】右边 $(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$，中间项抵消 $\Rightarrow a^3+b^3+c^3-3abc$",
        r"【配方】「完全平方」$a^2+b^2+c^2-ab-bc-ca=\dfrac{1}{2}\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$",
    ],
    ('R01', 'R11'): [
        r"【展开】左边 $(a^2+b^2)(c^2+d^2)=a^2c^2+a^2d^2+b^2c^2+b^2d^2$",
        r"【展开】右边 $(ac+bd)^2+(ad-bc)^2=a^2c^2+2abcd+b^2d^2+a^2d^2-2abcd+b^2c^2$",
        r"【合并】交叉项 $+2abcd$、$-2abcd$ 抵消：两边都是 $a^2c^2+a^2d^2+b^2c^2+b^2d^2$",
    ],
    ('S02', 'R12'): [
        r"【定义】「乘方定义」$a^m\cdot a^n$：$m$ 个 $a$ 再乘 $n$ 个 $a$，共 $m+n$ 个 $\Rightarrow a^{m+n}$",
    ],
    ('S03', 'P06'): [
        r"【代入】$b=\log_a N$ 代回 $a^b=N$：$a^{\log_a N}=N$",
        r"【代入】$N=a^b$ 代入 $b=\log_a N$：$\log_a a^b=b$",
    ],
    ('P05', 'P07'): [
        r"【设】$M=a^p$，$N=a^q$，即 $p=\log_a M$，$q=\log_a N$",
        r"【代入】「实数指数运算律」积 $MN=a^pa^q=a^{p+q}$；商 $\dfrac{M}{N}=a^p\div a^q=a^{p-q}$；幂 $M^n=(a^p)^n=a^{pn}$",
        r"【取对数】$\log_a(MN)=p+q$，$\log_a\dfrac{M}{N}=p-q$，$\log_a M^n=np$（「对数定义」）",
    ],
    ('P07', 'P08'): [
        r"【设】$\log_a b=x\Rightarrow a^x=b$",
        r"【取对数】两边取 $\log_c$：$\log_c a^x=\log_c b\Rightarrow x\log_c a=\log_c b$（「对数运算律」）",
        r"【同除】$x=\dfrac{\log_c b}{\log_c a}$（$a\ne 1\Rightarrow\log_c a\ne 0$）",
    ],
    ('P08', 'P09'): [
        r"【代换】「换底公式」都换成以 $c$ 为底（取 $c=10$）：$\log_a b\cdot\log_b a=\dfrac{\lg b}{\lg a}\cdot\dfrac{\lg a}{\lg b}=1$",
        r"【代换】「换底公式」$\log_{a^m}b^n=\dfrac{\lg b^n}{\lg a^m}=\dfrac{n\lg b}{m\lg a}=\dfrac{n}{m}\log_a b$（「对数运算律」）",
    ],
    ('P06', 'P10'): [
        r"【定义】指数式与对数式互化：$y=a^x\iff x=\log_a y$",
        r"【对称】交换 $x,y$：$y=\log_a x$，图像关于 $y=x$ 对称",
    ],
    ('S04', 'R13'): [
        r"【代入】$P(\cos\alpha,\sin\alpha)$ 在单位圆 $x^2+y^2=1$ 上 $\Rightarrow\cos^2\alpha+\sin^2\alpha=1$（「三角函数定义」）",
    ],
    ('S04', 'P11'): [
        r"【定义】$\tan\alpha=\dfrac{y}{x}$（「三角函数定义」）",
        r"【代入】交点 $(x,y)=(\cos\alpha,\sin\alpha)\Rightarrow\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}$（要求 $\cos\alpha\ne 0$）",
    ],
    ('R13', 'P12'): [
        r"【同除】$\sin^2\alpha+\cos^2\alpha=1$ 两边 $\div\cos^2\alpha\Rightarrow\dfrac{\sin^2\alpha}{\cos^2\alpha}+1=\dfrac{1}{\cos^2\alpha}$",
        r"【代换】$\dfrac{\sin^2\alpha}{\cos^2\alpha}=\tan^2\alpha\Rightarrow 1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}$（「商数关系」）",
    ],
    ('S04', 'R14'): [
        r"【对称】终边关于原点、$x$ 轴、$y$ 轴、$y=x$ 对称：交点 $(x,y)$ 变为 $(-x,-y)$、$(x,-y)$、$(-x,y)$、$(y,x)$（「三角函数定义」）",
        r"【代换】⑥：⑤ 中 $\alpha\to-\alpha$，再用「诱导公式③」",
        r"【拆角】⑦⑧：$\dfrac{3\pi}{2}\pm\alpha=\pi+\left(\dfrac{\pi}{2}\pm\alpha\right)$，用「诱导公式②」再用「诱导公式⑤⑥」",
    ],
    ('R14', 'P13'): [
        r"【相除】sin 式 $\div$ cos 式（「商数关系」）",
        r"【代入】如 $\tan(\pi+\alpha)=\dfrac{\sin(\pi+\alpha)}{\cos(\pi+\alpha)}=\dfrac{-\sin\alpha}{-\cos\alpha}=\tan\alpha$（「诱导公式②」）",
    ],
    ('S05', 'R15'): [
        r"【分解】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$",
        r"【展开】「分配律」$\vec a\cdot\vec b=x_1x_2\,\vec i\cdot\vec i+(x_1y_2+x_2y_1)\,\vec i\cdot\vec j+y_1y_2\,\vec j\cdot\vec j$",
        r"【代入】$\vec i\cdot\vec i=\vec j\cdot\vec j=1$，$\vec i\cdot\vec j=0\Rightarrow\vec a\cdot\vec b=x_1x_2+y_1y_2$",
    ],
    ('R15', 'R16'): [
        r"【设】$\overrightarrow{OA}=(\cos\alpha,\sin\alpha)$，$\overrightarrow{OB}=(\cos\beta,\sin\beta)$（单位向量）",
        r"【代入】「数量积坐标式」$\overrightarrow{OA}\cdot\overrightarrow{OB}=\cos\alpha\cos\beta+\sin\alpha\sin\beta$",
        r"【定义】「数量积定义」$\overrightarrow{OA}\cdot\overrightarrow{OB}=1\cdot 1\cdot\cos\theta=\cos\theta$（$\theta$ 为夹角）",
        r"【代换】$\alpha-\beta=\pm\theta+2k\pi\Rightarrow\cos(\alpha-\beta)=\cos\theta$（「诱导公式①③」）",
    ],
    ('R16', 'R17'): [
        r"【代换】$\beta\to-\beta$：$\cos(\alpha+\beta)=\cos\alpha\cos(-\beta)+\sin\alpha\sin(-\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$（「诱导公式③」）",
        r"【代换】$\sin(\alpha+\beta)=\cos\left[\dfrac{\pi}{2}-(\alpha+\beta)\right]=\cos\left[\left(\dfrac{\pi}{2}-\alpha\right)-\beta\right]$（「诱导公式⑤」）",
        r"【展开】$=\cos\left(\dfrac{\pi}{2}-\alpha\right)\cos\beta+\sin\left(\dfrac{\pi}{2}-\alpha\right)\sin\beta=\sin\alpha\cos\beta+\cos\alpha\sin\beta$",
        r"【代换】$\beta\to-\beta$：$\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$（「诱导公式③」）",
    ],
    ('R17', 'P14'): [
        r"【代入】$\tan(\alpha+\beta)=\dfrac{\sin(\alpha+\beta)}{\cos(\alpha+\beta)}=\dfrac{\sin\alpha\cos\beta+\cos\alpha\sin\beta}{\cos\alpha\cos\beta-\sin\alpha\sin\beta}$（「商数关系」「和角公式」）",
        r"【同除】分子、分母 $\div\cos\alpha\cos\beta\Rightarrow\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$",
        r"【代换】$\beta\to-\beta$ 得差角（「tan 的诱导公式」$\tan(-\beta)=-\tan\beta$）",
    ],
    ('R17', 'R18'): [
        r"【特例】令 $\beta=\alpha$：$\sin 2\alpha=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha$",
        r"【特例】令 $\beta=\alpha$：$\cos 2\alpha=\cos\alpha\cos\alpha-\sin\alpha\sin\alpha=\cos^2\alpha-\sin^2\alpha$",
        r"【代换】「勾股恒等式」$\sin^2\alpha=1-\cos^2\alpha$ 或 $\cos^2\alpha=1-\sin^2\alpha\Rightarrow\cos 2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$",
    ],
    ('P14', 'P15'): [
        r"【特例】令 $\beta=\alpha$：$\tan 2\alpha=\dfrac{\tan\alpha+\tan\alpha}{1-\tan\alpha\tan\alpha}=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$",
    ],
    ('R18', 'R19'): [
        r"【移项】$\cos 2\alpha=2\cos^2\alpha-1\Rightarrow 2\cos^2\alpha=1+\cos 2\alpha$；$\cos 2\alpha=1-2\sin^2\alpha\Rightarrow 2\sin^2\alpha=1-\cos 2\alpha$",
        r"【同除】两边 $\div 2\Rightarrow\cos^2\alpha=\dfrac{1+\cos 2\alpha}{2}$，$\sin^2\alpha=\dfrac{1-\cos 2\alpha}{2}$",
    ],
    ('R19', 'P16'): [
        r"【代换】$\alpha\to\dfrac{\alpha}{2}$：$\sin^2\dfrac{\alpha}{2}=\dfrac{1-\cos\alpha}{2}$，$\cos^2\dfrac{\alpha}{2}=\dfrac{1+\cos\alpha}{2}$",
        r"【开平方】$\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$，$\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$",
        r"【同乘】tan 式：$\tan\dfrac{\alpha}{2}=\dfrac{\sin\frac{\alpha}{2}}{\cos\frac{\alpha}{2}}$，前式分子、分母同乘 $2\cos\dfrac{\alpha}{2}\Rightarrow\dfrac{\sin\alpha}{1+\cos\alpha}$（「倍角」「升幂」）",
        r"【同乘】后式分子、分母同乘 $2\sin\dfrac{\alpha}{2}\Rightarrow\dfrac{1-\cos\alpha}{\sin\alpha}$",
    ],
    ('R17', 'R20'): [
        r"【相加】「和差角公式」$\sin(\alpha+\beta)+\sin(\alpha-\beta)=2\sin\alpha\cos\beta$；相减得 $\sin(\alpha+\beta)-\sin(\alpha-\beta)=2\cos\alpha\sin\beta$",
        r"【同除】两边 $\div 2$ 得积化和差",
        r"【相加】$\cos$ 的两式同理：$\cos(\alpha+\beta)+\cos(\alpha-\beta)=2\cos\alpha\cos\beta$，$\cos(\alpha+\beta)-\cos(\alpha-\beta)=-2\sin\alpha\sin\beta$",
    ],
    ('R20', 'R21'): [
        r"【代换】令 $\alpha+\beta=\theta$，$\alpha-\beta=\varphi\Rightarrow\alpha=\dfrac{\theta+\varphi}{2}$，$\beta=\dfrac{\theta-\varphi}{2}$",
        r"【代入】代入积化和差，左右互换即和差化积",
    ],
    ('R17', 'P17'): [
        r"【提取】提出 $r=\sqrt{a^2+b^2}$：$a\sin x+b\cos x=r\left(\dfrac{a}{r}\sin x+\dfrac{b}{r}\cos x\right)$",
        r"【代换】$\cos\varphi=\dfrac{a}{r}$，$\sin\varphi=\dfrac{b}{r}\Rightarrow=r(\sin x\cos\varphi+\cos x\sin\varphi)$",
        r"【逆用】「sin 和角公式」$=r\sin(x+\varphi)$",
    ],
    ('R18', 'P18'): [
        r"【补形】倍角写成分式，分母补上 $1=\sin^2\dfrac{\alpha}{2}+\cos^2\dfrac{\alpha}{2}$（「勾股恒等式」）：$\sin\alpha=\dfrac{2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}}{\sin^2\frac{\alpha}{2}+\cos^2\frac{\alpha}{2}}$",
        r"【同除】分子、分母 $\div\cos^2\dfrac{\alpha}{2}\Rightarrow\sin\alpha=\dfrac{2t}{1+t^2}$（$t=\tan\dfrac{\alpha}{2}$）",
        r"【同除】$\cos\alpha$ 同理：$\cos\alpha=\dfrac{\cos^2\frac{\alpha}{2}-\sin^2\frac{\alpha}{2}}{\sin^2\frac{\alpha}{2}+\cos^2\frac{\alpha}{2}}=\dfrac{1-t^2}{1+t^2}$",
    ],
    ('R14', 'P19'): [
        r"【代换】$A+B=\pi-C$：$\sin(A+B)=\sin C$，$\cos(A+B)=-\cos C$（「诱导公式④」）",
        r"【相除】$\tan(A+B)=-\tan C$（$C\ne\dfrac{\pi}{2}$）",
        r"【代换】$\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$：$\sin\dfrac{A+B}{2}=\cos\dfrac{C}{2}$，$\cos\dfrac{A+B}{2}=\sin\dfrac{C}{2}$（「诱导公式⑤」）",
    ],
    ('S04', 'P20'): [
        r"【定义】以 $a$ 为底，高 $h=b\sin C\Rightarrow S=\dfrac{1}{2}ah=\dfrac{1}{2}ab\sin C$（「三角函数定义」）",
        r"【代换】$C$ 为钝角：$h=b\sin(\pi-C)=b\sin C$（「诱导公式④」）",
    ],
    ('P20', 'P21'): [
        r"【同除】$\dfrac{1}{2}ab\sin C=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B$ 同除 $\dfrac{1}{2}abc\Rightarrow\dfrac{\sin C}{c}=\dfrac{\sin A}{a}=\dfrac{\sin B}{b}$",
        r"【取倒数】$\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}$",
        r"【补形】$=2R$：作直径 $BD$，$\angle BCD=90^\circ$，$\angle BDC$ 与 $A$ 相等或互补（「圆周角定理」）",
        r"【定义】$a=BD\sin\angle BDC=2R\sin\angle BDC=2R\sin A$（「诱导公式④」）",
        r"【特例】$A=90^\circ$：$BC$ 就是直径，$a=2R$ 直接成立",
    ],
    ('S06', 'R22'): [
        r"【展开】$(a+bi)(c+di)=ac+adi+bci+bdi^2$",
        r"【代入】$i^2=-1\Rightarrow ac+adi+bci-bd$",
        r"【合并】实部 $ac-bd$、虚部 $ad+bc\Rightarrow(ac-bd)+(ad+bc)i$",
    ],
    ('R22', 'R23'): [
        r"【展开】$z\bar z=(a+bi)(a-bi)=a^2-(bi)^2=a^2+b^2$（「平方差」）",
        r"【代换】$a^2+b^2=|z|^2\Rightarrow z\bar z=|z|^2$",
        r"【相加】$z+\bar z=2a$",
        r"【相减】$z-\bar z=2bi$",
    ],
    ('R23', 'P23'): [
        r"【同乘】分子、分母同乘 $c-di$（「共轭」）",
        r"【展开】分母 $(c+di)(c-di)=c^2+d^2$（实数）；分子 $(a+bi)(c-di)=(ac+bd)+(bc-ad)i$",
    ],
    ('S06', 'R24'): [
        r"【相乘】由 $i^2=-1$ 依次乘 $i$：$i^3=i^2\cdot i=-i$",
        r"【代入】$i^4=(i^2)^2=(-1)^2=1$",
        r"【相乘】$i^{n+4}=i^n\cdot i^4=i^n$：4 个一循环",
    ],
    ('R23', 'R25'): [
        r"【代入】$|z_1z_2|^2=z_1z_2\cdot\overline{z_1z_2}=z_1z_2\cdot\bar z_1\bar z_2=(z_1\bar z_1)(z_2\bar z_2)=|z_1|^2|z_2|^2$（「$z\bar z=|z|^2$」「$\overline{z_1z_2}=\bar z_1\bar z_2$」）",
        r"【开平方】$|z_1z_2|=|z_1||z_2|$",
    ],
    ('S06', 'P24'): [
        r"【定义】$z=a+bi\ne 0$，$r=|z|=\sqrt{a^2+b^2}$",
        r"【代入】$\left(\dfrac{a}{r}\right)^2+\left(\dfrac{b}{r}\right)^2=1\Rightarrow\left(\dfrac{a}{r},\dfrac{b}{r}\right)$ 在单位圆上（「三角函数定义」）",
        r"【代换】有角 $\theta$ 使 $\cos\theta=\dfrac{a}{r}$，$\sin\theta=\dfrac{b}{r}\Rightarrow z=r(\cos\theta+i\sin\theta)$",
    ],
    ('P24', 'R26'): [
        r"【展开】两个三角形式按多项式相乘，用 $i^2=-1$：$r_1r_2[(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)+i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)]$",
        r"【合并】实部、虚部分别合并",
    ],
    ('R17', 'R26'): [
        r"【相乘】实部 $\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2$，虚部 $\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2$",
        r"【逆用】「和角公式」实部 $=\cos(\theta_1+\theta_2)$，虚部 $=\sin(\theta_1+\theta_2)$",
    ],
    ('R26', 'P25'): [
        r"【相乘】$\dfrac{r_1}{r_2}[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)]\cdot r_2(\cos\theta_2+i\sin\theta_2)=r_1(\cos\theta_1+i\sin\theta_1)=z_1$（「三角形式乘法」）",
        r"【逆用】「除法是乘法的逆运算」：商乘 $z_2$ 等于 $z_1$，所以它就是 $\dfrac{z_1}{z_2}$",
    ],
    ('R26', 'R27'): [
        r"【特例】$n=1$ 成立",
        r"【归纳】「数学归纳法」设 $n=k$ 成立：$z^k=r^k(\cos k\theta+i\sin k\theta)$",
        r"【相乘】$z^{k+1}=z^k\cdot z$：模相乘、辐角相加（「三角形式乘法」）$\Rightarrow r^{k+1}[\cos(k+1)\theta+i\sin(k+1)\theta]$",
    ],
    ('S01', 'R28'): [
        r"【去括号】$(b_2-b_1)+(b_3-b_2)+\cdots+(b_{n+1}-b_n)\Rightarrow -b_1+b_2-b_2+b_3-b_3+\cdots+b_{n+1}$（「结合律」）",
        r"【相消】$b_2$ 与 $-b_2$、$b_3$ 与 $-b_3$……两两抵消 $\Rightarrow b_{n+1}-b_1$",
    ],
    ('S09', 'P26'): [
        r"【定义】「等差定义」$a_2-a_1=d$，…，$a_n-a_{n-1}=d$",
        r"【累加】$(n-1)$ 个 $d$ 相加 $\Rightarrow a_n-a_1=(n-1)d$",
        r"【移项】$a_n=a_1+(n-1)d$",
    ],
    ('P26', 'P27'): [
        r"【代入】「等差通项」$a_m+a_n=2a_1+(m+n-2)d$，$a_p+a_q=2a_1+(p+q-2)d$",
        r"【代换】$m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$",
    ],
    ('P27', 'P28'): [
        r"【倒序相加】$S_n=a_1+a_2+\cdots+a_n$，$S_n=a_n+a_{n-1}+\cdots+a_1$，对应项和都等于 $a_1+a_n$（「等差下标性质」）",
        r"【同除】$2S_n=n(a_1+a_n)\Rightarrow S_n=\dfrac{n(a_1+a_n)}{2}$",
    ],
    ('P28', 'R29'): [
        r"【特例】$a_1=1$，$d=1$",
        r"【代入】$S_n=n\cdot 1+\dfrac{n(n-1)}{2}\cdot 1=\dfrac{n(n+1)}{2}$",
    ],
    ('S09', 'P29'): [
        r"【定义】「等比定义」$\dfrac{a_2}{a_1}=q$，…，$\dfrac{a_n}{a_{n-1}}=q$",
        r"【累乘】$(n-1)$ 个 $q$ 相乘 $\Rightarrow\dfrac{a_n}{a_1}=q^{n-1}$",
        r"【同乘】$a_n=a_1q^{n-1}$",
    ],
    ('P29', 'P30'): [
        r"【代入】「等比通项」$a_ma_n=a_1^2q^{m+n-2}$，$a_pa_q=a_1^2q^{p+q-2}$",
        r"【代换】$m+n=p+q\Rightarrow a_ma_n=a_pa_q$",
    ],
    ('P29', 'P31'): [
        r"【错位相减】$S_n-qS_n=a_1-a_1q^n$",
        r"【同除】两边除以 $1-q$：$S_n=\dfrac{a_1(1-q^n)}{1-q}$",
    ],
    ('S09', 'P32'): [
        r"【定义】$S_n=a_1+\cdots+a_{n-1}+a_n$，$S_{n-1}=a_1+\cdots+a_{n-1}$",
        r"【作差】$S_n-S_{n-1}=a_n$（$S_{n-1}$ 要有意义，所以 $n\ge 2$）",
        r"【特例】$n=1$：$a_1=S_1$",
    ],
    ('R28', 'R30'): [
        r"【通分】$\dfrac{1}{k}-\dfrac{1}{k+1}=\dfrac{(k+1)-k}{k(k+1)}=\dfrac{1}{k(k+1)}$",
        r"【累加】$\displaystyle\sum_{k=1}^{n}\left(\dfrac{1}{k}-\dfrac{1}{k+1}\right)=1-\dfrac{1}{n+1}$（「累加相消」）",
    ],
    ('R05', 'R31'): [
        r"【展开】$(k+1)^3-k^3=3k^2+3k+1$（「两数和的立方」）",
        r"【累加】$k$ 从 1 加到 $n$：$(n+1)^3-1=3\sum k^2+\dfrac{3n(n+1)}{2}+n$（「累加相消」）",
        r"【移项】解出 $\sum k^2=\dfrac{n(n+1)(2n+1)}{6}$",
    ],
    ('R29', 'R32'): [
        r"【特例】$n=1$：$1=1$",
        r"【归纳】设 $n=k$ 时 $1^3+\cdots+k^3=\left[\dfrac{k(k+1)}{2}\right]^2$",
        r"【相加】两边加 $(k+1)^3$：$\left[\dfrac{k(k+1)}{2}\right]^2+(k+1)^3=\dfrac{(k+1)^2(k+2)^2}{4}$",
        r"【归纳】右边正是 $n=k+1$ 时的形式",
    ],
    ('S07', 'P33'): [
        r"【分步计数】第 1 位 $n$ 种，第 2 位 $n-1$ 种……第 $m$ 位 $n-m+1$ 种，相乘（「分步乘法原理」）",
    ],
    ('P33', 'P34'): [
        r"【分步计数】先选 $m$ 个再排列：$A_n^m=C_n^m\cdot m!$（「分步乘法原理」）",
        r"【同除】$C_n^m=\dfrac{A_n^m}{m!}$",
    ],
    ('P34', 'P35'): [
        r"【对称】选出 $m$ 个 ⟺ 留下 $n-m$ 个：$C_n^m=C_n^{n-m}$",
        r"【分类计数】某个指定元素选或不选：$C_{n+1}^m=C_n^m+C_n^{m-1}$（「分类加法原理」）",
    ],
    ('P34', 'R33'): [
        r"【展开】$n$ 个 $(a+b)$ 相乘，每个括号选 $a$ 或 $b$（「分步乘法原理」）",
        r"【分类计数】恰好选 $k$ 个 $b$ 有 $C_n^k$ 种，得项 $C_n^ka^{n-k}b^k$",
    ],
    ('R33', 'R34'): [
        r"【赋值】令 $a=b=1$：$C_n^0+C_n^1+\cdots+C_n^n=2^n$",
        r"【赋值】令 $a=1,\ b=-1$：交错和为 0",
    ],
    ('P34', 'P36'): [
        r"【代入】$kC_n^k=k\cdot\dfrac{n!}{k!(n-k)!}=n\cdot\dfrac{(n-1)!}{(k-1)!(n-k)!}=nC_{n-1}^{k-1}$",
        r"【分步计数】（另一路）选 $k$ 人委员会再选主席 $=$ 先选主席再选其余 $k-1$ 人",
    ],
    ('S08', 'R35'): [
        r"【定义】「导数定义」$\dfrac{(x+\Delta x)^n-x^n}{\Delta x}=nx^{n-1}+C_n^2x^{n-2}\Delta x+\cdots$",
        r"【取极限】令 $\Delta x\to 0$：$(x^n)'=nx^{n-1}$",
    ],
    ('R33', 'R35'): [
        r"【展开】$(x+\Delta x)^n=x^n+C_n^1x^{n-1}\Delta x+C_n^2x^{n-2}(\Delta x)^2+\cdots$（「二项式定理」）",
        r"【相减】减去 $x^n$",
        r"【同除】除以 $\Delta x$",
    ],
    ('S08', 'P37'): [
        r"【配凑】$u(x+\Delta x)v(x+\Delta x)-u(x)v(x)=[u(x+\Delta x)-u(x)]v(x+\Delta x)+u(x)[v(x+\Delta x)-v(x)]$",
        r"【取极限】同除 $\Delta x$，令 $\Delta x\to 0$；$v$ 可导 $\Rightarrow v$ 连续（课本承认）",
    ],
    ('S08', 'P38'): [
        r"【通分】【配凑】差商 $=\dfrac{\frac{u(x+\Delta x)-u(x)}{\Delta x}v(x)-u(x)\frac{v(x+\Delta x)-v(x)}{\Delta x}}{v(x+\Delta x)v(x)}$",
        r"【取极限】$v$ 连续且 $v(x)\ne 0$：$\Delta x$ 足够小时 $v(x+\Delta x)\ne 0$；令 $\Delta x\to 0$",
    ],
    ('P10', 'P39'): [
        r"【求导】对 $\ln(e^x)=x$ 两边求导：$(\ln)'(e^x)\cdot e^x=1$（「链式法则」）",
        r"【代换】令 $u=e^x$：$(\ln u)'=\dfrac{1}{u}$，$u$ 取遍 $(0,+\infty)$",
    ],
    ('P05', 'P40'): [
        r"【代换】$a^x=e^{x\ln a}$",
        r"【求导】$(a^x)'=e^{x\ln a}\cdot\ln a=a^x\ln a$（「链式法则」）",
    ],
    ('P08', 'P40'): [
        r"【代换】$\log_a x=\dfrac{\ln x}{\ln a}$（「换底公式」）",
        r"【求导】$(\log_a x)'=\dfrac{1}{\ln a}(\ln x)'=\dfrac{1}{x\ln a}$",
    ],
    ('S01', 'R36'): [
        r"【展开】「分配律」乘 $-1$ 去括号：$-(a+b)=(-1)a+(-1)b=-a-b$；$a-(b-c)=a+(-1)(b-c)=a-b+c$（减 $b$ 即加 $-b$）",
        r"【逆用】「分配律」合并同类项：$ma+na=(m+n)a$",
    ],
    ('S01', 'R37'): [
        r"【分类】按 $a,b$ 正负分四种情况，用「绝对值定义」逐一验证",
    ],
    ('S01', 'P42'): [
        r"【定义】除以 $b$ 即乘 $\dfrac{1}{b}$：$\dfrac{a}{b}=a\cdot\dfrac{1}{b}$",
        r"【约分】分子、分母同除非零式 $c$：$\dfrac{ac}{bc}\Rightarrow\dfrac{a}{b}$",
    ],
    ('P03', 'P45'): [
        r"【代入】「韦达定理」代入「互换式」，如 $x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2=\dfrac{b^2}{a^2}-\dfrac{2c}{a}$",
    ],
    ('R12', 'P41'): [
        r"【代入】「零指数、负指数的定义」$a^m\div a^n=a^m\cdot\dfrac{1}{a^n}=a^m\cdot a^{-n}$",
        r"【合并】$a^m\cdot a^{-n}=a^{m-n}$（正整数指数的运算律照样成立）",
    ],
    ('P41', 'P05'): [
        r"【推广】由整数指数推广到有理、实数指数（课本说明运算律仍成立）",
    ],
    ('P05', 'P43'): [
        r"【特例】取 $r=\dfrac{1}{2}$：$\sqrt{a}=a^{\frac{1}{2}}$",
        r"【代入】「实数指数运算律」$\sqrt{a}\sqrt{b}=a^{\frac{1}{2}}b^{\frac{1}{2}}=(ab)^{\frac{1}{2}}=\sqrt{ab}$",
        r"【定义】算术平方根非负：$\sqrt{a^2}=|a|$",
    ],
    ('P43', 'P44'): [
        r"【同乘】分子、分母同乘 $\sqrt{a}-\sqrt{b}$：$\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})}$（$a\ne b$）",
        r"【展开】「平方差」分母 $(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})=a-b$",
    ],
    ('R13', 'P46'): [
        r"【移项】$\sin^2\alpha+\cos^2\alpha=1\Rightarrow\sin^2\alpha=1-\cos^2\alpha$",
        r"【开平方】$\sin\alpha=\pm\sqrt{1-\cos^2\alpha}$，符号由 $\alpha$ 所在象限定",
    ],
    ('R18', 'R38'): [
        r"【展开】「完全平方」$(\sin\alpha\pm\cos\alpha)^2=\sin^2\alpha\pm 2\sin\alpha\cos\alpha+\cos^2\alpha$",
        r"【代换】$\sin^2\alpha+\cos^2\alpha=1$（「勾股恒等式」），$2\sin\alpha\cos\alpha=\sin 2\alpha$（「倍角」）$\Rightarrow 1\pm 2\sin\alpha\cos\alpha=1\pm\sin 2\alpha$",
    ],
    ('P11', 'P47'): [
        r"【同除】一次式：分子、分母 $\div\cos\alpha\Rightarrow\dfrac{a\tan\alpha+b}{c\tan\alpha+d}$",
        r"【代换】二次式：先用“1”的代换 $1=\sin^2\alpha+\cos^2\alpha$，如 $\sin\alpha\cos\alpha=\dfrac{\sin\alpha\cos\alpha}{\sin^2\alpha+\cos^2\alpha}$",
        r"【同除】再 $\div\cos^2\alpha\Rightarrow\dfrac{\tan\alpha}{1+\tan^2\alpha}$；$\sin^2\alpha=\dfrac{\tan^2\alpha}{1+\tan^2\alpha}$ 同理",
    ],
    ('S05', 'P49'): [
        r"【展开】「分配律」$|\vec a\pm\vec b|^2=(\vec a\pm\vec b)\cdot(\vec a\pm\vec b)$，$(\vec a+\vec b)\cdot(\vec a-\vec b)$，与「完全平方」「平方差」同型",
        r"【定义】垂直、夹角：由「数量积定义」变形，$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$",
    ],
    ('P49', 'P22'): [
        r"【代换】$\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$",
        r"【展开】「$|\vec a-\vec b|^2$」$|\overrightarrow{BC}|^2=|\overrightarrow{AC}|^2-2\overrightarrow{AC}\cdot\overrightarrow{AB}+|\overrightarrow{AB}|^2=b^2+c^2-2bc\cos A$",
    ],
    ('P20', 'P48'): [
        r"【平方】$S^2=\dfrac{1}{4}a^2b^2\sin^2C=\dfrac{1}{4}a^2b^2(1-\cos^2C)$（「勾股恒等式」）",
        r"【代入】$\cos C=\dfrac{a^2+b^2-c^2}{2ab}$（「余弦定理推论」）",
        r"【分解】两次「平方差」：$S^2=\dfrac{1}{16}[(a+b)^2-c^2][c^2-(a-b)^2]=\dfrac{(a+b+c)(a+b-c)(c+a-b)(c-a+b)}{16}=p(p-a)(p-b)(p-c)$",
    ],
    ('R28', 'P50'): [
        r"【累加】$a_2-a_1=f(1)$，…，$a_n-a_{n-1}=f(n-1)$，$n-1$ 个式子相加，中间项抵消 $\Rightarrow a_n=a_1+\sum_{k=1}^{n-1}f(k)$（「累加相消」）",
        r"【累乘】$\dfrac{a_2}{a_1}\cdot\dfrac{a_3}{a_2}\cdots\dfrac{a_n}{a_{n-1}}=\prod_{k=1}^{n-1}g(k)$，中间项约掉 $\Rightarrow a_n=a_1\prod_{k=1}^{n-1}g(k)$",
    ],
    ('S09', 'P51'): [
        r"【定义】成等差：相邻两项的差相等 $\Rightarrow b-a=c-b$",
        r"【移项】$2b=a+c$",
        r"【定义】成等比：相邻两项的比相等 $\Rightarrow\dfrac{b}{a}=\dfrac{c}{b}$",
        r"【同乘】$b^2=ac$",
    ],
    ('P31', 'P52'): [
        r"【错位相减】$S-qS=\sum q^{k-1}-nq^n$",
        r"【代入】「等比求和」$(1-q)S=\dfrac{1-q^n}{1-q}-nq^n$",
        r"【同除】$S=\dfrac{1-(n+1)q^n+nq^{n+1}}{(1-q)^2}$",
    ],
    ('R30', 'P53'): [
        r"【推广】仿 $\dfrac{1}{k(k+1)}$：两个因式相差 $d$ 时",
        r"【通分】右边 $\dfrac{1}{d}\cdot\dfrac{(k+d)-k}{k(k+d)}=\dfrac{1}{k(k+d)}$",
        r"【同乘】根式型：分子分母同乘 $\sqrt{k+1}-\sqrt{k}$（分母有理化，「平方差」）",
    ],
    ('P28', 'P54'): [
        r"【作差】等差：相邻片段和相减 $(S_{2m}-S_m)-S_m$",
        r"【分组】对应项都相差 $md$，共 $m$ 项 $\Rightarrow$ 差为 $m^2d$",
    ],
    ('R33', 'R39'): [
        r"【赋值】$f(x)=a_0+a_1x+\cdots+a_nx^n$ 对一切 $x$ 成立，令 $x=1$：各项系数和；$x=-1$：交错和",
        r"【相加】【相减】两式相加、相减再除以 2：偶次、奇次项系数和",
        r"【赋值】$x=0$：常数项",
    ],
    ('S12', 'P55'): [
        r"【特例】$(x^\alpha)'$ 取 $\alpha=-1,\ \dfrac{1}{2}$",
        r"【代换】$u=ax+b$（「链式法则」）",
    ],
    ('S14', 'R40'): [
        r"【分类计数】$A\cup B$ 分成“只在 $A$”“只在 $B$”“在 $A\cap B$”三类（「分类加法原理」）",
        r"【相减】$\mathrm{card}(A)+\mathrm{card}(B)$ 把 $A\cap B$ 数了两次，减去一次",
    ],
    ('R01', 'P59'): [
        r"【设】「带余除法」$f(x)=(x-a)q(x)+r$",
        r"【赋值】令 $x=a$：$f(a)=0\cdot q(a)+r\Rightarrow r=f(a)$",
    ],
    ('P59', 'R43'): [
        r"【相减】两边之差 $(a_n-b_n)x^n+\cdots+(a_1-b_1)x+(a_0-b_0)$ 对一切 $x$ 为 $0$",
        r"【反证】若不是零多项式，最多有 $n$ 个根（每个根提出一个因式，「因式定理」），与“对一切 $x$ 成立”矛盾 $\Rightarrow a_k=b_k$",
    ],
    ('R17', 'R44'): [
        r"【拆角】$\sin 3\alpha=\sin(2\alpha+\alpha)=\sin 2\alpha\cos\alpha+\cos 2\alpha\sin\alpha$（「和角公式」）",
        r"【代换】「倍角」「勾股恒等式」化成只含 $\sin\alpha$：$=2\sin\alpha(1-\sin^2\alpha)+(1-2\sin^2\alpha)\sin\alpha=3\sin\alpha-4\sin^3\alpha$",
        r"【代换】$\cos 3\alpha$ 同理：$=(2\cos^2\alpha-1)\cos\alpha-2\sin^2\alpha\cos\alpha=4\cos^3\alpha-3\cos\alpha$",
    ],
    ('P19', 'P60'): [
        r"【代入】$\tan(A+B)=-\tan C$ 代入「正切和角变形」$\tan A+\tan B=\tan(A+B)(1-\tan A\tan B)\Rightarrow\tan A+\tan B=-\tan C+\tan A\tan B\tan C$",
        r"【移项】$\tan A+\tan B+\tan C=\tan A\tan B\tan C$",
    ],
    ('S21', 'R41'): [
        r"【分解】$\vec a=x_1\vec i+y_1\vec j$，$\vec b=x_2\vec i+y_2\vec j$",
        r"【合并】「分配律」$\vec a\pm\vec b=(x_1\pm x_2)\vec i+(y_1\pm y_2)\vec j$，$\lambda\vec a=\lambda x_1\vec i+\lambda y_1\vec j$",
        r"【移项】中点：$\overrightarrow{AM}=\overrightarrow{MB}\Rightarrow\overrightarrow{OM}-\overrightarrow{OA}=\overrightarrow{OB}-\overrightarrow{OM}\Rightarrow\overrightarrow{OM}=\dfrac{1}{2}(\overrightarrow{OA}+\overrightarrow{OB})$",
    ],
    ('S21', 'P56'): [
        r"【代换】「共线」$\overrightarrow{AP}=t\overrightarrow{AB}\Rightarrow\overrightarrow{OP}-\overrightarrow{OA}=t(\overrightarrow{OB}-\overrightarrow{OA})$",
        r"【移项】$\overrightarrow{OP}=(1-t)\overrightarrow{OA}+t\overrightarrow{OB}$",
    ],
    ('P49', 'P57'): [
        r"【代入】$|\vec a|\cos\theta$，$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}\Rightarrow|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}$（「夹角公式」）",
        r"【相乘】投影向量 = 投影 × 单位向量 $\dfrac{\vec b}{|\vec b|}\Rightarrow\dfrac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$",
    ],
    ('P49', 'R42'): [
        r"【相减】$|\vec a+\vec b|^2-|\vec a-\vec b|^2=4\vec a\cdot\vec b$（「完全平方」）",
        r"【分解】$\overrightarrow{AB}=\overrightarrow{AM}+\overrightarrow{MB}$，$\overrightarrow{AC}=\overrightarrow{AM}-\overrightarrow{MB}$",
        r"【相乘】「和×差」$\overrightarrow{AB}\cdot\overrightarrow{AC}=|AM|^2-|BM|^2$",
    ],
    ('S06', 'P58'): [
        r"【代入】$\left(\pm\sqrt{-\Delta}\,i\right)^2=(-\Delta)i^2=\Delta\Rightarrow x+\dfrac{b}{2a}=\pm\dfrac{\sqrt{-\Delta}\,i}{2a}$",
    ],
    ('P01', 'P58'): [
        r"【配方】$ax^2+bx+c=0\Rightarrow\left(x+\dfrac{b}{2a}\right)^2=\dfrac{\Delta}{4a^2}<0$",
        r"【开平方】在复数范围内开方",
    ],
    ('S15', 'P61'): [
        r"【代入】奇函数 $f(-x)=-f(x)$ 中令 $x=0$：$f(0)=-f(0)\Rightarrow f(0)=0$",
        r"【相乘】$f,g$ 同为奇函数：$f(-x)g(-x)=[-f(x)][-g(x)]=f(x)g(x)$",
        r"【对称】点 $(x,y)$ 与 $(-x,y)$ 或 $(-x,-y)$ 同在图像上",
    ],
    ('P61', 'P62'): [
        r"【平移】令 $g(x)=f(x+a)$：$g$ 为偶函数 $\iff g(-x)=g(x)\iff f(a+x)=f(a-x)$",
        r"【平移】令 $g(x)=f(x+a)-b$：$g$ 为奇函数 $\iff f(a-x)-b=-[f(a+x)-b]\iff f(a+x)+f(a-x)=2b$",
    ],
    ('S15', 'P63'): [
        r"【代换】$f(x+a)=-f(x)$ 中 $x\to x+a$：$f(x+2a)=-f(x+a)$",
        r"【代入】用两次：$f(x+2a)=-f(x+a)=f(x)\Rightarrow T=2a$",
        r"【代换】$f(x+a)=\dfrac{1}{f(x)}$ 同理：$f(x+2a)=\dfrac{1}{f(x+a)}=f(x)\Rightarrow T=2a$",
    ],
    ('P62', 'P63'): [
        r"【代换】对称轴 $x=a$：$f(a+x)=f(a-x)$ 中 $x\to x-a$：$f(x)=f(2a-x)$",
        r"【代换】再用对称轴 $x=b$，把 $2a-x$ 当自变量：$f(x)=f(2a-x)=f[2b-(2a-x)]=f(x+2b-2a)$",
        r"【定义】「周期函数」周期 $T=2|b-a|$",
    ],
    ('S15', 'R45'): [
        r"【代入】$(x_0,y_0)$ 在 $y=f(x)$ 上 $\iff(x_0-h,\ y_0)$ 在 $y=f(x+h)$ 上（向左平移 $h$）",
        r"【代入】$(x_0,y_0)$ 在 $y=f(x)$ 上 $\iff\left(\dfrac{x_0}{\omega},\ y_0\right)$ 在 $y=f(\omega x)$ 上（横坐标变为 $\dfrac{1}{\omega}$）",
    ],
    ('R45', 'P64'): [
        r"【平移】$x\to x+\varphi$：$y=\sin x\Rightarrow y=\sin(x+\varphi)$",
        r"【伸缩】$x\to\omega x$：$y=\sin(x+\varphi)\Rightarrow y=\sin(\omega x+\varphi)$",
        r"【同乘】乘 $A$：$y=\sin(\omega x+\varphi)\Rightarrow y=A\sin(\omega x+\varphi)$",
    ],
    ('S16', 'P65'): [
        r"【定义】$k=\tan\alpha=\dfrac{y_2-y_1}{x_2-x_1}$",
        r"【定义】直线上任一点 $(x,y)$ 与 $(x_0,y_0)$ 连线的斜率都是 $k$：$\dfrac{y-y_0}{x-x_0}=k$",
        r"【同乘】$x-x_0$：$y-y_0=k(x-x_0)$",
    ],
    ('P49', 'P66'): [
        r"【定义】法向量 $\vec n_1=(A_1,B_1)$，$\vec n_2=(A_2,B_2)$",
        r"【代入】「垂直的坐标条件」两直线垂直 $\iff(A_1,B_1)\perp(A_2,B_2)\iff A_1A_2+B_1B_2=0$",
        r"【代入】「共线的坐标条件」平行或重合 $\iff$ 法向量共线（平行还要排除重合）",
    ],
    ('P57', 'P67'): [
        r"【取点】在直线上取一点 $Q(x_1,y_1)$：$Ax_1+By_1=-C$；法向量 $\vec n=(A,B)$",
        r"【代入】「投影的数量」$d=\dfrac{|\overrightarrow{QP}\cdot\vec n|}{|\vec n|}$",
        r"【展开】$\overrightarrow{QP}\cdot\vec n=A(x_0-x_1)+B(y_0-y_1)=Ax_0+By_0+C\Rightarrow d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$",
    ],
    ('S16', 'P68'): [
        r"【定义】到圆心 $(a,b)$ 距离为 $r$：$\sqrt{(x-a)^2+(y-b)^2}=r$（「两点距离公式」）",
        r"【平方】$(x-a)^2+(y-b)^2=r^2$",
    ],
    ('R03', 'P68'): [
        r"【配方】「完全平方」$x^2+Dx=\left(x+\dfrac{D}{2}\right)^2-\dfrac{D^2}{4}$，$y^2+Ey=\left(y+\dfrac{E}{2}\right)^2-\dfrac{E^2}{4}$",
        r"【移项】$x^2+y^2+Dx+Ey+F=0\Rightarrow\left(x+\dfrac{D}{2}\right)^2+\left(y+\dfrac{E}{2}\right)^2=\dfrac{D^2+E^2-4F}{4}$",
        r"【定义】右边 $>0$ 才是圆",
    ],
    ('P67', 'P69'): [
        r"【作垂线】圆心到弦作垂线，平分弦（「垂径定理」）：半弦长、$d$、$r$ 构成直角三角形",
        r"【开平方】「勾股定理」$\left(\dfrac{|AB|}{2}\right)^2+d^2=r^2\Rightarrow|AB|=2\sqrt{r^2-d^2}$",
    ],
    ('S16', 'P70'): [
        r"【定义】$|PF_1|+|PF_2|=2a$：$\sqrt{(x+c)^2+y^2}+\sqrt{(x-c)^2+y^2}=2a$",
        r"【移项】$\sqrt{(x+c)^2+y^2}=2a-\sqrt{(x-c)^2+y^2}$",
        r"【平方】两次：$a^2-cx=a\sqrt{(x-c)^2+y^2}\Rightarrow(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$",
        r"【代换】令 $b^2=a^2-c^2$：$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$",
        r"【代换】双曲线同理，令 $b^2=c^2-a^2$：$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$",
    ],
    ('S16', 'P71'): [
        r"【定义】到焦点 $\left(\dfrac{p}{2},0\right)$ 的距离 = 到准线 $x=-\dfrac{p}{2}$ 的距离：$|PF|=x_0+\dfrac{p}{2}$",
        r"【相加】焦点弦 = 两段焦半径之和：$|AB|=\left(x_1+\dfrac{p}{2}\right)+\left(x_2+\dfrac{p}{2}\right)=x_1+x_2+p$",
    ],
    ('P45', 'P72'): [
        r"【代入】两交点都在直线 $y=kx+m$ 上：$y_1-y_2=k(x_1-x_2)$",
        r"【代入】「两点距离公式」$|AB|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}=\sqrt{(1+k^2)(x_1-x_2)^2}$",
        r"【开平方】$|AB|=\sqrt{1+k^2}\,|x_1-x_2|$",
        r"【代入】「韦达定理」$|x_1-x_2|=\sqrt{(x_1+x_2)^2-4x_1x_2}$",
    ],
    ('P70', 'P73'): [
        r"【代入】$A(x_1,y_1)$、$B(x_2,y_2)$ 分别代入：$\dfrac{x_1^2}{a^2}+\dfrac{y_1^2}{b^2}=1$，$\dfrac{x_2^2}{a^2}+\dfrac{y_2^2}{b^2}=1$",
        r"【相减】「平方差」$\dfrac{(x_1+x_2)(x_1-x_2)}{a^2}+\dfrac{(y_1+y_2)(y_1-y_2)}{b^2}=0$",
        r"【同除】$(x_1+x_2)(x_1-x_2)$（$x_1\ne x_2$，$x_1+x_2\ne 0$）：$\dfrac{y_1+y_2}{x_1+x_2}\cdot\dfrac{y_1-y_2}{x_1-x_2}=-\dfrac{b^2}{a^2}$，即 $k_{OM}\cdot k_{AB}=-\dfrac{b^2}{a^2}$",
    ],
    ('S17', 'R46'): [
        r"【展开】$\vec a\cdot\vec b=(x_1\vec i+y_1\vec j+z_1\vec k)\cdot(x_2\vec i+y_2\vec j+z_2\vec k)=x_1x_2+y_1y_2+z_1z_2$（$\vec i^2=\vec j^2=\vec k^2=1$，交叉项为 0；与平面坐标式相同，多一项 $z_1z_2$）",
        r"【代入】$\vec b=\vec a$：$|\vec a|=\sqrt{\vec a\cdot\vec a}=\sqrt{x_1^2+y_1^2+z_1^2}$",
    ],
    ('R46', 'P74'): [
        r"【定义】「夹角公式」线线角取不超过 $\dfrac{\pi}{2}$ 的那个，加绝对值：$\cos\theta=|\cos\langle\vec u_1,\vec u_2\rangle|$",
        r"【代换】线面角 $\theta$ 与 $\langle\vec u,\vec n\rangle$ 互余（或差 $\dfrac{\pi}{2}$）：$\theta=\dfrac{\pi}{2}-\langle\vec u,\vec n\rangle$ 或 $\theta=\langle\vec u,\vec n\rangle-\dfrac{\pi}{2}$",
        r"【代入】「诱导公式」化成正弦：$\sin\theta=|\cos\langle\vec u,\vec n\rangle|$",
    ],
    ('P57', 'P75'): [
        r"【代入】「投影的数量」$\overrightarrow{AP}$ 在法向量 $\vec n$ 方向上投影的绝对值：$d=\dfrac{|\overrightarrow{AP}\cdot\vec n|}{|\vec n|}$",
    ],
    ('S18', 'P76'): [
        r"【补形】台体 = 大锥 − 小锥；小锥高 $x$ 满足 $\dfrac{x}{x+h}=\dfrac{\sqrt{S'}}{\sqrt{S}}$（面积比 = 相似比的平方）",
        r"【移项】$x\sqrt{S}=(x+h)\sqrt{S'}\Rightarrow x=\dfrac{h\sqrt{S'}}{\sqrt{S}-\sqrt{S'}}$",
        r"【相减】「锥体体积」$V=\dfrac{1}{3}S(x+h)-\dfrac{1}{3}S'x=\dfrac{1}{3}\left[Sh+x(S-S')\right]$",
        r"【代入】「平方差」$x(S-S')=\dfrac{h\sqrt{S'}(\sqrt{S}-\sqrt{S'})(\sqrt{S}+\sqrt{S'})}{\sqrt{S}-\sqrt{S'}}=h\left(\sqrt{SS'}+S'\right)$",
        r"【合并】$V=\dfrac{1}{3}h\left(S+\sqrt{SS'}+S'\right)$",
    ],
    ('R46', 'P77'): [
        r"【补形】长方体的体对角线就是外接球的直径：$2R=\sqrt{a^2+b^2+c^2}$（「长方体对角线」$l^2=a^2+b^2+c^2$）",
        r"【特例】正方体 $a=b=c$：$R=\dfrac{\sqrt{3}}{2}a$",
    ],
    ('S19', 'R47'): [
        r"【分解】$A\cup B=A\cup(\bar AB)$，$B=AB\cup(\bar AB)$，均为互斥并",
        r"【相减】两式用「互斥加法」后相减：$P(A\cup B)=P(A)+P(B)-P(A\cap B)$",
        r"【特例】对立：$A\cup\bar A=\Omega$，$P(A)+P(\bar A)=1$",
    ],
    ('S19', 'P78'): [
        r"【同乘】「条件概率定义」两边乘 $P(A)$：$P(AB)=P(A)P(B|A)$",
        r"【同除】古典概型分子、分母同除 $n(\Omega)$：$P(B|A)=\dfrac{n(AB)}{n(A)}$",
        r"【相减】$P(A\bar B)=P(A)-P(AB)=P(A)[1-P(B)]$",
    ],
    ('P78', 'P79'): [
        r"【分解】$B=A_1B\cup\cdots\cup A_nB$，各项两两互斥",
        r"【代入】每项用「乘法公式」，互斥相加",
        r"【作比】贝叶斯：$P(A_iB)$ 用两种「乘法公式」表示，相等后相除",
    ],
    ('S20', 'R48'): [
        r"【展开】$\sum(ax_i+b)p_i=a\sum x_ip_i+b\sum p_i$",
        r"【展开】$D(X)=\sum\left[x_i^2-2x_iE(X)+E(X)^2\right]p_i$",
        r"【合并】逐项求和",
    ],
    ('R48', 'R49'): [
        r"【特例】把每个数据看作取值概率为 $\dfrac{1}{n}$",
        r"【展开】分层：$\sum(x_i-\bar w)^2=\sum(x_i-\bar x)^2+m(\bar x-\bar w)^2$（交叉项 $\sum(x_i-\bar x)=0$）",
    ],
    ('R49', 'P82'): [
        r"【配方】$Q(a,b)=\sum(y_i-bx_i-a)^2$ 先对 $a$ 配方 $\Rightarrow a=\bar y-b\bar x$",
        r"【配方】再对 $b$ 配方",
    ],
    ('P78', 'P80'): [
        r"【相乘】指定 $k$ 次成功的一种情形概率为 $p^k(1-p)^{n-k}$（「独立事件乘法」）",
        r"【分类计数】共 $C_n^k$ 种，互斥相加",
    ],
    ('S19', 'P81'): [
        r"【分步计数】样本点总数 $C_N^n$，恰有 $k$ 件次品的有 $C_M^kC_{N-M}^{n-k}$ 种（「古典概型」）",
    ],
    ('S04', 'P83'): [
        r"【定义】弧度制：弧长与半径之比 $|\alpha|=\dfrac{l}{r}\Rightarrow l=|\alpha|r$",
        r"【作比】面积与圆心角成正比：$S=\dfrac{|\alpha|}{2\pi}\cdot\pi r^2=\dfrac{1}{2}|\alpha|r^2$",
    ],
    ('P78', 'P84'): [
        r"【代入】若独立，$P(AB)=P(A)P(B)$，即 $\dfrac{a}{n}\approx\dfrac{a+b}{n}\cdot\dfrac{a+c}{n}$",
        r"【作差】$an-(a+b)(a+c)=ad-bc$：$|ad-bc|$ 越大越偏离独立，$\chi^2$ 把它标准化（课本给出）",
    ],
    ('S20', 'P85'): [
        r"【对称】概率 = 曲线下的面积；关于 $x=\mu$ 对称的两块面积相等",
    ],
    ('R17', 'R50'): [
        r"【设】$a=r\cos\varphi$，$b=r\sin\varphi$，转后为 $(r\cos(\varphi+\theta),\ r\sin(\varphi+\theta))$",
        r"【展开】「和角公式」$r\cos(\varphi+\theta)=a\cos\theta-b\sin\theta$，$r\sin(\varphi+\theta)=a\sin\theta+b\cos\theta$",
    ],
    ('P21', 'P86'): [
        r"【代入】「正弦定理」$\triangle ABD$：$\dfrac{BD}{\sin\angle BAD}=\dfrac{AB}{\sin\angle ADB}$；$\triangle ACD$：$\dfrac{DC}{\sin\angle CAD}=\dfrac{AC}{\sin\angle ADC}$",
        r"【作比】$\angle BAD=\angle CAD$，$\sin\angle ADB=\sin\angle ADC$（互补，「诱导公式④」）$\Rightarrow\dfrac{BD}{DC}=\dfrac{AB}{AC}$",
    ],
    ('R14', 'P87'): [
        r"【对称】「诱导公式④」$\sin(\pi-\alpha)=\sin\alpha$ 给出 sin 的第二组角；$a=\pm 1$ 时两组合并",
        r"【对称】「诱导公式③」$\cos(-\alpha)=\cos\alpha$ 给出 cos 的 $\pm$；$a=\pm 1$ 时两组合并",
        r"【推广】再加周期：sin/cos 加 $2k\pi$，tan 加 $k\pi$（tan 周期 $\pi$，每个周期只有一个角）",
    ],
    ('S04', 'R52'): [
        r"【定义】终边上一点 $(x,y)$，$r=\sqrt{x^2+y^2}$",
        r"【取倒数】$\sec\alpha=\dfrac{r}{x}$，$\csc\alpha=\dfrac{r}{y}$，$\cot\alpha=\dfrac{x}{y}$",
    ],
    ('S15', 'P88'): [
        r"【对调】$y=f(x)$ 解出 $x=f^{-1}(y)$，对调 $x,y$：$y=f^{-1}(x)$",
        r"【对称】$(x,y)$ 与 $(y,x)$ 关于直线 $y=x$ 对称：$(a,b)$ 在 $f$ 上 $\iff(b,a)$ 在 $f^{-1}$ 上",
    ],
    ('P13', 'P89'): [
        r"【代入】「tan 的诱导公式」$\tan(\alpha+\pi)=\tan\alpha$，$\alpha=\omega x+\varphi$：$A\tan\left[\omega\left(x+\dfrac{\pi}{\omega}\right)+\varphi\right]=A\tan(\omega x+\varphi+\pi)=A\tan(\omega x+\varphi)$（$\omega x$ 增加 $\pi$ 为一个周期）",
        r"【定义】「周期函数」$T=\dfrac{\pi}{|\omega|}$",
    ],
    ('S14', 'R51'): [
        r"【定义】按“且”“或”“非”逐个元素验证（维恩图）",
    ],
    ('S01', 'R53'): [
        r"【同乘】若 $a\ne 0$，两边乘 $\dfrac{1}{a}$：$ab=0\Rightarrow\dfrac{1}{a}\cdot ab=\dfrac{1}{a}\cdot 0\Rightarrow b=0$",
    ],
    ('P05', 'P90'): [
        r"【累乘】每过一期乘一次 $1+r$：$a\Rightarrow a(1+r)\Rightarrow a(1+r)^2\Rightarrow\cdots\Rightarrow a(1+r)^x$",
    ],
    ('R27', 'P91'): [
        r"【设】$w^n=z$，$w=\rho(\cos\varphi+i\sin\varphi)$",
        r"【逆用】「棣莫弗公式」比较模和辐角：$\rho^n=r$，$n\varphi=\theta+2k\pi$（辐角相差 $2k\pi$）",
    ],
    ('P31', 'P92'): [
        r"【代换】各期还款的现值成等比数列，公比 $\dfrac{1}{1+r}$",
        r"【代入】「等比求和」",
    ],
    ('P31', 'P93'): [
        r"【取极限】$|q|<1$ 时 $q^n\to 0$（老教材数列极限）",
    ],
    ('S09', 'R54'): [
        r"【相加】每项由前两项相加",
    ],
    ('S07', 'P94'): [
        r"【分步计数】每一位 $n$ 种，共 $m$ 步（「分步乘法原理」）",
    ],
    ('P34', 'P95'): [
        r"【对应】$n$ 个元素排成一行，在 $n-1$ 个空中插 $r-1$ 块隔板",
        r"【代换】非负解令 $y_i=x_i+1$",
    ],
    ('S08', 'R55'): [
        r"【定义】$\Delta x$ 很小时差商 $\approx f'(x_0)$",
        r"【同乘】两边乘 $\Delta x$",
    ],
    ('P69', 'P96'): [
        r"【代入】交点同时满足两个方程，所以满足它们的任意组合：$f(x_0,y_0)=0$，$g(x_0,y_0)=0\Rightarrow f(x_0,y_0)+\lambda g(x_0,y_0)=0$",
        r"【赋值】圆系中 $\lambda=-1$：$x^2+y^2$ 项消去，得公共弦所在直线",
    ],
    ('P70', 'P97'): [
        r"【平方】椭圆标准方程推导中平方整理：$\sqrt{(x+c)^2+y^2}=a+\dfrac{c}{a}x$",
        r"【提取】$a+\dfrac{c}{a}x=\dfrac{c}{a}\left(x+\dfrac{a^2}{c}\right)$",
        r"【代换】$e=\dfrac{c}{a}$：$|PF_1|=e\cdot$（$P$ 到直线 $x=-\dfrac{a^2}{c}$ 的距离）",
    ],
    ('S04', 'P98'): [
        r"【代入】「三角函数定义」$\cos\theta=\dfrac{x}{\rho}$，$\sin\theta=\dfrac{y}{\rho}$：$x=\rho\cos\theta$，$y=\rho\sin\theta$",
        r"【定义】「单位圆」上的点是 $(\cos\theta,\sin\theta)$",
        r"【伸缩】横、纵坐标都乘 $r$：$(r\cos\theta,r\sin\theta)$；横乘 $a$、纵乘 $b$：$x=a\cos\varphi$，$y=b\sin\varphi$（椭圆）",
        r"【平移】$(r\cos\theta,r\sin\theta)$ 平移到圆心 $(a,b)$：$x=a+r\cos\theta$，$y=b+r\sin\theta$（圆）",
    ],
    ('S17', 'P99'): [
        r"【推广】「平面向量基本定理」加一个不在平面内的方向 $\vec c$：$\vec p=x\vec a+y\vec b+z\vec c$，$(x,y,z)$ 唯一",
    ],
    ('P74', 'P100'): [
        r"【作垂线】斜线 $PA$ 交平面于 $A$，$PO\perp$ 平面于 $O$，$AO$ 为射影；面内直线 $l$ 过 $A$，作 $OB\perp l$ 于 $B$，连 $PB$",
        r"【定义】「线面垂直判定」$l\perp PO$，$l\perp OB\Rightarrow l\perp$ 平面 $POB\Rightarrow l\perp PB$",
        r"【作比】$\mathrm{Rt}\triangle PAO$：$\cos\theta_1=\dfrac{AO}{PA}$；$\mathrm{Rt}\triangle AOB$：$\cos\theta_2=\dfrac{AB}{AO}$（$\theta_1$ 斜线与射影所成角，$\theta_2$ 射影与 $l$ 所成角）",
        r"【相乘】$\cos\theta_1\cos\theta_2=\dfrac{AB}{PA}=\cos\theta$（$\mathrm{Rt}\triangle PBA$）",
    ],
    ('S18', 'P101'): [
        r"【作垂线】球心 $O$ 与截面圆心 $O'$ 的连线垂直于截面，$OO'=d$",
        r"【开平方】「勾股定理」$r^2+d^2=R^2\Rightarrow r=\sqrt{R^2-d^2}$",
        r"【代入】北纬 $\varphi$：$d=R\sin\varphi$，$r=R\cos\varphi$，纬线长 $2\pi R\cos\varphi$",
    ],
    ('S18', 'P102'): [
        r"【对比】「祖暅原理」与球体积同法（老教材给出）：距球心 $t$ 的截面积 $\pi(R^2-t^2)$ = 圆柱截面 $\pi R^2$ − 圆锥截面 $\pi t^2$",
        r"【相减】$t$ 从 $R-h$ 到 $R$（$h\le R$）：球缺体积 = 圆柱段 − 圆台段 $=\pi R^2h-\dfrac{\pi}{3}\left[R^3-(R-h)^3\right]$",
        r"【展开】$=\pi R^2h-\dfrac{\pi}{3}\left(3R^2h-3Rh^2+h^3\right)=\pi h^2\left(R-\dfrac{h}{3}\right)$（$h>R$ 时用球体积减去高 $2R-h$ 的球缺，结果同式）",
    ],
    ('S23', 'P85'): [
        r"【对称】密度函数中 $x-\mu$ 只以平方出现，曲线关于 $x=\mu$ 对称",
    ],
    ('S23', 'P103'): [
        r"【展开】$X=\dfrac{Y-\mu}{\sigma}=\dfrac{1}{\sigma}Y-\dfrac{\mu}{\sigma}$",
        r"【代入】用 $E(aY+b)$、$D(aY+b)$：$E\left(\dfrac{Y-\mu}{\sigma}\right)=0$，$D\left(\dfrac{Y-\mu}{\sigma}\right)=1$",
        r"【定义】均值 0、方差 1，所以 $X\sim N(0,1)$（正态变量作线性变换后仍服从正态分布，课本承认）",
    ],
    ('S20', 'R56'): [
        r"【代入】$X$ 只取 1、0，概率 $p$、$1-p$，代入均值、方差的定义",
        r"【代入】$E(X)=1\cdot p+0\cdot(1-p)$；$D(X)=(1-p)^2p+(0-p)^2(1-p)=p(1-p)$",
    ],
    ('R49', 'R57'): [
        r"【合并】同值的数据合并，频率作权，就是加权平均",
    ],
}
