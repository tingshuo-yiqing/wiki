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
    s = inp()

    char = {'o': 0, 'x': 0}

    found = l = ans = 0
    for r, x in enumerate(s):
        char[x] += 1
        if char[x] == 1:
            found += 1
        
        while found >= 2:
            ans += n - r
            dc = s[l]
            char[dc] -= 1
            if char[dc] == 0:
                found -= 1
            l += 1
    
    print(ans)

if __name__ == "__main__":
    main()