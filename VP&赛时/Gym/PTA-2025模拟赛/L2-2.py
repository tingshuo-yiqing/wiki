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

    if n == 0:
        print(0)
        sys.exit(0)
    
    t = []
    for _ in range(n):
        s, e = inp().split()
        a, b, c = s.split(':')
        d, f, g = e.split(':')
        t.append((int(a) * 60 * 60 + int(b) * 60 + int(c), int(d) * 60 * 60 + int(f) * 60 + int(g)))
    
    t.sort(key=lambda x: x[1])

    ans = 1
    last = t[0][1]
    for i in range(1, n):
        if t[i][0] >= last:
            last = t[i][1]
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
