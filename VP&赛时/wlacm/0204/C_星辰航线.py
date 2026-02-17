import sys
from heapq import heappop, heappush
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m, k = MII()

    edges = []
    for _ in range(m):
        u, v, w = MII()
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    gg = edges[:k]

    # 离散化
    e = set()
    for u, v, w in gg:
        e.add(u)
        e.add(v)
    e = sorted(list(e))
    m = len(e)
    idx = {x: i for i, x in enumerate(e)}

    g = [[] for _ in range(m)]
    for u, v, w in gg:
        u, v = idx[u], idx[v]
        g[u].append((v, w))
        g[v].append((u, w))
    
    ans = []
    for start in range(m):
        dist = [inf] * m
        dist[start] = 0

        pq = [(0, start)]
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v)) 
        
        # 只选一半的
        for v in range(start + 1, m):
            if dist[v] != inf:
                ans.append(dist[v])
    ans.sort()
    print(ans[k-1])

if __name__ == "__main__":
    main()