import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

MOD = 998244353

def factors(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= MOD
    return res

MAXN = 200005

fact = [1] * MAXN
for i in range(2, MAXN):
    fact[i] = fact[i - 1] * i % MOD

def main():
    outs = []
    for _ in range(II()):
        n = II()

        a = LII()
        b = LII()

        mbi = min(b)

        t = 0
        for x in a:
            if x > mbi:
                t += 1
        outs.append(fact[t] * fact[n - t] % MOD)
        # outs.append(factors(t) * factors(n - t) % MOD)
                
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()