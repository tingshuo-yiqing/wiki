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

    MOD = 10 ** 9 + 7
    l = ans = 0
    s = 1
    for r, x in enumerate(a):
        s = s * x % MOD

        if r - l + 1 < k:  # 窗口没有到达k
            continue

        ans = (ans + s) % MOD

        s *= pow(a[l], -1, MOD)
        l += 1
    
    print(ans % MOD)

if __name__ == "__main__":
    main()
