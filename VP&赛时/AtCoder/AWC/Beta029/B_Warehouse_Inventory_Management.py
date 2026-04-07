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

    a = LII()

    for _ in range(q):
        o = LII()
        op = o[0]

        if op == 1:
            x, y = o[1:]
            x -= 1
            y -= 1
            a[y] += a[x]
            a[x] = 0
        else:
            i = o[1]
            print(a[i - 1])

if __name__ == "__main__":
    main()
