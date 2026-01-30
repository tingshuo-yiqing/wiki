import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

MOD = 10 ** 9 + 7

def main():
    L, R = MII()

    ans = 0
    p = 1
    for k in range(1, 20):
        low = p
        high = p * 10 - 1

        start = Max(L, low)  # 关键，时刻确定上下界
        end = Min(R, high)

        if start <= end:     # 取交集时，前期有start比end大的情况
            num = end - start + 1
            s = (start + end) * num // 2
            ans = (ans + s * k) % MOD
        
        p *= 10
        if p > R:
            break
    
    print(ans % MOD)

if __name__ == "__main__":
    main()