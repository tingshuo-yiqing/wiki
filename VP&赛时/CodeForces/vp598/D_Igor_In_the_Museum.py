import sys
from collections import deque
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m, k = MII()

    g = [inp() for _ in range(n)]

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    memo = [[-1] * m for _ in range(n)]  # -1是为了避免全为 . 没有 * 的情况

    outs = []
    for _ in range(k):
        a, b = MII()
        a -= 1
        b -= 1

        if memo[a][b] != -1:
            outs.append(memo[a][b])
            continue

        d = deque([(a, b)])
        t = [(a, b)]
        memo[a][b] = 0

        ans = 0
        while d:
            x, y = d.popleft() 
            for dx, dy in dir:
                xx, yy = x + dx, y + dy 
                if 0 <= xx < n and 0 <= yy < m:  
                    if g[xx][yy] == '*':
                        ans += 1
                    if g[xx][yy] == '.' and memo[xx][yy] == -1:
                        memo[xx][yy] = ans
                        d.append((xx, yy))
                        t.append((xx, yy))
        for i, j in t:
            memo[i][j] = ans

        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()