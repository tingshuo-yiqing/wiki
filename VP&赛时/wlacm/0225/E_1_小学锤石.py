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

    s = []
    cur = Min(a[0], a[-1])

    l, r = 0, n - 1
    if cur == a[0]:
        l += 1
        s.append('L')
    else:
        r -= 1
        s.append('R')

    while True:
        if a[l] <= cur and a[r] <= cur:
            break
        if a[l] > cur and a[r] > cur:
            if a[l] < a[r]:
                s.append('L')
                cur = a[l]
                l += 1
            else:
                s.append('R')
                cur = a[r]
                r -= 1
        elif a[l] > cur:
            s.append('L')
            cur = a[l]
            l += 1
        elif a[r] > cur:
            s.append('R')
            cur = a[r]
            r -= 1

    print(len(s))
    print(''.join(s))


if __name__ == "__main__":
    main()