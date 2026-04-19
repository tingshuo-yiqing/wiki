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
    n, m = MII()

    g = [[] for _ in range(m)]

    for _ in range(n):
        v = LII()
        for j in range(m):
            g[j].append(v[j])

    for i in range(m):
        g[i].sort()

    ans = 0
    for a in g:
        s = sum(a)
        for i in range(n - 1):
            s -= a[i]
            ans += s - (n - i - 1) * a[i]

    print(ans)
    
if __name__ == "__main__":
    main()
