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
    n, q = MII()

    g = [list(inp()) for _ in range(n)]

    alphas = []
    for i in range(26):
        alphas.append(chr(97 + i))
    
    to = {c: c for c in alphas}

    for _ in range(q):
        a, b = inp().split()
        for c in alphas:
            if to[c] == a:
                to[c] = b
    
    for s in g:
        for i in range(len(s)):
            s[i] = to[s[i]]
        print(''.join(s))

if __name__ == "__main__":
    main()
