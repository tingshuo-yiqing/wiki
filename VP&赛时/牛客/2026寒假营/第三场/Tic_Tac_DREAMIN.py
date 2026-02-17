import sys
from random import randint
from math import inf, dist, sqrt
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    x1, y1 = MII()
    x2, y2 = MII()

    # x1, y1 = randint(1, 10), randint(1, 10)
    # x2, y2 = randint(1, 10), randint(1, 10)
    A = (x1, y1)
    B = (x2, y2)

    AB = dist(A, B)
    # print(AB)
    
    # for c in range(-100, 100):
    C = (-0.5, 0)
    AC = dist(A, C)
    BC = dist(B, C)
    p = (AB + AC + BC) // 2
    s = sqrt(max(p * (p - AB) * (p - AC) * (p - BC), 0))
    print(s)

if __name__ == "__main__":
    main()