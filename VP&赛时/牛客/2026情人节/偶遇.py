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

    for k, v in mp.items():
        if v % 2 != 0:
            print("NO")
            return
    
    a.sort()
    print("YES")
    print(*a)

if __name__ == "__main__":
    main()