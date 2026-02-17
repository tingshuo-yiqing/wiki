## 结构

### 模板

```python
class DSU:
    def __init__(self, n) -> None:
        self._fa = list(range(n + 1))  # 默认节点是[1, n]
        self._size = [1] * (n + 1)
        self._cc = n  # 连通块大小
    
    def find(self, x):
        root = x
        while root != self._fa[root]:
            root = self._fa[root]

        # 路径压缩
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
        self._fa[x] = y # 将x挂到y上
        self._size[y] += self._size[x] # 合并大小
        self._cc -= 1  # 连通块大小减一
        return True
    
    def get_size(self, x):
        return self._size[self.find(x)]  # 当前节点所在集合的大小保存在根上
    
    def get_count(self):  # 返回连通块数量
        return self._cc
```

[并查集](https://www.nowcoder.com/practice/513111e4477c4fad8f19f14d4cdf49dc?tpId=388&tqId=11077218&channelPut=tracker1)，需要**启发式合并**或**按秩合并**不然会递归过深，不优化合并的话迭代路径压缩也可以过

### 查找

`2`种常见**路径压缩**方式：递归和迭代。

#### 递归

如果不优化合并的话容易，容易达到递归最大深度(python)

```python
def find(self, x):
    fa = self._fa
    if fa[x] != x:
        fa[x] = self.find(fa[x])
    return fa[x]
```

#### 迭代

```python
def find(self, x):
    root = x
    while root != self._fa[root]:
        root = self._fa[root]

    # 路径压缩
    while x != root:
        temp = self._fa[x]
        self._fa[x] = root
        x = temp
    return root
```

### 合并

`2`种常见的合并方式：启发式和按秩

#### 启发式合并

```python
if self._size[x] > self._size[y]: # 小挂大即可
    x, y = y, x
```

#### 按秩合并

```python

```

## 应用

### 0.标记信息

[E. Reach](https://atcoder.jp/contests/abc420/tasks/abc420_e)

### 1.最小生成树（Kruskal算法）

将所有边按边权排序，然后边加边边判断连通性。

[修复公路](https://www.nowcoder.com/practice/8111efc8c04d472da349b6e5010e1951?tpId=388&tqId=11294690&channelPut=tracker1)，注意这里是可以同时修复的，去最大时间即可

### 2.检测无向图种的环

[C. Cycle ](https://atcoder.jp/contests/abc404/tasks/abc404_c)，根据连通分量和度数判断是否是单环


