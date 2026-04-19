import sys
from math import inf
from heapq import heapify, heappop, heappush

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

    edges = [LII() for _ in range(m)]

    C = LII()
    for i in range(k):
        edges[C[i]-1][2] *= 2 
    
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    dist = [inf] * (n + 1)
    dist[1] = 0

    hq = [(0, 1)]
    while hq:
        d, u = heappop(hq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(hq, (dist[v], v))

    print(dist[n] if dist[n] != inf else -1)

if __name__ == "__main__":
    main()
