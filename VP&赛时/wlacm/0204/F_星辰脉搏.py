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
    n = II()
    a = LII()
    
    i = 0
    while i + 1 < n and a[i+1] > a[i]:
        i += 1
    while i + 1 < n and a[i+1] == a[i]:
        i += 1
    while i + 1 < n and a[i+1] < a[i]:
        i += 1

    print("YES" if i == n - 1 else "NO")

if __name__ == "__main__":
    main()