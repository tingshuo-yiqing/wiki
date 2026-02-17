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
    s = inp()

    res = [f'{s[0]}']

    l = 0
    for i in range(2, n):
        l += i
        if l >= n:
            break
        res.append(s[l])
        
    
    print(''.join(res))
if __name__ == "__main__":
    main()