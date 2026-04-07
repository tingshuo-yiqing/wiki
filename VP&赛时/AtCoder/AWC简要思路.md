食用方法：vjudge的链接是看题面翻译的，这上面的机器人提交不稳定，能在官网上提交就在官网上提交。语法问题和一些细节问 AI 。比如排序的方式，不同语言的 STL 的用法等。

AWC系列比赛官网：[AtCoder Weekday Contest](https://atcoder.jp/contests/archive?ratedType=0&category=20&keyword=) 

---

## AWC Beta0001

### A - Bacteria Growth Experiment

**难度：**简单，模拟

**题目链接：**https://vjudge.net/problem/AtCoder-awc0001_a#author=translator:1281309:zh

**简要题意：**

初始有一个菌落，每次产生**一个大小是它两倍**的菌落，种类只与大小有关。

**思路：**

考察模拟。看清楚是求种类的数量而不是菌落数量。或者看样例也能看出来。

**参考代码（Python）：**

```python
print(k + 1)
```

---

### B - Exam Passers

**难度：**简单，枚举

**题目链接：**https://vjudge.net/problem/AtCoder-awc0001_b#author=translator:1281309:zh

**简要题意：**

在符合要求的成绩范围 $[L,R]$ 里找出成绩最好的那个人的下标（1-based），如果有多个人就选第一个。

**思路：**

经典的打擂台，初始化好 `mx` ，一个一个比，符合条件就更新即可。

**参考代码（Python）：**

```python
ans = -1
mx = -1
for i, x in enumerate(a):  # Python的 (索引，元素) 枚举方式
    if L <= x <= R:
        if x > mx: # 严格大于的话，就是第一个
            mx = x
            ans = i + 1

print(ans)
```

---

### C - Discount Coupon

**难度：**简单，贪心

**题目链接：**https://vjudge.net/problem/AtCoder-awc0001_c#author=translator:1281309:zh

**简要题意：**

$N$ 件商品，每件商品 $D_i$ 元，要把所有商品买下，可以使用 $K$ 个优惠券将价格变为 $0$ 。问使用优惠券后最少需要字符多少钱。

**思路**：

很明显，让贵的变 $0$ 即可，所以只需要排个序取前 $N-K$ 个小的即可。

**参考代码（Python）：**

```python
print(sum(a[:n-k]))  # 数组切片后求和
```

---

### E - Temperature Fluctuation Range

**难度：**中等，单调队列

**题目链接：**https://vjudge.net/problem/AtCoder-awc0001_e#author=translator:1281309:zh

**简要题意：**

有连续 $N$ 天的温度记录，定义温度波动范围为“这段时间内的最高与最低温度的温度差”。求连续 $K$ 天中温度波动范围最大的值。

**思路：**

单调队列模版题，维护区间大小为 $K$ 的两个单调队列。不断对当前的最值作差取 $\max$ 即可。

**参考代码（Python）：**

```python
midq = deque()
mxdq = deque()

ans = 0
for i, x in enumerate(a):
    while midq and a[midq[-1]] >= x:
        midq.pop()
    midq.append(i)

    while mxdq and a[mxdq[-1]] <= x:
        mxdq.pop()
    mxdq.append(i)

    if i - midq[0] >= k:  # 判断是否过期，即离开了区间大小k的范围
        midq.popleft()
    if i - mxdq[0] >= k:
        mxdq.popleft()

    if i >= k - 1:
        ans = Max(ans, a[mxdq[0]] - a[midq[0]])
```



## AWC Beta0002

### B - Fruit Sorting

**难度：**简单，枚举

**题目链接：**https://vjudge.net/problem/AtCoder-awc0002_b#author=translator:1281309:zh

**简要题意：**

有 $N$ 个水果，每个水果都有一个甜度值 $A_i$ 。现在有 $M$ 个水果碰坏了，定义一个甜度门槛 $K$ 和残次品，如果既碰坏又甜度低于 $K$ 的话为残次品。求残次品数量和其甜度总和。

**思路：**

考察双指针和枚举

1. 对残次品下标 $B$ 数组进行排序。
2. 枚举所有甜度，然后进行条件判断即可，不要忘记移动 $B$ 数组指针。

**具体代码（Python）：**

```python
j = 0
ans = cnt = 0
for i in range(n):
    if j < m and i + 1 == b[j]:
        if a[i] < k:
            cnt += 1
            ans += a[i]
        j += 1
```

---

### C - Observing Plant Growth

**难度：**简单，枚举、数学

**题目链接：**https://vjudge.net/problem/AtCoder-awc0002_c#author=translator:1281309:zh

**简要题意：**

有 $N$ 种植物，第 $i$ 种植物在第 $d$ 天的生长状况为：
$$
A_i + B_i\times d
$$
问所有植物都高于 $M$ 最少天数是多少。

**思路：**

考察向上取整。可以这样想，无论 $d$ 多大，都必须要有完整的一天才可以长完。比如剩余 $1$ 截长到 $M$ ，此时每天可以长 $100$ 截，但是可以 $0.01$ 天就长完吗？条件不允许，必须完整的一天。

所以对每个植物进行上取整后取 $\max$ 即可。上取整公式为：
$$
\lceil \frac{a}{b} \rceil= \frac{a+b-1}{b}
$$
即除数变成了：除数加上被除数在减一。

**参考代码（Python）：**

```python
ans = 0
for _ in range(n):
    a, d = MII()

    ans = Max(ans, (M - a + d - 1) // d)
```

---

### D - Keys and Treasure Boxes

**难度：**简单，双指针、贪心

**题目链接：**https://vjudge.net/problem/AtCoder-awc0002_d#author=translator:1281309:zh

**简要题意：**

$N$ 个宝箱，锁的强度为 $C_i$ ， $M$ 个钥匙，开锁能力为 $R_i$ 。只有 $C_i \le R_i$ 才可以打开宝箱。一个钥匙只能使用一次，问最多可以打开多少个宝箱。

**思路：**

考察双指针。很明显排好序后一一对应，能开就开，开不了就换下一个更强的钥匙。直到其中一方没有了。

**参考代码（Python）：**

```python
a.sort()  # 宝箱
b.sort()  # 钥匙

i = j = 0
while i < n and j < m:
    if b[j] >= a[i]: # 可以开就开
        i += 1  # 消耗一个宝箱
        j += 1  # 消耗一把钥匙
    else:
        j += 1  # 开不了这个，只能换更大强度的钥匙

print(i)
```



## AWC Beta0003

### B - Line of Handshakes

**难度：**简单，枚举

**题目链接：**https://vjudge.net/problem/AtCoder-awc0003_b#author=translator:1281309:zh

**简要题意：**

$N$ 名同学从左到右站成一排，定义两种颜色 `N` 藏青色，`S` 白色，每个人左右手都带了手套。从左到右两两之间握手，左边人的右手与右边人的左手进行握手，定义一次尴尬的握手为手套颜色相同。问尴尬的握手的次数。

**思路：**

考察枚举。从左到右两两枚举判断即可。

**参考代码（Python)：**

