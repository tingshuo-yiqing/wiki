import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    score = []
    for _ in range(n):
        a, b = map(int, input().split())
        score.append(b)
        score.append(a - b)

    ans = 0
    for i, x in enumerate(sorted(score, reverse=True), 1):
        if i <= k:
            ans += x

    print(ans)

if __name__ == "__main__":
    main()