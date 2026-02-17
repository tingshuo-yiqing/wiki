import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()
    a = LII()

    s = set(a)

    for x in a:
        for i in range(31):
            p = 1 << i
            if x + p in s and x - p in s:
                print(3)
                print(x, x + p, x - p)
                return
    for x in a:
        for i in range(31):
            p = 1 << i
            if x + p in s:
                print(2)
                print(x, x + p)
                return
            if x - p in s:
                print(2)
                print(x, x - p)
                return
    print(1)
    print(a[0])

if __name__ == "__main__":
    main()