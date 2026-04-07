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
    n, m, k = MII()

    g = []
    for _ in range(n):
        a = LII()

        g.append((a[0], *a[2:]))
    
    g.sort(key=lambda x: -x[0])

    cnt = defaultdict(int)

    for y in g[:k]:
        for z in y[1:]:
            cnt[z] += 1
    
    ans = sum(1 for i in range(1, m + 1) if cnt[i] == k)

    print(ans)

if __name__ == "__main__":
    main()
