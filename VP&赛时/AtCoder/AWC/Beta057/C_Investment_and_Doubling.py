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
    mx = max(a) % MOD

    mxi = a.index(mx)

    ans = mx * pow(2, k, MOD) % MOD
    for i in range(n):
        if i == mxi:
            continue
        else:
            ans += a[i]
    
    print(ans % MOD)

if __name__ == "__main__":
    main()
