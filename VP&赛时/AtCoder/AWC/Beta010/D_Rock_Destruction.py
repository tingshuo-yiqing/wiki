import sys

Min = lambda x, y: x if x < y else y
Max = lambda x, y: x if x > y else y

inp = lambda:sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

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
    n, k, q = MII()

    a = [0] + LII()

    dsu = DSU(n + 1)

    for i in range(1, n):
        if abs(a[i] - a[i + 1]) <= k:
            dsu.union(i, i + 1)

    outs = []
    for _ in range(q):
        x, y = MII()
        outs.append("Yes" if dsu.is_same(x, y) else "No")

    print('\n'.join(outs))


if __name__ == "__main__":
    main()
