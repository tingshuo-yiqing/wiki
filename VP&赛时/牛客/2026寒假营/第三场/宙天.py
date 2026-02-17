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

    for i in range(1, n + 1):
        if n % i == 0:
            if i * (n // i) == n and abs(i - n // i) == 1:
                print("YES")
                sys.exit(0)
    print("NO")

if __name__ == "__main__":
    main()