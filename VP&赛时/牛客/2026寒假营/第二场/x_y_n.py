import sys
import math
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def solve(n):
    best_xor = float('inf')
    best_pair = (0, 0)
    
    # 策略1: 检查所有小的乘数对 (a, b)
    # 对于 $n$ 很大时，倍数很少，能搜完；
    # 对于 $n$ 小时，能搜到如 (4n, 5n) 等优秀的构造
    limit = min(2000, (2**63 - 1) // n)
    for a in range(1, limit + 1):
        # 实际上只需检查 b 离 a 很近的情况
        for b in range(a + 1, min(limit + 1, a + 10)):
            if math.gcd(a, b) == 1:
                val = (a * n) ^ (b * n)
                if val < best_xor:
                    best_xor = val
                    best_pair = (a * n, b * n)
    
    # 策略2: 检查 2 的幂次位移构造
    for k in range(1, 63):
        a = 1 << k
        b = a + 1
        if b * n < 2**63:
            val = (a * n) ^ (b * n)
            if val < best_xor:
                best_xor = val
                best_pair = (a * n, b * n)
                
    return best_pair

def main():
    for _ in range(II()):
        n = II()
        
        print(*solve(n))

if __name__ == "__main__":
    main()