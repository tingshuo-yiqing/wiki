除了第一个大题出了意外以外，其它都在可接受范围内。洛谷估分 $50$ 左右。

1. 枚举
2. 数学
3. 数论
4. 暴力：组合枚举
5. 博弈论
6. 并查集
7. 暴力：二进制枚举
8. 暴力：ST表、两层循环枚举区间

---

## A

字符串拼接再转 `int` 从 $1$ 开始判断是不是 $26$ 的倍数。

```python
def main():
    import sys
    sys.set_int_max_str_digits(10000)  # 最大10000位的进制转换
    ans = 0

    r = ''
    for i in range(1, 2027):
        r += str(i)

        if int(r) % 26 == 0:
            ans += 1
    
    print(ans)
```

注：一般在 $3.8.14$ 版本以上会有超大整数的报错，为了防止报错加上一行代码扩展。最大位数。

## B

枚举小于 $a+b$ 完全平方数，一一判断。思路很模糊，没算对。还没补完。

## C

小于 $4$ 的输出 $4$ ，大于 $4$ 的质数加一其它不变，都可以被分解成大于 $2$ 的两个数相乘。

```python
def main():
    for _ in range(II()):
        n = II()

        def is_prime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return n >= 2

        if n <= 4:
            print(4)
        else:
            if is_prime(n):
                n += 1
            print(n)
```

## D

先判断 $-1$ 使用哈希表储存判断有没有开不出来的情况。再组合枚举每一种情况。$m$ 个开关至少需要 $\lceil\dfrac{m}{2}\rceil$ 个开关，最多 $n$ 个开关。

使用了库函数 `combinations` 达到组合枚举的效果。需要注意两点：

1. 偶数相等于关的。
2. 一个开关对同一盏灯起作用的话只标记一次。

```python 
def main():
    outs = []
    for _ in range(II()):
        n, m = MII()

        op = [(i % m, 2 * i % m) for i in range(n)]

        cnt = defaultdict(int)
        for x, y in op:
            if x == y:
                cnt[x] += 1
            else:
                cnt[x] += 1 
                cnt[y] += 1 
        
        if len(cnt.keys()) != m:
            outs.append(str(-1))
            continue

        ok = False
        for k in range((m + 1) // 2, n + 1):  # m个灯至少需要m除以2上取整个开关
            for c in combinations(range(n), k):
                cnt = defaultdict(int)
                for i in c:
                    x, y = op[i]
                    if x == y:
                        cnt[x] += 1
                    else:
                        cnt[x] += 1
                        cnt[y] += 1
                f = False
                if len(cnt.keys()) == m:
                    if all(v & 1 for v in cnt.values()):  
                        f = True
                        outs.append(str(k))

                if f:
                    ok = True
                    break
            if ok:
                break

        if not ok:                    
            outs.append(str(-1))

    print('\n'.join(outs))
```

## E

不会，猜的。 

$1$ 只能操作一次，其它的最少操作两次，统计所有次数后。我猜奇数次先手赢输出 `L` 。

```python
def main():
    outs = []
    for _ in range(II()):
        n = II()
        a = LII()

        cnt = 0
        for x in a:
            cnt += 1 if x == 1 else 2
        
        outs.append('L' if cnt & 1 else 'Q')
    
    print('\n'.join(outs))
```

## F

并查集模板，暴力枚举判断每一个节点的根是否相同。

```python
class DSU:
    def __init__(self, n):
        self.n = n
        self.fa = list(range(n + 1))
        self.sz = [0] * (n + 1)

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.fa[rx] = ry
    
    def add(self, i, val):
        self.sz[i] += val

    def up(self, x, val):
        r = self.find(x)
        for i in range(1, self.n + 1):
            if self.find(i) == r:
                self.sz[i] += val
    
    def query(self, i):
        return self.sz[i]

def main():
    n, q = MII()

    dsu = DSU(n)

    outs = []
    for _ in range(q):
        o = LII()
        op = o[0]

        if op == 1:
            dsu.union(o[1], o[2])
        elif op == 2:
            dsu.add(o[1], o[2])
        elif op == 3:
            dsu.up(o[1], o[2])
        else:
            outs.append(str(dsu.query(o[1])))
    
    print('\n'.join(outs))
```

## G

二进制枚举生成每一个 $01$ 串，再统计。只能拿 $n\le 20$ 左右的分数。

```python
def main():
    n, m = MII()

    MOD = 10 ** 9 + 7

    ans = 0
    for i in range(1 << n):
        s = []
        for j in range(n):
            s.append('1' if (i >> j) & 1 else '0')
        s = ''.join(s)
        a = s.split('0')
        temp = sum(len(k) * (len(k) + 1) // 2 for k in a if k != '')
        if temp >= m:
            ans += 1
        ans %= MOD
    
    print(ans % MOD)
```

## H

预处理 `ST` 表，再两层 `for` 循环应该只能拿 $n\le3000$ 的分数。

```python
def main():
    n = II()
    a = LII()
    MOD = 998244353

    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    
    maxk = logs[n] + 1
    st = [[0] * n for _ in range(maxk)]

    st[0] = a[:]
    for k in range(1, maxk):
        for i in range(n - (1<<k) + 1):
            st[k][i] = Max(st[k-1][i], st[k-1][i + (1<<(k-1))])
    
    def query_max(l, r):
        k = logs[r - l + 1]
        return Max(st[k][l], st[k][r - (1<<k) + 1])
    
    def f(num):
        return len(str(num))
    
    ans = 0
    for i in range(n):
        for j in range(i, n):
            l = j - i + 1
            ans = (ans + f(l) * query_max(i, j)) % MOD
    
    print(ans)
```

