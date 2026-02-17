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
        n, k = MII()
        a = LII()
        ans = k + a[0]
        a.append(k)
        a = a[::-1]

        for i in range(n):
            ans = Max(ans, a[i] + a[i + 1])
        
        outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()