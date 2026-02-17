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

        c = [0] * n

        s = set()
        cnt = 0
        for i in range(n):
            if a[i] not in s:
                cnt += 1
                c[i] = cnt

        pf = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = pf[i] + c[i] 

        t = sum(pf)
        
        ans = 0
        for i in range(n):
            ans += (t - (pf[i] - 1) * (n - i))

        outs.append(ans)
    
    print(*outs, sep='\n')
if __name__ == "__main__":
    main()