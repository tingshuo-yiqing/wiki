## [C. Flip,Flip, and Flip......](https://atcoder.jp/contests/abc090/tasks/arc091_a)

考察找规律，因为总共要翻 $N\times M$ 次，不难看出每个卡片被翻的次数是固定的，说明可以直接找出规律。

* 一般的 $N>1$ 和 $M>1$ 时，只有最中间的（ $ans=(N-1)\times (M-1)$ ）才可能被翻奇数次即 $9$ 次，其它都是偶数次 $4$ 或 $6$ 。
* 当 $N=1$ 或 $M=1$ 时，两端为 $2$ 次，中间是 $3$ 次，所以有 $ans = N\times M-2$ 次。
* 特判 $N = 1$ 和 $M=1$ 的情况。



## [ C. Sort](https://atcoder.jp/contests/abc350/tasks/abc350_c)

考察模拟，一次遍历模拟交换过程。设置一个标准的有序排列，让数组和其一一对比，不相等就和对应位置交换。