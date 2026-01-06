import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = list(map(int, input().split()))

    bucket = defaultdict(int)

    cnt = 0
    for j in nums:
        bucket[j] += 1
        if j % 5 == 0:
            x = j // 5
            i, k = 7 * x, 3 * x
            if i in bucket and k in bucket:
                cnt += bucket[i] * bucket[k]
    
    bucket.clear()
    for j in reversed(nums):
        bucket[j] += 1
        if j % 5 == 0:
            x = j // 5
            i, k = 7 * x, 3 * x
            if i in bucket and k in bucket:
                cnt += bucket[i] * bucket[k]    
    
    print(cnt)
if __name__ == "__main__":
    main()