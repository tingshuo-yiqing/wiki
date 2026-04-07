import sys
from collections import defaultdict, Counter

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
    n, k, q = MII()
    a = LII()

    freq = Counter(a)

    outs = []
    for _ in range(q):
        o = LII()
        op = o[0]

        if op == 1:
            p, v = o[1:]
            freq[a[p-1]] -= 1
            a[p-1] = v
            freq[v] += 1
        else:
            is_ok = True
            for i in range(1, k + 1):
                if freq[i] == 0:
                    outs.append(-1)
                    is_ok = False
                    break
            if is_ok:
                mi = 10 ** 10
                cnt = defaultdict(int)
                have = l = 0

                for r, x in enumerate(a):
                    cnt[x] += 1
                    if cnt[x] == 1 and 1 <= x <= k:
                        have += 1
                    while have == k:
                        mi = Min(mi, r - l + 1)
                        dv = a[l]
                        cnt[dv] -= 1
                        if cnt[dv] == 0:
                            have -= 1
                        l += 1
                outs.append(mi)

    print(*outs, sep='\n')

if __name__ == "__main__":
    main()
