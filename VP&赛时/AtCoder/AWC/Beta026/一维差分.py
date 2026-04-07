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

    d = [0] * (n + 1)

    for _ in range(q):
        l, r = MII()

        d[l] += 1
        if r <= n:
            d[r] -= 1
    
    mx = 0
    cur = 0
    for i in range(n):
        cur += d[i]
        mx = Max(mx, cur)
    
    print(mx)

if __name__ == "__main__":
    main()
