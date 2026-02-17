import sys
from math import inf, cos, sin, dist, radians
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    a, b, c, d = MII()

    t = (c * 60 + d) / 60

    x1 = a * sin(radians(360 * t / 12))
    y1 = a * cos(radians(360 * t / 12))

    x2 = b * sin(radians(360 * t))
    y2 = b * cos(radians(360 * t))

    print(f'{dist((x1, y1), (x2, y2))}')

if __name__ == "__main__":
    main()