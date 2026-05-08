import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n, k = MII()
    a = LII()

    LOG = 40

    dp = [[0] * n for _ in range(LOG)]

    for i in range(n):
        dp[0][i] = a[i]
    
    for j in range(1, LOG):
        for i in range(n):
            dp[j][i] = dp[j-1][i] + dp[j-1][(i + dp[j-1][i]) % n]

    total = 0
    for j in range(LOG):
        if (k >> j) & 1:
            total += dp[j][total % n]
    
    print(total)

if __name__ == "__main__":
    main()
