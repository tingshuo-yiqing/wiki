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
        a = LII()
        b = LII()

        for i in range(n - 1):
            if a[i] != b[i]:
                d = b[i] - a[i]
                a[i] += d
                a[i + 1] += d

        if a[-1] == b[-1]:
            outs.append("Yes")
        else: 
            outs.append("No")
    
    print('\n'.join(outs))


if __name__ == "__main__":
    main()
