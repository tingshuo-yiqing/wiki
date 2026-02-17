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
    n = II()
    s = inp() + '#'

    cnt = ans = 0
    for x in s:
        if x == 'x':
            cnt += 1
        else:
            ans += Max(0, cnt - 2)
            cnt = 0
    
    print(ans)

if __name__ == "__main__":
    main()