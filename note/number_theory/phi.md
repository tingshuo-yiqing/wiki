部分整理自 [cp-algorithms](https://cp-algorithms.com/algebra/phi-function.html)

$1$ 到 $N$ 中与 $N$ （包含 $1$ 和 $N$ ）互质的数的个数被称为欧拉函数，记作 $\phi(N)$ 。

这里有一些重要的 $\phi$ 函数的特性。

如果 $N$ 是质数的话，因为质数和任何数都互质，所以有


$$
\phi(N) = N-1
$$


如果 $N$ 是质数且 $k\ge1$ 的话，有


$$
\phi(N^k)=\phi(N^k)-\phi(N^{k-1})=(N-1){N^{k-1}}
$$


如果 $a$ 和 $b$ 互质的话，有


$$
\phi(ab)=\phi(a)\cdot\phi(b)
$$


根据唯一分解定理和以上特性，如果 $n=p_1^{a_1}\cdot p_2^{a_2}\dots p_k^{a_k}$ ，那么有：


$$
\begin{aligned} \phi(n) & =\phi({p_1}^{a_1})\cdot\phi({p_2}^{a_2})\cdots\phi({p_k}^{a_k}) \\ & =\left({p_1}^{a_1}-{p_1}^{a_1-1}\right)\cdot\left({p_2}^{a_2}-{p_2}^{a_2-1}\right)\cdots\left({p_k}^{a_k}-{p_k}^{a_k-1}\right) \\ & =p_1^{a_1}\cdot\left(1-\frac{1}{p_1}\right)\cdotp_2^{a_2}\cdot\left(1-\frac{1}{p_2}\right)\cdots p_k^{a_k}\cdot\left(1-\frac{1}{p_k}\right) \\ & =n\cdot\left(1-\frac{1}{p_1}\right)\cdot\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_k}\right) \end{aligned}
$$


在质因数分解的基础上可以 $\sqrt{N}$ 求欧拉函数

```python
def phi(n):
    res = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res = res // i * (i - 1) 
            while n % i == 0:
                n //= i
    if n != 1:
        res = res // n * (n - 1)
    return res
# 测试链接: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D
```

线性筛法求 $1$ 到 $n$ 的欧拉函数，传入 $n$ 求的是 `[1, n]` 。

设 $m=p_j\cdot i$ $p_j$ 为最小质因子，利用三个性质

1. 如果 $i$ 是质数，则 $\phi(i) = i -1$

2. 如果 $i \% p=0$ ，即 $p_j$ 是最小质因子，则 $i$ 包含了 $m$ 的所有质因子

   $\phi(m)=m\times \prod_{k=1}^s{\dfrac{p^k-1}{p^k}} = p_j\times i\times \prod_{k=1}^s{\dfrac{p^k-1}{p^k}}$ 

   又因为 $i$ 包含了 $m$ 的所有质因子，所以后两个的乘积就是 $\phi(i)$ 可以推出

   $\phi(m) = p_j \times \phi(i)$

3. 如果 $i\%p \neq 0$ 即 $i$ 与 $p$ 互质，那么直接

   $\phi(m)=\phi(p_j\times i)=(p_j-1)\times\phi(i)$

```python
def euler(n):
    phi = [0] * (n + 1)
    phi[1] = 1
    primes = []
    is_prime = [True] * (n + 1)
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            phi[i] = i - 1  # 性质1
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:  
                phi[i * p] = phi[i] * p   # 性质2 
                break
            phi[i * p] = phi[i] * (p - 1)  # 性质3
    return phi
# 测试链接: https://www.spoj.com/problems/ETF/en/
```



