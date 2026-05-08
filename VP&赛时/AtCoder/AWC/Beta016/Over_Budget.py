import sys

# A

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
    ans = 0
    cnt = 0
    for _ in range(II()):
        a, b = MII()
        if a > b:
            cnt += 1
        ans += Max(0, a - b)
    
    print(cnt, ans)

if __name__ == "__main__":
    main()
