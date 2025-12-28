# import heapq

# n = int(input())

# nums = list(map(int, input().split()))

import sys
import heapq

# 使用 sys.stdin.read 一次性读取所有输入
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    n = int(next(iterator))
except StopIteration:
    exit()

# 生成器方式读取剩余数据，避免一次性在大列表中转换，节省内存
nums = [int(next(iterator)) for _ in range(n)]

heapq.heapify(nums)

ans = 0

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a + b)
    ans += (a + b)

print(ans)