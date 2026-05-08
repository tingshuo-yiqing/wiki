import sys
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
    n = II()

    d = defaultdict(int)

    for _ in range(n):
        x, l, r, v = MII()
        d[x - l] += v
        d[x + r + 1] -= v
    
    v = sorted(d.keys())

    cur = ans = 0
    for i in v:
        cur += d[i]
        ans = Max(ans, cur)
    
    print(ans)

if __name__ == "__main__":
    main()
