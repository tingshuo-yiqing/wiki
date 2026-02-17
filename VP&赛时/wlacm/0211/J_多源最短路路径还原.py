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

    ans = []
    l = 0
    while l < n:
        if a[l] == 1:
            r = l + 1
            idx = 2
            while r < n and a[r] == idx:
                r += 1
                idx += 1
            ans.append(r - l)
            l = r
            
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()