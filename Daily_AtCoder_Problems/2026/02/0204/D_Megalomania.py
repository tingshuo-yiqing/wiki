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

    t = [list(MII()) for _ in range(n)]

    t.sort(key=lambda x: (x[1], x[0]))

    cur = 0
    for k, v in t:
        if cur + k <= v:
            cur += k
        else:
            print("No")
            sys.exit(0)
    
    print("Yes")

if __name__ == "__main__":
    main()