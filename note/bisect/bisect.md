[AWC Beta0035B](https://atcoder.jp/contests/awc0035/tasks/awc0035_b) 

当你用 `i = bisect_left(b, x)` 得到下标后，会有三种情况：

1. **i == 0**：说明 `x` 比列表里所有数都小，最接近的就是第一个数 `b[0]`。
2. **i == len(b)**：说明 `x` 比列表里所有数都大，最接近的就是最后一个数 `b[-1]`。
3. **在中间**：此时 `x` 处于 `b[i-1]` 和 `b[i]` 之间。你需要对比这两个数，看谁离 `x` 更近。

模板代码：

```python
def main():
    n, m = MII()

    a = sorted(LII())
    b = sorted(LII())

    ans = 0
    for x in a:
        i = bisect_left(b, x)

        mi = b[0]
        if i == m:
            mi = b[-1]
        elif 0 < i < m:
            t1 = abs(b[i] - x)
            t2 = abs(b[i-1] - x)
            mi = b[i] if t1 < t2 else b[i-1]

        ans += abs(mi - x)

    print(ans)
```

[CF 702C](https://codeforces.com/problemset/problem/702/C)

[T90-007](https://atcoder.jp/contests/typical90/tasks/typical90_g)