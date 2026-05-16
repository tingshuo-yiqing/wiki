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

MAXV = 10 ** 6 + 5

def main():
    n, V = MII()

    items = []

    for _ in range(n):
        c, w = MII()
        items.append((c, w))
    
    dp = [inf] * (V + 1)  #! dp[i] 表示至少获得i天饭量的最小价值，初始化为无穷大
    dp[0] = 0

    for w, c in items:
        for j in range(V + 1):
            dp[j] = Min(dp[j], dp[Max(0, j - c)] + w)
    
    print(dp[V])

if __name__ == "__main__":
    main()
