import sys
from math import inf, gcd
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

def main():
    for _ in range(II()):
        n = II()
        a = LII()

        f = False
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(a[i], a[j]) > 1:
                    print(a[i], a[j])
                    f = True
                    break
            if f:
                break
        if not f:
            print(-1)
if __name__ == "__main__":
    main()