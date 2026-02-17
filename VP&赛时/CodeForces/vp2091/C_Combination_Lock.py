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
    for _ in range(II()):
        n = II()

        if n % 2 == 0:
            print(-1)
        else:
            a = []
            for i in range(1, n // 2 + 2):
                a.append(2 * i - 1)
            for i in range(1, n // 2 + 1):
                a.append(2 * i)
            print(*a)

if __name__ == "__main__":
    main()