import sys

input_data = sys.stdin.read().split()
it = iter(input_data)

II = lambda: int(next(it))

def main():
    MAXN = 10 ** 7 + 1

    is_prime = [1] * MAXN
    spf = [0] * MAXN

    primes = [0] * MAXN     
    pcnt = 0                # 当前质数个数

    for i in range(2, MAXN):
        if is_prime[i]:
            primes[pcnt] = i
            pcnt += 1
            spf[i] = i

        j = 0
        while j < pcnt:
            p = primes[j]
            if p * i >= MAXN:
                break

            is_prime[p * i] = 0
            spf[p * i] = p

            if i % p == 0:
                break
            j += 1

    a = [0] * MAXN
    for i in range(2, MAXN):
        a[i] = a[i - 1] + spf[i]

    t = II()
    res = []
    for _ in range(t):
        n = II()
        res.append(str(a[n]))

    sys.stdout.write('\n'.join(res))

if __name__ == "__main__":
    main()