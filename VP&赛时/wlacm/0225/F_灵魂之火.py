import sys
from collections import defaultdict
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
    a = LII()

    ans = {i+1: 0 for i in range(n)}

    for i in range(n):
        mx = a[i]
        ans[mx] += 1
        cnt = defaultdict(int)
        cnt[mx] += 1
        for j in range(i + 1, n):
            cnt[a[j]] += 1
            if cnt[a[j]] > cnt[mx]:
                mx = a[j]
            if cnt[a[j]] == cnt[mx] and a[j] < mx:
                mx = a[j]
            ans[mx] += 1
    
    print(*ans.values())

if __name__ == "__main__":
    main()