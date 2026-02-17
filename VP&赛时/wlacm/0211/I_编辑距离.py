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
    t = inp()

    a, b = len(s), len(t)

    l = 0
    while l < a and l < b and s[a-l-1] == t[b-l-1]:
        l += 1
    print(a + b - 2 * l)     

if __name__ == "__main__":
    main()