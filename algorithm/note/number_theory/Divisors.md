### 唯一分解定理 (Fundamental Theorem of Arithmetic)

任何一个大于 1 的整数 $n$ 都可以唯一地分解为若干个质数的乘积。
其标准分解式为：



$$
n = p_1^{a_1} \cdot p_2^{a_2} \cdot p_3^{a_3} \cdots p_k^{a_k} = \prod_{i=1}^{k} p_i^{a_i}
$$



其中：

- $p_i$ 是递增的质数 ($p_1 < p_2 < \dots < p_k$)。
- $a_i$ 是正整数，表示质因子 $p_i$ 的指数。

通过“试除法”在 $O(\sqrt{n})$ 时间内完成。

```python
n = t
for i in range(2, int(t ** 0.5) + 1):
    while n % i == 0:
        cnt += 1
        n //= i
if n != 1:  # 千万不要忘记了
    print(n, 1)
```

### 约数定理 (Divisor Theorem)

基于唯一分解式 $n = \prod_{i=1}^{k} p_i^{a_i}$，我们可以推导出约数的性质。

#### 约数个数定理

$n$ 的正约数个数记为 $d(n)$。每一个约数都可以表示为 $p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$，其中 $0 \le x_i \le a_i$。

根据乘法原理，每个 $p_i$ 的指数 $x_i$ 有 $(a_i + 1)$ 种选法（包括 0）。
公式：


$$
d(n) = (a_1 + 1)(a_2 + 1)(a_3 + 1) \cdots (a_k + 1)\\
d(n)=\prod_{i=1}^{k}(a_i+1)
$$



使用一个字典将分解质因数后的结果存起来，适合单个数或多个数相乘的约数个数

```python
def divs(n):
	res = defaultdict(int)
    t = n
    for i in range(2, int(n **0.5) + 1):
        while t % i == 0:
            res[i] += 1
            t //= i
    if t != 1:
        res[t] += 1
# 对n调用divs函数，最后执行 d(n) 公式
ans = 1
for k, v in res.items():
    ans *= (v + 1)
```



#### 约数和定理

$n$ 的所有正约数之和记为 $\sigma(n)$。
公式：



$$
\sigma(n) = (1 + p_1 + p_1^2 + \dots + p_1^{a_1})(1 + p_2 + p_2^2 + \dots + p_2^{a_2}) \cdots (1 + p_k + p_k^2 + \dots + p_k^{a_k})
$$



利用等比数列求和公式，可以简化为：



$$
\sigma(n) = \prod_{i=1}^{k} \frac{p_i^{a_i+1} - 1}{p_i - 1}
$$



使用一个字典将分解质因数后的结果存起来，再累乘。适合求当个数，或多个数相乘的约数之和。

```python
def decompos(n):
	cnt = defaultdict(int)
    t = n
    for i in range(2, int(n ** 0.5) + 1):
        while t % i == 0:
            cnt[i] += 1
            t //= i
    if t != 1:
        cnt[t] += 1

    res = 1
    for k, v in cnt.items():
        t = (pow(k, v+1) - 1) // (k - 1)
        res *= t
    return res
```

**注**：上述的 $d(n)$ 和 $\sigma(n)$ 函数都是积性函数，满足性质 $f(x\cdot y)=f(x)\cdot f(y)$ 

### 约数之积





模板题； [ Divisor Analysis](https://vjudge.net/problem/CSES-2182) 已经给出了唯一分解的结果了，直接一次遍历可求上述三个公式的结果
