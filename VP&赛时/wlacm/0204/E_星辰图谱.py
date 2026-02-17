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
    s = inp()
    n = II()

    if len(s) < n:
        print("impossible")
        sys.exit(0)

    t = len(set(s))
    print(n - t)
if __name__ == "__main__":
    main()