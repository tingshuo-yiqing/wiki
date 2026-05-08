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
    n, m, c = MII()

    a = sorted(LII())
    b = sorted(LII())

    i = j = 0
    while i < n and j < m:
        if a[i] >= b[j]:
            i += 1
            j += 1
        else:
            i += 1
    
    
    print(j * c)

if __name__ == "__main__":
    main()
