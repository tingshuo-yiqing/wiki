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
    s = inp()
    q = II()

    for _ in range(q):
        l, r, k = MII()
        l -= 1

        n = r - l
        k %= n
        sub = s[l:r]

        if k != 0:
            sub = sub[-k:] + sub[:-k]

        s = s[:l] + sub + s[r:]
    
    print(''.join(s))

if __name__ == "__main__":
    main()