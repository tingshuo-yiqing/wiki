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

    pf = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        v = LII()
        for j in range(m):
            pf[i + 1][j + 1] = v[j]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pf[i][j] += pf[i-1][j] + pf[i][j-1] - pf[i-1][j-1]

    outs = []

    for _ in range(II()):
        x1, y1, x2, y2 = MII()
        outs.append(pf[x2][y2] - pf[x1-1][y2] - pf[x2][y1-1] + pf[x1-1][y1-1])
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
