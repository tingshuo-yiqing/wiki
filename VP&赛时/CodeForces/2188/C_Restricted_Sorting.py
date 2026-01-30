import sys
from collections import defaultdict
from math import inf

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

        b = sorted(a)
        if a == b:
            outs.append(-1)
            continue

        mi, mx = min(a), max(a)
        c = []
        for i in range(n):
            if a[i] != b[i]:
                c.append(Max(abs(a[i] - mi), abs(a[i] - mx)))
        
        outs.append(min(c))
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()