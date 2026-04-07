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

# def printMat(g):    
#     for o in g:
#         print(*o)
#     print()

def main():
    n = II()

    g = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            g[i][j] = i * n + j + 1

    for _ in range(II()):
        op, x, y, L = MII()
        x -= 1
        y -= 1
        if L == 1:
            continue
        if op == 1:
            #! 挖出子矩阵
            P = [[0] * L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    P[i][j] = g[i+x][j+y]
            
            #! 顺时针旋转子矩阵复制到A
            A = [[0] * L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    A[j][L-i-1] = P[i][j]
            
            #! 还原到g中
            for i in range(L):
                for j in range(L):
                    g[i+x][j+y] = A[i][j]
        else:
            #! 挖出子矩阵
            P = [[0] * L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    P[i][j] = g[i+x][j+y]
            
            #! 逆时针旋转子矩阵复制到A
            A = [[0] * L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    A[i][j] = P[j][L-i-1]
            
            #! 还原到g中
            for i in range(L):
                for j in range(L):
                    g[i+x][j+y] = A[i][j]
        # printMat(g)
            
    outs = []
    for _ in range(II()):
        i, j = MII()
        i -= 1
        j -= 1
        outs.append(g[i][j])
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
