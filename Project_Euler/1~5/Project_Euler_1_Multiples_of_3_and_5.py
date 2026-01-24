import sys
from math import lcm
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def Sum(a, n):
    limit = n // a
    return a * (limit + 1) * limit // 2

def main():
    outs = []
    for _ in range(int(input())):
        n = int(input())

        c = lcm(3, 5)

        outs.append(Sum(3, n-1) + Sum(5, n-1) - Sum(c, n-1))    
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()