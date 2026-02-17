import sys
from collections import defaultdict
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y


MOD = 10 ** 9 + 7

def decompos(n):
    cnt = defaultdict(int)
    t = n
    for i in range(2, int(n ** 0.5) + 1):
        while t % i == 0:
            cnt[i] += 1
            t //= i
    if t != 1:
        cnt[t] += 1

    res = 1
    for k, v in cnt.items():
        temp = (pow(k, v+1) - 1) // (k - 1)
        res *= temp
    return res % MOD

def main():
    n = II()
    print(decompos(n))

if __name__ == "__main__":
    main()