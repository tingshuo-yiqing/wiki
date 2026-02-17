## 素数判定

### 试除法

```python
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2
```

### 埃氏筛

```python
def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:n+1:i] = [False] * len(is_prime[i*i:n+1:i])  # 切片赋值，瞬间消耗大量内存但是时间很快
    return is_prime
```

代码简洁，性价比高。由于切片优化的存在，在 Python 中处理 $10^7$ 以内的数字，埃氏筛往往比纯代码实现的线性筛还要快。

### 线性筛

```python
def liner_sieve(n):
    is_prime = [False] * 2 + [True] * (n - 2)
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i > n - 1: break
            is_prime[i * p] = False
            if i % p == 0: break
    return primes
```

可扩展性强，在需要计算积性函数时的不二选择。

### 分段筛



## 质因数

### 分解质因数

```python
n = t
for i in range(2, int(t ** 0.5) + 1):
    cnt = 0
    while n % i == 0:
        cnt += 1
        n //= i
    if cnt:
        print(i, cnt)
if n != 1:  # 千万不要忘记了
    print(n, 1)
```

### SPF筛



