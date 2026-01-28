import sys
from math import comb
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, m = map(int, input().split())

    print(comb(n, m))

if __name__ == "__main__":
    main()