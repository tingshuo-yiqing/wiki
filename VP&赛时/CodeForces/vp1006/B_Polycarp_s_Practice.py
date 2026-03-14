import sys
from math import inf
from collections import Counter
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    a = LII()

    b = sorted(a, reverse=True)[:m]
    print(sum(b))
    cnt = Counter(b)

    t = []
    e = 0
    for i, x in enumerate(a, start=1):
        if x in cnt and cnt[x]:
            cnt[x] -= 1
            t.append(i - e)
            e = i

    t[-1] += (n - e)

    print(*t)

if __name__ == "__main__":
    main()