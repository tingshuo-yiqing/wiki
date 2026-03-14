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

    a = [LII() for _ in range(n)]

    col = [0] * n
    row = [0] * n
    b = c = 0

    for i in range(n):
        for j in range(n):
            col[j] += a[i][j]
            row[i] += a[i][j]
            if i == j:
                b += a[i][j]
            if i + j == n - 1:
                c += a[i][j]

    s = set()
    for i in range(n):
        s.add(col[i])
        s.add(row[i])
    s.add(b)
    s.add(c)
    s = list(s)

    if len(s) > 2:
        print(-1)
        return
    elif len(s) == 2:
        print(abs(s[0] - s[1]))
    elif len(s) == 1:
        print(1)

if __name__ == "__main__":
    main()
