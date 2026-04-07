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

MAXN = 10 ** 6 + 1

def main():
    n = II()

    a = LII()

    cnt = [0] * MAXN
    for x in a:
        cnt[x] += 1
    
    for i in range(MAXN, 0, -1):
        s = 0
        for j in range(i, MAXN, i):
            s += cnt[j]
        if s > 1:
            print(i) 
            break

if __name__ == "__main__":
    main()