```python
t = []
for _ in range(n):
    u, v = inp().split()
    t.append((u, v))  # 从左到右读入每个人的左右手
    
ans = 0
for i in range(n-1):  # 两两遍历到n-1
    if t[i][1] == t[i + 1][0]:  # 左边的右手与右边的左手比较
        ans += 1
```

---

### C - Bargain Sale Selection

**难度：**简单，排序贪心

**题目链接：**https://vjudge.net/problem/AtCoder-awc0003_c#author=translator:1281309:zh

**简要题意：**

有 $N$ 个商品，每件商品有两种价格：原价 $A_i$ 和特价 $B_i$ ，保证特价不会高于原价即： $B_i \le A_i$ 。此时有 $K$ 张优惠券，优惠券可以使用特价买商品，问买掉所有 $N$ 件商品最少需要多少钱。

**思路：**

考察贪心、排序。一件商品省的钱为 $B_i-A_i$ ，所以储存商品的价格元组数组后，按这个标准排序即可。尽量买优惠最多的商品。

**参考代码（Python）：**

```python
t = []
for _ in range(n):
    a, b = MII()
    t.append((a, b))  # 读入 (原价，特价) 数组

t.sort(key=lambda x: -(x[0] - x[1]))  # 对这个数组进行排序

ans = 0
for i, (x, y) in enumerate(t):  # 这里 (x, y) 是元组的解包
    ans += y if i < k else x  # 如果是前 k 个就是特价y，否则是原价 x
```

