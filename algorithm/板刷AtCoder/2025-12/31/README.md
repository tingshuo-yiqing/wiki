## [A. Table Tennis Training](https://atcoder.jp/contests/agc041/tasks/agc041_a)

数据规模: 

* $2 \le N \le 10^{18}$
* $1 \le A < B \le N$

每次可以从 $X$ 位置到达 $X \pm 1$ 的位置，不难发现相向是最快的。

如果初始相差是偶数的话相向直接可以到达即为 $\dfrac{B-A}{2}$ 。

如果是奇数的话差一相向不能直接到达，需要其中一方先到达一方的边界然后改变之间的奇偶性再相向。

## [A. DEAD END](https://atcoder.jp/contests/arc021/tasks/arc021_1)

枚举每一个元素的四个方向，判断存不存在相同即可。只要存在一个相同就可以退出程序了。

## [C. XYZ Triplets](https://atcoder.jp/contests/aising2020/tasks/aising2020_c)

考察枚举上界，枚举 $x$ , $y$ , $z$ 记录可以组成小于等于 $n$ 的组数即可。

最大枚举到 $\sqrt{n}+1$ 即可。

## [D. FizzBuzz Sum Hard](https://atcoder.jp/contests/abc253/tasks/abc253_d)

考察数学求和公式的应用，只需要将 $n$ 的和减去 $a$ 的倍数和和 $b$ 的倍数和再加上多减去的 $a$ 和 $b$ 的最小公倍数的倍数和即可。

使用下整除确定小于等于 $n$ 的最大倍数。