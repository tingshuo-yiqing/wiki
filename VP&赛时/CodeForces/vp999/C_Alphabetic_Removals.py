import sys
from collections import Counter
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, k = MII()
    s = inp()

    cnt = Counter(s)

    char = sorted(list(cnt.keys()))

    for c in char:
        if k - cnt[c] > 0:
            k -= cnt[c]
            cnt[c] = 0
        else:
            cnt[c] -= k
            break
    
    ans = []
    for i in range(n-1, -1, -1):
        if cnt[s[i]]:
            cnt[s[i]] -= 1
            ans.append(s[i])
    
    print(''.join(ans)[::-1])

if __name__ == "__main__":
    main()