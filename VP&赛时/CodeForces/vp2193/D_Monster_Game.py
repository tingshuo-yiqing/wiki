import sys
from collections import defaultdict
from bisect import bisect_left
input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Inf = 10**19

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        a = sorted(list(map(int, input().split())))
        b = list(map(int, input().split()))

        a.append(-1)
        sa = []
        cur = a[0]
        cnt = 0
        for i in a:
            if i == cur:
                cnt += 1
            else:
                sa.append((cur, cnt))
                cnt = 1
                cur = i

        pf = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = pf[i] + b[i]

        ans = p = 0
        j = n  
        for x, v in sa:
            p += v
            times = n - p + v

            while pf[j] > times:
                j -= 1

            ans = Max(ans, x * j)
            
        outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()