import sys
from math import gcd
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())

    ans = 0
    for x in range(1, a + 1):
        if x % b == 0 or x % c == 0:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()