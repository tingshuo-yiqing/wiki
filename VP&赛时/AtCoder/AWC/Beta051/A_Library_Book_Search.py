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
    P = LII()
    L = LII()
    T = sorted(LII())

    j = 0
    mx = 0
    for i in range(m):
        if j < k and T[j] - 1 == i:
            mx = Max(mx, L[T[j] - 1])
            j += 1

    print(sum(x for x in P if x <= mx)) 

if __name__ == "__main__":
    main()
