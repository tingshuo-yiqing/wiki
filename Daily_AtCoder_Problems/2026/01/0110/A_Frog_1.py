import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()


def main():
    n = int(input())

    nums = [0] + list(map(int, input().split()))

    dp = [0] * (n + 2)
    dp[2] = abs(nums[2] - nums[1])

    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1] + abs(nums[i] - nums[i - 1]), dp[i - 2] + abs(nums[i] - nums[i - 2]))

    print(dp[n])
if __name__ == "__main__":
    main()