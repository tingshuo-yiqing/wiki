import sys
from math import comb
from collections import Counter
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = Counter(list(map(int, input().split())))

    ans = comb(a[1], 2) + comb(a[2], 2) + comb(a[3], 2)

    print(ans)

if __name__ == "__main__":
    main()