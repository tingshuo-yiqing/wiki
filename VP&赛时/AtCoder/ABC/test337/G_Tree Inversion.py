# ABC337G - Tree Inversion
# 题意：给定一棵 N 个顶点的树。对于每个顶点 u，定义 f(u) 为满足 v < w 且
#       w 在 u 到 v 的路径上的顶点对 (v, w) 的数量。求所有 f(u)。
# 思路：先以 1 为根，用 BIT 在 DFS 过程中统计每个节点子树内值小于它的节点数
#       (sub_less[w])。f(1) = Σ sub_less[w]。
#       然后用换根 DP 递推：对于从 parent p 转移到 child v，
#       f(v) = f(p) + (v - 1) - 2 * sub_less[v]。
#       含义：换根后，v 子树外的、值小于 v 的节点变为"w=v 在路径上"的新贡献，
#       而 v 子树内值小于 v 的节点不再以 v 为路径上的 w（变成在子树内）。

import sys
sys.setrecursionlimit(1 << 30)

class BIT:
    """Fenwick Tree"""
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

def solve():
    N = int(sys.stdin.readline())
    g = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        g[u].append(v)
        g[v].append(u)

    bit = BIT(N)
    ans = [0] * (N + 1)
    sub_less = [0] * (N + 1)  # sub_less[u] = u 子树中值小于 u 的节点数

    # 第一遍 DFS：以 1 为根，计算 sub_less 和 ans[1]
    def dfs1(u, p):
        # 进入子树前，BIT 中小于 u 的数量
        before = bit.sum(u - 1)
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
        # 离开子树后，BIT 中小于 u 的数量
        after = bit.sum(u - 1)
        sub_less[u] = after - before
        ans[1] += sub_less[u]
        bit.add(u, 1)  # 将 u 加入 BIT

    dfs1(1, 0)

    # 第二遍 DFS：换根 DP 递推所有节点的答案
    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            # 从 u 换根到 v 的公式
            ans[v] = ans[u] + (v - 1) - 2 * sub_less[v]
            dfs2(v, u)

    dfs2(1, 0)

    sys.stdout.write(" ".join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()