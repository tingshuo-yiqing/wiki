import sys
from itertools import combinations

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
    n, k, m = MII()
    a = LII()

    tests = [tuple(MII()) for _ in range(m)]

    ans = -10 ** 10
    for i in range(1 << n):
        if i.bit_count() > k:
            continue
        p = 0
        for j, x in enumerate(a):
            if (i >> j) & 1:
                p += x
        
        for l, r, x in tests:  # 1-based
            l -= 1
            if i & ( (1 << r) - (1 << l) ):
                p += x

        ans = Max(ans, p)
    
    print(ans)

if __name__ == "__main__":
    main()
