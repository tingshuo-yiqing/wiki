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
    A, B, AB, x, y = MII()

    ans = inf
    i = 1
    while i <= Max(x, y):
        ans = Min(ans, 2 * AB * i + Max(x - i, 0) * A + Max(y - i, 0) * B)
        i += 1

    print(Min(A * x + B * y, ans)) 

if __name__ == "__main__":
    main()