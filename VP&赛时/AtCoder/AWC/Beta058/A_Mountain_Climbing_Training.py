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
    n, p, t, c = MII()
    a = LII()

    if not a and p < t:
        print(-1)
        return
    if not a and p >= t:
        print(0)
        return

    ans = -1
    if p < t:
        if max(a) >= t:
            ans = c
    else:
        ans = 0
    
    print(ans)

if __name__ == "__main__":
    main()
