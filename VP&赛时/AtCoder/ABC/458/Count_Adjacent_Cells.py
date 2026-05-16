import sys

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

    g = [[0] * m for _ in range(n)]

    dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            t = 0
            for dx, dy in dirr:
                a, b = dx + i, dy + j
                if 0 <= a < n and 0 <= b < m:
                    t += 1
            g[i][j] = t
    
    for o in g:
        print(*o)

if __name__ == "__main__":
    main()
