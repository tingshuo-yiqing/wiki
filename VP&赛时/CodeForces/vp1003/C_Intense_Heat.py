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

    ans = -1.0
    for i in range(n - k + 1):
        s = sum(a[i:i+k])
        ans = Max(ans, s / k)
        for j in range(i + k, n):
            s += a[j]
            ans = Max(ans, s / (j - i + 1))
    
    print(f'{ans:.16}')

if __name__ == "__main__":
    main()