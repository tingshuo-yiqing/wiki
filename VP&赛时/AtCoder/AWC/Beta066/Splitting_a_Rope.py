import sys

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
    a = LII()

    def check(limit):
        cur = 0
        cnt = 0  #! 统计切割点
        for x in a:
            if cur + x <= limit:
                cur += x
            else:
                cnt += 1
                cur = x
        return cnt <= k - 1 
    
    l = max(a) - 1
    r = sum(a) + 1

    while l + 1 < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid
    
    print(r)

if __name__ == "__main__":
    main()
