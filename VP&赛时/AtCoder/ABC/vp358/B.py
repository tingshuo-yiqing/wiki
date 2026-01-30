import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n, k = MII()

    a = LII()

    print(k + a[0])
    cur = k + a[0]
    for i in range(1, n):
        cur = Max(a[i], cur) + k
        print(cur)

if __name__ == "__main__":
    main()