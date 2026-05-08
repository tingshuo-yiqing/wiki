import sys
from math import gcd

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y

input_type = 1

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

else:
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    for _ in range(II()):
        n = II()
        a = LII()

        ans = 0
        for i in range(n -1):
            if gcd(a[i + 1], a[i]) == Max(a[i + 1], a[i]) - Min(a[i + 1], a[i]):
                ans += 1
        
        print(ans)

if __name__ == "__main__":
    main()
