import sys
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
    n, m = MII()

    g = [[] for _ in range(n + 1)]

    din = [0] * (n + 1)
    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        din[v] += 1

    hq = [i for i in range(1, n + 1) if din[i] == 0]
    
    heapify(hq)

    topo = []
    while hq:
        u = heappop(hq)
        topo.append(u)
        for v in g[u]:
            din[v] -= 1
            if din[v] == 0:
                heappush(hq, v)
    
    print(*topo)

if __name__ == "__main__":
    main()
