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
    n, m, init = MII()

    a = LII()
    b = LII()

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]
    
    if init > pf[1]:
        print("YES")
        return

    l, r = 0, init
    idx = 1
    for i in range(m):
        l += b[i]
        r += b[i]

        while idx < n + 1 and l >= pf[idx]:
            idx += 1 

        if idx < n + 1 and l < pf[idx] < r:
            print("YES")
            return
        
    print("NO")

if __name__ == "__main__":
    main()