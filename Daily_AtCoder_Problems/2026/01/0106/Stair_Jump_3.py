import sys
from functools import lru_cache
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n, l = map(int, input().split())

    # @lru_cache(maxsize=None)
    # def dfs(n):
    #     if n <= 0:
    #         return 1
    #     if 0 < n < l:
    #         return 1
    #     return (dfs(n - 1) + dfs(n - l)) % MOD
    # print(dfs(n))

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= l:
            dp[i] = (dp[i] + dp[i - l]) % MOD

    print(dp[n])    

if __name__ == "__main__":
    main()