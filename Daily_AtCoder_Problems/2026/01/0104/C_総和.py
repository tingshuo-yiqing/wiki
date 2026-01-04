import sys
from itertools import accumulate
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    A = [0] + list(map(int, input().split()))

    pf = list(accumulate(A))

    su = 0
    for i in range(n - k + 1):
        j = i + k
        # print(i, j)
        su += (pf[j] - pf[i])

    print(su)

if __name__ == "__main__":
    main()