import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    coins = LII()

    dp = [inf] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = Min(dp[i], dp[i - c] + 1)

    print(dp[n])

if __name__ == "__main__":
    main()