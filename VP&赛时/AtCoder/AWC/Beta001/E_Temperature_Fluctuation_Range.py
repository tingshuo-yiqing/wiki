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

    midq = deque()
    mxdq = deque()

    ans = 0
    for i, x in enumerate(a):
        while midq and a[midq[-1]] >= x:
            midq.pop()
        midq.append(i)

        while mxdq and a[mxdq[-1]] <= x:
            mxdq.pop()
        mxdq.append(i)

        if i - midq[0] >= k:
            midq.popleft()
        if i - mxdq[0] >= k:
            mxdq.popleft()
        
        if i >= k - 1:
            ans = Max(ans, a[mxdq[0]] - a[midq[0]])
    
    print(ans)

if __name__ == "__main__":
    main()
