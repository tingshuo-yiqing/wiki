import sys
from math import lcm
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = list(map(int, input().split()))

    ans = 1
    for x in a:
        ans = lcm(ans, x)
    
    print(ans)

if __name__ == "__main__":
    main()