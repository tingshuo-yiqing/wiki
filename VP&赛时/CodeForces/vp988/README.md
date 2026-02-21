## 赛后复盘

赛时AB补CD

### [ Diverse Team](https://codeforces.com/contest/988/problem/A)

使用一个哈希集合或字典维护当前的元素，最后判断不同的元素够不够 $m$ 个。注意输出的是索引。

### [Substrings Sort](https://codeforces.com/contest/988/problem/B)

先按字符串长度排序，因为 $n\le100$ 所以可以直接使用 `in` 来判断子串。当有一个不符合要求时直接输出 `NO` 即可。

### [ Equal Sums](https://codeforces.com/contest/988/problem/C)

枚举每一个序列 $i$ 的每一个数 $j$ 进行模拟删除 $\mathrm{Sum_i-a_j}$ 并以 $(i,j)$ 的形式存入哈希表，当出现当前删除后的结果已经出现在哈希表中且是不同序列时即找到了。

### [Points and Powers of Two](https://codeforces.com/contest/988/problem/D)

关键是观察出，满足条件的最大子集是 $3$ ，所以可以将所有点存入集合，再枚举每一个点的 $x+2^d$ 和 $x-2^d$ 在不在集合中。

如果没有大小为 $3$ 的，再判断 $x+2^d$ 或 $x-2^d$ 。

最后如果只有 $1$ 的话随便一个也可以。