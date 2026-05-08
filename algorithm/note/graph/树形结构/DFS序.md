

DFS序有两种：

* 入栈序：只记录节点第一次被访问的时间戳。
* 欧拉序：进出各计一次。

入栈序是最常用的，其核心性质是：**节点的子树在入栈序中是连续的一段**。所以子树的维护问题可以转化为区间维护。

设置一下变量：

* 子树大小：`sz`
* 第一次被访问的时间戳：`tin`
* 离开的时间戳：`tout`
* 先序序列：`seq`

### 递归求DFS序的模版

```python
timer = 0
sz = [0] * (n + 1)
tin = [0] * (n + 1)
tout = [0] * (n + 1)
seq = []

def dfs(u, fa=-1):
    nonlocal timer
    timer += 1
    tin[u] = timer
    seq.append(u)

    sz[u] = 1
    for v in g[u]:
        if v != fa:
            dfs(v, u)
            sz[u] += sz[v]
    tout[u] = timer 

dfs(1)
```

### 迭代求DFS序的模版

```python
timer = 0
tin = [0] * (n + 1)
tout = [0] * (n + 1)
seq = []

st = [(-1, k, 0)]
while st:
    fa, u, state = st.pop()
    if state == 0:
        timer += 1
        tin[u] = timer
        seq.append(u)
        st.append((fa, u, 1))
        for v in g[u][::-1]:
            if v != fa:
                st.append((u, v, 0))
    else:
        tout[u] = timer
```

### 性质

1. **前序DFS序具有子树连续性**：节点 `u` （包括 `u` ）在先序中的一段连续的序列为 `[tin[u], tout[u]]` 在先序序列 `seq` 中也可以表示为 `seq[tin[u], tin[u] + sz[u] - 1]` 。



### 应用

#### 子树修改与查询

配合树状数组与线段树。通常将**带权树的权值映射到前序序列**。

```python
# w 为权值数组

bit = BIT(n)
for i, x in enumerate([tin[node - 1] for node in seq], start=1):
    bit.add(i, x)
 
seg = SegmentTree([tin[node - 1] for node in seq])
```

