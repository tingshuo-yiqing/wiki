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
    n = II()
    a = LII()

    s = sum(a)
    if s % n != 0:
        print(-1)
        return
    
    t = s // n

    ans = 0
    #! 模拟版
    # for i in range(n - 1):
    #     d = abs(a[i] - t)
    #     if a[i] < t:
    #         a[i + 1] -= d
    #     elif a[i] > t:
    #         a[i + 1] += d 
    #     ans += d
    
    #! 前缀和版
    cur = 0
    for i in range(n - 1):
        d = a[i] - t
        cur += d
        ans += abs(cur)

    print(ans)

if __name__ == "__main__":
    main()
