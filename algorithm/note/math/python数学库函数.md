常用函数一览：

- **math.gcd(a, b)**: 最大公约数。在处理分数、循环节或数论题时必用。
- **math.lcm(a, b)**: 最小公倍数（Python 3.9+ 引入）。
- **math.isqrt(n)**: 整数平方根。返回 $\lfloor\sqrt{n}\rfloor$ ，**避免了浮点数精度误差**，在判断质数或大数运算时非常有用。
- **math.comb(n, k)**: 计算组合数 $C_n^i$ （Python 3.8+）。
- **math.perm(n, k)**: 计算排列数  $A_n^i$ 。
- **math.factorial(n)**: 阶乘。
- **math.ceil(x) / math.floor(x)**: 向上/向下取整。
- **math.inf**: 表示正无穷大，常用于初始化最小值变量 min_val = math.inf。