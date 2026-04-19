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

        cnt = 0
        for x in a:
            cnt += 1 if x == 1 else 2
        
        outs.append('L' if cnt & 1 else 'Q')
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
