import sys
from heapq import heappop, heappush, heapify
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())

    nums = list(map(lambda x: -int(x), input().split()))

    heapify(nums)

    for _ in range(m):
        val = heappop(nums)
        heappush(nums, -(-val // 2))
    
    print(-sum(nums))

if __name__ == "__main__":
    main()