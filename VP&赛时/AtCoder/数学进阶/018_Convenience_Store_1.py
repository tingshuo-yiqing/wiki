import sys
from collections import Counter
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = Counter(list(map(int, input().split())))

    ans = 0
    for x in a.keys():
        ans += a[x] * a[500 - x]

    print(ans // 2)
if __name__ == "__main__":
    main()