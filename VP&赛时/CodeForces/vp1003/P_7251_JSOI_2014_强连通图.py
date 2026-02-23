import sys
sys.setrecursionlimit(100010)
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    
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
    scc_id = [-1] * (n + 1)
    rep = []
    scc_size = []

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
            rep.append(x)
            sz = 0
            while True:
                sz += 1
                cur = st.pop()
                inst[cur] = False
                scc_id[cur] = scc
                if cur == x:
                    break
            scc_size.append(sz)
            scc += 1
    
    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)
    
    din = [0] * scc
    dout = [0] * scc
    for u in range(1, n + 1):
        for v in g[u]:
            if scc_id[u] != scc_id[v]:
                din[scc_id[v]] += 1
                dout[scc_id[u]] += 1
    
    a = [i for i in range(scc) if din[i] == 0]
    b = [i for i in range(scc) if dout[i] == 0]
    
    print(max(scc_size))
    if scc == 1:
        print(0)
    else:
        k = Max(len(a), len(b))
        print(k)

        for i in range(k):
            u = b[i % len(b)]
            v = a[(i + 1) % len(a)]
            print(rep[u], rep[v])

if __name__ == "__main__":
    main()