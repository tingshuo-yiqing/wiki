import sys
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    k = int(input())

    ans = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for k in range(1, k + 1):
                ans += gcd(i, j, k)

    print(ans)
if __name__ == "__main__":
    main()