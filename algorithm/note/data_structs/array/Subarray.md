子数组问题一般与双指针、滑动窗口、前缀和有关。这里列举一些常见的题型。

### 和为k的子数组个数I

当数组元素全部为正数时区间和具有单调性，可以直接使用滑动窗口。

```python
l = 0
ans = w = 0
for r in range(n):
    w += a[r]
    while w > k:
        w -= a[l]
        l += 1
    if w == k:
        ans += 1
```



* [Subarray Sums I](https://cses.fi/problemset/task/1660)

***

### 和为k的子数组个数II

当数组有正也有负时就不可以直接滑动窗口了，因为次数区间和不具有单调性。使用哈希表维护已经存在的前缀和，解法同两数之和一样，边枚举边查找。

```python
idx = defaultdict(int)
idx[0] = 1  

ans = cur = 0
for x in a:
    cur += x
    ans += idx[cur - k]
    idx[cur] += 1
```



* [Subarray Sums II](https://cses.fi/problemset/task/1661)
* [ABC 233-D Count Interval](https://atcoder.jp/contests/abc233/tasks/abc233_d)

***

### 和为k的倍数的子数组

我们要找的是满足以下条件的 $(l,r)$ :


$$
(S_r-S_{l-1})\equiv 0\pmod{K}
$$


等价于: 


$$
S_l\equiv S_{l-1} \pmod{K}
$$


此时哈希表维护的是每次前缀和对 $K$ 的余数了。原理同样与两数之和一样，边枚举边查找。

```python
idx = defaultdict(int)
idx[0] = 1

ans = cur = 0
for x in a:
    cur += x
    ans += idx[cur % k]
    idx[cur % k] += 1
```



* [P8649 K倍区间](https://www.luogu.com.cn/problem/P8649)
* [ABC 105-D Candy Distribution](https://atcoder.jp/contests/abc105/tasks/abc105_d)

***
