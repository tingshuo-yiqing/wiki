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
    n = II()
    
    g = [[]]
    for _ in range(n):
        t = LII()
        g.append(t)
    
    Q = II()

    cnt = 0
    for _ in range(Q):
        u, v = MII()

        if g[u][v] > 0:
            g[u][v] -= 1
        else:
            cnt += 1
    
    for o in g[1:]:
        print(*o[1:])
    print(cnt)

if __name__ == "__main__":
    main()
