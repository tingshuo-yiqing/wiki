import sys
from math import inf,atan2, dist, pi, sin, cos
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    T = II()

    L, X, Y = MII()
    r = L / 2

    for _ in range(II()):
        t = II()

        t %= T
        y = -r * sin(2 * pi * t / T)
        z = r - r * cos(2 * pi * t / T)

        A = dist((0, y), (X, Y))
        B = z
        print(f'{atan2(B, A)*180/pi:.9f}')
        
if __name__ == "__main__":
    main()