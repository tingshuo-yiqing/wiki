## [C. Separated Lunch](https://atcoder.jp/contests/abc374/tasks/abc374_c)

在数据为 $2≤N≤20$ 的情况下考虑使用搜索和枚举

递归实现**指数型枚举**，即每一个部门都有下雨不选两种状态。最终取 $\max$ 即可。

```python
ans = max(ans, min(now, total - now))
```

也可以使用**二进制枚举**，选与不选组成的 $2^n$ 的方案数。 

## [B. V](https://atcoder.jp/contests/abc289/tasks/abc289_b)

根据题意不难理解，$a[i]$会把$a[i]$和$a[i] + 1$连在一起，我们只需要从小到大遍历依次**逆序输出**连在一起的连通块即可。

比如$a$数组为：

```
1 2 3 7 8 9
```

此时从小到大连通情况为：

```
1-2-3-4  5  6  7-8-9-10
```

分别逆序输出：

```python
4 3 2 1 5 6 10 9 8 7
```

我们可以使用一个大小为$n-1$的$\text{connect}$数组判断有没有连接在一起，因为大小为$n$的数组有$n-1$个连接位置。

最后双指针遍历即可。

## [A. I hate 1](https://atcoder.jp/contests/arc198/tasks/arc198_a)

条件是集合中任何一对元素都满足 $\:x\bmod y\not=1\:$ 我们知道连续两个数一定满足$x\bmod y=\:1\:$ 所以结果都是至少隔开的。

因为偶数模偶数一定是偶数，所以可以选择间隔偶数大小为 $\lfloor N \rfloor$ 。奇数模奇数可能是 $1$ 所以这里的好集合就是**间隔偶数**。

## [Many Oranges](https://atcoder.jp/contests/abc195/tasks/abc195_b)

找出隐含的条件、再遍历 $k$ 即可。

条件是：
$$
k⋅A≤T≤k⋅B
$$
