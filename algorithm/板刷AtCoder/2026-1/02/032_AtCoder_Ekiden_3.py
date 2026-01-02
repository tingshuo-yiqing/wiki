import sys
from itertools import permutations
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

inf = float('inf')

def main():
    n = int(input())

    g = [list(map(int, input().split())) for _ in range(n)]

    bad = [[False] * n for _ in range(n)]

    for _ in range(int(input())):
        u, v = map(lambda x: int(x) - 1, input().split())

        bad[u][v] = bad[v] [u] = True

    ans = inf
    for p in permutations(range(n)):  # p表示选手列表，p[j]就是第j个选手 0 <= p[j] < n

        # 枚举相邻两个选手，只要有一对不符合就直接跳过
        if any(bad[p[j]][p[j + 1]] for j in range(n - 1)):
            continue

        ans = min(ans, sum(g[p[j]][j] for j in range(n)))   # g[p[j]][j] 选手p[j]在j段的时间

    print(-1 if ans == inf else ans)


if __name__ == "__main__":
    main()