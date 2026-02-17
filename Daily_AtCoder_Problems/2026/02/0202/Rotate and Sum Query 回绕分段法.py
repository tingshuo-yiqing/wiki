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

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]
    
    outs = []
    off = 0
    for _ in range(q):
        o = LII()
        op = o[0]
        if op == 1:
            off = (off + o[1]) % n
        else:
            l, r = o[1], o[2] # 1-based
            l = (l + off - 1) % n 
            r = (r + off - 1) % n

            if l <= r:
                outs.append(pf[r + 1] - pf[l])
            else:
                outs.append(pf[n] - pf[l] + pf[r + 1])

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()