import sys
from bisect import bisect_right
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MAXN = 2 * 10 ** 6 + 10

def sieve_prime(n):
    is_primes = [False] * 2 + [True] * (n - 2)

    for i in range(2, int(n ** 0.5) + 1):
        if is_primes[i]:
            is_primes[i*i:n+1:i] = [False] * len(is_primes[i*i:n+1:i])
    
    return [i for i, p in enumerate(is_primes) if p]

def main():
    n = int(input())

    p = sieve_prime(MAXN)

    cnt1 = 0
    for i in range(15):
        if p[i] ** 8 > n:
            break
        else:
            cnt1 += 1

    i = 0
    ans = 0
    while p[i] ** 4 < n:
        t = p[i] ** 2
        j = i + 1
        while t * p[j] ** 2 <= n:
            j += 1
        # 二分
        ans += (j - i - 1)
        i += 1
    
    print(ans + cnt1)

if __name__ == "__main__":
    main()