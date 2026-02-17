import sys
from random import randint
from collections import defaultdict

if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    for _ in range(II()):
        n = II()
        a = LII()

        cnt = defaultdict(int)
        for x in a:
            cnt[x] += 1

        mx = max(cnt.keys())

        res = [''] * n

        if cnt[mx] & 1:
            for i in range(n):
                if a[i] == mx:
                    res[i] = '1'
                else:
                    res[i] = '0'
        else:
            for i, x in enumerate(a):
                if x != mx:
                    res[i] = '1'
                else:
                    res[i] = '0'
        
        print(''.join(res))
if __name__ == "__main__":
    main()