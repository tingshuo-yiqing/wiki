import sys
from math import inf
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

    if n == 1:
        print(a[0])
        return

    ans = inf
    for p in permutations(range(1, n)):
        t = abs(a[0] - a[p[0]]) * p[0]
        for i in range(n - 2): 
            t += abs(a[p[i + 1]] - a[p[i]]) * abs(p[i + 1] - p[i])
            if t >= ans:
                break
        ans = Min(ans, t)
    
    print(ans)

if __name__ == "__main__":
    main()
