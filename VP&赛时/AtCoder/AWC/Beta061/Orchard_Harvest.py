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

    dp = [0] * n
    dp[0] = a[0]

    for i in range(1, n):
        pre = i - k - 1
        if pre < 0:
            pre = 0
        else:
            pre = dp[pre]
        dp[i] = Max(dp[i - 1], pre + a[i])
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
