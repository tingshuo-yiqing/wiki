## 二进制枚举

通常用来枚举有顺序的子集和方案数，和对数组进行分段。

```python
# 二进制枚举的非递归写法（板子）
n = int(input())
for i in range(1 << n):  # 遍历 0 到 2^n - 1
    subset = []
    for j in range(n):
        if (i >> j) & 1: # 检查 i 的第 j 位是不是 1
            subset.append(j)
    print(f"{i}:", *subset)
```

**题目推荐**：

* [ITP2_11_A](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_11_A)，有顺序子集
* [ABC197-C ORXOR](https://atcoder.jp/contests/abc197/tasks/abc197_c)，对 $n-1$ 进行二进制枚举数组的分段

## 指数型枚举

递归实现指数型枚举



## 排列型枚举

### 库函数法

使用库函数 `itertools.permutations`进行枚举。

```python
A = [1, 2, 3]
for p in permutations(A):
    print(*p)

print()
for p in permutations(range(4)):
    for i in range(4):
        print(p[i], end=' ')
    print()
```

### 搜索

比赛时能使用 `itertools.permutations` 就不要手写，平时练习可以手写搜索，因为Python内置的 `permutations` 是由C语言实现的，相对而言比手写的递归快很多，除非一些题目需要剪枝。

```python

```

**题目推荐**：

- 032 - AtCoder Ekiden（★3）
- ABC183-C 「Travel」
- ABC145-C 「Average Length」
- ABC150-C 「Count Order」
- ABC054-C 「One-Stroke Path」

## 组合型枚举





