import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, p, q = map(int, input().split())

    nums = list(map(int, input().split()))

    cnt = 0
    for i in range(n - 4):
        for j in range(i + 1, n - 3):
            for k in range(j + 1, n - 2):
                for l in range(k + 1, n - 1):
                    for r in range(l + 1, n):
                        # if (nums[i] * nums[j] * nums[k] * nums[l] * nums[r]) % p == q:
                        # 直接计算虽然不会溢出，但是python的整数超过 2^63-1 后计算速度大大降低
                        # 计算过程中应该使用取模不断将数字压缩在 [0, p-1] 
                        if (nums[i] * (nums[j] % p) * (nums[k] % p) * (nums[l] % p) * (nums[r] % p)) % p == q:
                            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()