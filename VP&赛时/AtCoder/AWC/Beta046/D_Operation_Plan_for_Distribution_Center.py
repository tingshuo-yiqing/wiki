import sys
from math import inf
from bisect import bisect, bisect_left

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
    n, k = MII()
    a = sorted(LII())

    pf = [0] * (n + 1)
    for i in range(n):
        pf[i + 1] = pf[i] + a[i]

    def get_cost(s):
        e = s + k - 1

        l = bisect_left(a, s)
        lv = l * s - pf[l]

        r = bisect(a, e)
        rv = (pf[n] - pf[r]) - (n - r) * e

        return lv + rv

    mi = inf
    for x in a:
        mi = Min(mi, get_cost(x))
        mi = Min(mi, get_cost(x - (k - 1)))
    
    print(mi)

if __name__ == "__main__":
    main()
