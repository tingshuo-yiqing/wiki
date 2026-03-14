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

    ans = []
    for i in a:
        if i & 1:
            ans.append(i)
        else:
            ans.append(i - 1) 
    
    print(*ans)

if __name__ == "__main__":
    main()