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
        self.n = len(arr)
        self.tr = [0] * 4 * self.n
        self.add = [0] * 4 * self.n
        self.arr = arr
        self._build(1, 0, self.n-1)

    def _pushup(self, p):
        self.tr[p] = self.tr[p << 1] + self.tr[p << 1 | 1]
    
    def lazy(self, p, tag, length):
        self.tr[p] += tag * length
        self.add[p] += tag

    def _pushdown(self, p, l, r):
        if self.add[p] != 0:
            m = (l + r) >> 1
            tag = self.add[p]

            # 下发懒标记
            self.lazy(p << 1, tag, m - l + 1)
            self.lazy(p << 1 | 1, tag, r - m)

            self.add[p] = 0
            
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

    def _build(self, p, l, r):
        if l == r:
            self.tr[p] = self.arr[l]
            return 
        m = (l + r) >> 1
        self._build(p << 1, l, m)
        self._build(p << 1 | 1, m + 1, r)

        self._pushup(p)
    
    def _query(self, p, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tr[p]
        
        self._pushdown(p, l, r)

        res = 0
        m = (l + r) >> 1
        if ql <= m:
            res += self._query(p << 1, l, m, ql, qr)
        if qr > m:
            res += self._query(p << 1 | 1, m + 1, r, ql, qr)
        return res
    
    def update(self, ql, qr, val):
        self._update(1, 0, self.n-1, ql, qr, val)
    
    def query(self, ql, qr):
        return self._query(1, 0, self.n-1, ql, qr)


def main():
    n, q = MII()
    a = LII()

    seg = SegmentTree(a)

    outs = []
    for _ in range(q):
        o = LII()
        op = o[0]

        if op == 1:
            l, r, v = o[1:]
            l -= 1
            r -= 1
            seg.update(l, r, v)
        else:
            l, r = o[1:]
            l -= 1
            r -= 1
            outs.append(seg.query(l, r))

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
