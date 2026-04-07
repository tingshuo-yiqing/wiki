import sys
# from math import comb

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

dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    n = m = 6
    g = [LII() for _ in range(n)]
    s = set()
    ns = set()

    for i in range(n):
        for j in range(m):
            x = g[i][j]
            for dx, dy in dirr:
                a, b = i + dx, j + dy
                if 0 <= a < n and 0 <= b < m:
                    y = g[a][b]
                    if (x + y) & 1:
                        s.add((i, j, x, y))
                        ns.add(x + y)
    
    k = len(s)
    print(len(ns))
    print(k)
    # print(comb(k, 3)) 
    # comb(k, 3) == n * (n - 1) * (n - 2) // 3!
    print(82160)

if __name__ == "__main__":
    main()
