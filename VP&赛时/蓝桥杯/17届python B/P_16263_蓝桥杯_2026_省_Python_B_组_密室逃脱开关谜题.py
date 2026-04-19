import sys
from collections import defaultdict
from itertools import combinations

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
    outs = []
    for _ in range(II()):
        n, m = MII()

        op = [(i % m, 2 * i % m) for i in range(n)]

        cnt = defaultdict(int)
        for x, y in op:
            if x == y:
                cnt[x] += 1
            else:
                cnt[x] += 1 
                cnt[y] += 1 
        
        if len(cnt.keys()) != m:
            outs.append(str(-1))
            continue

        ok = False
        for k in range((m + 1) // 2, n + 1):
            for c in combinations(range(n), k):
                cnt = defaultdict(int)
                for i in c:
                    x, y = op[i]
                    if x == y:
                        cnt[x] += 1
                    else:
                        cnt[x] += 1
                        cnt[y] += 1
                f = False
                if len(cnt.keys()) == m:
                    if all(v & 1 for v in cnt.values()):
                        f = True
                        outs.append(str(k))

                if f:
                    ok = True
                    break
            if ok:
                break

        if not ok:                    
            outs.append(str(-1))

    print('\n'.join(outs))

if __name__ == "__main__":
    main()
