import sys
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())

    d = gcd(a, b, c)

    print(a // d - 1 + b // d - 1 + c // d - 1)    

if __name__ == "__main__":
    main()