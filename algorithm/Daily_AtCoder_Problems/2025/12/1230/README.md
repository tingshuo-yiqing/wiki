## [A. AtCoder Group Contest](https://atcoder.jp/contests/agc012/tasks/agc012_a)

要让小组实力的和尽可能的大，那必须尽量让越大的座位第二名。

逆序排序后取前 $n$ 组二元组的第二个元素的和即是最大。

## [B. Triangle (Easier)](https://atcoder.jp/contests/abc262/tasks/abc262_b)

顶点数很小， $3 \le M \le 100$ 使用邻接矩阵存图，再直接暴力枚举每一个可能的三角形。

```python
cnt = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if g[i][j] and g[j][k] and g[k][i]:
                cnt += 1
```

## [B. Coins](https://atcoder.jp/contests/abc087/tasks/abc087_b)

数据很小直接枚举每一种可能性，注意 $A=B=C=0$ 这种是不合法的，应该保证条件是： $A+B+C>0$ 。

## [C. Move Segment](https://atcoder.jp/contests/abc380/tasks/abc380_c)

将全由 $1$ 组成的子串为 $\text{Segment}$ 输出将第 $k$ 个和第 $k-1$ 个 $Segment$ 交换后的字符串。

先用双指针将每一段 $Segment$ 的起始和终止下标储存起来，再将第 $k$ 个和第 $k-1$ 个进行交换。

假设这两段的起始终止下标为 $a,b,c,d$ ，则有：

```python
s[:b] + s[c:d] + s[b:c] + s[d:]
```

