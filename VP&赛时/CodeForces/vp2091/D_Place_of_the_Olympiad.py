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
        n, m, k = MII()

        k = (k + n - 1) // n  # 此时k为人数最多的一行，最小值由这一行决定
        
        ans = m // (m - k + 1)  # 均分原理

        outs.append(ans)

    print(*outs, sep='\n')    

if __name__ == "__main__":
    main()