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

    ans = []
    n = len(s)

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        ans.append(s[i])
        ans.append(j - i)
        i = j
    
    print(''.join(map(str, ans)))

if __name__ == "__main__":
    main()