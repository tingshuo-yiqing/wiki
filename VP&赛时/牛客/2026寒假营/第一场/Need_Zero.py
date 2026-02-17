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
    n = n % 10
    if n == 0:
        print(1)
    elif n == 2:
        print(5)
    elif n == 5:
        print(2)
    else:
        print(10)

if __name__ == "__main__":
    main()