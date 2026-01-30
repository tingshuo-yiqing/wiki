

## 实现

### 1.使用int

先使用 `.replace()` 快速完成替换，将两种状态分别转化为 `01` 串的形式。

再使用 `int` 进行转化为整数 `int("01", 2)` 。

```python
s = "ooxx"
# 将 o 换成 1，x 换成 0
binary_str = s.replace('o', '1').replace('x', '0')
# 转换为 2 进制整数
mask = int(binary_str, 2)
```

### 2.循环

