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
    s = inp()

    cnt = defaultdict(int)

    cnt[0] = 1

    f = v = 0
    for i in range(n):
        f += (s[i] in "FB")
        v += (s[i] in "VB")
        cnt[f - v] += 1

    ans = 0

    for v in cnt.values():
        ans += v * (v - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()
