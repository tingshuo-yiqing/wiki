import sys
from array import array
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return is_prime
is_prime = sieve(10 ** 7 + 1)

def main():
    outs = []
    for _ in range(II()):
        n = II()

        ans = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                ans += n // i
        outs.append(ans)
        
    print(*outs, sep='\n')
if __name__ == "__main__":
    main()