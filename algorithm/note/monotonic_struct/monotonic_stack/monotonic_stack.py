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
    
    # 清空栈，更新栈中元素的左最值，右边默认是-1
    while st:
        cur = st.pop()
        if st:
            ans[cur][0] = st[-1]
    
    # 修正相等内容，保证严格单调
    for i in range(n - 2, -1, -1):
        if ans[i][1] != -1 and nums[ans[i][1]] == nums[i]:
            ans[i][1] = ans[ans[i][1]][1]
    return ans


def find_max(h, p):
    st, n = [], len(h)
    ans = [[-1, -1] for _ in range(n)]

    for i in range(n):
        while st and h[st[-1][0]] < h[i]:
            cur = st.pop()  # 当前的索引列表
            for j in cur:
                ans[j][1] = i
                if st:
                    ans[j][0] = st[-1][-1]
        
        # 遇到重复元素时
        if st and h[st[-1][0]] == h[i]:
            st[-1].append(i)
        else:
            st.append([i])

    # 处理栈中剩余元素
    while st:
        cur = st.pop()
        for j in cur:
            if st:
                ans[j][0] = st[-1][-1]

    return max(ans)


def find_right_min(nums):
    st, n = [], len(nums)
    ans = [-1] * n

    for i in range(n):
        while st and nums[st[-1]] > nums[i]:
            cur = st.pop()
            ans[cur] = i
        st.append(i)
    return ans


def find_left_min(nums):
    st, n = [], len(nums)
    ans = [-1] * n

    for i in range(n):
        while st and nums[st[-1]] >= nums[i]:  # 右边 >= 左边 < 
            st.pop()
        if st:
            ans[i] = st[-1]
        st.append(i)
    return ans


r = find_right_min(nums)
l = find_left_min(nums)
for i in range(n):
    print(l[i], r[i])

s = "dsak jf"

print(s.title())