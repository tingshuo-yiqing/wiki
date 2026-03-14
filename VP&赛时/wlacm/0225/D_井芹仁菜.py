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
    s = list(inp())

    a = LII()
    mp = {str(i+1): v for i, v in enumerate(a)}

    i = 0
    while i < n:
        if mp[s[i]] > int(s[i]):
            while i < n and mp[s[i]] >= int(s[i]):
                s[i] = str(mp[s[i]])
                i += 1
            break
        else:
            i += 1

    print(''.join(s))

if __name__ == "__main__":
    main()