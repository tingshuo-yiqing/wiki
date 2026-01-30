import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n = II()
    a = LII()

    pos = [-1] * (n + 1)
    for i in range(n):
        pos[a[i]] = i

    std = list(range(1, n + 1))

    outs = []
    for i, x in enumerate(a):
        if x != std[i]:
            lv, rv = x, std[i]
            plv, prv = pos[lv], pos[rv]
            outs.append((plv + 1, prv + 1))
            a[plv], a[prv] = a[prv], a[plv]
            pos[lv] = prv

    print(len(outs))
    for u, v in outs:
        print(u, v)

if __name__ == "__main__":
    main()