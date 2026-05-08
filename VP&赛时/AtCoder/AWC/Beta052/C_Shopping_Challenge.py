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
    n, S = MII()

    w = []
    c = []
    for _ in range(n):
        a, b = MII()
        w.append(a)
        c.append(b)

    dp = [-1] * (S + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(S, c[i]-1, -1):
            if dp[j - c[i]] >= 0:
                dp[j] = Max(dp[j], dp[j - c[i]] + w[i])

    print(dp[S])

if __name__ == "__main__":
    main()
