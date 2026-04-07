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

def main():
    n, m, q = MII()

    A = []
    C = []
    for _ in range(m):
        x, v = inp().split()
        A.append(int(x))
        C.append(v)
    
    outs = []
    for _ in range(q):
        s = inp()

        f = False
        for i, c in enumerate(C):
            idx = A[i] - 1
            if s[idx] != c:
                f = True
                break
        outs.append("No" if f else "Yes")
    
    print('\n'.join(outs))

if __name__ == "__main__":
    main()
