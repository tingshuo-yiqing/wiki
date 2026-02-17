import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

class DSU:
    def __init__(self, n) -> None:
        self._fa = list(range(n + 1))  
        self._size = [1] * (n + 1)
        self._cc = n  
    
    def find(self, x):
        fa = self._fa
        if fa[x] != x:
            fa[x] = self.find(fa[x])
        return fa[x]
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def merge(self, from_, to_):
        x, y = self.find(from_), self.find(to_)
        if x == y:
            return False
        self._fa[x] = y 
        self._size[y] += self._size[x] 
        self._cc -= 1  
        return True
    
    def get_size(self, x):
        return self._size[self.find(x)]  
    
    def get_count(self): 
        return self._cc

def main():
    n, m = MII()
    a = LII()

    edges = [list(MII()) for _ in range(m)]



if __name__ == "__main__":
    main()