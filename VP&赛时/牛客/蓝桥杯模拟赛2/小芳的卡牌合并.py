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

        if n == 1:
            outs.append('Fang')
            continue

        outs.append("Fang" if n.bit_count() == 1 else "Ben")
        # outs.append("Fang" if (n - 1) & n == 0 else "Ben")
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
