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
    n, Y, M = MII()

    NY = Y
    NM = M + 1
    if M == 12:
        NY = Y + 1
        NM = 1

    cur = nxt = 0
    for _ in range(n):
        a, b, c, d, v = MII()

        if c == Y and d == M:
            cur += v
        
        elif c == NY and d == NM:
            nxt += v
    
    print(cur, nxt)

if __name__ == "__main__":
    main()
