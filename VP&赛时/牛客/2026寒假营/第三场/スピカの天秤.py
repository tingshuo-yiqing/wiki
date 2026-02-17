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
    outs = []
    for _ in range(II()):
        n, m = MII()

        a = sorted(LII(), reverse=True)
        b = sorted(LII(), reverse=True)

        sa = sum(a)
        sb = sum(b)

        if sa == sb:
            outs.append(1)
        elif sa < sb:
            cnt = 0
            for x in b:
                sb -= x
                cnt += 1
                if sa >= sb:
                    outs.append(cnt)
                    break
        else:
            cnt = 0
            for x in a:
                sa -= x
                cnt += 1
                if sa <= sb:
                    outs.append(cnt)
                    break
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()