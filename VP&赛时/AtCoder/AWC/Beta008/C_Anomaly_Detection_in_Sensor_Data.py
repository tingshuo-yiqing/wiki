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

    cnt = 0

    l = s = 0
    for r, x in enumerate(a):
        s += x

        if r - l + 1 < k:
            continue

        if s <= 0:
            cnt += 1

        s -= a[l]
        l += 1

    print(cnt) 

if __name__ == "__main__":
    main()
