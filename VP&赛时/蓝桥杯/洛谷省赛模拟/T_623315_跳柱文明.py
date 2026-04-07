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
        n, X = MII()

        a = LII()

        f = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                if a[i] - a[i + 1] > X:
                    f = False
                    break
            elif a[i] < a[i + 1]:
                if a[i + 1] - a[i] > 1:
                    f = False
                    break
        
        outs.append("Win" if f else "Lose")
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
