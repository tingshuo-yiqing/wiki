import sys
from array import array
from math import log1p

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
    x = 93000000
    print(x / log1p(x))

    arr = array('I', [0, 1, 2, 3, 4])
    b = array('I', [1]) * 5

    print(*arr)
    # print(arr[4])
    print(*b)

    is_primes = bytearray(5)

    print(*is_primes)

if __name__ == "__main__":
    main()
