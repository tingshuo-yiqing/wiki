import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    a = list(map(int, input().split()))

    l = ans = 0
    while l < n:
        r = l + 1
        while r < n and a[r] - a[r-1] > 0:
            r += 1
        cnt = r - l
        ans += cnt * (cnt + 1) // 2
        l = r
    
    print(ans)

if __name__ == "__main__":
    main()