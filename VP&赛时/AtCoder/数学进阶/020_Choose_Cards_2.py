import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n = int(input())

    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for r in range(l+1, n):
                        if a[i] + a[j] + a[k] + a[l] + a[r] == 1000:
                            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()