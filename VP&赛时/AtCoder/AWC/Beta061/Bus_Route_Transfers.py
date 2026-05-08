import sys
from math import inf
from heapq import heappop, heappush
from collections import deque

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
    N, M, s, e = MII()

    g = [[] for _ in range(N + M + 1)]

    for i in range(1, M + 1):  #! 索引
        K, *A = MII()
        for x in A:
            g[N + i].append((x, 0))
            g[x].append((N + i, 1))

    dist = [inf] * (N + M + 1)
    dist[s] = 0

    # dq = deque([s])
    hq = [(dist[s], s)]

    # while dq:
    while hq:
        # u = dq.popleft()
        d, u = heappop(hq)
        if d > dist[u]:
            continue  
        for v, w in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                # if w == 0:
                #     dq.appendleft(v)  #! 入队的是节点而不是0和1
                # else:
                #     dq.append(v)
                heappush(hq, (dist[v], v))

    print(-1 if dist[e] == inf else dist[e])

if __name__ == "__main__":
    main()
