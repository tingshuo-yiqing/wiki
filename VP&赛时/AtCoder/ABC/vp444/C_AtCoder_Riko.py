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
    a.sort()

    #! 情况一，等于最大值
    l, r = 0, n - 1
    while r >= 0 and a[r] == a[-1]:
        r -= 1
    
    if r % 2 == 1:
        f1 = True
        while l < r:
            if l >= 0 and a[l] + a[r] != a[-1]:
                f1 = False
                break
            l += 1
            r -= 1

        if f1:
            print(a[-1], end=' ')
        
    #! 情况二，等于最大最小的和
    if n % 2 == 0:
        l, r = 0, n - 1

        f2 = True
        while l < r:
            if a[l] + a[r] != a[0] + a[-1]:
                f2 = False
                break
            l += 1
            r -= 1
        if f2:
            print(a[0] + a[-1])

if __name__ == "__main__":
    main()
