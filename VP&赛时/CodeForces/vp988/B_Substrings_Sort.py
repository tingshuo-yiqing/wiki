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
    g = [inp() for _ in range(n)]

    g.sort(key=len)

    for i in range(n - 1):
        if g[i] not in g[i + 1]:
            print("NO")
            return

    print("YES")
    for x in g:
        print(x)

if __name__ == "__main__":
    main()