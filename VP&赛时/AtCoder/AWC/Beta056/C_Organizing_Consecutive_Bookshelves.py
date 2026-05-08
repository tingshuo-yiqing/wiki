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

    ans = 0
    l = s = 0
    for r, x in enumerate(a):
        s += x

        while s > k:
            s -= a[l]
            l += 1

        ans = Max(ans, r - l + 1)

    print(ans)

if __name__ == "__main__":
    main()
