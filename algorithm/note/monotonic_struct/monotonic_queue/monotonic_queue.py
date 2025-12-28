import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

def monotonic_queue(nums, k, is_max=True):
    """获得大小为k的窗口的最值"""
    ans = []
    q = deque()

    for i, val in enumerate(nums):
        while q and (nums[q[-1]] <= val if is_max else nums[q[-1]] >= val):
            q.pop()
        q.append(i)
        if i - k == q[0]:  # 窗口大小限制，此时头部必须弹出
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    print(*monotonic_queue(nums, k, is_max=False))
    print(*monotonic_queue(nums, k))

if __name__ == "__main__":
    main()