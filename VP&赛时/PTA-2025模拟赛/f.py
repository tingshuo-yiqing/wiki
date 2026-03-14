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

    # 2 * i + 1

    a = []
    s = (n * 2 + 1) * n
    for i in range(2 * n + 1): 
        x = s + i
        a.append(f"{x}^2")
    
    print(' + '.join(a[:n + 1]) + ' =\n' + ' + '.join(a[n + 1:]))
    

if __name__ == "__main__":
    main()
