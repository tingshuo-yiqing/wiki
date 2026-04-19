import sys
from itertools import combinations
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

MOD = 10 ** 9 + 7

def main():
    n, k, m = MII()
    a = LII()

    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]

    def get_setsum(arr):
        n = len(arr)
        ret = defaultdict(lambda: defaultdict(int))
        for i in range(1 << n):
            total = 0
            cnt = 0
            for j in range(n):
                if (i >> j) & 1:
                    total += arr[j]
                    cnt += 1
            ret[cnt][total % m] += 1
        return ret

    cnt1 = get_setsum(a1)
    cnt2 = get_setsum(a2)

    ans = 0
    for k1 in range(k + 1):  
        k2 = k - k1
        
        if k1 > len(a1) or k2 > len(a2):
            continue
        
        left_rem = cnt1[k1]
        right_rem = cnt2[k2]

        for r1, c1 in left_rem.items():
            r2 = (m - r1) % m
            if r2 in right_rem:
                ans += c1 * right_rem[r2] % MOD

    print(ans)

if __name__ == "__main__":
    main()
