import sys
from collections import Counter

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
    n, m = MII()

    din = [[i, 0] for i in range(m + 1)]
    cnt = Counter()

    for _ in range(n):
        a, b = MII()
        if a > b:
            a, b = b, a
        cnt[(a, b)] += 1
        din[a][1] += 1
        din[b][1] += 1
    
    din.sort(key=lambda x: -x[1])

    mx = din[0][1] 
    s = set(din[i][0] for i in range(m + 1) if din[i][1] == mx)
    sz = len(s)

    ans = 0
    if sz > 1:
        t = 0
        mi = 10 ** 10

        for (x, y), v in cnt.items():
            if x in s and y in s:
                t += 1
                mi = Min(mi, v)

        ans = 2 * mx if sz * (sz - 1) // 2 > t else 2 * mx - mi

    else:
        mx2 = din[1][1]
        s2 = set(din[i][0] for i in range(m + 1) if din[i][1] == mx2)

        z = din[0][0]
        t = 0
        mi = 10 ** 10
        for (x, y), v in cnt.items():
            other = -1
            if x == z:
                other = y
            if y == z:
                other = x
            if other != -1 and other in s2:
                t += 1
                mi = Min(mi, v)
        
        ans = mx + mx2 if t < len(s2) else mx + mx2 - mi
    
    print(ans)

if __name__ == "__main__":
    main()
