测试连接：[单调栈结构(进阶)](https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb)，包含重复元素。使用这个数据结构时应该注意**重复元素**的影响。
尽量使用全局列表而不是在函数中返回列表

## 模板一：二次修正

左程云写法。可以一次遍历求左右两边**严格最值**，额外一个过程进行重复处理

```python
n = int(input())
nums = list(map(int, input().split()))

def find_min(nums):
    st, n = [], len(nums)
    ans = [[-1, -1] for _ in range(n)]
    # 遍历栈
    for i in range(n):
        while st and nums[st[-1]] >= nums[i]:
            cur = st.pop()
            if st:  # 记录前面left最小，如果栈不为 空的话 
                ans[cur][0] = st[-1]
            ans[cur][1] = i  # 记录后面right最小
        st.append(i)
    
    # 清空栈，更新栈中元素的左最值，右边没有最值了默认是-1
    while st:
        cur = st.pop()
        if st:
            ans[cur][0] = st[-1]
    
    # 修正相等内容，保证严格单调
    for i in range(n - 2, -1, -1):
        if ans[i][1] != -1 and nums[ans[i][1]] == nums[i]:
            ans[i][1] = ans[ans[i][1]][1]
    return ans

ans = find_min(nums)

for o in ans:
    print(*o)
```

## 模版二：索引列表

一次遍历求左右两边的**严格最值**
容易$MLE$，除了索引列表外，其它部分尽量使用单列表，尽量不要使用列表套列表或元祖列表。

```python
def find_min(nums):
    st, n = [], len(nums)
    ans = [[-1, -1] for _ in range(n)]  # 
g
    for i in range(n):
        while st and nums[st[-1][0]] > nums[i]:
            cur = st.pop()  # 当前的索引列表
            for j in cur:
                ans[j][1] = i  # 一定存在右最值，不在if内更新
                if st:
                    ans[j][0] = st[-1][-1]  # 找物理距离离它最近的，即后进列表的索引 

        if st and nums[st[-1][0]] == nums[i]:
            st[-1].append(i)
        else:
            st.append([i])

    # 处理栈中剩余元素
    while st:
        cur = st.pop()
        for j in cur:  # 右侧没有最值了
            if st:
                ans[j][0] = st[-1][-1]

    return ans
```

## 模板三：两次遍历

最简单、最模板，但是作用单一只能求**两边严格最值**的情况。

```python
def find_right_min(nums):
    st, n = [], len(nums)
    ans = [-1] * n
    for i in range(n):
        while st and nums[st[-1]] > nums[i]:  # 右边 > 左边 >= 
            cur = st.pop()
            ans[cur] = i
        st.append(i)
    return ans

def find_left_min(nums):
    st, n = [], len(nums)
    ans = [-1] * n
    for i in range(n):
        while st and nums[st[-1]] >= nums[i]:  # 右边 >= 左边 >
            st.pop()
        if st:
            ans[i] = st[-1]
        st.append(i)
    return ans
```

这两个$while$条件结合就是两边都是严格小于了，大于同理只是改变符号而已。
实际写题可以不用写函数返回答案列表，直接操作全局列表更介绍内存