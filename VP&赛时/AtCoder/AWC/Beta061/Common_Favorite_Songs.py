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

    cnt = [0] * (m + 1)

    for _ in range(n):
        v = LII()
        for x in v[1:]:
            cnt[x] += 1
    
    print(sum(1 for x in cnt if x >= n))

if __name__ == "__main__":
    main()
