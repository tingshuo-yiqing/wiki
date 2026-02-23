import sys
sys.setrecursionlimit(10000)
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m, s = MII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
    
    dfn = [-1] * (n + 1)
    low = [-1] * (n + 1)
    st = []
    inst = [False] * (n + 1)
    scc_id = [-1] * (n + 1)
    scc = 0
    timer = 1

    def tarjan(x):
        nonlocal timer, scc
        dfn[x] = low[x] = timer
        timer += 1
        st.append(x)
        inst[x] = True

        for y in g[x]:
            if dfn[y] == -1:
                tarjan(y)
                low[x] = Min(low[x], low[y])
            elif inst[y]:
                low[x] = Min(low[x], dfn[y])
        
        if dfn[x] == low[x]:
            while True:
                cur = st.pop()
                inst[cur] = False
                scc_id[cur] = scc
                if cur == x:
                    break
            scc += 1

    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)
    
    din = [0] * scc
    for u in range(1, n + 1):
        for v in g[u]:
            if scc_id[u] != scc_id[v]:
                din[scc_id[v]] += 1
    
    cnt = sum(1 for i in range(scc) if din[i] == 0)

    print(cnt - 1 if din[scc_id[s]] == 0 else cnt)

if __name__ == "__main__":
    main()