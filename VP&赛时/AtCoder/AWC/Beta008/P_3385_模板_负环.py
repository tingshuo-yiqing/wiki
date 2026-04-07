import sys
from math import inf
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
    for _ in range(II()):
        n, m = MII()

        g = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v, w = MII()
            if w < 0:
                g[u].append((v, w))
            else:
                g[u].append((v, w))
                g[v].append((u, w))
        
        def SPFA(s):
            dist = [inf] * (n + 1)
            dist[s] = 0
            cnt = [0] * (n + 1)
            inq = [True] * (n + 1)

            dq = deque([i for i in range(1, n + 1)])
            while dq:
                u = dq.popleft()
                inq[u] = False

                for v, w in g[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        cnt[v] = cnt[u] + 1
                        if cnt[v] >= n:
                            return True # 找到负环
                        if not inq[v]:
                            dq.append(v)
                            inq[v] = True
        
            return False
        
        print("YES" if SPFA(1) else "NO")

if __name__ == "__main__":
    main()
