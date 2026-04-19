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
    n, L = MII()
    a = LII()

    ans = 0
    mx = 0
    for i, D in enumerate(a):
        if L >= D:
            if D > mx:
                mx = D
                ans = i + 1

    print(ans if mx != 0 else -1)

if __name__ == "__main__":
    main()
