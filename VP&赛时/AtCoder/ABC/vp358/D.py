import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    a = sorted(LII())
    b = sorted(LII())

    i = j = 0
    ans = 0
    while i < n:
        if j < m and a[i] >= b[j]:
            ans += a[i]
            j += 1
            i += 1
        else:
            i += 1
    
    print(ans if j == m else -1)

if __name__ == "__main__":
    main()