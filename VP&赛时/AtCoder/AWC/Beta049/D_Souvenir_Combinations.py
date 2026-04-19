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
    n, m, k = MII()

    a = sorted(LII(), reverse=True)
    b = sorted(LII(), reverse=True)

    hq = [(-a[0] * b[0], 0, 0)]

    #! 之所以要去重是因为同一元组可能会被多次入堆
    #! 比如(1, 1)，可能会被(0, 1)和(1, 0)同时到达
    vised = {(0, 0)}

    ans = 0
    for _ in range(k):
        v, i, j = heappop(hq)
        ans += -v

        if i + 1 < n and (i + 1, j) not in vised:
            vised.add((i + 1, j))
            heappush(hq, (-a[i + 1] * b[j], i + 1, j))
            
        if j + 1 < m and (i, j + 1) not in vised:
            vised.add((i, j + 1))
            heappush(hq, (-a[i] * b[j + 1], i, j + 1))

    print(ans)

if __name__ == "__main__":
    main()
