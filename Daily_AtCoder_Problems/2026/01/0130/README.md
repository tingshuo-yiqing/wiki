## [ D. Longest X](https://atcoder.jp/contests/abc229/tasks/abc229_d)

可以将区间内的 $k$ 个 `.` 替换为 `X` ，求最长的连续 `X` 。即维护一个 `.` 最多为 $k$ 的窗口，取其中出现的最大的那个。  

## [ D. Enough Array](https://atcoder.jp/contests/abc130/tasks/abc130_d)

考虑滑动窗口。因为数组元素全为正数，当前窗口符合要求时后面的也一定符合要求 $ans := n - r$ 。

每次窗口元素和大于等于 $k$ 时再收缩窗口。