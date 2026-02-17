import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def factors(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
# 也可以预处理阶乘表

MAXN = 200005
MOD = 998244353

fact = [1] * MAXN
for i in range(2, MAXN + 1):
    fact[i] = fact[i] * (i - 1) % MOD

def main():
    for _ in range(II()):
        n = II()

        if factors(n) != n * (n + 1) // 2:
            print("NO")
            continue
        print("YES")
        print(*list(range(1, n +1)))

if __name__ == "__main__":
    main()