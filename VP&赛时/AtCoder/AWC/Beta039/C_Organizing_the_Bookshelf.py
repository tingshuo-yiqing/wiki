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
    n, k = MII()

    A = LII()
    B = LII()

    ans = 0

    l = 0
    w = s = 0

    for r, x in enumerate(B):
        w += x
        s += A[r]

        while w > k:
            w -= B[l]
            s -= A[l]
            l += 1
        
        ans = Max(ans, s)
    
    print(ans)

if __name__ == "__main__":
    main()
