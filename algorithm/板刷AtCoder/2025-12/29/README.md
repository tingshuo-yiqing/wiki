## [Large Queue](https://atcoder.jp/contests/abc413/tasks/abc413_c)

使用双端队列压缩数据 $(c,x)$ 不断的使用 $k$ 去消耗 $c$ 没有消耗完再执行 $\text{appendleft}$ 操作**放回原位置**。

 ## [Grid and Magnet](https://atcoder.jp/contests/abc351/tasks/abc351_d)

栈的典型应用：邻项相消（合并）

通过一个 $\text{while}$ 循环和 $\text{cur}$ 变量维护**当前值**和相邻相同合并，到相邻不相同时再入栈。

## [C. Brackets Stack Query](https://atcoder.jp/contests/abc428/tasks/abc428_c)

栈的典型应用：判断括号平衡、回到上一个状态（撤销）

使用两个变量共同判断是否平衡：

* $\text{balance}$ 判断当前左右括号是否相等
* $\text{min\_balance}$ 判断是否存在 $)$ 在 $($ 前的情况，这种即使 $\text{balance}$ 等于0也是不平衡的

当删除最末尾括号时，只需要 $\text{pop}$ 一次即可。

## [C. Max MEX](https://atcoder.jp/contests/abc290/tasks/abc290_c)

要取得最大的 $\text{mex}$ 需要前面的较小数都存在。比如序列 $[3,4,1,0,2]$ 较小的数都存在最大即是 $5$ 。

所以我们直接遍历 $0$ 到 $k-1$ 如果有哪个不存在，最大就是不存在的这个。