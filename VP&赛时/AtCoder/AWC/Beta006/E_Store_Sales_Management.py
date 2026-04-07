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
        self.tree = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def update(self, i, val):
        cur = self.pf(i) - self.pf(i-1)
        detal = val - cur
        self.add(i, detal)
    
    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def query(self, l, r):
        return self.pf(r) - self.pf(l - 1)
    
def main():
    n, q = MII()
    a = LII()

    bit = BIT(n)
    for i, x in enumerate(a):
        bit.add(i + 1, x)
    
    outs = []
    for _ in range(q):
        op, x, y = MII()

        if op == 1:
            outs.append(str(bit.query(x, y)))
        else:
            bit.update(x, y)
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
