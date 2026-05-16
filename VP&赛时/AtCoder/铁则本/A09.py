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
    n, m, q = MII()

    d = [[0] * (m + 2) for _ in range(n + 2)]

    def mark(x1, y1, x2, y2):
        d[x1][y1] += 1
        d[x2 + 1][y2 + 1] += 1
        d[x1][y2 + 1] -= 1
        d[x2 + 1][y1] -= 1
    
    for _ in range(q):
        mark(*MII())

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] += d[i-1][j] + d[i][j-1] -d[i-1][j-1]
            print(d[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()
