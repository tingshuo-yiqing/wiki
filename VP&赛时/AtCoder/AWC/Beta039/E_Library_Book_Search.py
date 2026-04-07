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
            i += i &-i
    
    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def query(self, l, r):
        return self.pf(r) - self.pf(l - 1)

def main():
    n, m, q, k = MII()

    bit = BIT(n)

    books = []
    for _ in range(m):
        S, D = MII()
        books.append((D, S))
    
    books.sort(reverse=True)

    querys = []
    for i in range(q):
        l, r, T = MII()
        querys.append((T, l, r, i))
    
    querys.sort(reverse=True)

    ans = [0] * q

    idx = 0
    for T, l, r, i in querys:
        while idx < m and books[idx][0] >= T:
            bit.add(books[idx][1], 1) 
            idx += 1

        ans[i] = Max(bit.query(l, r) - k, 0)
    
    print(*ans , sep='\n')

if __name__ == "__main__":
    main()
