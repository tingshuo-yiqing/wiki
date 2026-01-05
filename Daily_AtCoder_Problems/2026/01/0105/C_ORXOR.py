import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = list(map(int, input().split()))

    ans = float('inf')
    for i in range(1 << (n - 1)):
        xo = xor = 0

        for j in range(n):
            xo |= nums[j]
            
            if (j < n - 1 and i >> j & 1) or j == n - 1:
                xor ^= xo
                xo = 0

        ans = min(ans, xor)

    print(ans)

if __name__ == "__main__":
    main()