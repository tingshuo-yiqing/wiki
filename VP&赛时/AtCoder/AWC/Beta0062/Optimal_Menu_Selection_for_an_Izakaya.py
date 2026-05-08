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
    n, k, D = MII()

    t = []
    for _ in range(n):
        u, v = MII()
        t.append((u, v))

    ans = -10 ** 10
    for i in range(1 << n):
        s = 0
        d = 0
        for j in range(n):
            if (i >> j) & 1:
                s += t[j][0]
                d += t[j][1]

        ans = Max(ans, s - D * Max(0, d - k))

    print(ans)

if __name__ == "__main__":
    main()
