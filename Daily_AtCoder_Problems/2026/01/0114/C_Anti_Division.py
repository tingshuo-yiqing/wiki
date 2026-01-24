import sys
from math import lcm
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def count(a, b, x):
    return b // x - (a + x - 1) // x

def counter(a, b, x):
    return b // x - (a - 1) // x


def main():
    a, b, c, d = map(int, input().split())

    e = lcm(c, d)

    # cnt1 = count(a, b, c)
    # cnt2 = count(a, b, d)
    # cnt3 = count(a, b, e)
    # print((b - a) - cnt1 - cnt2 + cnt3)

    cnt1 = counter(a, b, c)
    cnt2 = counter(a, b, d)
    cnt3 = counter(a, b, e)
    print((b - a + 1) - cnt1 - cnt2 + cnt3)

if __name__ == "__main__":
    main()