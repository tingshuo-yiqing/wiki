import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MOD = 10 ** 9 + 7

def main():
    n, k = map(int, input().split())

    if n == 1:
        print(k)
        sys.exit(0)

    print(((k * (k - 1) % MOD) * pow((k-2) % MOD, n-2, MOD)) % MOD)

if __name__ == "__main__":
    main()