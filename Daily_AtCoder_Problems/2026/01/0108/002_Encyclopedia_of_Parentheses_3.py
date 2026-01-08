import sys
from math import comb
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    if n & 1:
        sys.exit()
    
    # ans = []
    # m = n // 2
    # path = [''] * n
    # def dfs(i, open):
    #     if i == n:
    #         ans.append(''.join(path))
    #         return 
    #     if open < m:
    #         path[i] = '('
    #         dfs(i + 1, open + 1)
    #     if i - open < open:
    #         path[i] = ')'
    #         dfs(i + 1, open)
    # dfs(0, 0)
    # print(*ans, sep='\n')

    def valid(path):
        b = mb = 0
        for c in path:
            b += 1 if c == '(' else -1
            mb = min(mb, b)
        return b == 0 and mb == 0

    outs = []
    for i in range(1 << n):
        if bin(i).count('1') != n // 2:
            continue

        path = [''] * n
        for j in range(n):
            path[j] = '(' if (i >> j) & 1 else ')'
        if valid(path):
            outs.append(''.join(path))
    
    outs.sort()
    print(*outs, sep='\n')
    print(20 * 2**20)
if __name__ == "__main__":
    main()