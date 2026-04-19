import sys
from collections import deque
from math import inf

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

    g = [inp() for _ in range(n)]

    dist = [[inf] * m for _ in range(n)]
    dist[0][0] = 0

    dq = deque([(0, 0)])    

    while dq:
        i, j = dq.popleft()
        for dx, dy in dirr:
            a, b = i + dx, j + dy
            if 0 <= a < n and 0 <= b < m and dist[a][b] == inf:
                if g[a][b] == '.':
                    dist[a][b] = dist[i][j]
                    dq.appendleft((a, b))
                else:
                    dist[a][b] = dist[i][j] + 1
                    dq.append((a, b))
    
    print(dist[n-1][m-1])

if __name__ == "__main__":
    main()
