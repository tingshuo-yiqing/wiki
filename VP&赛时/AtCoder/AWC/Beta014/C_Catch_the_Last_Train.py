class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # 用数组代替对象，极大地提高访问速度
        self.maxv = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _pushup(self, p):
        self.maxv[p] = max(self.maxv[p << 1], self.maxv[p << 1 | 1])

    def _pushdown(self, p):
        if self.lazy[p] != 0:
            lz = self.lazy[p]
            # 左子节点
            self.maxv[p << 1] += lz
            self.lazy[p << 1] += lz
            # 右子节点
            self.maxv[p << 1 | 1] += lz
            self.lazy[p << 1 | 1] += lz
            self.lazy[p] = 0

    def _build(self, p, l, r, arr):
        if l == r:
            self.maxv[p] = arr[l]
            return
        mid = (l + r) >> 1
        self._build(p << 1, l, mid, arr)
        self._build(p << 1 | 1, mid + 1, r, arr)
        self._pushup(p)

    def update(self, p, l, r, qL, qR, val):
        if qL <= l and r <= qR:
            self.maxv[p] += val
            self.lazy[p] += val
            return
        self._pushdown(p)
        mid = (l + r) >> 1
        if qL <= mid:
            self.update(p << 1, l, mid, qL, qR, val)
        if qR > mid:
            self.update(p << 1 | 1, mid + 1, r, qL, qR, val)
        self._pushup(p)

    def query(self, p, l, r, qL, qR):
        if qL <= l and r <= qR:
            return self.maxv[p]
        self._pushdown(p)
        mid = (l + r) >> 1
        res = -float('inf')
        if qL <= mid:
            res = max(res, self.query(p << 1, l, mid, qL, qR))
        if qR > mid:
            res = max(res, self.query(p << 1 | 1, mid + 1, r, qL, qR))
        return res