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
    g = [list(MII()) for _ in range(3)]

    s = sum(g[0])
    for l in g:
        if sum(l) != s:
            print("No")
            return
    
    if g[0][0] + g[1][1] + g[2][2] != s:
        print("No")
        return
    if g[2][0] + g[1][1] + g[0][2] != s:
        print("No")
        return
    
    for j in range(3):
        t = g[0][j] + g[1][j] + g[2][j]
        if t != s:
            print("No")
            return

    ss = set()
    for i in range(3):
        for j in range(3):
            ss.add(g[i][j])
    if len(ss) != 9:
        print("No")
        return

    print("Yes")

if __name__ == "__main__":
    main()