### 数组移动

#### 逻辑起点off

逻辑起点是对标物理数组的索引`0`的，所以要查询原数组的信息必须对标`off`。

[C - Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c) ，数组位移与前缀和结合

```python
if op[0] == 1:
    off = (off + op[1]) % n
else:
    l = (op[1] - 1 + off) % n   
    r = (op[2] - 1 + off) % n
    if l <= r:  
        outs.append(pre[r + 1] - pre[l])  # 常规中间[l, r]
    else:
        outs.append(pre[r + 1] + pre[n] - pre[l])  # 被断成2段，[0, r] + [l, n - 1]
```

`l`和`r`就是对标`off`的例子，逻辑数组中的$[l,r]$对应物理数组中的$[(l + off)\mod{n},(r + off)\mod{n}]$，因为我们依靠物理数组的信息进行映射到逻辑数组

#### 左移

[C - Rotatable Array](https://atcoder.jp/contests/abc410/tasks/abc410_c)，所有元素向左边挤，挤掉的一次放在右边

``` python
idx = (idx + off) % n
```

#### 右移

所有元素向右边挤，挤掉的一次放在左边

```python
(i - off % n + n) % n
```

