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
        n, m = MII()

        g = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = MII()
            g[u].append(v)
            g[v].append(u)
        
        

if __name__ == "__main__":
    main()
