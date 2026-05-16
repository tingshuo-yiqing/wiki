import sys
from math import inf

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
    n, V = MII()

    W = [0] * n
    C = [0] * n

    for i in range(n):
        u, v = MII()
        W[i] = u
        C[i] = v
    
    dp = [[-inf] * (V + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        w = W[i - 1]
        c = C[i - 1]
        for j in range(V, -1, -1):
            if j >= c:
                dp[i][j] = Max(dp[i - 1][j], dp[i - 1][j - c] + w)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][V] if dp[n][V] != -inf else -1)

if __name__ == "__main__":
    main()
