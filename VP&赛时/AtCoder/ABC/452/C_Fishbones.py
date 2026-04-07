import sys
from collections import defaultdict

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
    n = II()

    N = []
    for _ in range(n):
        l, idx = MII()
        N.append((l, idx-1))
    
    m = II()

    P = [[set() for _ in range(11)] for _ in range(11)]

    outs = []
    S = []
    for _ in range(m):
        s = inp()
        S.append(s)
        sz = len(s)

        for i in range(sz):
            P[sz][i].add(s[i])
        
    for k in range(m):
        s = S[k]
        if len(s) != n:
            outs.append("No")
        else:
            f = True
            for i, (l, idx) in enumerate(N):
                if s[i] not in P[l][idx]:
                    f = False
                    break
            outs.append("Yes" if f else "No")
    
    print('\n'.join(outs))


if __name__ == "__main__":
    main()
