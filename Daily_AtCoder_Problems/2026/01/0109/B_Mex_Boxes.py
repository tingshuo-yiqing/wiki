import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MAXN = 3 * 10**5 + 5
cnt = [0] * MAXN

def main():
    n, k = map(int, input().split())

    nums = sorted(list(map(int, input().split())))

    for i in nums:
        cnt[i] += 1

    ans = 0
    for _ in range(k):
        cur = 0
        while cnt[cur]:
            cnt[cur] -= 1
            cur += 1
        ans += cur

    print(ans)


if __name__ == "__main__":
    main()
