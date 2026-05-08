import sys
from collections import defaultdict
from bisect import bisect_left

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
    n, o, p = MII()

    T = defaultdict(int)
    for _ in range(n):
        x, y = MII()
        T[x] = y

    so = sorted(T.keys())

    def find(x):
        i = bisect_left(so, x)
        #! 二分找最接近的数
        ret = so[0]
        if 0 < i < n:
            a = so[i - 1]
            b = so[i]
            ret = a if abs(a - x) <= abs(b - x) else b
        elif i == n:
            ret = so[-1]
        return ret

    locat = find(o)
    locat1 = find(p)

    ans = 0
    if locat1 == locat:
        ans = T[locat] + 2
    else:
        ans = T[locat] + T[locat1] + 2
    
    print(ans)

if __name__ == "__main__":
    main()
