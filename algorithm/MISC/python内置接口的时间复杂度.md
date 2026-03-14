## 流式读入

```python
# ---------------------------------------------------------
# 1. 流式输入处理 (Stream Input)
# ---------------------------------------------------------
# read() 读取所有字符，split() 自动处理所有不规则的空格和换行
input_data = sys.stdin.read().split()

if not input_data:
    return

# 创建迭代器，比用索引访问列表更快且代码更简洁
iterator = iter(input_data)

try:
    # 使用 next(iterator) 依次获取下一个 token
    n = int(next(iterator))
    m = int(next(iterator))

    # 生成两个列表
    # 这里是一次性生成，如果内存非常吃紧，也可以保留 generator
    nums = [int(next(iterator)) for _ in range(n)]
    op = [int(next(iterator)) for _ in range(m)]
except StopIteration:
    return
```

