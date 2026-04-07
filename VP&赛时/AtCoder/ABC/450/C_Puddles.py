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

dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    n, m = MII()

    g = [list(inp()) for _ in range(n)]

    def BFS(i, j):
        g[i][j] = '#'
        dq = deque([(i, j)])

        while dq:
            x, y = dq.popleft()
            for dx, dy in dirr:
                a, b = x + dx, y + dy
                if 0 <= a < n and 0 <= b < m and g[a][b] == '.':
                    g[a][b] = '#'
                    dq.append((a, b))
    
    for i in range(n):
        if g[i][0] == '.':
            BFS(i, 0)
        if g[i][m-1] == '.':
            BFS(i, m-1)
    for i in range(m):
        if g[0][i] == '.':
            BFS(0, i)
        if g[n -1][i] == '.':
            BFS(n-1, i)
    
    for o in g:
        print(*o)

    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                ans += 1
                BFS(i, j)
    print(ans)

if __name__ == "__main__":
    main()
