## [C. March](https://atcoder.jp/contests/abc089/tasks/abc089_c)

考察枚举，使用一个桶统计所有符合要求的字母的频率，再三层循环枚举实现选 $3$ 个人。

具体代码为: 

```python
char = ['M', 'A', 'R', 'C', 'H']
ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += cnt[char[i]] * cnt[char[j]] * cnt[char[k]]
```

## [C. ORXOR](https://atcoder.jp/contests/abc197/tasks/abc197_c)

### 数据范围

- $1≤N≤20$
- $0≤A_i<2^{30}$

考察枚举，数组 $n$ 个元素 $n-1$ 个间隔，每个间隔分与不分根据乘法原理一共有 $2^{n-1}$ 种分割方法。这时候就可以二进制枚举每一个分割位置来分割数组。

**枚举思路**:

1. 枚举分割位置 $i$ 从 $0$ 到 $2^{n-1} - 1$
2. 枚举 $j$ 从 $0$ 到 $n$ , $i$ 的第 $j$ 位如果是 $1$ 就分割 $a_j$ 和 $a_{j+1}$ 。注意最后一段不要忘记了，当 $j = n-1$ 手动分割

关键代码为: 

```python
for i in range(1 << (n - 1)):
    xo = xor = 0  #  0和任何数位与、异或都为自身
    for j in range(n):
        xo |= nums[j]
        if (j < n - 1 and i >> j & 1) or j == n - 1:
            xor ^= xo
            xo = 0
 
```

