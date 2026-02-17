import sys

if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

class DSU:
    def __init__(self, n) -> None:
        self._fa = list(range(n + 1))  # 默认节点是[1, n]
        self._size = [1] * (n + 1)
        self._cc = n  # 连通块大小
    
    def find(self, x):
        # 迭代版路径压缩
        root = x
        while self._fa[root] != root:
            root = self._fa[root]
        
        curr = x
        while self._fa[curr] != root:
            next_node = self._fa[curr]
            self._fa[curr] = root
            curr = next_node
        return root
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def merge(self, from_, to_):
        x, y = self.find(from_), self.find(to_)
        if x == y:
            return False
        self._fa[x] = y # 将x挂到y上
        self._size[y] += self._size[x] # 合并大小
        self._cc -= 1  # 连通块大小减一
        return True
    
    def get_size(self, x):
        return self._size[self.find(x)]  # 当前节点所在集合的大小保存在根上
    
    def get_count(self):  # 返回连通块数量
        return self._cc

def main():
    n, m = MII()

    a = LII()
    mi = min(a)
    idx = a.index(mi) + 1

    edges = []
    for _ in range(m):
        u, v, w = MII()
        edges.append((u, v, w))
    
    for v in range(n):
        if v == idx - 1:
            continue
        edges.append((idx, v + 1, mi + a[v]))

    dsu = DSU(n)
    edges.sort(key=lambda x: x[2])

    ans = cnt = 0
    for edge in edges:
        u, v, w = edge
        if cnt == n - 1:
            break
        if not dsu.is_same(u, v):
            dsu.merge(u, v)
            ans += w
            cnt += 1
    
    print(ans)

if __name__ == "__main__":
    main()