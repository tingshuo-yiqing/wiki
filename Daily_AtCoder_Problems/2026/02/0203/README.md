## [C. : (Colon)](https://atcoder.jp/contests/abc168/tasks/abc168_c)

### 余弦定理

已知两条边和角度，直接使用余弦函数求第三边。


$$
c^2=a^2+b^2-2ab\cos(\theta)
$$


已知两针的旋转速度：

* 分针每分钟走 $6$ 度（360/60）
* 时针每小时走 $30$ 度（360/12），如何还有分钟的时间页要算，在每小时 $30$ 度的基础上每分钟 $30 / 60$ 即 $0.5$ 度

两针之间的夹角就是它们的度数差的绝对值，再调用 $\operatorname{radians}$ 函数将度数转化为弧度即可带入余弦定理了。

### 欧几里得距离

假设它们都在圆心为 $(0,0)$ 的点和正 $y$ 轴的方向顺时针旋转的话圆上的点的坐标是 $(r\sin\theta,r\cos\theta)$ 。

找到了两点后直接使用函数 $\operatorname{dist}$ 求欧几里得距离。

## [ C. Half and Half](https://atcoder.jp/contests/abc095/tasks/arc096_a)

枚举AB的个数 $0,2,4,6,\cdots$ 过程中计算当前所需的最大价格取 $\min$  即可，这种枚举涵盖了所有可能的情况。