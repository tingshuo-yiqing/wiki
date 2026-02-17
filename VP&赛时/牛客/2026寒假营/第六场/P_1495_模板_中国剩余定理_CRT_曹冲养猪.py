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
    n = II()

    M = 1
    rem = []
    mod = []
    for _ in range(n):
        m, r = MII()
        rem.append(r)
        mod.append(m)
        M *= m
    
    x = 0
    for i in range(n):
        c = M // mod[i]
        x += rem[i] * c * pow(c, -1, mod[i])
    
    print(x % M)

if __name__ == "__main__":
    main()