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
    n, R = MII()

    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2 = MII()

        if (x1 - x2)**2 + (y1 - y2)**2 <= R*R:
            cnt += 1
        
    print(cnt)


if __name__ == "__main__":
    main()
