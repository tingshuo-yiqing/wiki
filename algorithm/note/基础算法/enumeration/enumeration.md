## 二进制枚举

通常用来枚举有顺序的子集和方案数

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



## 递归枚举

### 递归实现指数型枚举





### 递归实现排列型枚举





### 递归实现组合型枚举





