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


def main():
    n, k = MII()

    T = []
    for _ in range(n):
        a, b = MII()
        T.append((a, b))

    T.sort()

    mi = deque()

    s = mx = l = 0
    for i, (x, y) in enumerate(T):
        s += x
        while mi and T[mi[-1]][1] >= y:
            mi.pop()

        mi.append(i)
        
        if i - mi[-1] >= k:
            mi.popleft()
            
        if i >= k - 1:
            mx = Max(mx, s * T[mi[-1]][1])
            s -= T[l][0]
            l += 1

    print(mx)

if __name__ == "__main__":
    main()
    
