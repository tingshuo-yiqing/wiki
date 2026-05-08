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
        u, v, w = MII()
        g[u].append((v, w))
        g[v].append((u, w))

    def Dijkstra(start, end):
        dist = [inf] * (n + 1)
        dist[start] = 0

        hq = [(0, start)]

        while hq:
            d, u = heappop(hq)
            if d > dist[u]:
                continue
            if u == end:
                return dist[u]
            for v, w in g[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(hq, (dist[v], v))
    
        return -1
    
    d1 = Dijkstra(1, k)
    d2 = Dijkstra(k, n)
    if d1 == -1 or d2 == -1:
        print(-1)
    else:
        print(d1 + d2)    

if __name__ == "__main__":
    main()
