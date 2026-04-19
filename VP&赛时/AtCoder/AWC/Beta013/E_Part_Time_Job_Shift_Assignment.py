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

    g = [[]]
    for _ in range(n):
        g.append(LII()[1:])
    
    match = [-1] * (m + 1)
    ans = 0

    def dfs(u, vised):
        for v in g[u]:
            if not vised[v]:
                vised[v] = True
                if match[v] == -1 or dfs(match[v], vised):
                    match[v] = u
                    return True
        return False
    
    for i in range(1, n + 1):
        vised = [False] * (m + 1)
        if dfs(i, vised):
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
