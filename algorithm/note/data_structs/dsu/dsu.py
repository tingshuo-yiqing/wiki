import sys

class DSU:
    def __init__(self, n) -> None:
        self._fa = list(range(n + 1))
        self._size = [1] * (n + 1)
        self._cc = n  # 连通块大小

    def find(self, x):
        root = x
        while root != self._fa[root]:
            root = self._fa[root]

        while x != root:
            temp = self._fa[x]
            self._fa[x] = root
            x = temp
        return root
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def merge(self, from_, to_):
        x, y = self.find(from_), self.find(to_)
        if x == y:
            return False
        
        if self._size[x] > self._size[y]: # 启发式合并
            x, y = y, x

        self._fa[x] = y # 将x挂到y上
        self._size[y] += self._size[x] # 合并大小
        self._cc -= 1  # 连通块大小减一
        return True
    
    def get_size(self, x):
        return self._size[self.find(x)]  # 当前节点所在集合的大小保存在根上
    
    def get_count(self):
        return self._cc

