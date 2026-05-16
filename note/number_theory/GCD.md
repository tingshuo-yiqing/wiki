### 辗转相除法

递归写法，Python不推荐这种写法。

```python
def gcdx(a, b):
    return gcdx(b, a % b) if b else a
```

迭代写法

```python
def gcdx(a, b):
    while b:
        c = b
        b = a % b
        a = c
    return a
```

求一组数的 $\gcd$ 和 $\operatorname{lcm}$ 时初始化为 $1$。

### 裴蜀定理

一定存在整数 $x$ 和 $y$ ，使得
$$
ax+by=\gcd(a,b)
$$
不难看出
$$
ax+by=gcd(a,b)\times n
$$
再推广可得
$$
\sum_{i=1}^nA_iX_i=\gcd(A_1,A_2,\cdots,A_n)
$$
对原始式子直观的理解是，对两个整数 $a,b$ 进行加减可以凑出什么数字，那就是它们最大公约数的倍数。

* [P4549裴蜀定理](https://www.luogu.com.cn/problem/P4549) 推广二，就是求一系列数可以凑出的最小正整数，输入可能是负的所以在求 $\gcd$ 时要取绝对值。
* [HDU - 5512 ](https://vjudge.net/problem/HDU-5512/origin) 使用规则可以修理的塔的编号为 $xj+yk$ ，那么可以凑出的整数是 $d=\gcd(j,k)$ ，在 $n$ 的范围内一共有 $\left\lfloor\dfrac{n}{d}\right\rfloor$ 座，奇数的话先手会赢。
* [poj-1597](https://vjudge.net/problem/OpenJ_Bailian-1597#author=GPT_zh) 要均匀的生成 $0$ 到 $\mathrm{MOD}-1$ 的所有数字的话，必须要 $xa+by=1$ 即 $a,b$ 互质。 

可以使用扩展欧几里得算法求具体的 $x,y$ 。

### 扩展欧几里得算法

求 $ax+by=\gcd(a,b)$ 的一组整数解时，当 $b=0$ 时，一组解为 $x=1,y=0$ 。于是我们可以通过一层一层**辗转相除**来让 $b=0$ 再一层一层返回，这个过程可以计算出 $x,y$ 的一般解。

辗转相除过程中有 $\gcd(a,b)=\gcd(b,a \% b)$ ，有裴蜀定理得
$$
\begin{aligned}
\mathrm{gcd}(a,b) & =ax+by \\
\mathrm{gcd}(b,a\%b) & =bx_1+(a\%b)y_1 \\
 & =bx_{1}+(a-\left\lfloor\frac{a}{b}\right\rfloor\times b)y_{1} \\
 & =ay_{1}+b(x_{1}-\frac{a}{b}y_{1})
\end{aligned}
$$
所以 $x=y_1,y=x_1-\frac{a}{b}y_1$ ，可以递归求解。

```python
 def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = exgcd(b, a % b)
    return d, y, x - a // b * y   # 返回元组 (gcd(a, b), x, y)
# 测试链接: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E
```

令 $d=\gcd(a,b)$ 可以构造通解。
$$
\begin{cases}
x=x_0+\frac{b}{d}*k \\
y=y_0-\frac{a}{d}*k & 
\end{cases}
$$


#### 应用一：求逆元

求 $ax\equiv1\pmod{m}$ 中的 $x$ ，可以转化为 $ax+my=1$ ，这是标准的使用扩欧求解 $x,y$ 的不定方程。如果 $\gcd(a,m)\neq1$ 则逆元不存在。

```python
def exinv(a, m):
    d, x, y = exgcd(a, m)  # 扩欧模板
    if d != 1:
        return None
   	return x % m   # Python负数直接模成正数
```

Python3.8+ 可以直接使用 `pow(a, -1, m)` 函数求逆元，其底层实现就是扩展欧几里得算法。

#### 应用二：解线性同余方程

求解 $ax \equiv b\pmod{m}$ 中的 $x$ 等价于 $ax+my=b$ 。这是一个裴蜀等式的变体。

1. 调用扩欧函数得到 $d,x,y$ 后建立一个方程 $ax+my=d$ 

2. 判断是否有解，如果 $b$ 不能被 $d$ 整除则方程无解

3. 求特解，如果有解将等式两边同时乘以 $\dfrac{b}{d}$ 
   $$
   a\cdot(x_0\cdot\frac{b}{d})+m\cdot(y_0\cdot\frac{b}{d})=b
   $$
   所以，一个特解是 $x\cdot \frac{b}{d}$ 。

   方程通解周期为 $\dfrac{m}{d}$ 最小正整数解是
   $$
   x_{ans}=(x\cdot\frac{b}{d})\quad(\mathrm{mod~}\frac{m}{d})
   $$
   

```python
def cong(a, b, m):
    d, x, y = exgcd(a, m)  # 扩欧模板
    if b % d != 0:
        return None
    mod = m // d
    return x * (b // d) % mod
# 测试链接: https://www.luogu.com.cn/problem/P1082
```

