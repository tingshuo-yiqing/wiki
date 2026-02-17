import sys
sys.setrecursionlimit(3000)
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
    b = LII()

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = Max(Max(0, 0 - a[0]), 0 ^ b[0])
    
    for i in range(1, n):
        dp[i]

    print(dp[n-1])
if __name__ == "__main__":
    main()