import sys
from math import inf
from collections import Counter
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
    t = inp()

    cnt = Counter(s + t)
    print(cnt)

if __name__ == "__main__":
    main()