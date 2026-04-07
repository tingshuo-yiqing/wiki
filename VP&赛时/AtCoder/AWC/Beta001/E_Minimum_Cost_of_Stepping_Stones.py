import sys
from collections import deque
from math import inf

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n, k = MII()

    a = LII()

    dp = [inf] * n
    dp[0] = a[0]

    midq = deque([0])  #! 为什么要初始化一个0？

    for i in range(1, n):
        if midq and midq[0] < i - k:
            midq.popleft()
        
        dp[i] = dp[midq[0]] + a[i]

        while midq and dp[midq[-1]] >= dp[i]:
            midq.pop()
        midq.append(i)
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
