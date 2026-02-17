import sys
from collections import deque
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    n, m = MII()
    g = [list(inp()) for _ in range(n)]

    cnt = 0
    starts = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                starts.append((i, j))
                cnt += 1
    if cnt <= 2:  # 已经是断开状态了
        print(-1)
        sys.exit(0)
    
    def is_connect(ti, tj):
        si, sj = -1, -1
        for i, j in starts:
            if (i, j) != (ti, tj):
                si, sj = i, j
                break

        d = deque([si * m + sj])
        vised = [0] * n * m
        vised[si * m + sj] = 1

        cnt = 1
        while d:
            u = d.popleft()
            i, j = divmod(u, m)
            for dx, dy in dir:
                x, y = i + dx, j + dy
                ns = x * m + y
                if 0 <= x < n and 0 <= y < m and g[x][y] == '#' and not vised[ns]:
                    cnt += 1  # if里面计数时初始化为1
                    vised[ns] = 1
                    d.append(ns)

        return cnt == len(starts) - 1  # 连通

    for i, j in starts:
        g[i][j] = '.'
        if not is_connect(i, j):
            print(1)
            sys.exit()
        g[i][j] = '#'

    print(2)

if __name__ == "__main__":
    main()