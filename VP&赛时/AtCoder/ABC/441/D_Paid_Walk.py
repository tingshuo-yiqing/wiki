import sys
sys.setrecursionlimit(200100)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, l, s, p = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    ans = [0] * (n + 1)

    for _ in range(m):
        u, v, c = map(int, input().split())
        g[u].append((v, c))

    def dfs(u, cnt, weight):
        if cnt > l or weight > p:
            return 
        if cnt == l and s <= weight <= p:
            ans[u] = 1
            return 
        for v, w in g[u]:
            dfs(v, cnt + 1, weight + w)
    
    dfs(1, 0, 0)
    for i, x in enumerate(ans):
        if x == 1:
            print(i, end=' ')

if __name__ == "__main__":
    main()