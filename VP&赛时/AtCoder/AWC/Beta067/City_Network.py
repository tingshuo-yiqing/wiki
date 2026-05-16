import sys
from math import inf

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
    n, m = MII()

    S = [-1] + LII()

    d = [[inf] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = MII()
        d[u][v] = w
        d[v][u] = w
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = Min(d[i][j], d[i][k] + d[k][j])
    
    ans = 0

    C = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and d[i][j] > S[i]:
                C[i] += 1
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if d[i][j] <= S[i] and d[i][j] <= S[j] and C[i] == C[j]:
                ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
