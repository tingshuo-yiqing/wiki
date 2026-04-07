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
    a = LII()

    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    
    maxk = logs[n] + 1

    st_min = [[0] * n for _ in range(maxk)]
    st_max = [[0] * n for _ in range(maxk)]

    st_max[0] = a[:]
    st_min[0] = a[:]

    for k in range(1, maxk):
        for i in range(n - (1 << k) + 1):
            st_min[k][i] = Min(st_min[k-1][i], st_min[k-1][i + (1 << (k-1))])
            st_max[k][i] = Max(st_max[k-1][i], st_max[k-1][i + (1 << (k-1))])
    
    def query_min(l, r):
        k = logs[r - l + 1]
        return Min(st_min[k][l], st_min[k][r - (1 << k) + 1])

    def query_max(l, r):
        k = logs[r - l + 1]
        return Max(st_max[k][l], st_max[k][r - (1 << k) + 1])

    outs= []
    for _ in range(q):
        op, l, r = MII()
        l -= 1
        r -= 1
        outs.append(query_max(l, r) if op == 2 else query_min(l, r))
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
