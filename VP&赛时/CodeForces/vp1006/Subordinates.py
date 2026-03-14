import sys

input_type = 0

if input_type:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

else:
    input_data = sys.stdin.read().split()
    
    if not input_data:
        sys.exit()

def main():
    it = iter(input_data)
    
    try:
        n = int(next(it))
        pa = [int(next(it)) for _ in range(n - 1)]
    except StopIteration:
        sys.exit()

    g = [[] for _ in range(n + 1)]

    for v, u in enumerate(pa, start=2):
        g[u].append(v)

    sz = [0] * (n + 1)
    st = [(1, 0)]
    while st:
        u, state = st.pop()
        if state == 0:
            st.append((u, 1))
            for v in g[u]:
                st.append((v, 0))
        else:
            cur = 1
            for v in g[u]:
                cur += sz[v]
            sz[u] = cur

    print(*sz[1:])

if __name__ == "__main__":
    main()