---

### D - Consecutive Practice Days

**难度：**中等，滑动窗口

**题目链接：**https://vjudge.net/problem/AtCoder-awc0003_d#author=translator:1281309:zh

**简要题意：**

求长度不少于 $K$ ，且元素和至少达到 $M$ 的子数组个数。注：元素全为正的！！！

**思路：**

考察滑动窗口。一道滑动窗口模版题，先看右端点 $r$ ，如果此时子数组符合要求的话，那么后面的数组都是可以的，即在 $r$ 右边的 $n-r$ 个子数组。使用一个 While 循环控制左端点 $l$ 的收缩。

**参考代码（Python）：**

```python
l = s = 0

ans = 0
for r, x in enumerate(a):  # 右端点一直移动
    s += x

    while r - l + 1 >= k and s >= m:  # 符合这两个条件的话更新答案
        ans += n - r
        s -= a[l]
        l += 1  # 收缩左端点，继续判断可不可以更新答案
```



## AWC Beta0004

### A - Preparations Before Departure

**难度：**简单，模拟

**题目链接：**https://vjudge.net/problem/AtCoder-awc0004_a#author=translator:1281309:zh

**简要题意：**

从 $S$ 开始，到 $T$ 结束，问在这期间可不可以完成 $A_1+A_2+\cdots+A_N$ 分钟的工作。

**思路：** 

考察向上取整，如果 $\sum_{i=0}^{i=N}A_i$ 对 $60$ 上整除小于等于 $T-S$ 就是可以完成的。

参考代码（Python）：

```python
a = sum(LII())  # 读入A数组

print("Yes" if (a + 59) // 60 <= S - T else "No")  # 向上取整方法上文有提及
```

---

### B - Battery Level

**难度：**简单，模拟

**题目链接：**https://vjudge.net/problem/AtCoder-awc0004_b#author=translator:1281309:zh

**简要题意：**

有 $N$ 部手机，时间为 $0$ 电量为 $A_i$ ，每部手机都以 $B_i$ 的速度消耗电量，但是电量下限为 $0$ ，即手机不会出现负的电量。问在时间 $T$ 时所有手机的电量和。

**思路：**

考察模拟，一次枚举判断即可注意对 $0$ 取 $\max$ 。

**参考代码（Python）：**

```python
ans = 0
for _ in range(n):
    A, B = MII()

    ans += max(A - B * T , 0)
```

---

### C - Battery Level

**难度：**简单，排序

**题目链接：**https://vjudge.net/problem/AtCoder-awc0004_b#author=translator:1281309:zh

**简要题意：**

温度从 $0$ 开始，经过一系列变化最后再回到 $0$ ，在这个变化过程中定义变化能量为 $|H_{i}-H_{i+1}|$ （ $H_i$ 为温度），求通过合理的安排温度的顺序使得消耗的能量最小。

消耗的能量为：
$$
|0-H_{p_1}|+|H_{p_2}-H_{p_1}|+\cdots+|H_{p_N}-H_{p_{N-1}}|+|H_{p_N}-0|
$$
**思路：**

考察排序，能量变化取决于元素的高度差，什么顺序可以使得元素相邻的差最小呢？大胆假设一下顺序。

**参考代码（Python）：**

```python
a = sorted(LII())

ans = abs(a[0]) + abs(a[-1]) 
for i in range(n - 1):
    ans += abs(a[i + 1] - a[i])
```

---

### D - Parking Lot Assignment

**难度：**难，排序、贪心、优先队列

**题目链接：**https://vjudge.net/problem/AtCoder-awc0004_d#author=translator:1281309:zh

**简要题意：**

