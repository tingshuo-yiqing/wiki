并查集是非常灵活和高效的数据结构，常见应用是维护无向图的连通分量个数、大小，最小生成树的 Kruskal 算法和最近公共祖先等。

并查集维护了若干个不相交的集合，每个集合通过一棵树来组织，根节点为该集合的代表。

三个基本操作：

1. `init(n)` ：初始化含有 $n$ 个集合的并查集，每个集合的代表为自身。
2. `find(x)` ：寻找元素 $x$ 所在集合的代表。
3. `union(x, y)` ：将元素 $x,y$ **所在的集合**合并，如果已经是处于同一集合的话就不合并。

一个简单的并查集示例，可以先看图理解，再理解代码结构。

<div align="center">
    <img src="https://img2024.cnblogs.com/blog/3769106/202603/3769106-20260304201820789-1091862260.jpg" style="width: 80%; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <div style="color: #999; padding: 10px; font-size: 14px;">并查集初始化、合并及查找图例</div>
</div>

图示的一个关键理解是：当 `fa[x] == x` 时，说明 `x` 是根节点。**很多题目按这个来找所有集合的代表**，比如将所有连通分量相连时，就可以按 `root1 - root2, root2 - root3 ···` 来将分量连起来

### 初始化

初始化代码

```python
def __init__(self, n):
    self.fa = list(range(n + 1))
```

### find函数

`find` 函数查找到元素所在集合的根，并且在查找过程中进行**路径压缩**（Path Compression）。

路径压缩目的是把树的高度压低，使得长链可以变成扁平的放射状，从而大大降低时间复杂度。

递归写法（直观、适合带权并查集写法）

```python
def find(self, x):
    if self.fa[x] == x:
        return x
    
    root = self.find(self.fa[x]) 
    self.fa[x] = root 
    return root
```

非递归写法（Python 推荐，避免栈溢出）

这里采用**路径减半**策略，效率高且代码简洁。

```python
def find(self, x):
    while self.fa[x] != x:
        
        self.fa[x] = self.fa[self.fa[x]]
        x = self.fa[x]
    return x
```

在查找时**当自身不是根时**往上跳，跳到根节点，然后再返回的过程中改变途径节点的父节点，统一改成根。

### 合并

合并的话先使用 `find` 函数找到对应的根，再链接即可。

```python
def union(self, x, y):
    rx = self.find(x)
    ry = self.find(y)
    if rx != ry:
        self.fa[rx] = ry  # 将 rx -> ry
```

这里也可以使用一个简单的启发式策略——按秩合并。维护一个 `size` 数组把小集合挂到大集合里去。

```python
def union(self, x, y):
    rx = self.find(x)
    ry = self.find(y)
    if rx != ry:
        self.fa[rx] = ry  # 将 rx -> ry
        if size[rx] > size[ry]:
            rx, ry = ry, rx
        self.fa[rx] = ry
        size[ry] += size[rx]
```

### 获取根数组

一个很重要的操作，利用前面提到的理解：当 `fa[x] == x` 时，说明 `x` 是根节点。获取所有集合的根。

```python
    def get_root(self):  
        return [x for x in range(1, len(self.fa)) if self.fa[x] == x]
```

### 模板

具体模板为

```python
class DSU:
    def __init__(self, n):
        self.fa = list(range(n + 1))
    
    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.fa[rx] = ry
    
    def is_same(self, x, y):  # 判断两元素是否在同一集合
        rx = self.find(x)
        ry = self.find(y)
        return rx == ry
    
    def get_root(self):  
        return [x for x in range(1, len(self.fa)) if self.fa[x] == x]
```

### 例题

