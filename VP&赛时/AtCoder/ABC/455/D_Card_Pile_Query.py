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

    nxt = list(range(n + 1))

    for _ in range(q):
        u, v = MII()
        nxt[u] = v
    
    din = [True] * (n + 1)
    for i in range(1, n + 1):
        if nxt[i] != i:
            din[nxt[i]] = False

    # print(din)

    s = set()
    ans = [0] * (n + 1)
    for i, x in enumerate(din[1:]):
        if x:
            cur = i + 1
            cnt = 0
            while cur not in s:
                # print(cur,z end=' ')
                cnt += 1
                s.add(cur)
                cur = nxt[cur]
            # print()
            ans[cur] = cnt

    print(*ans[1:])        

if __name__ == "__main__":
    main()
