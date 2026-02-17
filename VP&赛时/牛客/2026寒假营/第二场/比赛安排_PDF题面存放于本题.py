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
    for _ in range(II()):
        a, b, c = MII()

        mi = min(a, b, c)
        mx = max(a, b, c)

        print("YES" if mx - mi < 2 else "NO")

if __name__ == "__main__":
    main()