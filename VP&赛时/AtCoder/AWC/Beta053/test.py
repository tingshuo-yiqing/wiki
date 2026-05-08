import sys

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
    n, q = MII()
    a = [0] + LII()

    value = a[:]
    sz = [1] * (n + 1)

    nxt = list(range(n + 2))

    def find(x):
        while nxt[x] != x:
            nxt[x] = nxt[nxt[x]]
            x = nxt[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            sz[ry] += sz[rx]
            value[ry] += value[rx]
            nxt[rx] = ry

    outs = []
    for _ in range(q):
        op, x, *y = MII()

        if op == 1:
            cur = find(x)
            while cur < y[0]:
                nx = find(cur + 1)
                union(cur, nx)
                cur = nx
        else:
            root = find(x)
            outs.append(f'{value[root] / sz[root]:.10f}')

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
