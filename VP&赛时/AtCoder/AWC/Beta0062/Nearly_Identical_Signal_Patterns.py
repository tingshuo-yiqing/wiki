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

    s = inp()

    cnt = defaultdict(list)

    for i in range(n):
        for j in range(i, n):
            cnt[j - i + 1].append(int(s[i:j+1], 2))

    ans = 0
    for _, a in cnt.items():    
        sz = len(a)
        for i in range(sz):
            for j in range(i + 1, sz):
                if (a[i] ^ a[j]).bit_count() == 1:
                    ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
