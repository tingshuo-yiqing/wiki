## [C. Factors of Factorial](https://atcoder.jp/contests/abc052/tasks/arc067_a)

考察约数定理，直接对 $N!$ 计算是不现实的 $N$ 最大为 $10^3$ 。根据约数定理，一个数的约数个数等于其分解质因数后的质因数指数加一的乘积。具体参考[Divisors](../../../../algorithm/note/number_theory/Divisors.md)。

所以我们就可以统计 $N!$ 的阶乘的质因子指数的个数，然后再累乘。

## [C. Poll](https://atcoder.jp/contests/abc155/tasks/abc155_c)

考察STL，直接使用哈希表模拟即可。

## [C. Typical Stairs](https://atcoder.jp/contests/abc129/tasks/abc129_c)

考察线性递推，与常规爬楼梯不同的是这里有部分楼梯损坏不能爬，所以我们只需要在递推的过程中加上限制条件即可，将损坏的楼梯跳过掉。

## [No.864 四方演算](https://yukicoder.me/problems/no/864)

考察因式分解，$ab + bc + cd + da = K$ 可以分解为 $(a+c)(b+d)=K$ 此时只需要枚举 $K$ 的因子即可。

对于 $x+y=S(1\le x,y\le N)$ 难点在于如何找到有多少组 $x + y$ 会等于因子 $S$ ，这里直接给出数学结论: 


$$
count = 
\begin{cases}
S-1&(2\le S\le N+1)\\
2N-S+1&(N+1<S\le 2N)\\
0&其它
\end{cases}
$$


推导并理解了公式后可以写更加简洁的代码: 


$$
count = \max(0,\min(S-1,2N-S+1))
$$


正确统计了组合数之后就直接遍历所有因子对了，如果因子对的因子不相等的话可以互换还要再乘一次。





