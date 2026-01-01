import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())

        g[u].append(v)
        g[v].append(u)
    
    ans = 0
    for u in range(1, n + 1):
        cnt = 0
        for v in sorted(g[u]):
            if v < u:
                cnt += 1
            else:
                break
        if cnt == 1:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()