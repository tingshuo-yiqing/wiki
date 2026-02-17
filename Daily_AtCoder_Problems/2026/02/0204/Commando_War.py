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
    idx = 0
    while True:
        n = II()
        if n == 0:
            break
    
        t = [list(MII()) for _ in range(n)]

        t.sort(key=lambda x: -x[1])

        ans = 0
        cur = 0
        for k, v in t:
            cur += k
            ans = Max(cur + v, ans)
        
        idx += 1
        print(f'Case {idx}: {ans}')

if __name__ == "__main__":
    main()