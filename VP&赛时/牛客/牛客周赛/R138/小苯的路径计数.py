import sys
sys.setrecursionlimit(200100)

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
    for _ in range(II()):
        n = II()
        c = [-1] + LII()

        g = [[] for _ in range(n + 1)]

        for _ in range(n - 1):
            u, v = MII()
            g[u].append(v)
        
        dp = [0] * (n + 1)
        dp[1] = 1

        ans = 0
        def dfs(u, fa=0):
            nonlocal ans
            if c[u] == c[fa]:
                dp[u] = dp[fa] + 1
            else:
                dp[u] = 1

            #! 增量
            ans += dp[u] - 1

            for v in g[u]:
                if v != fa:
                    dfs(v, u)
        
        dfs(1)

        print(ans)

if __name__ == "__main__":
    main()