有 $N$ 个停车位排成一排，编号为 $1、2、\cdots N$ 。今天有 $M$ 辆车需要停车，第 $i$ 辆车的可以停在 $L_i$ 到 $R_i$ 之间（包含）的任意一个车位。每辆车只能分配一个车位且同一个车位不能被多辆车占据。问能不能给这 $M$ 辆车都分配好位置。

**思路：**

在左边界相同时，优先停放右边小的，使用优先队列维护当前最小值。

1. 先按左边界排序。
2. 遍历车位 $j$ 从 $1$ 到 $N$ 。
   * 将所有 $L_i=j$ 的车的右边界 $R_i$ 放入一个优先队列中。
   * 如果优先队列不为空，判断当前车位 $j$ 是否大于 $R_i$ ，大于的话说明分不了位置了直接输出 `No` .
   * 每正常安排好一个位置计数器 $cnt$ 加一。
3. 如果最后计数器等于 $M$ 则输出 `Yes` 否则输出 `No` 。

**参考代码（Python）：**

```python
t.sort()

hq = []

i = 0
cnt = 0
for j in range(1, n + 1):
    while i < m and t[i][0] == j:
        heappush(hq, t[i][1])
        i += 1
    if hq:
        R = heappop(hq)
        if R < j:  # 当前j小于R说明R这个位置已经被占用了，无法再分配
            print("No")
            return
        else:
            cnt += 1

print("Yes" if cnt == m else "No")
```



---

### E - Sum of Intervals

**难度：**中等，前缀和、哈希表

**题目链接：**https://vjudge.net/problem/AtCoder-awc0004_e#author=translator:1281309:zh

**简要题意：**

给定一个序列，这个序列元素范围为 $-10^9\le A_i\le 10^9$ 。从这个序列中选出一个连续子数组，使得这个子数组的和恰好等于整数 $K$ 。问有多少种方法可以选出这样的子数组。

**思路：**

如果序列全为正数的话可以使用滑动窗口，有正有负的话在前缀和的基础上有两种方法，一种是哈希表一种是二分。由于这里哈希表不会被卡，所以优先选择哈希表的方法。

这种方法类似两数之和，即变边枚举边回头查询。

**参考代码（Python）：**

``` python
mp = defaultdict(int)
mp[0] = 1

cur = ans = 0
for x in a:
    cur += x  # 先获得当前的前缀和
    if cur - k in mp:  # 查能不能和以前的前缀和进行匹配
        ans += mp[cur - k]
    mp[cur] += 1  # 插入当前已经查完了的前缀和
```



## AWC Beta0036

### A - Library Loan Management

**难度：**简单，模拟

**题目链接：**https://vjudge.net/problem/AtCoder-awc0036_a#author=translator:1281309:zh

**简要题意：**

有 $N$ 座图书馆，第 $i$ 座图书馆有 $M_i$ 种藏书，每种藏书有 $S_{i,j}$ 本。现在有 $Q$ 条藏书请求，第 $k$ 条请求是：从第 $v_k$ 座图书馆借出 $d_k$ 类别的书 $1$ 本。

* 如果第 $v_k$ 座的 $d_k$ 类别的书数量不少于 $1$ ，借书成功，该类别藏书数量减少 $1$ 。
* 如果第 $v_k$ 座的 $d_k$ 类别的书数量不足 $0$ ，借书失败，该类别藏书数量保持不变。

输出 $Q$ 次查询后每座图书馆的书的数量情况，以及失败的请求数量。

**思路：**

考察模拟，题意把步骤描述的很清晰了，开一个二维数组储存书再一个 for 循环进行判断，嘴鸥再输出这个二维数组即可。

**参考代码（Python）：**

```python
g = [[]]  # 转成 1-based 更方便一点
for _ in range(n):
    t = LII()
    g.append(t)

Q = II()

cnt = 0
for _ in range(Q):
    u, v = MII()

    if g[u][v] > 0:
        g[u][v] -= 1
    else:
        cnt += 1
```

---

### B - Managing the Guest List

**难度：**简单，STL的简单应用

**题目链接：**https://vjudge.net/problem/AtCoder-awc0036_b#author=translator:1281309:zh

**简要题意：**

