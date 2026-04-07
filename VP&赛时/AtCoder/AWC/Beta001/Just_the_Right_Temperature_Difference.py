import sys
from collections import deque

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

    def atMost(k):
        if k < 0:
            return 0
        
        midq = deque()
        mxdq = deque()

        l = res = 0
        for r, x in enumerate(a):
            while midq and a[midq[-1]] >= x:
                midq.pop()
            midq.append(r)
            while mxdq and a[mxdq[-1]] <= x:
                mxdq.pop()
            mxdq.append(r)

            # 小于等于k的区间个数
            while a[mxdq[0]] - a[midq[0]] > k:
                l += 1
                # 随着区间的变化队列头元素会过期
                if l > midq[0]:
                    midq.popleft()
                if l > mxdq[0]:
                    mxdq.popleft()
            
            res += r - l + 1
        
        return res

    print(atMost(k) - atMost(k-1))

if __name__ == "__main__":
    main()
