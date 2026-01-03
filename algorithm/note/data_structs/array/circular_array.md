## 数组移动

### 逻辑起点off

#### 1.计算逻辑起点

逻辑起点是对标物理数组的索引 `0` 的，所以要查询原数组的信息必须对标 `off` 。

``` python
off = (off + x) % n  # 左移
```

在 C++ 或 Java 中，`(-1) % n` 可能会得到  `-1` ，所以你必须写成 `(off - 1 + n) % n` 。但在 **Python** 中，% 运算符会保证结果与除数（n）符号一致。直接写

```python
off = (off - x) % n # 右移
off = (off - x % n + n) % n  # C/C++/Java
```

#### 2.下标映射

无论是左移还是右移，下标映射都是: 

```python
new_i = (i + off - 1) % n  # 减1是为了转成 0-based
```

### 双端队列

双端队列 `deque` 右一个接口为 `rotate` 可以在 $O(1)$ 的情况下进行数组移位。

```python
from collections import deque

d = deque([3, 1, 4, 1, 5])
d.rotate(1)  # 向右循环移动 1 位，O(1) 复杂度
d.rotate(-1) # 向左循环移动 1 位，O(1) 复杂度
```

随机访问是 $O(k)$ 的，但是一般情况下是够用的。

### 例题：

* ABC 199-C IPFL
* ABC 189-E Rotate and Flip
* ABC 410-C Rotatable Array
* [ABC 425-C Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c)
* [典型90: 044 - Shift and Swapping (★3)](https://atcoder.jp/contests/typical90/tasks/typical90_ar)

