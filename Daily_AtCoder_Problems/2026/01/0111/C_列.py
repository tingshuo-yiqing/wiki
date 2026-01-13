import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    a = [int(input()) for _ in range(n)]

    if 0 in a:
        print(n)
        sys.exit(0)
    if k == 0:
        print(0)
        sys.exit(0)
    
    w = 1
    l = 0
    ans = 0
    for r in range(n):
        w *= a[r]

        while w > k:
            w //= a[l]
            l += 1

        ans = max(ans, r - l + 1)
        
    print(ans)


if __name__ == "__main__":
    main()