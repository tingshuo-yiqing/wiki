import sys
from math import comb
from itertools import permutations

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()


def main():
    n, target = MII()

    for p in permutations(range(1, n + 1)):
        s = 0
        for i in range(n):
            # 使用杨辉三角系数优化，直接计算最底层结果
            s += comb(n-1, i) * p[i]
        if s == target:
            print(*p)
            break

if __name__ == "__main__":
    main()
