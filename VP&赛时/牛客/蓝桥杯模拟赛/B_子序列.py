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

MOD = 10 ** 9 + 7

def C(a, b):
    return a * (a - 1) // 2

def main():
    a = []
    for _ in range(2026):
        a.append(2)
        a.append(0)
        a.append(2)
        a.append(6)
    n = len(a)

    pf0 = [0] * (n + 1)
    for i in range(n):
        pf0[i + 1] = pf0[i] + (a[i] == 0)

    pf2 = [0] * (n + 1)
    for i in range(n):
        pf2[i + 1] = pf2[i] + (a[i] == 2)

    pf6 = [0] * (n + 1)
    for i in range(n):
        pf6[i + 1] = pf6[i] + (a[i] == 6)

    cnt = Counter(a)

    ans = 0
    for i in range(1, n + 1):
        cur = a[i - 1]

        if cur == 2:
            ans += (C(cnt[2] - pf2[i], 2)) % MOD # [2, 2, 2]
        elif cur == 6:
            ans += (C(cnt[6] - pf6[i], 2)) % MOD # [6, 6, 6]
            ans += (C(cnt[0] - pf0[i], 2)) % MOD # [6, 0, 0]
            ans += ((cnt[6] - pf6[i]) * (cnt[0] - pf0[i])) % MOD  # [6, 6, 0]
        elif cur == 0:
            ans += (C(cnt[0] - pf0[i], 2)) % MOD # [0, 0, 0]
            ans += (C(cnt[6] - pf6[i], 2)) % MOD # [0, 6, 6]
            ans += ((cnt[6] - pf6[i]) * (cnt[0] - pf0[i])) % MOD  # [0, 6, 0]

    print(ans % MOD)

if __name__ == "__main__":
    main()
