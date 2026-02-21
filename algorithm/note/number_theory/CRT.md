在求解**模数两两互质**的线性同余方程组时，可以使用中国剩余定理。
$$
\begin{cases}
x\equiv r_1(modm_1) \\
x\equiv r_2(modm_2) \\
\vdots \\
x\equiv r_n(modm_n) & 
\end{cases}
$$
具体步骤为

1. 计算所有模数的积 $M$ 
2. 计算第 $i$ 个方程的 $c_i=\frac{M}{m_i}$ 
3. 计算 $c_i$ 在模 $m_i$ 意义下的逆元 $c_i^{-1}$ 
4. 最终结果 $x=\sum_{i=1}^n r_ic_ic_i^{-1}\pmod{M}$ 

```python
def crt(r, m):
    n = len(r)

    M = 1
    for x in m:
        M *= x
    
    s = 0
    for i in range(n):
        c = M // m[i]
        s += r[i] * c * pow(c, -1, m[i])

    return s % M
# 测试链接: https://www.luogu.com.cn/problem/P1495
```

扩展中国剩余定理



```python
```

