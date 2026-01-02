import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

""" 2<=n<=20 深度优先搜索求最优方案 """

inf = float('inf')

def bit_enum(n, time):
    ans = inf
    total = sum(time)
    for i in range(1 << n):
        temp = 0
        for j in range(n):
            if (i >> j) & 1:
                temp += time[j]
        ans = min(ans, max(temp, total - temp))
    return ans

def main():
    n = int(input())

    nums = sorted(list(map(int, input().split())))
    total = sum(nums)
    
    ans = inf

    def dfs(i, now):
        nonlocal ans
        if now > ans:  # 剪枝
            return 
        if i >= n:  # 到达叶子，就取答案如何返回
            ans = min(ans, max(now, total - now))
            return 
        # 枚举选与不选
        dfs(i + 1, now + nums[i])
        dfs(i + 1, now)
    
    # dfs(0, 0)
    # print(ans)
    ret = bit_enum(n, nums)
    print(ret)
if __name__ == "__main__":
    main()