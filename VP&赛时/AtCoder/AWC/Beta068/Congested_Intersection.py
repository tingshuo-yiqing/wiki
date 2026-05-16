import sys
from heapq import heappop, heappush
from math import inf

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

    deg = [0] * (n + 1)
    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    dist = [inf] * (n + 1)
    dist[1] = 0

    hq = [(0, 1)]

    while hq:
        d, u = heappop(hq)

        if d > dist[u]:
            continue
        
        for v in g[u]:
            w = 1 + (v != n and deg[v] >= k)  #! 终点不计拥堵费
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(hq, (dist[v], v))
        
    print(-1 if dist[n] == inf else dist[n])

if __name__ == "__main__":
    main()
