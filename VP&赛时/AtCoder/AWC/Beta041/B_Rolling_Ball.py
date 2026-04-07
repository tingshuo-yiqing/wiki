import sys
from bisect import bisect_left, bisect_right

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
    b = LII()
    a = LII()

    t = []
    mx = -1
    for i, x in enumerate(b, start=1):
        if x > mx:
            mx = x
            t.append((x, i))
    t.append((t[-1][0], m))
    # for o in t:
    #     print(*o)
    # print()
    target = [i for i, j in t]

    res = [1] * n
    for i, x in enumerate(a):
        idx = bisect_right(target, x)
        if idx == len(target):
            idx -= 1
        res[i] = t[idx][1]
    
    print(*res, sep='\n')

if __name__ == "__main__":
    main()


