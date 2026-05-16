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
    s = '.' + inp()

    MOD = 10 ** 9 + 7

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, 4):
            if i - j >= 0:
                if s[i - j] == '#':
                    continue
                dp[i] += dp[i - j]
                dp[i] %= MOD
    
    print(dp[n] % MOD)

if __name__ == "__main__":
    main()
