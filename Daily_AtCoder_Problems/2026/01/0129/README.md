## [ C. Comma](https://atcoder.jp/contests/abc195/tasks/abc195_c)

按照 $(10^{3k},10^{3k + 3}-1)$ 对 $n$ 进行分段，将每段的结果累加即可，这里每次枚举到一段时要确定开始和结束的点。

```python
start = max(n, low)
end = min(m, high)
```

如何只有当合法的一段时才可以计算结果，即 `start >= end` 。

## [D. Xor Sum 2](https://atcoder.jp/contests/abc098/tasks/arc098_b)

根据异或是不进位的加法可推出，当且仅当每个数的二进制位上的 $1$ 都是不同的才满足 $\sum A_i= ⨁A_i$ 。

那么这就产生了单调性，可以使用滑动窗口解决。这就相当于窗口中的无重复的字符，一旦有重复就收缩窗口一样，当 $\sum A_i \not= ⨁A_i$ 出现时，肯定有一个元素在同一位上的 $1$ 重复了。

相当于求无重复字符的区间个数。