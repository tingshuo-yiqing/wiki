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

    g = [set() for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].add(v)
    
    ans = set()
    for u in range(1, n + 1):
        for v in g[u]:
            if u in g[v]:
                ans.add((u, v))
                ans.add((v, u))
    
    print(len(ans) // 2)


if __name__ == "__main__":
    main()
