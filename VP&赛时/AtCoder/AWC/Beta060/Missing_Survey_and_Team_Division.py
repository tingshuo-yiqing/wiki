import sys
from collections import Counter

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

    s = [inp() for _ in range(n)]

    cnt = Counter(s)

    r = cnt['R']
    w = cnt['W']
    a = cnt['?']

    mi = Min(r, w)
    mx = Max(r, w)
    d = mx - mi

    if a >= d:
        c = a - d
        print(0 if c % 2 == 0 else 1)
    else:
        print(d - a)

if __name__ == "__main__":
    main()
