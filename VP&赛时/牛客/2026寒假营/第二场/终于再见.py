import sys
from math import inf
from collections import deque
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()

    deg = [0] * (n + 1)

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    mp = [[] for _ in range(n + 1)]  # [等级: 节点]
    for i in range(1, n + 1):
        d = deg[i]
        mp[d].append(i)

    res = [-1] * (n + 1)
    dist = [inf] * (n + 1)

    for i in range(n, 0, -1):

        for j in mp[i]: # 更新当前层级的节点
            res[j] = dist[j] if dist[j] != inf else -1
            dist[j] = 0  # 多源起点设为 0 

        dq = deque(mp[i])

        while dq:
            u = dq.popleft()
            for v in g[u]:
                if dist[u] + 1 < dist[v]:  # 松弛操作
                    # 有了松弛操作后相当于有了vised数组
                    dist[v] = dist[u] + 1
                    dq.append(v)

    print(*res[1:])
if __name__ == "__main__":
    main()