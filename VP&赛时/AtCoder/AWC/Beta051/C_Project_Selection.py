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
    n, m, K = MII()

    C = [0] * n
    P = [0] * n

    for i in range(n):
        x, y = MII()
        C[i] = x
        P[i] = y

    limit = [[] for _ in range(n)]
    for _ in range(m):
        u, v = MII()
        u -= 1
        v -= 1
        limit[u].append(v)
        limit[v].append(u)
    
    ans = 0
    for i in range(1 << n):
        s = res = 0
        for j in range(n):
            if (i >> j) & 1:
                for v in limit[j]:
                    i = i & ~(1 << v)   #! 关键: 将第v位置为0
                s += C[j]
                res += P[j]
        if s <= K:
            ans = Max(ans, res)
    
    print(ans)

if __name__ == "__main__":
    main()
