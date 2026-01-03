import sys
from itertools import accumulate
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, q = map(int, input().split())

    nums = [0] + list(map(int, input().split()))
    A = list(accumulate(nums))

    off = 0

    outs = []
    for _ in range(q):
        o = list(map(int, input().split()))

        if o[0] == 1:
            off = (off + o[1]) % n
        else:
            l = (o[1] - 1 + off) % n  # 先转成 0-based
            r = (o[2] - 1 + off) % n
            if l <= r:
                outs.append(A[r + 1] - A[l])   # 0-based前缀和求法
            else:
                outs.append(A[r + 1] + A[n] - A[l])
    
    print(*outs, sep='\n')
if __name__ == "__main__":
    main()