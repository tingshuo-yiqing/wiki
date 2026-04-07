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

    cnt = defaultdict(int)

    for _ in range(n):
        l, r = MII()

        cnt[l] += 1
        cnt[r] -= 1
    
    v = sorted(cnt.keys())
    
    cur = 0
    mx = 0
    for i in v:
        cur += cnt[i]
        mx = Max(mx, cur)
    
    print(mx)

if __name__ == "__main__":
    main()
