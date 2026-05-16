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
    n, q = MII()

    Books = []
    for i in range(n):
        a, b, c = MII()
        Books.append((b, i + 1, a * c))
    
    Queries = []
    for i in range(q):
        l, r, T = MII()
        Queries.append((T, l, r, i))
    
    Books.sort()
    Queries.sort()

    bit = BIT(n)

    outs = [0] * q
    p = 0

    for T, l, r, i in Queries:
        while p < n and Books[p][0] <= T:
            _, pos, v = Books[p]
            bit.add(pos, v)
            p += 1
        outs[i] = bit.pf(r) - bit.pf(l - 1)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
