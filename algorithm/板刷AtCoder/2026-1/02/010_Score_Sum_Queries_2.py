import sys
from itertools import accumulate
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    A = [0] * (n + 1)
    B = [0] * (n + 1)

    for i in range(1, n + 1):
        c, p = map(int, input().split())

        if c == 1:
            A[i] = p
        else:
            B[i] = p

    pA = list(accumulate(A))   # 使用这个库函数时，建议数组开到 n+1
    pB = list(accumulate(B))

    outs = []
    for _ in range(int(input())):
        l, r = map(int, input().split())

        sa = pA[r] - pA[l - 1]  # 1-based 的前缀和求法
        sb = pB[r] - pB[l - 1]

        outs.append((sa, sb))

    for o in outs:
        print(*o)

if __name__ == "__main__":
    main()