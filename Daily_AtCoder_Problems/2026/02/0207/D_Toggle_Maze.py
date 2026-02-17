import sys
from collections import deque
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()

    g = [inp() for _ in range(n)]

    si = sj = gi = gj = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                si, sj = i, j
            if g[i][j] == 'G':
                gi, gj = i, j

    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    dist[si][sj][0] = 0

    dq = deque([(si, sj, 0)])
    while dq:
        x, y, s = dq.popleft()
        if x == gi and y == gj:
            print(dist[x][y][s])
            sys.exit(0)
        for dx, dy in dir:  
            a, b = x + dx, y + dy
            if 0 <= a < n and 0 <= b < m and g[a][b] != '#':
                c = g[a][b]
                if c == 'o' and s == 1:
                    continue
                if c == 'x' and s == 0:
                    continue
                ns = 1 - s if c == '?' else s
                if dist[a][b][ns] == -1:
                    dist[a][b][ns] = dist[x][y][s] + 1
                    dq.append((a, b, ns))             
    print(-1)

if __name__ == "__main__":
    main()