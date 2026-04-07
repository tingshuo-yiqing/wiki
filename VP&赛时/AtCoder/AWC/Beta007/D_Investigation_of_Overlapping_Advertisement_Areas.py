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
    N, n, m = MII()

    t = []
    for _ in range(n):
        r1, c1, r2, c2 = MII()
        t.append((r1, c1, r2, c2))
    
    c = []
    for _ in range(m):
        r1, c1, r2, c2 = MII()
        c.append((r1, c1, r2, c2))
    
    A = [[0] * (N + 2) for _ in range(N + 2)]
    B = [[0] * (N + 2) for _ in range(N + 2)]

    for r1, c1, r2, c2 in t:
        for i in range(r1, r2 + 1):
            A[i][c1] += 1
            A[i][c2 + 1] -= 1
    
    for r1, c1, r2, c2 in c:
        for i in range(r1, r2 + 1):
            B[i][c1] += 1
            B[i][c2 + 1] -= 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[i][j] += A[i][j-1]
            B[i][j] += B[i][j-1]

    print(sum(1 for i in range(1, N + 1) for j in range(1, N + 1) if A[i][j] and B[i][j]))

if __name__ == "__main__":
    main()
