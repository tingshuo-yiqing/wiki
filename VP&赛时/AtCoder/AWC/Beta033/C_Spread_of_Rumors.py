import sys
from collections import deque, defaultdict

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
    n, m, k, t = MII()

    c = LII()

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        g[v].append(u)

    dq = deque(c)

    is_know = [False] * (n + 1)
    for i in dq:
        is_know[i] = True
    cnt = defaultdict(int)

    while dq:
        u = dq.popleft()

        for v in g[u]:
            if not is_know[v]:
                cnt[v] += 1
                if cnt[v] >= t:
                    is_know[v] = True
                    dq.append(v)

    print(sum(is_know))

if __name__ == "__main__":
    main()
