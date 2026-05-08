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
    n, V = MII()

    W = [0] * n
    C = [0] * n

    for i in range(n):
        w, c = MII()
        W[i] = w
        C[i] = c

    dp = [[0] * (V + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        cur_w = W[i - 1]
        cur_c = C[i - 1]
        for j in range(V + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= cur_c:
                if j - cur_c >= 0:
                    dp[i][j] = Max(dp[i][j], dp[i - 1][j - cur_c] + cur_w)

    print(dp[n][V])

if __name__ == "__main__":
    main()
