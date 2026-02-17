import sys
from heapq import heappop, heappush, heapify
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

MOD = 10 ** 9 + 7

def main():
    n = II()

    def cal(c, w):
        hq = [w] * c
        ret = 0
        while len(hq) > 1:
            a = heappop(hq)
            b = heappop(hq)
            ret = (ret + a + b) % MOD
            heappush(hq, a + b)
        return ret

    hq = []
    res = 0
    for _ in range(n):
        c, w = MII()
        if c > 2:
            res += ((c - 2) * 4 * w) % MOD
            heappush(hq, ((c - 2) * 4 * w) % MOD)
        elif c == 2:
            res += 2 * w
            heappush(hq, 2 * w)
        else:
            heappush(hq, w)
            
    # print(cal(8, 1))

    while len(hq) > 1:
        a = heappop(hq)
        b = heappop(hq)
        res = (res + a + b) % MOD
        heappush(hq, a + b)

    print(res % MOD)

if __name__ == "__main__":
    main()