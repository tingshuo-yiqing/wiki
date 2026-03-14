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
        self.fa = list(range(n + 1))

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.fa[rx] = ry

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    n, m = MII()

    deg = [0] * (n + 1)

    dsu = DSU(n)

    for _ in range(m):
        u, v = MII()
        deg[u] += 1        
        deg[v] += 1        
        dsu.union(u, v)

    for i in range(1, n + 1):
        if not dsu.is_same(1, i) or deg[i] != 2:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()
