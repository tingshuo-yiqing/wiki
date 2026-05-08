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

    nxt = list(range(n + 2))

    def find(x):
        while nxt[x] != x:
            nxt[x] = nxt[nxt[x]]
            x = nxt[x]
        return x
    
    res = [0] * (n + 1)

    for _ in range(q):
        l, r, v = MII()

        cur = find(l)
        # 
        while cur <= r:
            nx = find(cur + 1)
            if cur != v:
                res[cur] = v
                nxt[cur] = nx
            # 胜者还是非占用的，可以继续下一轮比赛，所以 cur != v 才更新打败他的人
            # 即更新 res[cur] = v 和 nxt[cur] = nx, 胜者没有nx
            cur = nx
    
    print(*res[1:])

if __name__ == "__main__":
    main()
