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

    l = 0
    r = n - 1

    ans1 = ans2 = 0
    for i in range(n):
        if i % 2 == 0:
            ans1 += Max(a[l], a[r])
            if a[l] > a[r]:
                l += 1
            else:
                r -= 1
        else:
            ans2 += Max(a[l], a[r])
            if a[l] > a[r]:
                l += 1
            else:
                r -= 1
    
    print(ans1, ans2)

if __name__ == "__main__":
    main()
