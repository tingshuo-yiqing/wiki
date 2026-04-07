import sys
from collections import deque
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

    for _ in range(m):
        u, v, w = MII()
        if w >= k:
            g[u].append(v)
            g[v].append(u)

    
    dist = [-1] * (n + 1)
    dist[1] = 0

    dq = deque([1])

    while dq:
        u = dq.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    
    print(dist[n])

if __name__ == "__main__":
    main()
