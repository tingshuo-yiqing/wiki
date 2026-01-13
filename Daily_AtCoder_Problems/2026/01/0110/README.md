## [C. Squared Error](https://atcoder.jp/contests/abc194/tasks/abc194_c)

考察枚举，将平方差展开再分步求和即可。


$$
(A_i-A_j)^2=A_i^2-2A_iA_j + A_j^2
$$


此时每个 $A_i$ 都有 $n-1$ 个贡献，再对所有 $A_iA_j$ 进行因式分解即可。

## [ A. Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)

考察动态规划，动态规划先三步走：定义状态、最小子问题、状态转移方程。

1. 状态: 当前石头上的最小花费
2. 最小子问题: $dp_1 = 0$ ， $dp_2 = abs(a_2-a_1)$ 
3. 令 $cost(i,j)=abs(a_i-a_j)$ 定义状态转移方程为 $dp_i=\min(dp_{i-1}+cost(i,i-1),dp_{i-2}+cost(i,i-2))$

## [D. 9 Divisors](https://atcoder.jp/contests/abc383/tasks/abc383_d)

数据范围:

* $1≤N≤4×10^{12}$

考察唯一分解定理和双指针，题目要求为小于等于 $N$ 中仅有 $9$ 个因子的整数个数。根据唯一分解定理仅有 $9$ 个因子的数的情况只有两种: 

* $a^8$ 
* $a^2b^2$

于是就转化为寻找符合条件的 $ab$ 的数量了，一个条件好求直接枚举 $a^8$ 就可以了。第二个条件可以双指针枚举素数。

使用埃氏筛筛筛出 $\sqrt{N}$ 的所有素数即可，也可以使用二分。