import sys

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())


def main():
    n, k = MII()

    a = sorted(LII())
    
    ans = 0
    l, r = 0, n - 1
    while l < r:
        t = a[l] + a[r]
        if t >= k:
            ans += r - l
            r -= 1
        elif t < k:
            l += 1

    print(ans)

if __name__ == "__main__":
    main()
    
