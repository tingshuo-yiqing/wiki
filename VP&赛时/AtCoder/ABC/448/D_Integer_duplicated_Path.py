import sys
from collections import deque, Counter
sys.setrecursionlimit(200005)

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
    n = II()
    a = [-1]
    a += LII()

    g = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = MII()
        g[u].append(v)
        g[v].append(u)

    is_same = [False] * (n + 1)

    cnt = Counter()

    def dfs(u, fa=-1, state=False):
        if state or cnt[a[u]] > 0:
            is_same[u] = True
            state = True
        cnt[a[u]] += 1
        
        for v in g[u]:
            if v != fa:
                dfs(v, u, state)
                
        cnt[a[u]] -= 1
    
    dfs(1)

    outs = []
    for i in range(1, n + 1):
        outs.append("Yes" if is_same[i] else "No")
    
    print('\n'.join(outs))


if __name__ == "__main__":
    main()
