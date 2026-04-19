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
    a = LII()

    T = [(x, i+1) for i, x in enumerate(a)]
    T.sort(reverse=True)

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        g[v].append(u)
    
    for i in range(1, n + 1):
        g[i].sort()
    
    vised = [-1] * (n + 1)

    for _, i in T:
        if vised[i] == -1:
            for j in g[i]:
                if vised[j] == -1:
                    vised[j] = i
                    vised[i] = j
                    break

    # print(*vised[1:])
    print(vised[1])

if __name__ == "__main__":
    main()
