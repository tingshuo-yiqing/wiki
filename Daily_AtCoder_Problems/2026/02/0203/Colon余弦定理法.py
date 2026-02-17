import sys
from math import inf, cos, radians
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    a, b, h, m = MII()

    d1 = m * 6  # 分针过了 m 分钟后的度数
    d2 = h * 30 + 30 * m / 60   # 时针过了 h 小时 m 分钟后的度数

    d = abs(d1 - d2)

    c = a ** 2 + b ** 2 - 2 * a * b * cos(radians(d))
    print(f'{c ** 0.5:.10}')

if __name__ == "__main__":
    main()