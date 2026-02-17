import sys
from heapq import heapify, heappop, heappush
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, k = MII()

    if k > n or k < n.bit_count():
        print("NO")
        sys.exit(0) 
    print("YES")
    
    s = bin(n)
    a = []
    for i, c in enumerate(s[2:][::-1]):
        if c == '1':
            a.append(-1 << i)

    heapify(a)

    for i in range(k - n.bit_count()):
        t = heappop(a)
        t //= 2
        heappush(a, t)
        heappush(a, t)
    
    for i in a:
        print(-i, end=' ')


if __name__ == "__main__":
    main()