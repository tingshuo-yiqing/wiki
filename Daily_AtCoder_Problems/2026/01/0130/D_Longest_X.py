import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    s = inp()
    k = II()

    win = l = 0
    ans = 0
    for r, x in enumerate(s):
        if x == '.':
            win += 1
        
        while win > k:
            if s[l] == '.':
                win -= 1
            l += 1
        ans = Max(ans, r - l + 1)
    
    print(ans)

if __name__ == "__main__":
    main()