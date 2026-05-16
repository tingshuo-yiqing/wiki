树状数组（Binary Indexed Tree, BIT，也称 Fenwick Tree）是算法竞赛中极其常用的数据结构。它的核心优势在于：**代码短小精悍、常数极小、内存占用少**。

虽然它的功能是线段树的子集，但在处理“动态前缀和”相关问题时，BIT 通常是首选。

<div align="center">
    <img src="https://img2024.cnblogs.com/blog/3769106/202602/3769106-20260223230845974-1278954480.png" style="width: 80%; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <div style="color: #999; padding: 10px; font-size: 14px;">来自董晓算法，对两个关键函数原理的图解</div>
</div>

BIT 结构模板为

```python
class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1) # 初始化为一颗空树
    
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i
    
    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def query(self, l, r): # 查询区间为 [l, r]
        return self.pf(r) - self.pf(l - 1)
```

**已知大小为 $n$ 的数组**，有两种初始化方式一种为 $O(n\log n)$ 一种为 $O(n)$ 。

前者只需要调用 $n$ 次 `add` 函数即可，具体为

```python
bit = BIT(n)
for i, x in enumerate(a):
    bit.add(i + 1, x)  # 注意这里应该要 1-based 初始化
```

后者的话在初始化时传入的是数组而不是数组大小，具体为

```python
def __init__(self, arr):  # 传入数组
    n = len(arr)
    self.tree = [0] + arr[:]  # 列表加法可能会炸内存
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            self.tree[j] += self.tree[i]
```

[P3374 【模板】树状数组 1](https://www.luogu.com.cn/problem/P3374) 点修区查

[P3368 【模板】树状数组 2](https://www.luogu.com.cn/problem/P3368) 区修点查

这是树状数组最基本的演变形式，其它功能主要通过**差分思想**实现切换。比如可以使用一颗**空树状数组当作差分数组**，区修就变成了对这可空树进行两次点修，点查就变成了**原始值加修改值**了，即 `a[i] + sum(i)` 。

**树状数组（BIT）本质上是一个维护“增量”或“前缀和”的辅助结构，它本身并不直接存储原数组的当前值。**
