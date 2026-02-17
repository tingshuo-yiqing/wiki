import sys
from collections import defaultdict
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    q = II()
    
    idx = defaultdict(list)

    ans = []
    i = 0
    for _ in range(q):
        o = LII()
        if o[0] == 1:
            ans.append(o[1])
            idx[o[1]].append(i)
            i += 1
        else:
            x, y = o[1:]
            if x == y: 
                continue
            for j in idx[x]:
                ans[j] = y
            for j in idx[x]:
                idx[y].append(j)

            idx[x].clear()

    # print(idx)
    print(*ans)
        
if __name__ == "__main__":
    main()