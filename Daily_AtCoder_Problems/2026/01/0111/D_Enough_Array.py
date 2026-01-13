import sys 
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    a = [0] + list(map(int, input().split()))

    pf = [0] * (n + 1)
    for i in range(1, n + 1):
        pf[i] = pf[i - 1] + a[i]
    
    l = ans = 0
    for r in range(1, n + 1):
        while pf[r] - pf[l] >= k:
            ans += (n - r + 1)
            l += 1
    
    print(ans)

if __name__ == "__main__":
    main()