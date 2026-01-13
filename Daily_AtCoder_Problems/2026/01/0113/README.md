## [C. Monsters Battle Royale](https://atcoder.jp/contests/abc118/tasks/abc118_c)

考察最大公约数，每次都可以选一个攻击另一个使其减少当前选择的体力，不难想到最大公约数的求法之一即最原始的辗转相减法，最终两数相等就是最大公约数。

这题的解法就是求整个数组的最大公约数。

## [C. Ubiquity](https://atcoder.jp/contests/abc178/tasks/abc178_c)

考察容斥原理，也可以理解为正难则反。这种正难则反的条件一般简单但是实现起来很复杂，比如这道题: [B. Similar Arrays](https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b)

这里如果直接使用排列组合的思想的话会多选，比如我一开始就直接想当然的先为0和9选好两个位置 $n(n-1)$ 再剩下随意安排 $10^{n-2}$ 。这种会有重复。

所以可以先算反面，这种问题反面一般很简单。可以先求没有0没有1的（这两种情况相等）再总数减去它们的并集。


$$
总数−(没有0∪没有9)\\
Ans=A−(B+C−B∩C)
$$

## [D. Multiple of 2019](https://atcoder.jp/contests/abc164/tasks/abc164_d)

考察同余式，对于单个数，2019的倍数可以表示为 $A\equiv0 \pmod{2019}$ ，但这样明显不能判断所有子串是否是2019的倍数会超时，前面已经做过类似的问题了 [ABC 200-C Ringo's Favorite Numbers 2](https://atcoder.jp/contests/abc200/tasks/abc200_c) 这个问题里求得是200的倍数，对所有数进行 mod 200 ，将所有数限制在200以内，当余数相同时它们的差就是可以被200整除的。这里也是一样的。

后缀积 mod 2019 统计余数相等的即可。

