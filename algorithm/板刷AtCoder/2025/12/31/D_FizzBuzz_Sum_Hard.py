import sys
from math import lcm
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def Sum(n):
    return n * (n + 1) // 2

def main():
    n, a, b = map(int, input().split())

    c = lcm(a, b)

    print(Sum(n) - a * Sum(n // a) - b * Sum(n // b) + c * Sum(n // c))

if __name__ == "__main__":
    main()