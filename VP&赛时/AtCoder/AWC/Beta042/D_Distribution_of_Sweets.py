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
    n, k =  MII()

    a = LII()
    a = [x % k for x in a]

    cnt = defaultdict(int)
    cnt[0] = 1
    ans = cur = 0

    for x in a:
        cur = (cur + x) % k
        ans += cnt[cur]
        cnt[cur] += 1
    
    print(ans)

if __name__ == "__main__":
    main()
