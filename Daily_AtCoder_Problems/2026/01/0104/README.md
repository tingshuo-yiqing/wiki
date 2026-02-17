## [GCD on Blackboard](https://atcoder.jp/contests/abc125/tasks/abc125_c)

考察 $\gcd$ 和前缀和，修改或减少数组中的元素只会让数组的 $、gcd$ 变小或不变，题目要求修改一个数使数组 $\gcd$ 最大。

于是我们就可以枚举每一个元素作为待删除的元素，预处理前后缀 $\gcd$ 后就变成了: 

```python
pf = [0] * (n + 1)
for i in range(1, n + 1):
    pf[i] = gcd(pf[i - 1], A[i])

sf = [0] * (n + 2)
for i in range(n, 0, -1):
    sf[i] = gcd(sf[i + 1], A[i])

ans = 0
for i in range(1, n + 1):
    # 模拟删除操作，不包含A[i]的前后缀gcd的gcd
    ans = max(ans, gcd(pf[i - 1], sf[i + 1]))
```

### 前后缀分解模板

```python
def solve(arr):
    n = len(arr)
    pre = [0] * (n + 1)
    suf = [0] * (n + 1)
    
    # 这里的 0 是 gcd 的单位元 (gcd(0, x) = x)
    for i in range(n):
        pre[i+1] = math.gcd(pre[i], arr[i])
        
    for i in range(n-1, -1, -1):
        suf[i] = math.gcd(suf[i+1], arr[i])
        
    ans = 0
    # 枚举被删掉的下标 i
    for i in range(n):
        # 核心：左边是 pre[i], 右边是 suf[i+1]
        res = math.gcd(pre[i], suf[i+1])
        ans = max(ans, res)
    return ans
```

推荐这样模拟删除操作。

## [C.IPFL](https://atcoder.jp/contests/abc199/tasks/abc199_c)

考察数组的下标映射。不要真的去模拟操作，一定会超时的。我们可以定义一个 $bool$ 变量判断此时数组是否处以翻转状态。

非翻转状态下，直接交换即可。翻转状态下下标要进行映射: 

* 如果下标 $\ge N$ ，则它的实际下标为 $idx - N$
* 如果下标 $\le N$ ，则它的实际下标为 $idx + N$

最后如果数组还是翻转状态的话就翻转输出，否则顺序输出。

## [C. 総和](https://atcoder.jp/contests/abc037/tasks/abc037_c)

考察前缀和，前缀和模板题定长区间的和直接: 



$$
\sum_{i=0}^{n-k} (pf_{i+k}-pf_i)
$$

