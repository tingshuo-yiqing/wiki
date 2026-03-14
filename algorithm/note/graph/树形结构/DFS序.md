[CF1006E - CodeForces](https://codeforces.com/contest/1006/problem/E) 

**题意**：给定一颗有根树，根节点没有上级，其它节点是其子树的上级。要求在有顺序的 DFS 遍历下，进行 $q$ 个 $(u_i,k_i)$ 查询。意思为第 $u_i$ 个节点的 $k_i$ 的下属是什么。

<div align="center">
    <img src="https://img2024.cnblogs.com/blog/3769106/202603/3769106-20260302102923649-2038376110.png" style="width: 80%; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <div style="color: #999; padding: 10px; font-size: 14px;">这里的接收顺序是DFS序</div>
</div>

是 DFS 序的裸题。不过数据量比较大可能需要使用 Python3 进行提交，不然可能会 MLE 或 RE。

如果一定要使用 Pypy3 的话，请使用栈模拟的递归。



综上，这道题就可以当作模版题练习

```python
def main():
    n, q = MII()
    pa = LII()  #! 给出的节点是有序的

    g = [[] for _ in range(n + 1)]

    for v, u in enumerate(pa, start=2):
        g[u].append(v)

    sz = [0] * (n + 1)
    tin = [0] * (n + 1)
    seq = []

    def dfs(u):
        tin[u] = len(seq)
        seq.append(u)

        sz[u] = 1
        for v in g[u]:  #! 这里子节点已经是有序的了
            dfs(v)
            sz[u] += sz[v]
    dfs(1)

    outs = []
    for _ in range(q):
        u, k = MII()

        if k > sz[u]:
            outs.append('-1')
        else:
            outs.append(str(seq[tin[u] + k - 1]))

    print(*outs, sep='\n')
```

