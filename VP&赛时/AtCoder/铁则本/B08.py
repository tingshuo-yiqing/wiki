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
    n = II()
    N = 1502

    A = [[0] * N for _ in range(N)]

    for _ in range(n):
        x, y = MII()
        A[x][y] += 1

    for i in range(1, N):
        for j in range(1, N):
            A[i][j] += A[i-1][j] + A[i][j-1] - A[i-1][j-1] 

    outs = []
    for _ in range(II()):
        x1, y1, x2, y2 = MII()
        outs.append(A[x2][y2] - A[x1-1][y2] - A[x2][y1-1] + A[x1-1][y1-1])

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
