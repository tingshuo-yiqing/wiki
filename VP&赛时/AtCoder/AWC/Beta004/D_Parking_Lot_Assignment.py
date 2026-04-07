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
    n, m = MII()

    if n < m:
        print("No")
        return
    
    t = []
    for _ in range(m):
        l, r = MII()
        t.append((l, r))
    
    t.sort()

    hq = []

    i = 0
    cnt = 0
    for j in range(1, n + 1):
        while i < m and t[i][0] == j:
            heappush(hq, t[i][1])
            i += 1
        if hq:
            R = heappop(hq)
            if R < j:
                print("No")
                return
            else:
                cnt += 1
    
    print("Yes" if cnt == m else "No")


if __name__ == "__main__":
    main()
