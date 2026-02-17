import sys
from math import atan2, dist, pi, sin, cos, degrees, radians
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
        y = -r * sin(radians(360 * t / T))
        z = r - r * cos(radians(360 * t / T))

        A = dist((0, y), (X, Y))
        B = z
        print(f'{degrees(atan2(B, A)):.9f}')  # 弧度转角度直接使用degrees函数
        
if __name__ == "__main__":
    main()