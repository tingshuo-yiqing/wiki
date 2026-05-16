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
    x = II()

    mi = [x]
    mx = []

    outs = []
    for _ in range(II()):
        u, v = MII()
        
        mid = mi[0]
        if u >= mid:
            heappush(mi, u)
        else:
            heappush(mx, -u)
        if v >= mid:
            heappush(mi, v)
        else:
            heappush(mx, -v)

        while len(mx) > len(mi):
            heappush(mi, -heappop(mx))
        while len(mi) - len(mx) > 1:
            heappush(mx, -heappop(mi))
        
        mid = mi[0]
        outs.append(mid)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
