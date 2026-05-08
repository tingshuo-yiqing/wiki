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
    n = II()
    w = LII()

    dp = 1
    for x in w:
        dp |= (dp << x)
    
    outs = []
    for i in range(1, sum(w) + 1):
        if (dp >> i) & 1:
            outs.append(i)
    
    print(len(outs))
    print(*outs)

if __name__ == "__main__":
    main()
