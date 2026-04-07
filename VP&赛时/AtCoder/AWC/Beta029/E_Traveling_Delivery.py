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
    n, m = MII()

    g = [[] for _ in range(n + 1)]
    # rg = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = MII()
        g[u].append((v, w))
        # rg[v].append((u, -w))


    def Dijkstra(start, g):
        dist = [inf] * (n + 1)
        dist[start] = 0

        hq = [(0, start)]

        while hq:
            d, u = heappop(hq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(hq, (dist[v], v))
        
        return dist
    
    s, k = MII()
    arr = LII()
    
    dists = Dijkstra(s, g)

    ans = 0
    for x in arr:
        if dists[x] != inf:
            ans += dists[x]
        else:
            print(-1, "这是s到达不了k的-1")
            return

    mi = inf    # 找到一条最小的，可以返回的距离
    for x in arr:
        dist = Dijkstra(x, g)
        mi = Min(mi, dist[s])
    
    print(ans if mi == inf else ans + mi)

if __name__ == "__main__":
    main()
