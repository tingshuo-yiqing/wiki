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
    n, L, k = MII()

    a = sorted(LII())

    cnt = 0
    for i, x in enumerate(a):
        if i == k + 1:
            break
        if L - x >= 0:
            L -= x
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()
