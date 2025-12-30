import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    g = [[False] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u][v] = True
        g[v][u] = True

    cnt = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if g[i][j] and g[j][k] and g[k][i]:
                    cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()