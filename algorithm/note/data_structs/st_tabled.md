**ST表**（Sparse Table），也叫稀疏表

主要解决RMQ问题（区间最小、最大值）及其延伸。主要应用**倍增思想**，可以实现$O(nlogn)$预处理和$O(1)$的查询

ST表要求操作满足**等幂性**：
$$
f(x,x) = x
$$
这些操作要求：两个小区间的重叠不影响大区间的结果

常见的有：

- `min(x, y)`
- `max(x, y)`
- `gcd(x, y)`
- `and/or`

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;cin >> x;
    cout << __gcd(x, x) << '\n';
    cout << min(x, x) << '\n';
    cout << max(x, x) << '\n';
    cout << (x | x) << '\n';
    cout << (x & x) << '\n';
    return 0;
}
```

```
输入：
5
输出：
5
5
5
5
5
```

[gcd区间](https://www.luogu.com.cn/problem/P1890)、[ST表模板](https://www.luogu.com.cn/problem/P3865)

### 1.预处理ST表

使用倍增递推：用两个小区间拼凑成一个大区间

定义状态`st[i][j]`为以第`i`哥数为起点，长度为`j`的区间中的最值（或其它的性质，比如`gcd`、`|`、`&`）

递推式：
$$
st[i][k] = max(st[i][k-1],st[i+2^{k-1}][k-1])
$$

```cpp
for (int i = 1; i <= n; ++i) cin >> st[i][0];  // 初始化

for (int k = 1; k < m; ++k) {
    for (int i = 1; i + (1 << k) - 1 <= n; ++i) {
        // 因为 st[i][k] 覆盖区间长度是2^k，所以i + (1<<k) - 1不能超过 n。
        st[i][k] = max(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);
    }
}
```

<img src="https://cdn.jsdelivr.net/gh/tingshuo-yiqing/PicGo-tuchuang/img/20250829165329231.png" style="zoom:40%;" />

  ### 2.处理查询

对查询区间进行分割拼凑，区间指数为：
$$
k=\left\lfloor log_2(r - l + 1)\right\rfloor
$$

```cpp
int k = log2(r - l + 1);
cout << max(st[l][k], st[r - (1 << k) + 1][k]) << '\n';
```

<img src="https://cdn.jsdelivr.net/gh/tingshuo-yiqing/PicGo-tuchuang/img/20250829165252694.png" style="zoom:50%;" />

两个子区间将查询区间覆盖