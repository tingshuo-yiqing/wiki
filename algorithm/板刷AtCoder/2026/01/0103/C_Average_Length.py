import sys
from itertools import permutations
from math import dist, factorial
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())    

    coor = [list(map(int, input().split())) for _ in range(n)]

    g = [[0.0] * n for _ in range(n)]

    for i in range(n):  # 生成邻接矩阵
        for j in range(i, n):
            g[i][j] = g[j][i] = dist(coor[i], coor[j])

    # print(g)

    su = 0
    for p in permutations(range(n)):
        su += sum(g[p[j]][p[j+1]] for j in range(n-1))

    print(f'{su / factorial(n):.11}')
if __name__ == "__main__":
    main()