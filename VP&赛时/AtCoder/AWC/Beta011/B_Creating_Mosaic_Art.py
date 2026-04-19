import sys

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
    n, m, k = MII()
    c1, c2 = inp().split()

    g = [inp() for _ in range(n)]

    res = []
    for s in g:
        t = []
        for c in s:
            t.append(c1 * k if c == '#' else c2 * k)
        t = ''.join(t)
        for _ in range(k):
            res.append(t)
    
    for o in res:
        print(o)

if __name__ == "__main__":
    main()
