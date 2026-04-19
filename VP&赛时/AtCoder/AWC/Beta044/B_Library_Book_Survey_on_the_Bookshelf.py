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

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]
    
    outs = []
    for _ in range(q):
        l, r = MII()
        outs.append(str(pf[r] - pf[l-1]))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
