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
    n, k = MII()

    a = LII()

    dp = [inf] * n

    dp[0] = a[0]
    dp[1] = dp[0] + a[1]

    for i in range(2, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = Min(dp[i], dp[i-j] + a[i])
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
