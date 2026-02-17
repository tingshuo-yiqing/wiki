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
    outs = []
    for _ in range(II()):
        n = II()
        a = LII()
        mx = max(a)
        i = a.index(mx)
        if i == 0:
            outs.append(mx * (n - 1) + a[-1])
        elif i == n  - 1:
            outs.append(mx * (n - 1) + a[0])
        else:
            outs.append(mx * (n - 2) + a[0] + a[-1])
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()