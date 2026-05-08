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

class BIT:
    def __init__(self, n):
        self.tr = [0] * (n + 1)
    
    def add(self, i, val):
        while i < len(self.tr):
            self.tr[i] += val
            i += i & -i
    
    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tr[i]
            i -= i & -i
        return s

def main():
    n, m = MII()
    q = LII()

    bit = BIT(n)
    for i in range(1, n + 1):
        bit.add(i + 1, 1)
    
    for x in q:
        print(bit.pf(x) + 1)
        bit.add(x, -1)

if __name__ == "__main__":
    main()
