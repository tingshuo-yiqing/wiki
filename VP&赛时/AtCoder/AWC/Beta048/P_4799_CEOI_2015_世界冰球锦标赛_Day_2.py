import sys
from bisect import bisect, bisect_left
from collections import defaultdict

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
    n, T = MII()
    a = LII()

    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]

    def get_setsum(arr):
        n = len(arr)
        ret = []
        for i in range(1 << n):
            s = 0
            ok = True
            for j in range(n):
                s += arr[j] if (i >> j) & 1 else 0
                if s > T:
                    ok = False
                    break
            if ok:
                ret.append(s)
        return ret

    left = get_setsum(a1)
    right = get_setsum(a2)

    left.sort()

    ans = 0
    for s in right:
        t = T - s
        ans += bisect(left, t)
    
    print(ans)

if __name__ == "__main__":
    main()
