import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    a = LII()

    s = set()
    idx = []
    for i in range(n):
        if a[i] not in s:
            idx.append(i + 1)
            s.add(a[i])

    t = len(idx)
    if t < m:
        print("NO")
        return
    
    print("YES")
    print(*idx[:m])

if __name__ == "__main__":
    main()