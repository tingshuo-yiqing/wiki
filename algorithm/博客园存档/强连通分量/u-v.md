[从u到v还是从v到u？ - AcWing](https://www.acwing.com/problem/content/description/403/) 貌似数据较弱？
[P10944 Going from u to v or from v to u? - 洛谷](https://www.luogu.com.cn/problem/P10944) 两倍经验


已知一个有向图，要求任意两点 $u, v$ 都满足 $u$ 可以到达 $v$ **或** $v$ 可以到达 $u$ 。请你判断要求能不能成立。

不难看出强连通图是一定成立的，那我们就可以将图缩点成一个 DAG 然后判断源点的数量，如果源点数量大于 $1$ 则一定不行，然后也不能出现支线，否则支线之间无法到达。

于是就变成了判断是否存在一条哈密顿路径。对于 DAG 来说其等价于拓扑排序的唯一性判断。要求每次队列中只能有一个节点

具体代码为

```python
import sys
from collections import deque
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    for _ in range(II()):
        n, m = MII()
        
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
        
        dag = [[] for _ in range(scc)]
        din = [0] * scc
        for u in range(1, n + 1):
            for v in g[u]:
                su = scc_id[u]
                sv = scc_id[v]
                if su != sv:
                    dag[su].append(sv)
                    din[sv] += 1
        
        dq = deque([i for i in range(scc) if din[i] == 0])
        
        f = True
        while dq:
            if len(dq) > 1:
                f = False
                break
            u = dq.popleft()
            for v in dag[u]:
                din[v] -= 1
                if din[v] == 0: 
                    dq.append(v)
        
        print("Yes" if f else "No")
        

if __name__ == "__main__":
    main()
```

