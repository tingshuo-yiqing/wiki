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

    g = [list(inp()) for i in range(n)]

    dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    d = deque()

    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                d.append((i, j))
                g[i][j] = 'B'
                while d:
                    cur_i, cur_j = d.popleft()
                    for dx, dy in dir:
                        x, y = cur_i + dx, cur_j + dy 
                        if 0 <= x < n and 0 <= y < m and g[x][y] == '.':
                            g[x][y] = 'B' if g[cur_i][cur_j] == 'W' else 'W'
                            d.append((x, y))
            
    for o in g:
        print(''.join(o))

if __name__ == "__main__":
    main()