import sys
from itertools import permutations

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
    n = II()

    a = LII()
    w = LII()

    mx = 0
    for p in permutations(range(n)):
        s = 0
        for i in range(n-1):
            s += abs(a[p[i]] - a[p[i+1]]) * w[i]
        mx = Max(mx, s)

    print(mx)

if __name__ == "__main__":
    main()
