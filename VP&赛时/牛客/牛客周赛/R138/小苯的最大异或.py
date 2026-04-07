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
    for _ in range(II()):
        x, y = MII()

        a = [0, x]
        while x != 0:
            x //= 2
            a.append(x)
        
        b = [0, y]
        while y != 0:
            y //= 2
            b.append(y)
        
        ans = 0
        for i in a:
            for j in b:
                ans = Max(ans, i ^ j)

        print(ans)

if __name__ == "__main__":
    main()
