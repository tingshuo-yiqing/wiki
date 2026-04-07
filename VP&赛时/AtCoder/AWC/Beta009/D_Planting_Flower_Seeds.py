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


def main():
    n, m = MII()

    d = defaultdict(int)
    for _ in range(m):
        l, r = MII()
        d[l] += 1
        d[r] -= 1

    v = sorted(d.keys())

    sz = 0
    cur = 0
    pre = 0
    for i in v:
        cur += d[i]
        if cur > 0:
            sz += i - pre + 1
        pre = i

    print(sz + n)

if __name__ == "__main__":
    main()
