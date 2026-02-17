import sys
from math import inf
from collections import defaultdict
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    k, s = MII()

    ans = 0
    cnt = set()

    for i in range(k + 1):
        for j in range(k + 1):
            val = i + j
            rem = s - val
            if 0 <= rem <= k:
                ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()