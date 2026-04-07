import sys
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
    n, d, s, t = MII()

    a = [LII() for _ in range(n)]

    g = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = a[i][0], a[i][1] 
            x2, y2 = a[j][0], a[j][1] 
            if (x1 - x2)**2 + (y1 - y2)**2 <= d * d:
                g[i].append(j)
                g[j].append(i)
    
    distt = [-1] * n
    distt[s-1] = 0

    dq = deque([s-1])

    while dq:
        u = dq.popleft()

        if distt[t-1] != -1:
            print(distt[t-1])
            return

        for v in g[u]:
            if distt[v] == -1:
                distt[v] = distt[u] + 1
                dq.append(v)
    
    print(-1)

if __name__ == "__main__":
    main()
