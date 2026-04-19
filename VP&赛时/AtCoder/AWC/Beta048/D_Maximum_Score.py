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
    n, m, k = MII()

    divs = []
    for i in range(1, k + 1):
        if k % i == 0:
            divs.append((i - 1, k // i - 1))

    pf = [[0] * (m + 1)]

    for _ in range(n):
        s = inp()
        t = [0] * (m + 1)
        for i in range(m):
            t[i + 1] = int(s[i])
        pf.append(t)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pf[i][j] += pf[i-1][j] + pf[i][j-1] - pf[i-1][j-1]
    
    ans = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for dx, dy in divs:
                x, y = i + dx, j + dy
                if 0 <= x <= n and 0 <= y <= m:
                    t = pf[x][y] - pf[i-1][y] - pf[x][j-1] + pf[i-1][j-1]
                    ans = Max(ans, t)

    print(ans)

if __name__ == "__main__":
    main()
