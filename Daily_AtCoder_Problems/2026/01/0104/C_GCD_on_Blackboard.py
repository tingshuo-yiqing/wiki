import sys
from itertools import accumulate
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

 
def main():
    n = int(input())

    A = [0] + list(map(int, input().split()))

    pf = list(accumulate(A, gcd))
    sf = list(accumulate(A[::-1], gcd))[::-1] + [0]

    # pf = [0] * (n + 1)
    # for i in range(1, n + 1):
    #     pf[i] = gcd(pf[i - 1], A[i])
    
    # sf = [0] * (n + 2)
    # for i in range(n, 0, -1):
    #     sf[i] = gcd(sf[i + 1], A[i])
    
    # print(pf)
    # print(sf)

    ans = 0
    for i in range(1, n + 1):
        # 模拟删除操作，不包含A[i]的前后缀gcd的gcd
        ans = max(ans, gcd(pf[i - 1], sf[i + 1]))

    print(ans)

if __name__ == "__main__":
    main()