import sys
from collections import defaultdict

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

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.fa[rx] = ry
            return True
        return False
    
    def get_fa(self):
        return [i for i in range(1, self.n + 1) if self.find(i) == i]

def main():
    n = II()

    a = LII()

    dsu = DSU(n)

    nxt = [0] * (n + 1)
    for v, u in enumerate(a, start=1):
        nxt[v] = u
        dsu.union(v, u)

    fa = dsu.get_fa()

    sz = [0] * (n + 1)

    def get_k(start):
        pos = start
        vised = defaultdict(int)
        step = 0

        while pos not in vised:
            vised[pos] = step
            pos = nxt[pos]
            step += 1

        return step - vised[pos]

    for x in fa:
        sz[x] = get_k(x)

    for i in range(1, n + 1):
        sz[i] = sz[dsu.find(i)]

    print(*sz[1:])

if __name__ == "__main__":
    main()
