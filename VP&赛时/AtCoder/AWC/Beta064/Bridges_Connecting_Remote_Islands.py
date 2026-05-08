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
            return True
        return False

def main():
    n, m = MII()

    dsu = DSU(n)

    edges = []
    for _ in range(m):
        u, v, w = MII()
        edges.append((u, v, w))
    
    edges.sort(key=lambda x: x[2])

    cnt = 0
    ans = 0
    for u, v, w in edges:
        if dsu.union(u, v):
            cnt += 1
            ans += w
            if cnt == n - 1:
                print(ans)
                return

    print(-1 if n != 1 else 0)

if __name__ == "__main__":
    main()
