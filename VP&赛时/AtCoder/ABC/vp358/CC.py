import sys
from itertools import permutations
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

"""使用了位掩码进行状态压缩，时间复杂度为: O(N! * N)"""
def main():
    n, m = MII()

    masks = [int(inp().replace('x', '0').replace('o', '1'), 2) for _ in range(n)]
    t = (1 << m) - 1

    ans = inf
    for p in permutations(masks):
        cur = 0
        for i, val in enumerate(p):
            if i + 1 >= ans:
                break
            cur |= val  # 从O(M)优化为O(1)
            if cur == t:
                ans = Min(ans, i + 1)
    
    print(ans)
            
if __name__ == "__main__":
    main()