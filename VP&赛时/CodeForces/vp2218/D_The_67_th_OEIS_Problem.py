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

MAXN = 10 ** 6

is_prime = [False] * 2 + [True] * (MAXN - 2)

for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

primes = [i for i, x in enumerate(is_prime) if x]

def main():
    for _ in range(II()):
        n = II()

        res = []
        for i in range(n):
            res.append(primes[i] * primes[i + 1])

        print(*res)

if __name__ == "__main__":
    main()
