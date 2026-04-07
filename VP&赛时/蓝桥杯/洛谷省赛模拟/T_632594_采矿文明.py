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
    n, m, k = MII()

    C = LII()
    W = LII()

    if k == 1:
        weight = 0
        mx = Min(W[0], m)
        for i in range(n - 1):
            weight += C[i]
            if m > weight:
                v = m - weight
                if v >= W[i + 1]:
                    mx = Max(mx, W[i + 1])
        print(mx)
        return

    ans = Min(W[0], m)
    m -= W[0]
    k -= 1

    for i in range(1, n):
        if k:
            if m - C[i - 1] >= 0:
                m -= C[i - 1]
                if m >= W[i]:
                    m -= W[i]
                    ans += W[i]
                    k -= 1
    
    print(ans)

if __name__ == "__main__":
    main()
