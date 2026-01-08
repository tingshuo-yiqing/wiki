## 应用

栈与卡特兰数紧密相连，栈序列个数和合法括号数量都是对应的[卡特兰数](../../number_theory/Catalan)。

### 生成合法括号序列

在构造合法括号序列时需要用到**组合型回溯**，括号序列的前缀一定满足左括号数量大于等于右括号数量。

```python
path = [''] * n
def dfs(i, open):
    if i == n:
        ans.append(''.join(path))
        return 
    if open < m:  # m是括号的对数
        path[i] = '('
        dfs(i + 1, open + 1)
    if i - open < open:
        path[i] = ')'
        dfs(i + 1, open)
```

另一种方法更简单但是复杂度有点高——二进制枚举。先生成所有可能的序列再一个一个判断是否合法

```python
def valid(path):
    b = mb = 0
    for c in path:
        b += 1 if c == '(' else -1
        mb = min(mb, b)
    return b == 0 and mb == 0

outs = []
for i in range(1 << n):
    if bin(i).count('1') != n // 2:  # 小小的剪枝，可以减小常数因子
        continue
    path = [''] * n
    for j in range(n):
        path[j] = '(' if (i >> j) & 1 else ')'
    if valid(path):
        outs.append(''.join(path))
```



### 验证栈序列

```python
```



**例题： **

* [P1044 栈](https://www.luogu.com.cn/problem/P1044)
* [002. Encyclopedia of Parentheses（★3）](https://atcoder.jp/contests/typical90/tasks/typical90_b)
* [P4387 验证栈序列](https://www.luogu.com.cn/problem/P4387)
* [P1750 出栈序列](https://www.luogu.com.cn/problem/P1750)
