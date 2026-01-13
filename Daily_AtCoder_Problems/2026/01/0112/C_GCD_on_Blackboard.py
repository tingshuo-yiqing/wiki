import sys
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = [0] + list(map(int, input().split()))

    pf = [0] * (n + 1)
    for i in range(1, n + 1):
        pf[i] = gcd(pf[i - 1], a[i])

    sf = [0] * (n + 2)
    for i in range(n, 0, -1):
        sf[i] = gcd(sf[i + 1], a[i])
    
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, gcd(pf[i - 1], sf[i + 1]))
    
    print(ans)

if __name__ == "__main__":
    main()