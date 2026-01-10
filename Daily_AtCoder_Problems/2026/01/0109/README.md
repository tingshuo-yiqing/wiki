## [ C. Bowls and Dishes](https://atcoder.jp/contests/abc190/tasks/abc190_c)

数据范围：

- $2≤N≤100$
- $1≤M≤100$
- $1≤A_i<B_i≤N$
- $1≤K≤ 16$
- $1≤C_i<D_i≤N$

考察二进制枚举，最多 $16$ 个人，且内部最多遍历 $100$ 次条件。时间复杂度为 $O(N\times2^{K})$ 在可接受范围内。

准备两个数组 $conditions$ 和 $behave$ 分别存条件和人的选择。而二进制位对应人的选择恰好对应的两个选择 $C_i、D_i$ 

```python
for i in range(1 << k):
    dish = [0] * (n + 1)
    for j in range(k):
        dish[behave[j][(i >> j) & 1]] += 1  # 选择了就加一
    cnt = 0
    for a, b in conditions:
        if dish[a] and dish[b]:
            cnt += 1
```

## [B. Mex Boxes](https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b)

考察枚举，枚举 $k$ 次，每次边查边删动态的求 $mex$ ，可以在 $k$ 次下每次求到最大的 $\text{mex}$ 直到 $k$ 次或 $\text{mex}$ 已经为 $0$ 了。

## [Mex and Update](https://atcoder.jp/contests/abc330/tasks/abc330_e)

考察数据结构，$\text{mex}$ 的单点修改模板题，每次修改一个地方并输出当前数组的 $\text{mex}$ 。可以使用有序集合或懒删除堆（Python没有内置的有序集合）。

有序集合方法模板具体可以看这篇文章: [MEX (minimal excluded) of a sequence](https://cp-algorithms.com/sequences/mex.html#mex-with-array-updates)

重点讲一下懒删除堆的方法。
