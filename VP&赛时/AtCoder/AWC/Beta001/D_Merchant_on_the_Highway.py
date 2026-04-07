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
    n, V, k = MII()

    a = [LII() for _ in range(n)]

    mx = -1
    for t in range(n-k):  # 进行窗口大小为k+1的完全背包
        dp = [0] * (V + 1)
        for i in range(t, t+k+1):
            for j in range(a[i][1], V+1):
                dp[j] = Max(dp[j], dp[j-a[i][1]] + a[i][0])

        mx = Max(mx, dp[V])
    
    print(mx)

if __name__ == "__main__":
    main()
