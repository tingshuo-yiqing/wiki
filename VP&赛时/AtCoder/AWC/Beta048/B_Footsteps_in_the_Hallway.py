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
    n = II()
    H = LII()
    D = LII()

    def check(i):
        return H[i] != 0 and D[i] != 0 

    dp = [0] * n
    dp[0] = check(0)
    dp[1] = dp[0] + check(1)

    for i in range(2, n):
        dp[i] = Min(dp[i-1], dp[i-2]) + check(i)
    
    print(dp[n - 1])

if __name__ == "__main__":
    main()
