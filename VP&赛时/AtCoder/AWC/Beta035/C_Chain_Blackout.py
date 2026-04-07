import sys
from collections import deque

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

    T = [-1] + LII()

    g = [[] for _ in range(n + 1)]

    din = [0] * (n + 1)
    for _ in range(m):
        u, v = MII()
        g[u].append(v)
        din[v] += 1
    
    dq = deque([i for i in range(1, n + 1) if din[i] > T[i]])

    is_block = [False] * (n + 1)
    for i in dq:
        is_block[i] = True

    while dq:
        u = dq.popleft()

        for v in g[u]:
            if not is_block[v]:  # 会死循环
                din[v] += 1
                if din[v] > T[v]:
                    is_block[v] = True
                    dq.append(v)

    ans = [i for i in range(1, n + 1) if is_block[i]]

    if len(ans) == 0:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main()
