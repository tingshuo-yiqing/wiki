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

class BIT:
    def __init__(self, n):
        self.tr = [0] * (n + 1)
    
    def add(self, i, val):
        while i < len(self.tr):
            self.tr[i] += val
            i += i & -i

    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tr[i]
            i -= i & -i
        return s

def main():
    n = II()

    cnt = {}
    for _ in range(n):
        u, v = MII()
        cnt[u] = v
    
    a = [cnt[u] for u in sorted(cnt.keys())]

    rank = {x: i + 1 for i, x in enumerate(sorted(set(a)))}
    m = len(rank)

    bit = BIT(m)

    ans = 0
    for i, x in enumerate(a):
        r = rank[x]
        ans += bit.pf(r - 1)
        bit.add(r, 1)
    
    print(ans)

if __name__ == "__main__":
    main()
