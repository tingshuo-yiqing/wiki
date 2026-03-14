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

        if n % 2 == 0:
            outs.append(0)
            continue
        
        s = str(n)
        f = False
        for i, x in enumerate(s):
            if int(x) % 2 == 0:
                if i == 0:
                    outs.append(1)
                else:
                    outs.append(2)
                f = True
                break
        if not f:
            outs.append(-1)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
