import sys
from math import inf

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

    a = [0] * (n + 1)
    b = [0] * (n + 1)

    for i in range(1, n + 1):
        u, v = MII()
        a[i] = u
        b[i] = v


    outs = []
    for _ in range(m):
        c = LII()

        mi1 = mi2 = inf

        for x in c[1:]:
            if b[x] == 0:
                mi1 = Min(mi1, a[x])
            else:
                mi2 = Min(mi2, a[x])
        
        outs.append(str(-1) if mi1 + mi2 == inf else str(mi1 + mi2))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
