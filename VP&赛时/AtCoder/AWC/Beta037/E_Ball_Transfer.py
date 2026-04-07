import sys
from math import log2, gcd

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

    # 预处理 log2
    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    
    max_k = logs[n] + 1
    st = [[0] * n for _ in range(max_k)]

    st[0] = a[:]

    for k in range(1, max_k):
        for i in range(n - (1 << k) + 1):
            st[k][i] = Min(st[k-1][i], st[k - 1][i + (1 << (k-1))])
    
    def query_min(l, r):
        k = logs[r - l + 1]
        return Min(st[k][l], st[k][r - (1 << k) + 1])

    stack = []
    mxr = [n] * n
    ans = 0
    for i in range(n-1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            mxr[i] = stack[-1]
        
        ans += 0 if mxr[i] == n else query_min(i, mxr[i])

        stack.append(i)
    
    print(ans)

if __name__ == "__main__":
    main()
