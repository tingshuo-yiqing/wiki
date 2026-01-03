## [038. Large LCM（★3）](https://atcoder.jp/contests/typical90/tasks/typical90_al)

考察大数处理，Python的话没有这个顾虑直接模拟就可以了，但是C/C++的话必须**先乘后除**防止溢出，既然涉及到除法就得保证分母不为 $0$。具体为: 

```cpp
// a * b / __gcd(a, b) > inf 变为两个除法的比较
if (b / __gcd(a, b) > inf / a)
    cout << "Large" << '\n';
else
    cout << a / __gcd(a, b) * b << '\n';   // 能到达这里说明是安全的
```

## [044. Shift and Swapping（★3）](https://atcoder.jp/contests/typical90/tasks/typical90_ar)

考察数组移位，使用一个变量记录偏移量 $off$ ，偏移数组的各种操作都是相对于这个逻辑起点来的，比如这里的交换。

1. 先更新偏移量

   ```python
   off = (off - 1) % n  # 右移1次
   ```

2. 再根据偏移量映射到物理下标

   ```python
   new_i = (i - 1 + off) % n  # 减1是为了转成0-based
   ```

## [C. Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c)

考察数组偏移和前缀和，先对原数组进行前缀和，再记录偏移量。这里 $l$, $r$ 可能会出现 $l \gt r$ 的情况即分段了，此时直接求对应段的前缀和即: 
$$
\sum_{i=0}^{r}a_i+\sum_{i=l}^na_i
$$


## [C. Travel](https://atcoder.jp/contests/abc183/tasks/abc183_c)

考察全排列枚举，固定从 $1$ 开始再到 $1$ 结束，所以只需要对 $range(1,n)$ 全排列，再利用题目给出的邻接矩阵进行求和即可。

## [C. Average Length](https://atcoder.jp/contests/abc145/tasks/abc145_c)

考察图论建模和全排列枚举，这里并没有直接给出点与点之间距离的邻接矩阵，可以通过两个for循环进行构建。

全排列枚举每一种排列即可。