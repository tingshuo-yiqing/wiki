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

    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print('/', end='')
            else:
                print('\\', end='')
        print()

if __name__ == "__main__":
    main()