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
    n, v = MII()
    a = LII()
    t = LII()

    ans = []
    cur = 0
    for i in range(n - 1):
        cur += a[i]
        if t[i] * v > cur:
            ans.append(i + 2)

    if ans:
        print(*ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
