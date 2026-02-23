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
    n, q = MII()

    a = LII()

    outs = []
    for _ in range(q):
        t = II()
        print(bin(t))

if __name__ == "__main__":
    main()