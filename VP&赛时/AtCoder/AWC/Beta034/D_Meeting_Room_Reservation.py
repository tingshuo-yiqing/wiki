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

    t = []
    for _ in range(n):
        l, r = MII()
        t.append((l, r))

    t.sort(key=lambda x: x[1])

    ans = 0
    last = -1 
    for i in range(n):
        curl, curr = t[i]
        if curl >= last:
            ans += 1
            last = curr
    
    print(ans)

if __name__ == "__main__":
    main()
