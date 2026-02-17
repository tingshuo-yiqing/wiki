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
        m = II()

        g = [LII() for _ in range(2)]

        pf = [0] * (m + 1)
        for i in range(m):
            pf[i + 1] = pf[i] + g[0][i]
        
        sf = [0] * (m + 1)
        for i in range(m-1, -1, -1):
            sf[i] = sf[i + 1] + g[1][i]
        
        a = sum(g[0])
        b = sum(g[1])
        ans = inf
        for i in range(m):
            ans = Min(ans, Max(a - pf[i + 1], b - sf[i]))

        outs.append(ans)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()