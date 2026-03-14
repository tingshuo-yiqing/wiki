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
    a = sorted(LII())

    ans = inf
    for i in range(1, 101):
        ans = Min(ans, abs(a[0] - i) + abs(a[1] - i) + abs(a[2] - i))

    print(ans)
    
if __name__ == "__main__":
    main()