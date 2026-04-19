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
    a = LII()
    MOD = 998244353

    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    
    maxk = logs[n] + 1
    st = [[0] * n for _ in range(maxk)]

    st[0] = a[:]
    for k in range(1, maxk):
        for i in range(n - (1<<k) + 1):
            st[k][i] = Max(st[k-1][i], st[k-1][i + (1<<(k-1))])
    
    def query_max(l, r):
        k = logs[r - l + 1]
        return Max(st[k][l], st[k][r - (1<<k) + 1])
    
    def f(num):
        return len(str(num))
    
    ans = 0
    for i in range(n):
        for j in range(i, n):
            l = j - i + 1
            ans = (ans + f(l) * query_max(i, j)) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()
