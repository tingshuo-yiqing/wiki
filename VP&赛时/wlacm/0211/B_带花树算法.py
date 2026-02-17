import sys
from collections import Counter
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

    mp = Counter(a)

    ans = 0
    for x in a:
        ok = False
        for i in range(1, 33): 
            ...
        if ok:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()