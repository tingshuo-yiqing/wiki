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
        n, u = MII()
        a = sorted(LII(), reverse=True)

        ans = 0
        cnt = 0
        for x in a:
            cnt += 1
            if cnt * x >= u:  # 从大到小，每次 x 就是当前的最小值
                ans += 1
                cnt = 0
        outs.append(ans)
    
    print(*outs, sep='\n')


if __name__ == "__main__":
    main()