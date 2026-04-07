import sys
sys.setrecursionlimit(200010)

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

        g = [[] for _ in range(n + 1)]

        for _ in range(n - 1):
            u, v = MII()
            g[u].append(v)
            g[v].append(u)
        
        P = LII()

        ans = 0
        def dfs(u, fa, level):
            nonlocal ans
            path.sort()
            i = 0
            f = True
            for x in sorted(P[:level]):
                if path[i] == x:
                    i += 1
                else:
                    f = False
                    break
            if f:
                ans = Max(ans, level)

            for v in g[u]:
                if v != fa:
                    path.append(v)
                    dfs(v, u, level + 1)
                    path.pop()
        
        for x in P:
            path = [x]
            dfs(x, -1, 1)
        
        print(ans)

if __name__ == "__main__":
    main()
