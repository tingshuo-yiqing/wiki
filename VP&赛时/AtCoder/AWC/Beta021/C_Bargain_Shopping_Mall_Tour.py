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

    cost = []
    for _ in range(n):
        v = LII()
        cost.append(sum(v[2:]) - v[0])
    
    cost.sort(reverse=True)

    ans = 0
    for i, x in enumerate(cost):
        if i == m:
            break
        ans += Max(x, 0)
    print(ans)

if __name__ == "__main__":
    main()
