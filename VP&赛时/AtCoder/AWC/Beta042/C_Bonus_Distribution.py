import sys
from math import gcd, prod

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

MOD = 998244353

def main():
    n, M = MII()

    P = LII()
    W = LII()

    S = sum(P) % MOD
    A = sum(W) % MOD

    T = 1
    for x in P:
        T = T * x * pow(S, -1, MOD) % MOD 

    R = pow(A, n, MOD) * T % MOD

    print(R % MOD)

if __name__ == "__main__":
    main()
