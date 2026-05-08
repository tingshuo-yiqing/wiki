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

MOD = 998244353

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.su = [0] * 4 * n
        self.po = [0] * 4 * n
        self.add = [0] * 4 * n
        self._build(1, 0, n - 1)

    def _pushup(self, p):
        self.su[p] = self.su[p << 1] + self.su[p << 1 | 1]
        self.po[p] = self.po[p << 1] + self.po[p << 1 | 1]

    def _build(self, p, l, r):
        if l == r:
            return 
        m = (l + r) >> 1
        self._build(p << 1, l, m)
        self._build(p << 1 | 1, m + 1, r)
        self._pushup(p)
    
    def lazy(self, p, val, length):
        self.po[p] = (self.po[p] + 2 * val * self.su[p] + length * val * val) % MOD
        self.su[p] = (self.su[p] + val * length) % MOD
        self.add[p] = (self.add[p] + val) % MOD

    def _pushdown(self, p, l, r):
        if self.add[p] != 0:
            tag = self.add[p]
            m = (l + r) >> 1
            self.lazy(p << 1, tag, m - l + 1)
            self.lazy(p << 1 | 1, tag, r - m)
            self.add[p] = 0
 
    def _query(self, p, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.su[p], self.po[p]
        self._pushdown(p, l, r)
        m = (l + r) >> 1
        res_su = res_po = 0
        if ql <= m:
            x, y = self._query(p << 1, l, m, ql, qr)
            res_su = (res_su + x) % MOD
            res_po = (res_po + y) % MOD
        if qr > m:
            x, y = self._query(p << 1 | 1, m + 1, r, ql, qr)
            res_su = (res_su + x) % MOD
            res_po = (res_po + y) % MOD
        return res_su % MOD, res_po % MOD

    def _update(self, p, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self.lazy(p, val, r - l + 1)
            return
        self._pushdown(p, l, r)
        m = (l + r) >> 1
        if ql <= m:
            self._update(p << 1, l, m, ql, qr, val)
        if qr > m:
            self._update(p << 1 | 1, m + 1, r, ql, qr, val)
        self._pushup(p)
    
    def query(self, ql, qr):
        x, y = self._query(1, 0, self.n - 1, ql ,qr)
        return (x * x - y) * pow(2, -1, MOD) % MOD

    def update(self, ql, qr, val):
        self._update(1, 0, self.n - 1, ql, qr, val)


def main():
    n, q = MII()

    seg = SegmentTree(n)

    outs = []
    for _ in range(q):
        l, r, v = MII()
        l -= 1
        r -= 1
        seg.update(l, r, v)
        outs.append(seg.query(l, r))
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
