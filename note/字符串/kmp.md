这篇博客为总结的**解题流程和模板**，如果想要算法具体的原理和数学证明的话请参考：[Prefix function. Knuth–Morris–Pratt algorithm](https://cp-algorithms.com/string/prefix-function.html) 

[1753 String Matching - CSES](https://vjudge.net/problem/CSES-1753)  模式串匹配模版

[1732 Finding Borders - CSES](https://vjudge.net/problem/CSES-1732)  求出字符串所有 Border

[1733 Finding Periods CSES](https://vjudge.net/problem/CSES-1733)  求出所有的周期大小

[459. 重复的子字符串 - 力扣](https://leetcode.cn/problems/repeated-substring-pattern/)  判断是否存在完全循环

带着这些问题阅读效果更好！

---

## 最长相等真前后缀

最长相等前后缀也被称为 Border ，KMP算法就利用了其性质来进行匹配优化。

* 前缀：从字符串第一个字符开始的子串。
* 后缀：以字符串最后一个字符结束的子串。
* 真：长度严格小于原字符串长度。

求法（ $O(n^2)$ ）：

```python
def border(s):
    n = len(s)
    L = 0
    for i in range(1, n):  # 长度为 i 上限为 n-1 确保为真前后缀
        if s[:i] == s[n-i:n]:
            L = i
    return L
```

还有更加高效的算法，可以优化到 $O(n)$ 。正是这个优化产生了 KMP 算法。

## 前缀函数

在 KMP 中的前缀函数的到数组 $\pi$ ，其中 $\pi[i]$ 表示字符串的前缀 $t[0\dots i]$ 中，**最长的相等真前后缀**的长度。

如果使用暴力枚举每个子串进行一次 `border` 函数的话时间复杂度是 $O(n^3)$ 

```python
b = []
for i in range(len(s)):
    b.append(border(s[:i + 1])) 
```

通过递推可以在 $O(n)$ 时间内求出前缀数组 $\pi$

1. 假设我们正在计算 $\pi[i]$ ，并且已知 $\pi[i-1]=j$ 。
2. 这意味着 $t[0\dots j-1]$ 是 $t[0\dots i-1]$ 的最长相等前后缀。
3. 情况A：如果 $t[i]==t[j]$ ，那么 $\pi[i] = j+1$ 。
4. 情况B：如果 $t[i] \ne t[j]$ ，我们需要一个更短的相等前后缀。于是我们可以让 $j=\pi[j-1]$ ，然后重复 $t[i]$ 和 $t[j]$ 的比较过程，直到匹配或 $j$ 降为 $0$ 。

具体代码为

```python
def get_pi(s):
    n = len(s)
    pi = [0] * n

    for i in range(1, n): 
        j = pi[i - 1]  # 取前一个的位置的pi

        while j > 0 and s[i] != s[j]:  # 情况B
            j = pi[j - 1]
        if s[i] == s[j]:  # 情况A
            j += 1
        pi[i] = j

    return pi
```

## 应用

### 模式串匹配

已知模式串 $t$ 和匹配串 $s$ ，在预处理完**模式串的 $\pi$ 数组**后可以通过双指针匹配。

1. 指针 $i$ ：始终在 $s$ 上向右移动，不回退。
2. 指针 $j$ ：在 $t$ 上移动，如果匹配 `j++` 如果失配 $j$ 根据 $\pi$ 数组向左跳，跳到一个可以让前面部分继续匹配的位置。

这个根据 $\pi$ 数组向左跳的过程可以理解成下面这句有名名的话：

> 一个人能走的多远不在于他在顺境时能走的多快，而在于他在逆境时多久能找到曾经的自己。

```python
m, n = len(t), len(s)
pi = get_pi(t)

j = 0  # 模式串指针
for i in range(n):  # 文本串指针永不回退
    while j > 0 and s[i] != t[j]:
        j = pi[j - 1]

    if s[i] == t[j]:
        j += 1

    if j == m:  # 匹配成功
        # 位置为 i - j + 1 0-based
        j = pi[j - 1]  # 继续匹配可能重叠的下一处
```



### 求字符串周期

先利用预处理的 $\pi$ 数组求出所有的 Border ，再根据这些 Border 就可以构造出所有的周期串了。

#### 求字符串所有周期

由于 $\pi$ 数组记录了最长 Border ，而次长的 Border 可能通过 $\pi[\pi[n-1]-1]$ 递归求得，因此我们可以不断回跳，求出所有的 Border 后，周期就是 n - Border。 

```python
n = len(s)
pi = get_pi(s)

b = []
k = pi[n - 1]
while k:
    b.append(n - k)
    k = pi[k - 1]
b.append(n)

print(*b)
```

不要忘记了 $s$ 自身也是周期，然后每个周期串就是 `s[:b[i]]` 。

#### 完全循环

在 $\pi[n-1]>0$ 基础上，当它的**最小正周期** $n-\pi[n-1]$ 可以被总长度 $n$ 整除时，存在完全循环。

```python
n = len(s)
pi = get_pi(s)

k = n - pi[n - 1]
print("YES" if pi[n - 1] > 0 and n % k == 0 else "NO")
```
