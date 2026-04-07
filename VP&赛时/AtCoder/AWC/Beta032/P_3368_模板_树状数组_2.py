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
    
    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

def main():
    n, q = MII()

    a = LII()

    bit = BIT(n)

    for _ in range(q):
        o = LII()

        op = o[0]
        if op == 1:
            l, r, v = o[1:]
            bit.add(l, v)
            bit.add(r + 1, -v)
        else:
            i = o[1]
            print(a[i-1] + bit.pf(i))

if __name__ == "__main__":
    main()
