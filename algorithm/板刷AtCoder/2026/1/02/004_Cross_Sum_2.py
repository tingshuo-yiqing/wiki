import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    g = [list(map(int, input().split())) for _ in range(n)]

    row, col = [0] * n, [0] * m

    for i in range(n):
        for j in range(m):
            row[i] += g[i][j]
            col[j] += g[i][j]

    for i in range(n):
        for j in range(m):
            print(row[i] + col[j] - g[i][j], end=' ')
        print()
    
if __name__ == "__main__":
    main()