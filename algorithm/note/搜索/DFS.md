### 模型一  - 有向状态搜索 + 记忆化

#### 例题：

- [ABCPATH - SPOJ](https://vjudge.net/problem/SPOJ-ABCPATH#author=0) 

#### 题意：

给你一个二维字母网格图，求从字母 `A` 开始的最长连续字母路径长度，枚举方向包括水平、垂直和对角线。

#### 思路：

1. **DFS参数**：从根节点向周围扩散，取子节点返回的最大值作为当前的返回值。
2. **搜索条件**：有明显的方向，比如这里 `A -> B -> C -> D ···` ，可以不使用 `vised` 数组。可以理解为**网格图上进行拓扑排序求最长路**。
3. **关键优化**：存在重叠子问题需要**记忆化**。

#### 具体代码为：

```python
memo = [[0] * m for _ in range(n)]  # 记忆化数组，标记这个位置已经更新
def dfs(i, j):
    if memo[i][j] != 0:
        return memo[i][j]
    res = 1
    for dx, dy in dirr:
        a, b = i + dx, j + dy
        if 0 <= a < n and 0 <= b < m:
            if ord(g[a][b]) == ord(g[i][j]) + 1:  # 保持有方向的搜索
                res = Max(res, 1 + dfs(a, b))  # 对子节点的贡献取max
    memo[i][j] = res
    return res
```

#### 类似题目：

*  [Longest Path - CodeChef](https://www.codechef.com/problems/LPATH)  
   *  这道题目数据较弱不需要记忆化也可以通过。

*  [P1101 单词方阵 - 洛谷](https://www.luogu.com.cn/problem/P1101)  
   *  可以使用搜索，也可以直接枚举八个方向判断是否为直线目标。


### 模型二 - DFS暴力枚举路径

#### 例题：

* [EAGLE1 - SPOJ](http://www.spoj.com/problems/EAGLE1/) 
* [Tree Distances I - CSES](https://vjudge.net/problem/CSES-1132#author=GPT_zh) 

#### 题意：

计算每个节点到其它节点的最远距离

> 因为正在进行 DFS 的练习，所以这里先进行 $n$ 次 DFS 的暴力做法。本题是**树的直径扩展问题**，需要树形DP（两次DFS）。

#### 思路：

1. **DFS参数**：传入一个 `cur` 参数表示当前经过的边权和。

#### 具体代码为：

```python
def dfs(u, fa, cur):
    nonlocal mx
    mx = Max(mx, cur)  # 每次进入子节点都更新一下最值
    for v, w in g[u]:
        if v != fa:
            dfs(v, u, cur + w)
```

### 模型三 - 路径状态维护

#### 例题：

* [Integer-duplicated Path](https://atcoder.jp/contests/abc448/tasks/abc448_d)

#### 题意：

给定一棵树，每个节点都有值。在从节点 $1$ 到节点 $k$ 的简单路径（不经过重复节点的路径）上，如果存在两个不同的顶点有着相同的值，输出 `Yes` 否则输出 `No` 。

#### 思路：

1. **DFS状态传递**：当当前节被判断为 `Yes` 时，那从这个节点出发所到达的节点都是 `Yes` 。
2. **回溯维护路径信息**：在进入节点（先序阶段）时判断当前是否合法，离开当前节点（后序阶段）时恢复现场。

#### 具体代码为：

```python
is_same = [False] * (n + 1)
cnt = Counter()

def dfs(u, fa=-1, state=False):
    if state or cnt[a[u]] > 0:
        is_same[u] = True
        state = True
    cnt[a[u]] += 1
    for v in g[u]:
        if v != fa:
            dfs(v, u, state)
    cnt[a[u]] -= 1
```

#### 相关例题：

* [CF580C Kefa and Park - CodeForces](https://codeforces.com/contest/580/problem/C) 
  * 递归维护连续的猫的个数 `cnt` 和**叶子节点的判断方法**。




