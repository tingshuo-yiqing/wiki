import sys
from heapq import heapify, heappop, heappush

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
    n, M = MII()

    hq = []
    for _ in range(n):
        a, b = MII()
        hq.append([-a, b])
    
    ans = 0
    for _ in range(M):
        x, y = heappop(hq)
        ans += -x
        heappush(hq, [-Max(-x-y, 0), y])

    print(ans)

if __name__ == "__main__":
    main()
