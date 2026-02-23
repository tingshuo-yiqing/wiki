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
    a, b, x = MII()

    s = '1' if a < b else '0'

    core = []
    curr = s
    for _ in range(x + 1):
        core.append(curr)
        curr = '1' if curr == '0' else '0'
    
    ra = a - core.count('0')
    rb = b - core.count('1')

    i0 = core.index('0')
    i1 = core.index('1')

    ans = []
    for i, c in enumerate(core):
        ans.append(c)
        if i == i0:
            ans.append('0' * ra)
        if i == i1:
            ans.append('1' * rb)

    print(''.join(ans))

if __name__ == "__main__":
    main()