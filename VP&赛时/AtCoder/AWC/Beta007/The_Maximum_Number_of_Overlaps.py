import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(lambda x: int(x)+1, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    t = II()

    def mark(mat, x1, y1, x2, y2): #! 边缘不算覆盖
        mat[x1][y1] += 1
        mat[x2][y2] += 1
        mat[x1][y2] -= 1
        mat[x2][y1] -= 1
    
    n = 1000
    A = [[0] * (n + 2) for _ in range(n + 2)]

    for _ in range(t):
        mark(A, *MII())
    
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[i][j] += A[i-1][j] + A[i][j-1] - A[i-1][j-1]
            ans = Max(ans, A[i][j])
    
    print(ans)

if __name__ == "__main__":
    main()
