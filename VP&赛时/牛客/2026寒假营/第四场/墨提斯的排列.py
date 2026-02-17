import sys
from itertools import permutations
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

"""
4 0 1 3 2
4 1 0 2 3
4 2 3 1 0
4 3 2 0 1
12 0 1 3 2 6 7 5 4
12 7 6 4 5 1 0 2 3
"""

def main():
    n = II()
    
    times = 1 << n

    for i in range(times):
        print(i ^ (i >> 1), end=' ')

if __name__ == "__main__":
    main()