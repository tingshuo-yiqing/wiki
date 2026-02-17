## 赛后复盘

### [Olympiad Date](https://codeforces.com/contest/2091/problem/A)

使用哈希表存对应的数量，一旦满足要求就退出即可。

### [Team Training](https://codeforces.com/contest/2091/problem/B)

逆序排序后最小值就是当前遍历的值，然后贪心的选即可。

### [Combination Lock](https://codeforces.com/contest/2091/problem/C)

从样例不难看出，构造的序列为连续的一段 $1,3,5\cdots$ 再接一段连续的 $2,4\cdots$ 

### [Place of the Olympiad](https://codeforces.com/contest/2091/problem/D)

二分答案法。`check` 函数判断当前的最长凳 $mid$ 对应的总人数人数是否超过 $k$ 。

```python
def check(mid):
    need = n * (m - m // (mid + 1))  # 有 m//(mid + 1) 个空格，剩下都可以坐人
    return need >= k
l, r = 0, m + 1
while l + 1 < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid
```

在单行最长为 $mid$ 时，单前行的空座位是 $mid+1$ 的循环次数即 $\left\lfloor \dfrac{m}{mid+1} \right\rfloor$ 个，那剩下都是坐了人的。

$O(1)$ 法。可以发现，最短的最长凳取决于最多人的那行，所以我们可以先求出最多人数的行的人数 $t = \lceil\dfrac{k}{n}\rceil$ 。再均分该行：


$$
E=m-t\\
Ans=\lceil\frac{t}{E+1}\rceil
$$


$E$ 为该行的空凳子数，然后空凳子将人分为 $E+1$ 块区域，最长的那块区域为上取整得到的值。

### [ Interesting Ratio](https://codeforces.com/contest/2091/problem/E)

将 $\dfrac{\operatorname{lcm}(a,b)}{\gcd(a, b)}$ 化简为 $\dfrac{a\cdot b}{\gcd(a,b)^2}$ ，又因为结果是质数且 $a < b$ 所以 $a=\gcd(a,b)$ ，式子可以进一步化为 $\dfrac{b}{a}$ 。

于是我们可以枚举小于等于 $n$ 的所有质数，每个质数组成的对数有 $\lfloor \frac{n}{p} \rfloor$ 。

假设 $n = 10$：
*   小于等于 10 的素数有：2, 3, 5, 7。
*   当 $p = 2$ 时：$\lfloor 10/2 \rfloor = 5$ 对。它们是 $(1,2), (2,4), (3,6), (4,8), (5,10)$。
*   当 $p = 3$ 时：$\lfloor 10/3 \rfloor = 3$ 对。它们是 $(1,3), (2,6), (3,9)$。
*   当 $p = 5$ 时：$\lfloor 10/5 \rfloor = 2$ 对。它们是 $(1,5), (2,10)$。
*   当 $p = 7$ 时：$\lfloor 10/7 \rfloor = 1$ 对。它们是 $(1,7)$。
*   **总计**：$5 + 3 + 2 + 1 = 11$ 对。



