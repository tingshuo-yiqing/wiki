import sys
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
    n, m = MII()

    a = sorted(LII())
    b = sorted(LII())

    ans = 0
    for x in a:
        i = bisect_left(b, x)

        mi = b[0]
        if i == m:
            mi = b[-1]
        elif 0 < i < m:
            t1 = abs(b[i] - x)
            t2 = abs(b[i-1] - x)
            mi = b[i] if t1 < t2 else b[i-1]

        ans += abs(mi - x)

    print(ans)

if __name__ == "__main__":
    main()
