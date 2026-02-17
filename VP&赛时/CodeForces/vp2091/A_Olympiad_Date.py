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
    outs = []
    for _ in range(II()):
        n = II()
        a = LII()

        ans = 0
        cnt = defaultdict(int)
        for i, x in enumerate(a):
            cnt[x] += 1
            if cnt[0] >= 3 and cnt[1] >= 1 and cnt[3] >= 1 and cnt[2] >= 2 and cnt[5] >= 1:
                ans = i + 1
                break
        outs.append(ans)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()