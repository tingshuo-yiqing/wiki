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
    n, q = MII()
    cur = n

    a = [0] + LII()

    outs = []
    for _ in range(q):
        k = II()

        if 1 <= k < len(a):
            a[k] -= 1
            if a[k] == 0: 
                a = a[:k] + a[k+1:]
                cur -= 1
        
        outs.append(str(cur))

    print('\n'.join(outs))

if __name__ == "__main__":
    main()
