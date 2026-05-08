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

    t = []
    for _ in range(n):
        u, v = MII()
        t.append((u, v))

    ans = inf
    for i in range(1 << n):
        if i.bit_count() >= 2:
            f = 1
            b = 1
            for j in range(n):
                if (i >> j) & 1:
                    f *= t[j][0]
                    b *= t[j][1]

            if f == b:
                ans = Min(ans, i.bit_count())
    
    print(ans if ans != inf else -1)

if __name__ == "__main__":
    main()
