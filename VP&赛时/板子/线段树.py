import sys
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

inf = 10**10

class SegmentTree:
    def __init__(self, data, op=lambda x, y: x + y, padding=0) -> None:
        self.data = data
        self.n = len(data)
        self.op = op
        self.padding = padding
        self.tree = [padding] * (self.n << 2)
        self.build(1, 0, self.n-1)

    lc = staticmethod(lambda rt: rt << 1)
    rc = staticmethod(lambda rt: rt << 1 | 1)

    def push_up(self, rt):
        self.tree[rt] = self.op(self.tree[self.lc(rt)], self.tree[self.rc(rt)])

    def build(self, rt, l, r):
        if l == r:
            self.tree[rt] = self.data[l]
            return
        m = (l + r) >> 1
        self.build(self.lc(rt), l, m)
        self.build(self.rc(rt), m + 1, r)
        self.push_up(rt)

    def _update(self, rt, l, r, idx, val):
        if l == r:
            self.tree[rt] = val
            return 
        m = (l + r) >> 1
        if idx <= m:
            self._update(self.lc(rt), l, m, idx, val)
        else:
            self._update(self.rc(rt), m+1, r, idx, val)
        self.push_up(rt)
    
    def _query(self, rt, l, r, L, R):
        if L <= l and r <= R:  # 完全覆盖
            return self.tree[rt]
        m = (l + r) >> 1
        res = self.padding
        if L <= m:
            vl = self._query(self.lc(rt), l, m, L, R)
            res = self.op(res, vl)  # 不能写死了加法
        if R > m:
            vr = self._query(self.rc(rt), m+1, r, L, R)
            res = self.op(res, vr)
        return res

    def update(self, idx, val):
        self._update(1, 0, self.n-1, idx, val)

    def query(self, L, R):
        return self._query(1, 0, self.n-1, L, R)


def main():
     ...
if __name__ == "__main__":
    main()
