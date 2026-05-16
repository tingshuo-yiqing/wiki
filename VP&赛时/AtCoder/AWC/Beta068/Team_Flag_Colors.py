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
        """合并之后直接返回当前的根"""
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.fa[rx] = ry
            return ry
        return rx

def main():
    n, m = MII()

    dsu = DSU(n)

    C = [-1] * (n + 1)

    for _ in range(m):
        u, v, w = MII()
        r = dsu.union(u, v)
        C[r] = w
    
    s = set()
    for i in range(1, n + 1):
        if i == dsu.fa[i] and C[i] != -1:
            s.add(C[i])
    
    print(len(s))

if __name__ == "__main__":
    main()
