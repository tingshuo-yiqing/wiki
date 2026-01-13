## [C. Rotatable Array](https://atcoder.jp/contests/abc410/tasks/abc410_c)

考察数组操作，不要真正的操作数组而是使用一个变量记录偏移量再根据这个偏移量进行映射到实际下标。操作后的一切操作，交换、修改、翻转等等都是根据记录的偏移量来计算的。

## [C. 列](https://atcoder.jp/contests/abc032/tasks/abc032_c)

考察双指针操作，因为是乘积不超过 $K$ 所以先特判 $0$ 如果有的话就直接输出 $n$ 即可。再特判 $K$ 等于 $0$ 的时候，直接输出 $0$ 即可。

接下来就是使用双指针组成的**滑动窗口**了，右指针不断向右扩展不断更新 $ans$ ，如果不满足条件就直接收缩左边界。

## [D. Enough Array](https://atcoder.jp/contests/abc130/tasks/abc130_d)

考察前缀和和双指针，先预处理前缀和数组，再右指针不断扩展，当次区间符合要求时再收缩左指针即可。
