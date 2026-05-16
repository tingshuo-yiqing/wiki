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

class SegmentTree:
    def __init__(self, arr):
        self. n = len(arr)
        self.arr = arr
        self.su = [0] * 4 * self.n
        self.add = [0] * 4 * self.n
        self._build(1, 0, self.n - 1)

    def _pushup(self, p):
        self.su[p] = self.su[p << 1] + self.su[p << 1 | 1]

    def _build(self, p, l, r):
        if l == r:
            self.su[p] = self.arr[l]
            return
        m = (l + r) >> 1
        self._build(p << 1, l, m)
        self._build(p << 1 | 1, m + 1, r)
        self._pushup(p)

    def _apply(self, p, tag, length):
        self.su[p] += tag * length
        self.add[p] += tag
    
    def _pushdown(self, p, l, r):
        if self.add[p] != 0:
            m = (l + r) >> 1
            self._apply(p << 1, self.add[p], l - m + 1)
            self._apply(p << 1 | 1, self.add[p], r - m)
            self.add[p] = 0

    def _query(self, p, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.su[p]
        self._pushdown(p, l, r)
        m = (l + r) >> 1
        res = 0
        if ql <= m:
            res += self._query(p << 1, l, m, ql, qr)
        if qr > m:
            res += self._query(p << 1 | 1, m + 1, r, ql, qr)
        return res

    def _update(self, p, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self._apply(p, val, r - l + 1)
            return
        self._pushdown(p, l, r)
        m = (l + r) >> 1
        if ql <= m:
            self._update(p << 1, l, m, ql,qr, val)
        if qr > m:
            self._update(p << 1 | 1, m + 1, r, ql,qr, val)
        self._pushup(p)

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)
    
    def update(self, ql, qr, val):
        self._update(1, 0, self.n - 1, ql, qr, val)

    def get_avg(self, l, r):
        res = self.query(l, r)
        # return f'{res / (r - l + 1):.4f}'
        return round(res / (r - l + 1), 4)
        # return f'{round(res / (r - l + 1)):.4f}'

def main():
    n, q = MII()
    a = LII()

    seg = SegmentTree(a)

    outs = []
    for _ in range(q):
        op, l, r, *v = MII()
        l -= 1
        r -= 1
        if op == 1:
            seg.update(l, r, v[0])
        elif op == 2:
            outs.append(seg.get_avg(l, r))

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
