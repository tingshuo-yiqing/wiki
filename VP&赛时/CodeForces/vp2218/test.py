from math import gcd

MAXN = 10 ** 6

is_prime = [False] * 2 + [True] * (MAXN - 2)

for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

primes = [i for i, x in enumerate(is_prime) if x]

res = []
for i in range(10):
    res.append(primes[i] * primes[i + 1])
print(*res)

for i in range(10-1):
    print(gcd(res[i], res[i + 1]), end=' ')