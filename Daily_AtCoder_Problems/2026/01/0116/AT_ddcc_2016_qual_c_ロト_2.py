import sys
from math import gcd
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = defaultdict(int)
    for x in a:
        cnt[gcd(x, k)] += 1
    
    b = list(cnt.keys())
    # print(b)
    ans = 0
    for i in range(len(b)):
        g1 = b[i]
        for j in range(i, len(b)):
            g2 = b[j]
            if g1 * g2 % k == 0:
                if i < j:
                    ans += cnt[b[i]] * cnt[b[j]]
                else:
                    ans += cnt[g1] * (cnt[g1] - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()