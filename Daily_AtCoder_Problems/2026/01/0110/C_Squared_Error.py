import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = list(map(int, input().split()))

    su = sum((n - 1) * x ** 2 for x in a)

    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += -2 * a[i] * s

    print(ans + su)

if __name__ == "__main__":
    main()