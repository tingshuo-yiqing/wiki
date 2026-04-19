import sys
from math import inf
from heapq import heappop, heappush

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n, m, k = MII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u,v , w = MII()
        g[u].append((v, w))
        g[v].append((u, w))

    Toll = [0] * (n + 1)
    for _ in range(k):
        x, y = MII()
        Toll[x] = y
    
    dist = [inf] * (n + 1)
    dist[1] = Toll[1]  #! 1处也可能有点权

    hq = [(dist[1], 1)]

    while hq:
        d, u = heappop(hq)

        if d > dist[u]:
            continue

        for v, w in g[u]:
            nd = dist[u] + w + Toll[v]  #! 边权有变化，要加上可能的点权
            if nd < dist[v]:
                dist[v] = nd
                heappush(hq, (dist[v], v))

    print(dist[n])


if __name__ == "__main__":
    main()
