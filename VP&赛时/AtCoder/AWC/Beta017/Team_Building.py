import sys
from math import inf

# D

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
    n, m, k = MII()
    A = LII()

    g = [[0] * n for _ in range(n)]

    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        g[u][v] = w

    mx = -inf
    for i in range(1 << n):
        if i.bit_count() != k:
            continue
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += A[j]
                for x in range(n):
                    if x != j and (i >> x) & 1:
                        s -= g[j][x]
        mx = Max(mx, s)
    
    print(mx)

if __name__ == "__main__":
    main()
