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
    a = sorted(LII())
    b = sorted(LII())

    hq = [(a[0] + b[0], 0, 0)]

    vised = {(0, 0)}

    outs = []
    for _ in range(n):
        v, i, j = heappop(hq)
        outs.append(v)

        if i + 1 < n and (i + 1, j) not in vised:
            vised.add((i + 1, j))
            heappush(hq, (a[i + 1] + b[j],i + 1, j))

        if j + 1 < n and (i, j + 1) not in vised:
            vised.add((i, j + 1))
            heappush(hq, (a[i] + b[j + 1],i, j + 1))
    
    print(*outs)

if __name__ == "__main__":
    main()
