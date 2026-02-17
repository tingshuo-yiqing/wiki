import sys
from math import inf

if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

dir = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (0, 0),
    (-2, 0),
    (0, 2),
    (2, 0),
    (0, -2),
]


def main():
    n, m, q = MII()

    g = [LII() for _ in range(n)]

    mx = 0
    md = (0, 0)
    M = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    s += g[x][y]
            M[i][j] = s
            if s > mx:
                mx = s
                md = (i, j)

    for _ in range(q):
        a, b, z = MII()
        a -= 1
        b -= 1
        for dx, dy in dir:
            x, y = a + dx, b + dy
            if 0 <= x < n and 0 <= y < m:
                M[x][y] += z
                if M[x][y] > mx:
                    mx = M[x][y]
                    md = (x, y)
        # print("----------------------")
        # for o in M:
        #     print(*o)
        c, d = md
        print(c + 1, d + 1)


if __name__ == "__main__":
    main()
