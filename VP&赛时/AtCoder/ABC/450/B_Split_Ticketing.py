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

    g = []
    for _ in range(n - 1):
        t = LII()
        g.append(t)
    
    for i in range(n - 1):
        for j in range(n - i - 2):
            if g[i][0] + g[i + 1][j] < g[i][j + 1]:
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    main()
