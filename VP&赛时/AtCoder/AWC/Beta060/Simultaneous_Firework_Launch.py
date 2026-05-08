import sys
from math import gcd, lcm

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
    n = II()

    a = 1
    b = 0
    for _ in range(n):
        u, v = MII()  #! u, v已经是最简的分式，才可以使用这个公式
        a = lcm(a, u)
        b = gcd(b, v)

    print(a, b)

if __name__ == "__main__":
    main()
