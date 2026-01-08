import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n = int(input())

    cnt = defaultdict(int)

    for x in range(1, n + 1):
        t = x
        for i in range(2, int(t ** 0.5) + 1):
            while t % i == 0:
                cnt[i] += 1
                t //= i
        if t != 1:
            cnt[t] += 1
    
    ans = 1
    for x in cnt.values():
        ans = (ans * (x + 1)) % MOD

    print(ans)

if __name__ == "__main__":
    main()