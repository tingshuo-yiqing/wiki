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
    n = II()
    s = inp()

    pf = [0] * (n + 1)

    cur = 0
    for i in range(n):
        if s[i] == 'A':
            cur += 1
        elif s[i] == 'B':
            cur -= 1
        pf[i + 1] = cur

    rank = {x: i+1 for i, x in enumerate(sorted(set(pf)))}
    m = len(rank)

    bit = BIT(m)

    ans = 0
    for x in pf:
        r = rank[x]
        ans += bit.pf(r - 1)
        bit.add(r, 1)

    print(ans)

if __name__ == "__main__":
    main()
