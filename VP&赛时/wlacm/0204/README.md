## 赛后复盘

[比赛链接](https://codeforces.com/group/BMD0S1NXbC/contest/668437)

赛时4题EKIG，补ABDHF

### A. [ Circular Dance](https://codeforces.com/problemset/problem/1095/D)

条件比较好满足，只有两种情况要么 $i,j,k$ 要么 $i,k,j$ ，判断方式也很直接，判断 $k$ 在不在 $g_j$ 里面就可以了。

* 如果 $k$ 在$g_j$ 里，说明顺序是 $i,j,k$ 的

关键是输出路径，使用一个数组储存路径，然后再 不断地更新。具体代码为：

```python
ans = [1]
ans.append(g[1][0])

for _ in range(n - 2):
    # 使用数组存酒不需要第三个临时变量了
    cur = ans[-2]
    nxt = ans[-1]

    #! 判断一次 nxt 的下两个不能是 cur 
    if nxt == g[cur][0]:
        ans.append(g[cur][1])
    else:
        ans.append(g[cur][0])
```

### [B.Almost Regular Bracket Sequence](https://codeforces.com/contest/1095/problem/E)

**前后缀分解**解决括号序列匹配问题，修改第 $i$ 个括号时需要前 $i-1$ 个和 $i + 1$ 到最后面的序列**都要满足**两个条件：

1. 前 $i-1$ 的括号序列 $pf_i$ 大于等于 $0$

### [C. K-th Path](https://codeforces.com/contest/1196/problem/F)

前 $k$ 短的路径一定由前 $k$ 短的边组成，**离散化**一下可以 $k^3$ 或 $k^2\log k$ 跑最短路。

这里要注意两个点：离散化和防止重复计算。具体步骤看 [Editoral](../../../Daily_AtCoder_Problems/2026/02/0206/README.md)

### D.  [Cutting Figure](https://codeforces.com/contest/193/problem/A)

> 这道题 PyPy3直接使用 BFS 会超时需要优化，比较简单的优化是坐标压缩（扁平化）去掉元组哈希集合的查找，将二维坐标映射成一维索引，使用一个数组进行真正的 $O(1)$ 查找。

题意：一个 $n\times m$ 的网格，含有若干星星且为连通的，移除最少多少个星星才可以将图变为不连通的。根据定义，空集和仅包含一颗星星的集合也是连通的。

在网格图中，假如全图全都是星星，那最少需要去掉两个星星才可以将一个连通图变成两个，因此一般的解得最大值不超过 $2$ 。且根据定义当星星的个数大于等 $3$ 时才有解。

*  $1\le n,m\le 40$ 数据量下，我们可以枚举每一个星星并将其去掉
* 去掉后判断剩下的图连不连通，如果连通那么最少个数就是 $1$ 否则还得再移至少一个

判断连通的话可以枚举第一个星星再使用 BFS 判断覆盖的星星数有没有**总星星数减一**来判断连通性。

### E. 星辰图谱

给定一个字符串计算修改其至少有 $k$ 种字符的最小次数。只需判断：

* 字符长度是否小于 $k$ ？若小于直接 `impossible`
* 再使用集合看看当前字符串有多少种字符，再 $\max(len(set(s))-k, 0)$ 即可。

### F. 星辰脉搏

三个 while 循环依次检验对应的三个条件，如果最终 $i=n-1$ 的话说明这个序列是符合对应的三个要求的。

还可以使用**状态机** $state$ 维护三种条件的状态。$0,1,2$ 分别对应上升、平，下降。

* 当 $a_i<a_{i+1}$ 时，如果此时状态不等于 $0$ 时返回 NO
* 当 $a_i=a_{i+1}$ 时，将状态设为 $1$ 且等于 $2$ 时返回 NO
* 当 $a_i > a_{i+1}$ 时，将状态设为 $2$ 即可

### G. [Powers  Of  Two](https://codeforces.com/problemset/problem/1095/C)

判断一个数能不能恰好被分成 $k$ 个 $2$ 的幂（ $1,2,4,8,\cdots$ ）。先确定上下界， $n$ 的二进制位 $1$ 的个数 $cnt1$ 就是下界， $n$ 本身就是上界（全为 $1$ 时）。

确定上下界后，一个数分成的最少得序列就是它的二进制的对应的 $1$ 位的 $2$ 的幂的序列，我们只需在这个序列的基础上维护当前序列最大的值再不断地将最大值除 $k-cnt1$ 次 $2$ 就可以的到目标序列。

### H. [DZY Loves Chessboard](https://codeforces.com/problemset/problem/445/A)

实现不要管 `-` ，没有如何影响。

网格图上实现二分图染色的话直接用 $(i+j)\bmod 2$ 就可以构造一个网格二分图。

如何也可以使用 BFS/DFS 枚举邻边染色。这里使用 BFS 时犯了两个错误：

1. 只将 `.` （第一个）进了一次队列，后面遍历完了后还有剩余的 `.` 没有进队列
2. 复制代码时，没有修改变量，导致内部循环的 $i,j$ 和外部的 $i,j$ 重名了

### I.[Repeating Cipher](https://codeforces.com/contest/1095/problem/A)

模拟即可。从 $2$ 开始一个一个添加进数组。

### [J. Make It Connected](https://codeforces.com/contest/1095/problem/F)

假如没有特殊边的话，最小代价就是代价中的最小值 $u$ 与其它所有边的连接。假如有特殊边的话那就把特殊边也加入边集进行一次 Kruskal 即可。这里要使用到并查集。

### K. [Array Stabilization](https://codeforces.com/contest/1095/problem/B)

最大差值一定是最小值和最大值产生的，所以只需要去掉最小值或最大值再求一下新的最大差值（取 $\min$ ）就可以了