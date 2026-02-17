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
    n, Y = MII()
    a, b, c = 10000, 5000, 1000

    x, y, z = -1, -1, -1
    for i in range(n + 1):
        if i * a > Y:
            break
        for j in range(n + 1):
            val = i * a + j * b
            if val > Y:
                break
            rem = Y - val
            if rem >= 0 and rem % c == 0:
                if rem // c == n - (i + j):
                    x, y, z = i, j, rem // c
                    print(x, y, z)
                    sys.exit(0)

    print(x, y, z)

if __name__ == "__main__":
    main()