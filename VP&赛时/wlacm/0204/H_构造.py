import sys
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

    g = [list(inp()) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j] == '-':
                continue
            g[i][j] = 'B' if (i + j) & 1 else 'W'
    
    for o in g:
        print(''.join(o))

if __name__ == "__main__":
    main()