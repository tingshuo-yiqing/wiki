import sys
from math import lcm
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

inf = 10 ** 18

def main():
    a, b = map(int, input().split())

    if lcm(a, b) > inf:
        print("Large")
    else:
        print(lcm(a, b))

if __name__ == "__main__":
    main()