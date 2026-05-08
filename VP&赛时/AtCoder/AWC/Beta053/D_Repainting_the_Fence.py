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
    n, q = MII()

    T = []
    for _ in range(q):
        l, r, v = MII()
        T.append((l, r, v))
    
    nxt = list(range(n + 2))

    def find(x):
        while nxt[x] != x:
            nxt[x] = nxt[nxt[x]]
            x = nxt[x]
        return x

    res = [0] * (n + 1)
    for l, r, v in T[::-1]:
        cur = find(l)
        while cur <= r:
            res[cur] = v
            nxt[cur] = find(cur + 1)
            cur = nxt[cur]

    print(*res[1:])

if __name__ == "__main__":
    main()
