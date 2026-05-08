"""
题意: 给定N个节点的树，对每个节点u，求满足"u到v的路径经过w"且"v<w"的点对(v,w)的个数f(u)。
思路: 推导得 f(u) = N(N-1)/2 - Σ_{w≠u} less_dir(u,w)，其中less_dir(u,w)是w到u方向子树中编号<w的节点数。
通过按编号从小到大激活节点+BIT统计每个方向子树信息，再用差分数组做树上区间加减得到答案。
"""
import sys

sys.setrecursionlimit(1 << 20)

def solve() -> None:
    input = sys.stdin.readline
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    # 第一次DFS: 求parent, in/out, 子节点列表
    parent = [-1] * N
    order = [0] * N  # Euler Tour 节点序列
    in_t = [0] * N
    out_t = [0] * N
    children = [[] for _ in range(N)]

    stack = [(0, -1, 0)]  # (node, parent, state)
    timer = 0
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            in_t[u] = timer
            order[timer] = u
            timer += 1
            stack.append((u, p, 1))
            for v in g[u]:
                if v == p:
                    continue
                parent[v] = u
                children[u].append(v)
                stack.append((v, u, 0))
        else:
            out_t[u] = timer - 1

    # ---------- BIT 1: 用于查询子树中已激活节点数 ----------
    class BIT:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)
        def add(self, idx, val):
            i = idx + 1
            n = self.n
            while i <= n:
                self.bit[i] += val
                i += i & -i
        def sum(self, idx):
            """前缀和 [0, idx]"""
            if idx < 0:
                return 0
            i = min(idx + 1, self.n)
            s = 0
            while i > 0:
                s += self.bit[i]
                i -= i & -i
            return s
        def range_sum(self, l, r):
            if l > r:
                return 0
            return self.sum(r) - self.sum(l - 1)

    bit1 = BIT(N)

    # less_sub[u]: u的子树中编号<u的节点数
    less_sub = [0] * N

    # 对每个节点u，存其子节点v对应的 less_child = v的子树中编号<u的节点数
    # 用列表存 (子节点v, less_child_value)
    child_less = [[] for _ in range(N)]

    # 按编号从小到大处理节点 (0-based，即实际编号+1)
    # 激活前查询
    for u in range(N):
        # 对每个子节点v，查询v子树中的已激活节点数 = 编号<u且在v子树中的节点数
        for v in children[u]:
            cnt = bit1.range_sum(in_t[v], out_t[v])
            child_less[u].append((v, cnt))
        # 查询u子树中的已激活节点数
        less_sub[u] = bit1.range_sum(in_t[u], out_t[u])
        # 激活节点u
        bit1.add(in_t[u], 1)

    total = N * (N - 1) // 2

    # ---------- BIT 2: 差分数组用于区间加减 ----------
    bit2 = BIT(N)

    # 对每个节点u，处理其所有方向（子节点方向+父节点方向）
    for u in range(N):
        # 每个子节点方向: 对该子树中所有节点减去 less_child
        for v, less_val in child_less[u]:
            if less_val > 0:
                l = in_t[v]
                r = out_t[v]
                # 区间[l, r]减去less_val
                bit2.add(l, -less_val)
                bit2.add(r + 1, less_val)
        # 父节点方向: 对"不在u子树中的节点"减去 less_parent
        less_parent = u - less_sub[u]  # 编号<u且在u子树外的节点数 = (编号<u的总数) - (在子树中的)
        if less_parent > 0:
            l = in_t[u]
            r = out_t[u]
            # 整体减去less_parent
            bit2.add(0, -less_parent)
            # 子树内加回来 (即子树内的不减去)
            bit2.add(l, less_parent)
            bit2.add(r + 1, -less_parent)

    ans = [0] * N
    for i in range(N):
        diff = bit2.sum(i)
        u = order[i]
        ans[u] = total + diff

    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()