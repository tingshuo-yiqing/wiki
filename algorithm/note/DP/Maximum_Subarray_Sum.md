## 动态规划

### 1. 状态定义

设 $dp[i]$ 表示：**以第 $i$ 个元素结尾的连续子数组的最大和**。

### 2. 状态转移方程
对于第 $i$ 个元素 $a[i]$，我们只有两种选择：
1.  **将其加入到前面的子数组中**：即 $dp[i-1] + a[i]$。
2.  **自己作为新子数组的起点**（丢弃前面的结果）：即 $a[i]$。

我们需要在这两者中选最大的，因此方程为：


$$
dp[i] = \max(dp[i-1] + a[i], \,\, a[i])
$$


**另一种等价写法：**


$$
dp[i] = a[i] + \max(0, \,\, dp[i-1])
$$


### 3. 最小子问题
第一个元素结尾的最大和就是它本身：
$$dp[0] = a[0]$$

### 4. 最终答案
整个数组的最大子数组和，并不一定是以最后一个元素结尾的，所以最终答案是 $dp$ 数组中的**最大值**：


$$
\text{Ans} = \max_{0 \le i < n} \{dp[i]\}
$$




### 5. 空间优化
观察方程 $dp[i] = \max(dp[i-1] + a[i], a[i])$，可以发现 $dp[i]$ 只与 $dp[i-1]$ 有关。因此，我们不需要开辟一个数组，只需用一个变量来维护即可：

#### Python 代码示例：
```python
def max_subarray_sum(nums):
    curr_max = nums[0]  # 相当于 dp[i]
    global_max = nums[0] # 记录过程中的最大值
    
    for i in range(1, len(nums)):
        # 转移方程：要么接上，要么重新开始
        curr_max = max(nums[i], curr_max + nums[i])
        # 更新全局最大值
        if curr_max > global_max:
            global_max = curr_max
            
    return global_max
```



## 维护最小值

