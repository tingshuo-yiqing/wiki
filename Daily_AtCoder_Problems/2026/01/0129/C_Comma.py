import sys
from math import inf

inp = lambda: sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

def main():
    n = II()

    p = 1
    ans = 0
    for i in range(17):
        low = p
        high = p * 1000 - 1

        end = Min(n, high)
        if low <= end:
            ans += i * (end - low + 1)
        
        p *= 1000
        if end >= n:
            break
    
    print(ans)

if __name__ == "__main__":
    main()