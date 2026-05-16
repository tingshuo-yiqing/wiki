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
    n = II()
    a = LII()

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]
    
    mx = -inf
    mi = inf
    for i in range(n + 1):
        mx = Max(pf[i] - mi, mx)
        mi = Min(mi, pf[i])
        if i > 0:
            print(mx)

if __name__ == "__main__":
    main()
