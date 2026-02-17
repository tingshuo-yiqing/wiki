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
    n, q, s = MII()
    a = LII()

    pf = [s] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + (a[i])
    # print(pf)

    outs = []
    for _ in range(q):
        x, y = MII()
        outs.append(pf[x-1] + y - 1)
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()