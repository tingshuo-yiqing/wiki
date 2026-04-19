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
    n, k, m = MII()
    t = k - m

    T = sorted([LII() for _ in range(n)], key=lambda x: (-x[0], -x[1]))

    ans = 0
    for u, v in T:
        if u == 1 and m:
            ans += v
            m -= 1
        elif u == 0 and t:
            ans += v
            t -= 1
    
    print(ans if m == t == 0 else -1)

if __name__ == "__main__":
    main()
