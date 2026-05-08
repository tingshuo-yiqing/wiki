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
    s = inp()

    l = ans = 0

    MOD = 998244353

    for r, c in enumerate(s):

        if r >= 1 and s[r] == s[r-1]:
            l = r

        ans += (r - l + 1) % MOD
    
    print(ans % MOD)

if __name__ == "__main__":
    main()
