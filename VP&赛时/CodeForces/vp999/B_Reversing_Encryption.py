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

    for i in range(1, n + 1):
        if n % i == 0:
            s = s[:i][::-1] + s[i:]
    
    print(s)

if __name__ == "__main__":
    main()