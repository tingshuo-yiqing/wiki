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
    w = [-1] + LII()
    p = LII()

    fa = [0] * (n + 1)
    for i, x in enumerate(p, start=2):
        fa[i] = x
    
    pf = [0] * (n + 1)
    for i in range(1, n + 1):
        pf[i] = pf[fa[i]] + w[i]
    
    outs = []
    for _ in range(q):
        x = II()
        outs.append(str(pf[x]))

    print("\n".join(outs))

if __name__ == "__main__":
    main()
