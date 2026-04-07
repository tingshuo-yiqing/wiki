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
        self.tree = [0] * (n + 1)
    
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def pf(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

def main():
    n, q = MII()

    B = int(n ** 0.5) + 1
    memo = [0] * (B + 1)

    a = LII()

    bit = BIT(n)
    for i, x in enumerate(a):
        bit.add(i + 1, x)

    outs = []
    for _ in range(q):
        o = LII()
        op = o[0]
 
        if op == 1:
            k, v = o[1:]
            if k > B:
                for i in range(k, n + 1, k):
                    if i % k == 0:
                        bit.add(i, v)
            else:
                memo[k] += v
        else:
            x = o[1]
            total = sum((x // k) * memo[k] for k in range(1, B + 1))
            outs.append(str(bit.pf(x) + total))

    print('\n'.join(outs))

if __name__ == "__main__":
    main()
