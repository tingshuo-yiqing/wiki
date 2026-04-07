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
    n, k = MII()

    a = LII()

    mp = defaultdict(int)
    mp[0] = 1

    cur = ans = 0
    for x in a:
        cur += x
        if cur - k in mp:
            ans += mp[cur - k]
        mp[cur] += 1
    
    print(ans)

if __name__ == "__main__":
    main()
