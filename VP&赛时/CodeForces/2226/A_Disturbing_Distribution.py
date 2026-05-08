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
    MOD = 676767667
    outs = []
    for _ in range(II()):
        n = II()
        a = LII()

        ans = 0
        for i in range(n):
            if a[i] != 1:
                ans += a[i]
        
        ans += (a[-1] == 1)
        outs.append(ans % MOD)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
