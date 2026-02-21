import sys
from math import inf
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
    timer = 1
    scc = 0
    scc_size = []
    scc_id = [-1] * (n + 1)

    def tarjan(x):
        nonlocal timer, scc
        dfn[x] = low[x] = timer
        timer += 1

        st.append(x)
        inst[x] = True
        for y in g[x]:  # 入
            if dfn[y] == -1:
                tarjan(y)
                low[x] = Min(low[x], low[y])  # 回
            elif inst[y]:
                low[x] = Min(low[x], dfn[y])

        if dfn[x] == low[x]:   # 离
            s = 0
            while True:
                cur = st.pop()
                inst[cur] = False
                scc_id[cur] = scc
                s += 1
                if cur == x: break
            scc_size.append(s)
            scc += 1
    
    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)

    din = [0] * scc
    for u in range(1, n + 1):
        for v in g[u]:
            if scc_id[u] != scc_id[v]:
                din[scc_id[v]] += 1
    
    ans = sum(1 for i in range(scc) if din[i] == 0)

    if din[scc_id[s]] == 0:
        print(ans - 1)
    else:
        print(ans)

if __name__ == "__main__":
    main()