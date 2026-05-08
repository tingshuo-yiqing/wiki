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
    n, m = MII()

    u = LII()
    v = LII()

    g = [[] for _ in range(n + 1)]

    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])

    color = [0] * (n + 1)
    def bfs(u):
        dq = deque([u])
        color[u] = 1
        while dq:
            x = dq.popleft()
            c = color[x]
            for y in g[x]:
                if color[y] == 0:
                    color[y] = 3 - c
                    dq.append(y)
                elif color[y] == c:
                    return True
        return False
    
    for i in range(1, n + 1):
        if not color[i]:
            if bfs(i):
                print("No")
                return
    print("Yes")

if __name__ == "__main__":
    main()
