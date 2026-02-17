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
        a, b = MII()

        t = Min(a, b)
        s = "01" * t
        rem = Max(a, b) - t

        if a > b:
            s = '0' * (rem // 2) + s + '0' * (rem // 2 + (rem & 1))
        else:
            s = '1' * (rem // 2) + s + '1' * (rem // 2 + (rem & 1))
        
        print(s)

if __name__ == "__main__":
    main()