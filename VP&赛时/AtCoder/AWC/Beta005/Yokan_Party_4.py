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
    n, L = MII()
    k = II() + 1

    t = [0] + LII() + [L]
    a = [t[i + 1] - t[i] for i in range(n + 1)]

    def check(m):
        cur = cnt = 0
        for x in a:
            cur += x
            if cur >= m:
                cnt += 1
                cur = 0
        return cnt >= k

    l = min(a) - 1
    r = sum(a) + 1

    while l + 1 < r:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m

    print(l)

if __name__ == "__main__":
    main()
