import sys
from math import comb

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
    n, m = MII()

    MOD = 10 ** 9 + 7

    k = n - m + 1

    if m > k:
        print(0)
        return

    f = [1] * (n + 1)
    for i in range(2, n + 1):
        f[i] = i * f[i - 1] % MOD
    
    invf = [1] * (n + 1)
    invf[n] = pow(f[n], -1, MOD)
    for i in range(n-1, -1, -1):
        invf[i] = (i + 1) * invf[i + 1] % MOD
    
    # print(f[k] * invf[m] * invf[k - m] % MOD)
    print(f[k] * pow(f[m], -1, MOD) * pow(f[k - m], -1, MOD) % MOD)

if __name__ == "__main__":
    main()
