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
    n, k, G = MII()

    a = []
    for _ in range(n):
        _, t = MII()
        a.append(t)

    ans = 0

    l = s = 0
    for r, x in enumerate(a):
        s += x

        if r - l + 1 < k:
            continue

        ans = Max(s, ans)
        s -= a[l]
        l += 1
    
    print(sum(a) - ans + G)

if __name__ == "__main__":
    main()
