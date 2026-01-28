import sys
from collections import defaultdict, Counter
input = lambda: sys.stdin.readline().strip()

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, input().split())))

        cnt = Counter(a)
        a = sorted(list(cnt.keys()))
        dd = []
        for i in range(len(a)-1):
            d = a[i+1] - a[i]
            dd.append(d)
        
        ans = cnt = 0
        nn = len(dd)

        for l in range(nn):
            if dd[l] == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0     
        ans = max(ans, cnt)
        outs.append(max(ans+1, 1))

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()