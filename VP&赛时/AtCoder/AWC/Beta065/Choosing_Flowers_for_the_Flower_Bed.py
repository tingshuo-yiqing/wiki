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
    a = LII()

    dp = [0] * (n + 1)
    dp[1] = a[0] 
    
    for i in range(2, n + 1):
        dp[i] = Max(dp[i-1], dp[i - 2] + a[i-1])
    
    print(dp[n])

if __name__ == "__main__":
    main()
