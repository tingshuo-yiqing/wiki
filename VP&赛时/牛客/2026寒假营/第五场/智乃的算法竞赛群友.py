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
    outs = []
    for _ in range(II()):
        n, x, y = MII()
        if n <= 1:
            outs.append(0)
            continue

        ans = n // 2 * y

        ans2 = n // 8 * (x + y)
        nn = n - n // 8 * 8
        ans2 = ans2 + nn // 2 * y

        ans1 = n // 7 * x
        n -= n // 7 * 7
        ans1 = ans1 + n // 2 * y

        outs.append(max(ans, ans1, ans2))

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()