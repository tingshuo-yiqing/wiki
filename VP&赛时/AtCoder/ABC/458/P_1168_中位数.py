import sys
from heapq import heappop, heappush

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
    n = II()
    a = LII()
    print(a[0])

    mi = [a[0]]
    mx = []

    outs = []
    for i, x in enumerate(a[1:]):
        mid = mi[0]

        if x >= mid:
            heappush(mi, x)
        if x < mid:
            heappush(mx, -x)

        while len(mi) - len(mx) > 1:
            heappush(mx, -heappop(mi))
        
        while len(mx) - len(mi) > 0:
            heappush(mi, -heappop(mx))

        mid = mi[0]

        if i & 1:
            outs.append(mid)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
