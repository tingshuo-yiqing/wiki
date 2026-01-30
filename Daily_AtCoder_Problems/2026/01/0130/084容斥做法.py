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

    ans = n * (n + 1) // 2

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        ans -= (j - i) * (j - i + 1) // 2
        i = j
        
    print(ans)

if __name__ == "__main__":
    main()