import sys
from math import inf, log
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def getk(n):
    k = 0
    b = bin(n)[2:]
    for i in range(len(b)):
        if b[i] == '1':
            k = len(b) - i
            break
    return k

def main():
    for _ in range(II()):
        n, q = MII()

        # levels = getk(n)
        levels = n.bit_length()

        # print(levels)
        outs = []
        for _ in range(q):
            nums = II()
            # k = getk(nums) - 1
            k = nums.bit_length() - 1
            
            if k != levels - 1:
                outs.append(1 << k)
            else:
                outs.append(n - (1 << k) + 1)
        
        print(*outs, sep='\n')
             

if __name__ == "__main__":
    main()