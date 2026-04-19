import sys
from math import log2

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
    s, t, k = MII()

    if t % s != 0:
        print(-1)
        return
    
    n = t // s
    if n & (n - 1) == 0:
        b = n.bit_length() - 1  #! 得到 log2(n)
        if b <= k:
            print(b)
            return

    print(-1)

if __name__ == "__main__":
    main()
