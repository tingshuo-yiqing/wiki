import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

"""二进制枚举: O(2^N * N * M) 可以通过"""
def main():
    n, m = MII()

    a = [inp() for _ in range(n)]

    ans = inf
    for i in range(1 << n):
        std = m
        vised = [True] * m
        for j in range(n):
            if (i >> j) & 1:
                for k in range(m):
                    if a[j][k] == 'o' and vised[k]:
                        std -= 1
                        vised[k] = False
            if std == 0:
                ans = Min(ans, bin(i).count('1'))

    print(ans)
if __name__ == "__main__":
    main()