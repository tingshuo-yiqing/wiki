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
    n, m, k = MII()

    g = [list(inp()) for _ in range(n)]

    op = inp()

    i = j = 0
    for o in op:
        if g[i][j] == '#':
            g[i][j] = '.'
        
        if o =='U':
            if i - 1 >= 0:
                i -= 1
        elif o == 'D':
            if i + 1 < n:
                i += 1
        elif o == 'R':
            if j + 1 < m:
                j += 1
        else:
            if j - 1 >= 0:
                j -= 1
    if g[i][j] == '#':
        g[i][j] = '.'

    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
