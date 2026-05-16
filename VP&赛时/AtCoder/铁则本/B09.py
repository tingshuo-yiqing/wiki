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
    N = 1505

    A = [[0] * N for _ in range(N)]

    def mark(x1, y1, x2, y2):
        A[x1][y1] += 1
        A[x2 + 1][y2 + 1] += 1
        A[x2 + 1][y1] -= 1
        A[x1][y2 + 1] -= 1

    for _ in range(II()):
        a, b, c, d = MII()
        x1 = Min(a, c)
        y1 = Min(b, d)
        x2 = Max(a, c)
        y2 = Max(b, d)
        mark(x1 + 1, y1 + 1, x2, y2)
        # mark(a + 1, b + 1, c, d)
    
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            A[i][j] += A[i-1][j] + A[i][j-1] - A[i-1][j-1]
            ans += (A[i][j] != 0)    
    
    # for o in A:
    #     print(*o)

    print(ans)

if __name__ == "__main__":
    main()
