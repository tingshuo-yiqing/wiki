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
    n, m, q, T = MII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = MII()
        g[u].append((v, w))
        g[v].append((u, w))
    
    Toll = [False] * (n + 1)

    t = LII()
    for x in t:
        Toll[x] = True
    
    dist = [inf] * (n + 1)
    dist[1] = T if Toll[1] else 0

    hq = [(dist[1], 1)]

    while hq:
        d, u = heappop(hq)

        if d > dist[u]:
            continue

        for v, w in g[u]:
            nd = dist[u] + w + (T if Toll[v] else 0)
            if nd < dist[v]:
                dist[v] = nd
                heappush(hq, (dist[v], v))
    
    print(dist[n])

if __name__ == "__main__":
    main()
