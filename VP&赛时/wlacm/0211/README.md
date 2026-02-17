## 赛后复盘

### [ 带花树算法](https://codeforces.com/group/BMD0S1NXbC/contest/670808/problem/B)

使用哈希表储存，枚举后构造 $2$ 的幂判断在不在哈希表中，注意不能和自身相同除非在数组中有不止一个数。 

### [最小割游戏](https://codeforces.com/group/BMD0S1NXbC/contest/670808/problem/C)

最大化最小值，经典的 **Minmax** 问题。想到枚举前缀与后缀但是没有想到最小化最大值。

先预处理前缀和和后缀和数组。 $pf_i$ 表示前 $i-1$ 的和， $sf_i$ 表示从当前 $i$ 到最后的和。

```python
pf = [0] * (m + 1)
for i in range(m):
    pf[i + 1] = pf[i] + g[0][i]

sf = [0] * (m + 1)
for i in range(m-1, -1, -1):
    sf[i] = sf[i + 1] + g[1][i]
```

然后枚举每一个点作为小Q的拐点，对手则只有两种方式可以获取流量：左下角那块和右上角那块。于是我们先满足对手的条件，每次从两块中选最大的，再满足小Q的条件整体取最小值。

```python
a = sum(g[0])
b = sum(g[1])
ans = inf
for i in range(m):
    ans = Min(ans, Max(a - pf[i + 1], b - sf[i]))
```

### [ 小Q的子集和问题](https://codeforces.com/group/BMD0S1NXbC/contest/670808/problem/D)

先排序，排序后只有两种情况：

* 假如是最后一个，那枚举前 $n-1$ 个模拟删除，看看删除完哪个会等于最后一个
* 假如倒数第二个是的话，那 $a$ 数组只能是前 $n-2$ 个，判断一下
* 以上两个都不满足输出 $-1$ 即可



### [编辑距离](https://codeforces.com/group/BMD0S1NXbC/contest/670808/problem/I)

### [ 多源最短路路径还原](https://codeforces.com/group/BMD0S1NXbC/contest/670808/problem/J)

