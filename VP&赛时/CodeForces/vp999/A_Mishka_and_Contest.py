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

    ans = 0
    for i in range(n):
        if a[i] > k:
            break
        else:
            ans += 1
    t = ans - 1
    for i in range(n-1, -1, -1):
        if i == t or a[i] > k:
            break
        else:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()