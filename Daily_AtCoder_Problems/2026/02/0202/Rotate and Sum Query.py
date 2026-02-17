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
    n, q = MII()
    a = LII()
    a = a + a

    pf = [0] * (2 * n + 1)
    for i in range(2 * n):
        pf[i + 1] = pf[i] + a[i]
    
    outs = []
    off = 0
    for _ in range(q):
        o = LII()
        op = o[0]
        if op == 1:
            off = (off + o[1]) % n
        else:
            l, r = o[1], o[2]
            outs.append(pf[r + off] - pf[l + off - 1])
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()