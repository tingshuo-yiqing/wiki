import sys
from collections import defaultdict

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
    s = inp()

    dAB = defaultdict(int)
    dAC = defaultdict(int)
    dBC = defaultdict(int)
    dABBC = defaultdict(int)

    dAB[0] = 1
    dAC[0] = 1
    dBC[0] = 1
    dABBC[(0, 0)] = 1

    a = b = c = 0
    for ch in s:
        if ch == 'A':
            a += 1
        elif ch == 'B':
            b += 1
        else:
            c += 1
        dAB[a - b] += 1
        dAC[a - c] += 1
        dBC[b - c] += 1
        dABBC[(a - b, b - c)] += 1

    ans = n * (n + 1) // 2

    for v in dAB.values():
        ans -= v * (v - 1) // 2
    
    for v in dAC.values():
        ans -= v * (v - 1) // 2
    
    for v in dBC.values():
        ans -= v * (v - 1) // 2
    
    for v in dABBC.values():
        ans += v * (v - 1)
    
    print(ans)

if __name__ == "__main__":
    main()
