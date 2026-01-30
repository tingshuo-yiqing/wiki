import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n, m = MII()
    if n == m == 1:
        print(1)
        sys.exit(0)
        
    ans = n * m - 2 
    if n > 1 and m > 1:
        ans = (n - 2) * (m - 2)
    
    print(ans)
if __name__ == "__main__":
    main()