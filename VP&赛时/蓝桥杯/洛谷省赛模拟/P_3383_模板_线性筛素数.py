import sys
from array import array

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
    MAXN, q = MII()

    #! 关键空间优化
    is_prime = bytearray([1]) * MAXN
    primes = array('I', [0]) * MAXN
    pcnt = 0

    for i in range(2, MAXN):
        if is_prime[i]:
            primes[pcnt] = i
            pcnt += 1
        
        j = 0
        while j < pcnt:
            p = primes[j]
            if p * i > MAXN-1:
                break

            is_prime[p * i] = 0

            if i % p == 0:
                break
            j += 1
    
    outs = []
    for _ in range(q):
        x = II()
        outs.append(str(primes[x - 1]))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
