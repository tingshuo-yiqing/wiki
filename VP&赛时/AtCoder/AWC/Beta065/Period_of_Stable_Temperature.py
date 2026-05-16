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
    n, K, D = MII()
    a = LII()

    ans = -1
    l = 0

    midq = deque()
    mxdq = deque()

    for r, x in enumerate(a):
        while mxdq and a[mxdq[-1]] <= x:
            mxdq.pop()
        mxdq.append(r)
        while midq and a[midq[-1]] >= x:
            midq.pop()
        midq.append(r)

        mx = a[mxdq[0]]
        mi = a[midq[0]]

        while mx - mi > D:
            l += 1
            if mxdq and mxdq[0] < l:
                mxdq.popleft()
            if midq and midq[0] < l:
                midq.popleft()
            mx = a[mxdq[0]]
            mi = a[midq[0]]
        
        if r - l + 1 >= K:
            ans = Max(ans, r - l + 1)
    
    print(ans)

if __name__ == "__main__":
    main()
