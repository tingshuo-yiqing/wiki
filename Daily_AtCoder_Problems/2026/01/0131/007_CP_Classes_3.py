import sys
from bisect import bisect_left
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
    A = sorted(LII())

    q = II()
    B = [II() for _ in range(q)]

    outs = []
    for x in B:
        i = bisect_left(A, x)

        ans = abs(x - A[0])
        if i == n:
            ans = abs(x - A[-1])
        elif 0 < i < n:
            l, r = A[i - 1], A[i]
            now = l if abs(l - x) <= abs(r - x) else r
            ans = abs(x - now)
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()