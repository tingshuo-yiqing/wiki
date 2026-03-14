import sys
from math import inf
from heapq import heappop, heapify, heappush

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
        u, v, t = MII()
        g[u].append((v, t))
        g[v].append((u, t))
    
    p = [1] + LII() + [n]

    def Dijkstra(start, nxt):
        dist = [inf] * (n + 1)
        dist[start] = 0

        hq = [(0, start)]

        while hq:
            d, u = heappop(hq)
            if u == nxt:
                return d
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(hq, (dist[v], v))
        
        return dist[nxt] if dist[nxt] != inf else -1
    
    ans = 0
    for i in range(len(p) - 1):
        d = Dijkstra(p[i], p[i + 1])
        if d == -1:
            print(-1)
            return
        ans += d

    print(ans)

if __name__ == "__main__":
    main()
