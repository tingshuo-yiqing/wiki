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

    def check(m):
        cnt = 0
        cur = 0
        for x in a:
            if cur + x > m:
                cnt += 1
                cur = x
            else:
                cur += x
        return cnt <= k

    l, r = max(a) - 1, sum(a) + 1  #! 注意左边界

    while l + 1 < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m
    
    print(r)

if __name__ == "__main__":
    main()
