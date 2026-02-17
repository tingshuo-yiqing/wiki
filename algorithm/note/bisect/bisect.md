## 模版



## 应用

### 1.寻找最接近的数

当你用 `idx = bisect_left(arr, target)` 得到下标后，会有三种情况：

1. **idx == 0**：说明 target 比列表里所有数都小，最接近的就是第一个数 arr[0]。
2. **idx == len(arr)**：说明 target 比列表里所有数都大，最接近的就是最后一个数 arr[-1]。
3. **在中间**：此时 target 处于 arr[idx-1] 和 arr[idx] 之间。你需要对比这两个数，看谁离 target 更近。

模板代码：

```python
for x in a:
    i = bisect_right(b, x)

    nums = b[0]  # 默认为i == 0的情况
    if i == m:
        nums = b[-1]
    elif 0 < i < m:
        j, k = abs(b[i] - x), abs(b[i-1] - x)
        nums = b[i] if j <= k else b[i-1]
    ans = max(ans, abs(nums-x))
```



**例题：**

* [CF 702C](https://codeforces.com/problemset/problem/702/C)
* [T90-007](https://atcoder.jp/contests/typical90/tasks/typical90_g)