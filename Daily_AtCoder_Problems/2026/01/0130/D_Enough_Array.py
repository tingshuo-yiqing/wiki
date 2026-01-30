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
    n, k = MII()
    a = LII()

    win = l = 0
    ans = 0
    for r, x in enumerate(a):
        win += x

        while win >= k:
            ans += (n - r)
            win -= a[l]
            l += 1
    
    print(ans)

if __name__ == "__main__":
    main()