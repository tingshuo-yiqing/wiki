import sys
from collections import defaultdict

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
    n, k = MII()

    d = defaultdict(int)
    for _ in range(n):
        l, r = MII()
        d[l] += 1
        d[r] -= 1
    
    coor = sorted(d.items())
    
    ans = 0
    cur = 0
    pre = 0  #! 前一个坐标
    for x, delta in coor:  #! 顺序枚举当前坐标
        if cur >= k:
            ans += (x - pre)  #! 相邻区间大小
        cur += delta
        pre = x

    print(ans)

if __name__ == "__main__":
    main()
