import sys
sys.setrecursionlimit(200005)
from collections import deque

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
    a = LII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
    
    dfn = [-1] * (n + 1)
    low = [-1] * (n + 1)
    st = []
    inst = [False] * (n + 1)
    scc_id = [-1] * (n + 1)
    scc_size = []
    scc = 0
    timer = 0

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
            s = 0
            while True:
                cur = st.pop()
                inst[cur] = False
                scc_id[cur] = scc
                s += a[cur - 1]
                if cur == x:
                    break
            scc += 1
            scc_size.append(s)
    
    for i in range(1, n + 1):
        if dfn[i] == -1:
            tarjan(i)
    
    din = [0] * scc
    dag = [[] for _ in range(scc)]
    for u in range(1, n + 1):
        for v in g[u]:
            su = scc_id[u]
            sv = scc_id[v]
            if su != sv:
                dag[su].append(sv)
                din[sv] += 1
    
    mx = [0] * scc

    dq = deque([i for i in range(scc) if din[i] == 0])
    for i in dq:
        mx[i] = scc_size[i]
    
    while dq:
        u = dq.popleft()
        for v in dag[u]:
            mx[v] = Max(mx[v], mx[u] + scc_size[v])  #! 最长路的转移方程
            din[v] -= 1
            if din[v] == 0:
                dq.append(v)
    
    print(max(mx))

if __name__ == "__main__":
    main()
