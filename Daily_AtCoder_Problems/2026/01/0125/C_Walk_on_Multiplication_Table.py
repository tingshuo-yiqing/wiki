import sys
from math import inf
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    ans = inf
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans = min(ans, i-1 + n // i - 1)
    
    print(ans)

if __name__ == "__main__":
    main()