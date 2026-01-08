## [D. Div Game](https://atcoder.jp/contests/abc169/tasks/abc169_d)

考察唯一分解定理，从 $z = p^e$ 不难看出这里需要将 $n$ 分解成若干质数的乘积然后贪心的分配指数。

比如样例一：


$$
24=2^3\times3^1
$$


就可以分配成 $2、2^2、3$ 所以输出 $3$ 。

可以使用while循环来将每个质数指数分解成三角数。

## [C. Cream puff](https://atcoder.jp/contests/abc180/tasks/abc180_c)

考察因数分解、裸题可以 $\sqrt{N}$ 下分解出所有因数。

## [A. Simple Math](https://atcoder.jp/contests/arc107/tasks/arc107_a)

* $1\le A,B,C\le 10^9$

考察因式分解。


$$
\sum_{a=1}^A\sum_{b=1}^B\sum_{c=1}^Cabc
$$


直接模拟的话肯定是会超时的，根据**乘法分配律**可以转化为: 


$$
\sum_{a=1}^Aa\sum_{b=1}^Bb\sum_{c=1}^Cc
$$


直接利用求和公式 $\dfrac{n(n+1)}{2}$ 在 $O(1)$ 下求和再相乘即可。