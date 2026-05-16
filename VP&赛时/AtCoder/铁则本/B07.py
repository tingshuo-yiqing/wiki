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

    d = [0] * (n + 2)

    for _ in range(II()):
        l, r = MII()
        l += 1
        r += 1
        d[l] += 1
        d[r + 1] -= 1
    
    cur = 0
    for i in range(1, n + 1):
        cur += d[i]
        print(cur)

if __name__ == "__main__":
    main()
