import sys

# C

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
    n, L, R, T = MII()

    t = []
    for i in range(n):
        p, s = MII()

        if s >= T and L <= p <= R:
            t.append((p, s, i))
    
    if t:
        t.sort(key=lambda x: (x[0], -x[1], x[2]))
        print(t[0][2] + 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
