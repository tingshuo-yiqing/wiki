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
    for _ in range(II()):
        n, m = MII()
        g = [list(inp()) for _ in range(n)]
        res = [list("Y" * m) for _ in range(n)]

        f = False
        cnt1 = 0
        cnt0 = 0
        c = []
        d = []
        for i in range(n):
            for j in range(m):
                if g[i][j] == '1':
                    cnt1 += 1
                    c.append((i, j))
                else:
                    cnt0 += 1
                    d.append((i, j))
                # 一般情况
                if cnt1 > 1 and cnt0 > 1:
                    for s in res:
                        print(''.join(s))
                    f = True
                    break
            if f:
                break

        if not f:
            # 只有一种
            if cnt1 == 0 or cnt0 == 0:
                for s in res:
                    print(''.join(s))
                continue
            if cnt1 == 1:
                si, sj = c[0]
                res[si][sj] = 'N'
            if cnt0 == 1:
                si, sj = d[0]
                res[si][sj] = 'N'    
            for s in res:
                print(''.join(s))

if __name__ == "__main__":
    main()