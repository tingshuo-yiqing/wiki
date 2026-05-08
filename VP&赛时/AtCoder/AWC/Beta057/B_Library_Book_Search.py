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
    n = II()

    g = [[]]

    for _ in range(n):
        v = inp().split()
        g.append(v[1:])

    outs = []
    for _ in range(II()):
        t = inp()
        ans = 0
        for s in g:
            for S in s:
                ok = False
                i = 0
                for c in S:
                    if i < len(t) and t[i] == c:
                        i += 1
                    if i == len(t):
                        ok = True
                        ans += 1
                        break
                if ok:
                    break

        outs.append(ans)
    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
