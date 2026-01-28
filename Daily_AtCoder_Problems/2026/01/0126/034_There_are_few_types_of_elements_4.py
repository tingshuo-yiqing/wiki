import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = defaultdict(int)

    ans = 0
    win = l = 0
    for r, x in enumerate(a):
        cnt[x] += 1
        if cnt[x] == 1:
            win += 1
        
        while win > k:
            dv = a[l]
            l += 1
            cnt[dv] -= 1
            if cnt[dv] == 0:
                win -= 1
        
        ans = max(ans, r - l + 1)

    print(ans) 

if __name__ == "__main__":
    main()