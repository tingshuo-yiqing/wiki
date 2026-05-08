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
    q, n = MII()

    T = []

    for _ in range(q):
        l, x = MII()
        T.append((Min(n, l), Min(n, l + x)))
    
    T.sort()
    T.append((n + 1, n + 1))

    ans = 0
    start = T[0][0]
    end = T[0][1]
    for s, e in T[1:]:
        if s <= end:
            end = Max(e, end)  #! 有可能当前区间被上一区间包含，不能直接end = e
        else:
            ans += end - start
            start = s
            end = e
    
    print(ans)

if __name__ == "__main__":
    main()
