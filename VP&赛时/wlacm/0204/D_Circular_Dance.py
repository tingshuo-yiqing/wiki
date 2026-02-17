import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()

    g = [[] for _ in range(n + 1)]

    for a in range(1, n + 1):
        u, v = MII()
        g[a].append(u)
        g[a].append(v)
    
    for i in range(1, n + 1):
        if g[i][1] not in g[g[i][0]]:
            g[i][1], g[i][0] = g[i][0], g[i][1]
    
    ans = [1]
    ans.append(g[1][0])

    for _ in range(n - 2):
        # 使用数组存酒不需要第三个临时变量了
        cur = ans[-2]
        nxt = ans[-1]

        #! 判断一次 nxt 的下两个不能是 cur 
        if nxt == g[cur][0]:
            ans.append(g[cur][1])
        else:
            ans.append(g[cur][0])
        
    print(*ans)

if __name__ == "__main__":
    main()