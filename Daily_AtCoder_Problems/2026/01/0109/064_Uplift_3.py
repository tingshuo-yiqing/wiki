import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, q = map(int, input().split())

    nums = [0] + list(map(int, input().split()))

    diff = [0] * (n + 1)

    ans = 0
    for i in range(2, n + 1):
        diff[i] = nums[i] - nums[i - 1]
        ans += abs(diff[i])
    print(nums)
    print(diff)
    outs = []
    for _ in range(q):
        l, r, x = map(int, input().split())
        if l > 1:
            old = abs(diff[l])
            diff[l] += x
            new = abs(diff[l])
            ans += (new - old)

        if r < n:
            old = abs(diff[r + 1])
            diff[r + 1] -= x
            new = abs(diff[r + 1])
            ans += (new - old) 

        outs.append(ans)
        
    print(*outs, sep='\n')

if __name__ == "__main__":
    main()