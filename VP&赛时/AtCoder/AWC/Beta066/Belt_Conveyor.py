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
    n, q = MII()
    a = [-1] + LII()

    for _ in range(q):
        x = II()

        if x != n:
            a[x + 1] += a[x]
            a[x] = 0
        elif x == n:
            a[x] = 0
        
    print(*a[1:])

if __name__ == "__main__":
    main()
