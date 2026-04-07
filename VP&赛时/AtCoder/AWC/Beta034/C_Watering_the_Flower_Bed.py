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
    n, k, t, c = MII()

    a = LII()

    d = [0] * (n + 1)

    cnt = cur = 0
    for i in range(n-k):  #! 窗口有约束，必须连续的k个才可以浇水
        cur += d[i]
        v = cur + a[i]
        if v < t:
            diff = t - v
            cnt += diff

            cur += diff  #! 当前点立即更新
            if i + k < n:
                d[i + k] -= diff

    
    mx = 0
    #! 此时，前面的更新对最后面的k个有影响
    for i in range(n-k, n):
        cur += d[i]  #! 接上之前的cur继续前缀和复原原数组
        a[i] += cur
        if a[i] < t:
            mx = Max(mx, t - a[i])
    cnt += mx

    print(cnt * c)

if __name__ == "__main__":
    main()
