import sys

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
    """Fenwick Tree for frequency counting with binary lifting (find_kth)"""
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        # Precompute largest power of two <= n for binary lifting
        self.max_pow = 1
        while (self.max_pow << 1) <= n:
            self.max_pow <<= 1

    def add(self, idx, delta):
        """Add delta at position idx (1-based)"""
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def pf(self, idx):
        """Prefix sum up to idx (1-based)"""
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def find_kth(self, k):
        """
        Find the smallest index such that prefix sum >= k (1-indexed k)
        k is 1-indexed: find the k-th smallest element
        Returns the index (1-based) in the compressed coordinate space.
        """
        idx = 0
        bitmask = self.max_pow
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1  # 1-based index in BIT


def main():
    Q = II()
    queries = []
    all_vals = set()

    for _ in range(Q):
        parts = inp().split()
        op = parts[0]
        x = int(parts[1])
        queries.append((op, x))
        all_vals.add(x)

    # Coordinate compression
    sorted_vals = sorted(all_vals)
    comp = {v: i + 1 for i, v in enumerate(sorted_vals)}  # 1-based for BIT
    decomp = {i + 1: v for i, v in enumerate(sorted_vals)}

    N = len(sorted_vals)
    bit = BIT(N)
    total = 0  # current number of elements in multiset
    ans = 0

    for op, x in queries:
        idx = comp[x]
        if op == '+':
            bit.add(idx, 1)
            total += 1
        else:
            # Before removal, find the median
            # median position = ceil(total / 2)
            k = (total + 1) // 2  # (total + 1) // 2 = ceil(total / 2)
            median_idx = bit.find_kth(k)
            median_val = decomp[median_idx]

            if median_val == x:
                ans += 1

            # Perform removal
            bit.add(idx, -1)
            total -= 1

    print(ans)


if __name__ == "__main__":
    main()