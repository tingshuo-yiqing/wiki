## [004. Cross Sum（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_d)

考察预处理，只需要预处理两个数组`row`和`col`分别代表每一列和每一行的和即可。
$$
A_{ij}=col_j+row_i-a_{ij}
$$

## [010. Score Sum Queries（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_j)

考察前缀和，使用两个 $1-based$ 的数组储存两种成绩，再使用前缀和`pre`。区间 $(l,r)$ 的和为：

```python
pre[r] - pre[l - 1]
```

## [022. Cubic Cake（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_v)

考察最大公约数，能被切成的最大正方体取决于三边的最大公约数。

当确定好了最大正方体后，接下来就计算三边分别要切多少次再加起来即可。要切的次数为：边长除以最大公约数减一。

## [024. Select +／- One（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_x)

考察数学，不难发现我们可以直接确定的是从A到B的最小次数 $mi$ ，即：
$$
mi=\sum_{i=0}^{N}|A_i-B_i|
$$
如果还要再增加次数的话，就必须**成对增加**。所以如果 $mi > k$ 和 $k-mi$ 是偶数的话就可以恰好 $k$ 次从A变到B。

## [032. AtCoder Ekiden（★3）](https://atcoder.jp/contests/typical90/tasks/typical90_af)

考察全排列，使用库函数可以很方便的生成所有排列。本题 $N\le 10$ 比较小，枚举量为 $10! = 3,628,800$ 。

再使用一个二维bool数组进行储存选手之间的关系。在枚举的过程中如果发现相邻选手不和就直接跳过此排列，这里可以用到短路特性。