import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    mi = sum(abs(A[i] - B[i]) for i in range(n))

    print("Yes" if mi <= k and (k - mi) % 2 == 0 else "No")

if __name__ == "__main__":
    main()