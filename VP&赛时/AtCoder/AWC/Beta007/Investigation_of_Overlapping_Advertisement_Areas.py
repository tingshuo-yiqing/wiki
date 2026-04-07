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

    def mark(mat, x1, y1, x2, y2):
        mat[x1][y1] += 1
        mat[x2 + 1][y2 + 1] += 1
        mat[x1][y2 + 1] -= 1
        mat[x2 + 1][y1] -= 1
    
    A = [[0] * (N + 2) for _ in range(N + 2)] 
    B = [[0] * (N + 2) for _ in range(N + 2)] 

    for _ in range(n):
        mark(A, *MII())
    for _ in range(m):
        mark(B, *MII())

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[i][j] += A[i-1][j] + A[i][j-1] - A[i-1][j-1]
            B[i][j] += B[i-1][j] + B[i][j-1] - B[i-1][j-1]

            if A[i][j] and B[i][j]:
                ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
