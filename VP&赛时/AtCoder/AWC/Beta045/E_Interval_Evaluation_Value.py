import sys
from math import inf
from collections import deque

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())


def main():
    n, k, w = MII()
    a = LII()

    mi = deque()
    s = l = 0

    ans = -inf
    for r, x in enumerate(a):
        s += x
        while mi and a[mi[-1]] >= x:
            mi.pop()
        mi.append(r)
        if r - mi[0] >= k:
            mi.popleft()

        if r >= k - 1:
            ans = Max(ans, s + a[mi[0]] * w)
            s -= a[l]
            l += 1

    print(ans)

if __name__ == "__main__":
    main()
