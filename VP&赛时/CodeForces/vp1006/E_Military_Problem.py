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
    it = iter(input_data)

    II = lambda: int(next(it))
    SI = lambda: next(it)
    
    if not input_data:
        sys.exit()

def main():
    n = II()
    q = II()
    pa = [II() for _ in range(n - 1)]

    g = [[] for _ in range(n + 1)]

    for v, fa in enumerate(pa, start=2):
        g[fa].append(v)
    
    sz = [0] * (n + 1)
    tin = [0] * (n + 1)
    seq = []

    st = [(1, 0)]
    while st:
        u, state = st.pop()
        if state  == 0:
            tin[u] = len(seq)
            seq.append(u)
            st.append((u, 1))
            for v in sorted(g[u], reverse=True):
                st.append((v, 0))
        else:
            cur = 1
            for v in g[u]:
                cur += sz[v]
            sz[u] = cur

    outs = []
    for _ in range(q):
        i = II()
        k = II()

        if k > sz[i]:
            outs.append('-1')
        else:
            outs.append(str(seq[tin[i] + k - 1]))
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
