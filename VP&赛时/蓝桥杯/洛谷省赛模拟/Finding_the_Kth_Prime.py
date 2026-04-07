import sys
from array import array

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 0

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

    q = II()

    MAXN = 90000000

    is_prime = bytearray(b'\x01') * MAXN

    for i in range(2, int(MAXN**0.5) + 1):
        if is_prime[i]:
            # for j in range(i * i, MAXN, i):
            #     is_prime[j] = 0
            is_prime[i*i:MAXN:i] = b'\x00' * ((MAXN -1 - i*i)//i + 1)

    primes = array('I', (i for i in range(2, MAXN) if is_prime[i]))

    outs = []
    for _ in range(q):
        k = II()
        outs.append(str(primes[k-1]))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
