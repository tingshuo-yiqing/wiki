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
    n, q, MOD = MII()

    D = [-1]
    P = [-1]
    for _ in range(n):
        d, p = MII()
        D.append(d)
        P.append(p)
    
    outs = []

    for _ in range(q):
        s, k = MII()
        

if __name__ == "__main__":
    main()