一开始没人到场，现在给出 $Q$ 个查询，对于第 $i$ 次查询有类别 $T_i$ 和客人编号 $X_i$ 对于每一个操作有：

* $T_i=1$ （记录到场）：记录 $X_i$ 为到场，保证此时 $X_i$ 不在名单内。
* $T_i=2$ （到处查询）：检查 $X_i$ 是否到场。

**思路：**

考察STL的用法。这里直接使用一个集合维护元素是否存在。

**参考代码（Python）：**

```python
s = set()
for _ in range(n):
    T, X = MII()

    if T == 1:
        s.add(X)
    else:
        print("Yes" if X in s else "No")
```

---

### C - Splitting Logs

**难度：**难，二分答案（画匠问题）

**题目链接：**https://vjudge.net/problem/AtCoder-awc0036_c#author=translator:1281309:zh

**简要题意：**

一根分成了 $N$ 段的木头，第 $i$ 段的长度为 $A_i$ 。相邻两段之间有 $N-1$ 个分界线，从这些分界线中选择 $K$ 个把木头分成 $K+1$ 段，设 $M$ 为这 $K+1$ 段中最长的，求尽可能小的 $M$ 。

**思路：**

经典的画匠问题。二分答案的关键是找出二分的参数和 `chaeck()` 函数。一般求什么什么就是需要二分的答案，比如这里的 $M$ 。与单调性有关的是 $K$ ，假设当前每段最长是 $M$ ，可以将木头分成 $d$ 段，那么有：

* $d > K$ ：此时说明 $M$ 太小了，左指针右移
* $d \le K$ ：此时说明 $M$ 太大了，右指针左移

根据单调性可以用二分的两个指针不断将最优的答案逼出来。这里的上下界很关键，下界是最大值，上界是木头的和。这里使用双开区间的二分写法。

**参考代码（Python）：**

```python
def check(m):
    cnt = cur = 0
    for x in a:  # 在最长短为 m 下最多可以分成多少段
        if cur + x > m:
            cnt += 1
            cur = x
        else:
            cur += x
    return cnt <= k

l, r = max(a) - 1, sum(a) + 1  #! 注意左边界

while l + 1 < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m
```

---

### D - Meeting Room Reservation

**难度：**中等，哈希表、排序、差分

**题目链接：**https://vjudge.net/problem/AtCoder-awc0036_d#author=translator:1281309:zh

**简要题意：**

安排 $N$ 场会议，第 $i$ 场会议从 $S_i$ 开始到 $E_i$ 结束，每次会议编号占用的时间是**半开区间** $[S_i,E_i)$ 。两场会议不能重叠，特别的，如果一场会议的开始时间等于另一场的结束时间则可以使用同一个会议室。问安排完 $N$ 场会议后使用最少的会议室是多少。

**思路：**

看最多有多少会议是重叠的，这些重叠的区间肯定是要用不同的会议室，所以问题转化为了**最大重叠区间问题**，差分的经典用法。由于时间范围很大 $0\le S_i < E_i \le 10^9$ 不能使用数组储存，使用哈希表存，再按时间排好序，注意半开区间的差分写法。

**参考代码（Python）：**

```python
cnt = defaultdict(int)  # 默认值为0的字典

for _ in range(n):
    l, r = MII()

    cnt[l] += 1  # 左闭
    cnt[r] -= 1  # 右开

v = sorted(cnt.keys())  # 按时间排序

cur = 0  # 前缀和变量
mx = 0
for i in v:
    cur += cnt[i]
    mx = Max(mx, cur)
```



## AWC Beta0037

## AWC Beta0040

### C - Apple Harvest

**难度：**简单，双指针

**题目链接：**https://vjudge.net/problem/AtCoder-awc0040_c#author=translator:1281309:zh

**简要题意：**



**思路：**



**参考代码（Python）：**

```python
```



---

### D -  Crossing the Desert

**难度：**中等，贪心，优先队列

**题目链接：**https://vjudge.net/problem/AtCoder-awc0040_d#author=translator:1281309:zh

**简要题意：**



**思路：**



**参考代码（Python）：**

```python 
```





















