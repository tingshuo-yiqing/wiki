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
    n = II()
    a = LII()

    l, r = 0, n - 1

    ans = 0
    sl = a[l]
    sr = a[r]
    while l < r:
        if sl < sr:
            l += 1
            sl += a[l]
        elif sl > sr:
            r -= 1
            sr += a[r]
        else:
            ans = sl
            l += 1
            sl += a[l]
            r -= 1
            sr += a[r]

    print(ans)

if __name__ == "__main__":
    main()