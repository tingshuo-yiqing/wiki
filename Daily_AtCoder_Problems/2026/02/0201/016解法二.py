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
    a, b, c = MII()

    P = 9999

    ans = inf
    for i in range(P + 1):
        if i * a > n:
            break
        for j in range(P + 1):
            rem = n - i * a - j * b
            if rem < 0:
                break
            if rem % c == 0:
                ans = Min(ans, i + j + rem // c)
    print(ans)
if __name__ == "__main__":
    main()