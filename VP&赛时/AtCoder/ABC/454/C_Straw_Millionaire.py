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
    n, m = MII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
    
    vised = [0] * (n + 1)

    def dfs(u):
        vised[u] = 1

        for v in g[u]:
            if not vised[v]:
                dfs(v)
    
    dfs(1)

    print(sum(vised))

if __name__ == "__main__":
    main()
