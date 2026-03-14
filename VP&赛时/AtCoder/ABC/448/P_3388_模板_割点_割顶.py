import sys
sys.setrecursionlimit(20005)

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
        g[v].append(u)
    
    dfn = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0

    is_cut = [False] * (n + 1)

    def tarjan(x, fa=-1):
        nonlocal timer
        dfn[x] = low[x] = timer
        timer += 1
        child = 0
        for y in g[x]:
            if y == fa:
                continue
            if dfn[y] == -1:
                child += 1
                tarjan(y, x)
                low[x] = Min(low[x], low[y])
                if low[y] >= dfn[x]:
                    if fa != -1 or child > 1:
                        is_cut[x] = True
            else:
                low[x] = Min(low[x], dfn[y])

    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)

    cuts = [i for i in range(1, n + 1) if is_cut[i]]
    print(len(cuts))
    print(*cuts)

if __name__ == "__main__":
    main()
