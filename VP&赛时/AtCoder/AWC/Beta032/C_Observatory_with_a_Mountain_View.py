import sys
from bisect import bisect_right, bisect_left

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
    n, q = MII()

    h = []
    for _ in range(n):
        u, v = MII()
        h.append((u, v))
    
    h.sort()

    arr = [h[i][0] for i in range(n)]

    sf = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        sf[i] = sf[i + 1] + h[i][1]
    
    for _ in range(q):
        x = II()
        i = bisect_left(arr, x)
        print(sf[i])

if __name__ == "__main__":
    main()
