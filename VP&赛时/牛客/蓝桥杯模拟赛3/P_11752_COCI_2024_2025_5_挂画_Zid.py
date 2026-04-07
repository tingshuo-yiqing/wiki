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

    g = [[0] * (m + 1)]
    for _ in range(n):
        t = [0] * (m + 1)
        s = inp()
        for i in range(1, m + 1):
            t[i] = 0 if s[i-1] == '.' else 1
        g.append(t)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            g[i][j] += g[i-1][j] + g[i][j-1] - g[i-1][j-1]
    
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for x in range(i, n + 1):
                for y in range(j, m + 1):
                    t = g[x][y] - g[i-1][y] - g[x][j-1] + g[i-1][j-1]
                    if t <= 1:
                        cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()
