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

    cnt = 0
    for i in range(n):
        for j in range(m):
            for l in range(i, n):
                for r in range(j, m):
                    f = True
                    for x in range(i, l + 1):
                        for y in range(j, r + 1):
                            if g[x][y] != g[i + l - x][j + r -y]:
                                f = False
                                break 
                        if not f:
                            break
                    cnt += f
    print(cnt)

if __name__ == "__main__":
    main()
