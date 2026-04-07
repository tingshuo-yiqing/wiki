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
    outs = []
    for _ in range(II()):
        n = II()

        arr = LII()

        x = y = 0

        ans = 0
        for z in arr:
            d1 = abs(x - z)
            d2 = abs(y - z)

            if d1 < d2:
                x = z
                ans += d1
            else:
                y = z
                ans += d2
        
        outs.append(ans)

    print(*outs, sep='\n')


if __name__ == "__main__":
    main()
