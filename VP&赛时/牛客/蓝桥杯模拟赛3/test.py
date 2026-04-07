# s = "12.34.54.."

# # print(sum(map(int, (s.split('.')))))

# t = s.split('.')

# print(sum(int(x) for x in t if x != ''))
def printMat(g):    
    for o in g:
        print(*o)
    print()

n = 3

g = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        g[i][j] = i * n + j + 1

# L = x = y = 2
# x -= 1
# y -= 1
# P = [[0] * L for _ in range(L)]
# for i in range(L):
#     for j in range(L):
#         P[i][j] = g[i+x][j+y]

# printMat(g)
# printMat(P)


# tg = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         tg[i][j] = g[j][n-i-1]  #! 逆时针

printMat(g)

tg = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        tg[j][n-i-1] = g[i][j]  #! 顺时针

printMat(tg)