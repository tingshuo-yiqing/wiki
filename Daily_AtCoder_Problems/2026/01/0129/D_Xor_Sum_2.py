import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n = II()
    a = LII()

    l = ans = su = xor = 0
    for r, x in enumerate(a):
        su += x
        xor ^= x

        while su != xor:
            su -= a[l]
            xor ^= a[l]  # 异或一个数第二次相当于减法
            l += 1
        
        ans += (r - l + 1)

    print(ans)

if __name__ == "__main__":
    main()