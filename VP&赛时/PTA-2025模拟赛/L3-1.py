import sys
from math import inf
from heapq import heappop, heappush, heapify

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
    n, m ,s, t = MII()

    weight = LII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = MII()
        g[u].append((v, w))
        g[v].append((u, w))
    
    dist = [inf] * (n + 1)
    dist[s] = 0

    hq = []
    heappush(hq, (0, s))

    mx = [-inf] * (n + 1)
    mx[s] = 0
    while hq:
        d, u = heappop(hq)

        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                mx[v] = Max(mx[v], weight[u])
                heappush(hq, (dist[v], v))
            elif dist[v] == dist[u] + w:
                if mx[v] <
    
    if dist[t] == inf:
        print("Impossible")
    else:
        print(dist[t])

if __name__ == "__main__":
    main()
