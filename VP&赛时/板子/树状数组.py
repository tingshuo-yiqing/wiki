class BIT:
    def __init__(self, n_or_arr) -> None:
        if isinstance(n_or_arr, int):
            self.n = n_or_arr
            self.tree = [0] * (self.n + 1)   # 可以作为差分数组使用

        else:
            self.n = len(n_or_arr)
            self.tree = [0] + n_or_arr

            for i in range(1, self.n + 1):
                j = i + (i & -i)
                if j <= self.n:
                    self.tree[j] += self.tree[i]

    def add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & (-i)

    def pf(self, i):
        su = 0
        while i > 0:
            su += self.tree[i]
            i -= i & (-i)
        return su

    def query(self, l, r):
        if l > r:
            return 0
        return self.pf(r) - self.pf(l - 1)