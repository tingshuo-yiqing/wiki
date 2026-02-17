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
    s = set()
    for x in a[::-1]:
        if x not in s:
            ans.append(x)
            s.add(x)
    
    print(len(ans))
    print(*ans[::-1])

if __name__ == "__main__":
    main()