## [027. Sign Up Requests （★2）](https://atcoder.jp/contests/typical90/tasks/typical90_aa)

 使用数据结构哈希集合判断是否存在。

## [033. Not Too Bright（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_ag)

核心考察：分类讨论和贪心策略，条件是：

* 在 $2\times2$ 区域下有且仅有一个点亮的LED

1. 平台情况，当 $H$ 和 $W$ 大于 $1$ 时，不难看出要最大化点亮LED只要:  

$$
\lfloor\frac{H}{2}\rfloor\times\lfloor\frac{W}{2}\rfloor
$$
2. 特殊情况，重要的是要考虑到 $H$ 和 $W$ 其中一个为 $1$ 的时候已经没有条件的限制了，此时**全部都可以点亮**。  

$$
H\times W
$$

## [055. Select 5（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_bc)

数据范围：

* $5\le N\le 100$
* $0\le A_i\le 10^9$
* $0\le Q<P\le10^9$

考察暴力枚举。从数据量来看是可以五层循环遍历来寻找符合条件的组合，因为时间复杂度有一个很小的常数: $\dfrac{1}{120}$
  所以总的时间复杂度是:   
$$
\frac{N(N-1)(N-2)(N-3)(N-4)}{5!}\approx \frac{1}{120}N^5
$$
总的数据量大概是 $10^8$ 左右，可以勉强通过。

除此之外，单个元素高达 $10^9$ 如果直接相乘后高达 $10^{45}$ 即使python可以支持高精度但也会变得很慢，而c++肯定是存不下的。
所以需要每一步取一次模。

## [061. Deck（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_bi)

考察双端队列操作。不过不建议直接使用双端队列，因为双端队列的随机访问是 $O(k)$ （k是更靠近两端的距离） 的。如果有大量的中间访问，可能会超时。

这里使用数组模拟双端队列，开一个 $2\times N$ 的数组从中间维护两个指针:   
$$
l=\lfloor \frac{2\times N}{2} \rfloor \\
r = l + 1
$$
 中间的元素使用偏移量访问，即 $d[l+x]$ 为双端队列的第 $x$ 个元素。

## [067. Base 8 to 9（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_bo)

考察模拟，简单的模拟进制再字符串替换。

## [078. Easy Graph Problem（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_bz)

考察图的储存和遍历，使用邻接表存图再遍历每一个点的出边即可。

