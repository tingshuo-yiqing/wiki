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
    n, m = MII()

    MOD = 10 ** 9 + 7

    ans = 0
    for i in range(1 << n):
        s = []
        for j in range(n):
            s.append('1' if (i >> j) & 1 else '0')
        s = ''.join(s)
        a = s.split('0')
        temp = sum(len(k) * (len(k) + 1) // 2 for k in a if k != '')
        if temp >= m:
            ans += 1
        ans %= MOD
    
    print(ans % MOD)

if __name__ == "__main__":
    main()
