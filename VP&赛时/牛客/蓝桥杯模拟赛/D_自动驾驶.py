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
    s = inp()

    cnt = defaultdict(int)

    for i in range(n - k + 1):
        cnt[s[i:i+k]] += 1
    
    ans = 0
    # print(cnt)
    for c, v in cnt.items():
        if v > 1:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
