import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    a = list(map(int, input().split()))

    t = 100000
    idx = defaultdict(int)

    ans = 0
    for i in a:
        if t - i in idx:
            ans += idx[t-i]
        idx[i] += 1

    print(ans)

if __name__ == "__main__":
    main()