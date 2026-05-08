import sys

# C

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
    a = LII()

    pf = [0] * (n + 1)
    for i in range(n):
        val = 0
        if i < n - 1:
            val = (a[i] == a[i + 1])
        pf[i + 1] = pf[i] + val

    # print(*pf) 
    
    outs = []

    for _ in range(q):
        l, r = MII()

        #! 不包括右边界的贡献
        outs.append(pf[r-1] - pf[l - 1])
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
