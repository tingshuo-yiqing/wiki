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
    g = [LII() for _ in range(3)]

    res = [[1] * 3 for _ in range(3)]

    dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(3):
        for j in range(3):
            if g[i][j] & 1:
                res[i][j] = 1 - res[i][j]
                for dx, dy in dirr:
                    a, b = i + dx, j + dy
                    if 0 <= a < 3 and 0 <= b < 3:
                        res[a][b] = 1 - res[a][b]
    
    for o in res:
        for x in o:
            print(x, end='')
        print()

if __name__ == "__main__":
    main()