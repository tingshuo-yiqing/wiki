## [Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c)

考察**带循环移位的区间和查询**，不能真正的移动数组。

### 断环成链

因为移动 $n$ 次后会变回原数组，所以我们只需要将数组**复制一份放在后面**就可以**涵盖所有移位的情况**。

记录移位的次数 $off$ （要对 $n$ 取模），然后预处理 $2\times n$ 数组的前缀和，只要对查询下标偏移 $off$ 次，就可以映射到轮转后的数组上，且相对位置没有变化，查询出来的和也是相同的。

先预处理前缀和。

```python
a = a + a
pf = [0] * (2 * n + 1)
for i in range(2 * n):
    pf[i + 1] = pf[i] + a[i]
```

确定逻辑起点后查询。

```python
if op == 1:
    off = (off + o[1]) % n
else:
    l, r = o[1], o[2]
    outs.append(pf[r + off] - pf[l + off - 1])
```

### 分段回绕法

同样需要记录逻辑起点，但是这种方法取模后可能会出现起点比终点大的情况，需要分类讨论。

而且这里起点与终点必须要使用 **0-based** 。

```python
if op == 1:
    off = (off + o[1]) % n
else:
    l, r = o[1], o[2] 
    l = (l + off - 1) % n # 必须转化为 0-based
    r = (r + off - 1) % n

    if l <= r:
        outs.append(pf[r + 1] - pf[l])
    else:
        outs.append(pf[n] - pf[l] + pf[r + 1])
```

这个方法只需要 $O(N)$ 的空间，因为我们判断了 $l\le r$ 的情况。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

两种情况理论上是一样的，只不过前者使用额外的空间涵盖了所有轮转后的情况不逊要判断 $l\le r$ 的情况而已。