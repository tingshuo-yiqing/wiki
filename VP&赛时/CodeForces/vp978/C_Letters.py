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
    n, m = MII()
    a = LII()
    b = LII()

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]
    
    idx = 1
    i = 0
    while i < m:
        if idx < n + 1 and b[i] <= pf[idx]:
            print(idx, b[i] - pf[idx-1])
            i += 1
        else:
            idx += 1

if __name__ == "__main__":
    main()