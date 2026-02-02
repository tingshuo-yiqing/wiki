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
        n = II()

        ans = n * (n + 1) // 2

        p = 1
        while p <= n:
            ans -= p * 2
            p *= 2
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

if __name__ == "__main__":
    main()