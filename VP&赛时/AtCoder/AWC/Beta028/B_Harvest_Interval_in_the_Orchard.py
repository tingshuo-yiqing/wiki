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
    n, L, R = MII()

    a = LII()

    i = mx = 0
    while i < n:
        j = i
        while j < n and L <= a[j] <= R:
            j += 1
        mx = max(mx, j - i)
        i = j + 1
    
    print(mx)

if __name__ == "__main__":
    main()
