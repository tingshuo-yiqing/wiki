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
    init = 0

    g = [[3, 2, 1, 0], 
         [0, 3, 2, 1], 
         [1, 0, 3, 2], 
         [2, 1, 0, 3], 
         [1, 2, 3, 0], 
         [3, 0, 1, 2]]

    # s = "012345"
    s = "0112233445142015320125410214530214510214102302142025101203201451451522302514203214510021454101002532"

    for i in s:
        i = int(i)
        init = g[i][init]
        print(init, end='')
    print()
if __name__ == "__main__":
    main()