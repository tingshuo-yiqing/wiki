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

class DSU:
    def __init__(self, n):
        self.n = n
        self.fa = list(range(n + 1))
        self.sz = [0] * (n + 1)

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.fa[rx] = ry
    
    def add(self, i, val):
        self.sz[i] += val

    def up(self, x, val):
        r = self.find(x)
        for i in range(1, self.n + 1):
            if self.find(i) == r:
                self.sz[i] += val
    
    def query(self, i):
        return self.sz[i]

def main():
    n, q = MII()

    dsu = DSU(n)

    outs = []
    for _ in range(q):
        o = LII()
        op = o[0]

        if op == 1:
            dsu.union(o[1], o[2])
        elif op == 2:
            dsu.add(o[1], o[2])
        elif op == 3:
            dsu.up(o[1], o[2])
        else:
            outs.append(str(dsu.query(o[1])))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
