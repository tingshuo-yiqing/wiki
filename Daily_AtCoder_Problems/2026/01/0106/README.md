## [C. Ringo's Favorite Numbers 2](https://atcoder.jp/contests/abc200/tasks/abc200_c)

考察同余原理，题目要求 $A_i-A_j$ 是 $200$ 的倍数，在数学上可以表示为: 


$$
A_i-A_j \equiv0\pmod{200}
$$


根据同余式的性质，这等价于: 


$$
A_i \equiv A_j\pmod{200}
$$


翻过来看就是如果两个数被 $200$ 除的余数相同，那它们的差可以被 $200$ 整除。

在这题里条件是: 

* $1\le i < j\le N$
* $A_i - A_j$ is a multiple of $200$

所以我们只需要对每个元素都对 $200$ 取模，统计每个模数的频率。这些频率就是余数相同的元素个数。

## [D. Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)

考察贪心，典型的优先队列贪心，每次选当前的最大值使用券是性价比最高的。

## [D. Kadomatsu Subsequence](https://atcoder.jp/contests/abc439/tasks/abc439_d)

考察枚举，
