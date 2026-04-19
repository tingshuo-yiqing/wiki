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

dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    n, m = MII()

    sx, sy = MII()
    ex, ey = MII()
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1

    g = [inp() for _ in range(n)]

    dist = [[[inf] * 4 for _ in range(m)] for _ in range(n)]

    dq = deque()

    #! 初始4个方向
    for d in range(4):
        a, b = sx + dirr[d][0], sy + dirr[d][1]
        if 0 <= a < n and 0 <= b < m and g[a][b] != '#':
            dist[a][b][d] = 0
            dq.appendleft((a, b, d))

    while dq:
        i, j, pd = dq.popleft()

        if i == ex and j == ey:
            print(min(dist[i][j]))
            return
        
        for f in range(4):
            a, b = dirr[f][0] + i, dirr[f][1] + j
            if 0 <= a < n and 0 <= b < m and g[a][b] != '#':
                
                #! 变换方向才需要花费
                cost = 1 if f != pd else 0
                
                if dist[a][b][f] > dist[i][j][pd] + cost:
                    dist[a][b][f] = dist[i][j][pd] + cost
                    if cost == 1:
                        dq.append((a, b, f))
                    else:
                        dq.appendleft((a, b, f))


if __name__ == "__main__":
    main()
