import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = list(map(int, input().split()))

    cnt = [0] * 200
    
    for i, x in enumerate(nums):
        cnt[x % 200] += 1

    ans = 0
    for i in range(200):
        ans = ans + (cnt[i] - 1) * cnt[i] // 2
    
    print(ans)

if __name__ == "__main__":
    main()