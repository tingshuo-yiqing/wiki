**ST表**（Sparse Table），也叫稀疏表

主要解决**静态RMQ问题**（区间最小、最大值）及其延伸。主要应用**倍增思想**，可以实现$O(nlogn)$预处理和$O(1)$的查询

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



### 1.预处理ST表



<img src="https://cdn.jsdelivr.net/gh/tingshuo-yiqing/PicGo-tuchuang/img/20250829165329231.png" style="zoom:40%;" />

  ### 2.处理查询

对查询区间进行分割拼凑，区间指数为：
$$
k=\left\lfloor log_2(r - l + 1)\right\rfloor
$$



<img src="https://cdn.jsdelivr.net/gh/tingshuo-yiqing/PicGo-tuchuang/img/20250829165252694.png" style="zoom:50%;" />

