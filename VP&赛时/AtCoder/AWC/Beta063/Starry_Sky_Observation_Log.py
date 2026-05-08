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
    n, m = MII()

    g = [inp() for _ in range(n)]

    outs = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'T':
                outs.append((i, j))
    
    print(len(outs))
    for i, j in outs:
        print(i + 1, j + 1)

if __name__ == "__main__":
    main()
