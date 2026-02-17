import sys
from heapq import heappop, heappush
from math import sqrt
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def hypot(a, b):
    return sqrt(a * a + b * b)

def diff(a, b):
    d = hypot(a, b) - hypot(a, b-1)
    return d

def main():
    n, w = MII()

    hq = [] 
    ans = 0
    for _ in range(n):
        a, b = MII()
        ans += hypot(a, b) 
        heappush(hq, (-diff(a, b), a, b))
    
    t = []
    for _ in range(w):
        if hq:
            d, a, b = heappop(hq)
            b -= 1
            ans += d
            if b:
                heappush(hq, (-diff(a, b), a, b))
            else:
                t.append(a)
        else:
            break
    
    print(f'{ans:.9f}')

if __name__ == "__main__":
    main()