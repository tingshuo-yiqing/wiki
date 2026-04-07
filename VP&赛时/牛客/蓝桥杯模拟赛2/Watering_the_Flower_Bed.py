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

    d = [0] * (n + k)

    cnt = cur = 0
    for i, x in enumerate(a):
        cur += d[i]

        v = cur + x
        if v < t:
            diff = t - v
            cnt += diff
            cur += diff
            d[i + k] -= diff
    
    print(cnt * c)

if __name__ == "__main__":
    main()
