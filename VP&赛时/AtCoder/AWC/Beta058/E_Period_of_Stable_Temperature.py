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
    n, m = MII()
    a = LII()

    midq = deque()
    mxdq = deque()

    l = 0
    ans = 0
    for r, x in enumerate(a):
        while midq and a[midq[-1]] >= x:
            midq.pop()
        midq.append(r)
        
        while mxdq and a[mxdq[-1]] <= x:
            mxdq.pop()
        mxdq.append(r)

        mx = a[mxdq[0]]
        mi = a[midq[0]]
        while mx - mi > m:
            l += 1
            if midq[0] < l:
                midq.popleft()
                mi = a[midq[0]]
            if mxdq[0] < l:
                mxdq.popleft()
                mx = a[mxdq[0]]
        
        ans = Max(ans, r - l + 1)

    print(ans)

if __name__ == "__main__":
    main()
