import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n, m = map(int, input().split())

    g = [False] * (n + 1)
    for _ in range(m):
        g[int(input())] = True

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if g[i]:
            continue
        if not g[i - 1]:
            dp[i] += dp[i - 1]
        if i > 1 and not g[i - 2]:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    
    print(dp[n])

if __name__ == "__main__":
    main()