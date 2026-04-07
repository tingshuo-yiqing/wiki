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
MAXN = 10 ** 7 + 1

is_prime = bytearray(b'\x01') * MAXN

for i in range(2, int(MAXN**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = 0
        # 切片赋值
        # is_prime[i*i:MAXN:i] = b'\x00' * ((MAXN -1 - i*i)//i + 1)

primes = array('I', (i for i in range(2, MAXN) if is_prime[i]))
```

切片赋值可以通过洛谷模板题

### 线性筛

```python
#! 关键空间优化
is_prime = bytearray([1]) * MAXN
primes = array('I', [0]) * MAXN
pcnt = 0

for i in range(2, MAXN):
    if is_prime[i]:
        primes[pcnt] = i
        pcnt += 1

    j = 0
    while j < pcnt:
        p = primes[j]
        if p * i > MAXN-1:
            break
        is_prime[p * i] = 0
        if i % p == 0:
            break
        j += 1
```

可以通过洛谷的模板题

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





