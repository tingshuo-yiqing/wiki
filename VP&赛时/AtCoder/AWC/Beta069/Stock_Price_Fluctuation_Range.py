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
    n, m = MII()

    mx = -1

    D = []
    for _ in range(n):
        A = LII()
        s = 0
        for i in range(m - 1):
            s += abs(A[i] - A[i + 1])
        mx = Max(mx, s)
        D.append(s)

    for i, x in enumerate(D):
        if x == mx:
            print(i + 1)
            break

if __name__ == "__main__":
    main()
