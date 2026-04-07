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
    n, m = MII()

    MOD = 998244353

    A = LII()
    B = LII()

    pfA = [0] * (n + 1)
    for i in range(n):
        pfA[i + 1] = (pfA[i] + A[i]) % MOD

    Ai = 0
    for i in range(1, n + 1):
        Ai = (Ai + A[i-1] * i) % MOD 

    ans = 0
    for j in range(1, m + 1):
        s = 0
        for k in range(1, n // j + 1):
            l = j * k
            r = Min(n, (k + 1) * j - 1)
            s = (s + (pfA[r] - pfA[l-1]) * k) % MOD
        ans = (ans + B[j-1] * (Ai - s * j)) % MOD
    print(ans % MOD)

if __name__ == "__main__":
    main()
