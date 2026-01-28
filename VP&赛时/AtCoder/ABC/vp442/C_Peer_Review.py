import sys
from math import comb
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, m = map(int, input().split())

    g = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u] += 1
        g[v] += 1
    
    for i in range(1, n+1):
        print(comb(n-g[i]-1, 3), end=' ')


if __name__ == "__main__":
    main()