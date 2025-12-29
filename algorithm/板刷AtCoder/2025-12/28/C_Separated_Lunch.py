import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

""" 2<=n<=20 深度优先搜索求最优方案 """

def main():
    n = int(input())

    nums = sorted(list(map(int, input().split())))
    total = sum(nums)
    
    ans = float('inf')

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
    
    dfs(0, 0)
    print(ans)
if __name__ == "__main__":
    main()