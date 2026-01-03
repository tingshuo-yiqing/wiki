import sys
from collections import deque
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()


def main():
    n, q = map(int, input().split())

    nums = list(map(int, input().split()))

    off = 0   # 相对索引为0的位置
    d = deque(nums)

    outs = []
    for _ in range(q):
        o = list(map(int, input().split()))

        # if o[0] == 1:
        #     a = (o[1] - 1 + off) % n
        #     b = (o[2] - 1 + off) % n
        #     nums[a], nums[b] = nums[b], nums[a]
        # elif o[0] == 2:
        #     off = (off - 1 + n) % n   # 右移o[1]次
        # else:
        #     idx = (o[1] - 1 + off) % n
        #     outs.append(nums[idx])

        if o[0] == 1:
            a, b = o[1] - 1, o[2] - 1
            d[a], d[b] = d[b], d[a]
        elif o[0] == 2:
            d.rotate(1)   # 正数右移，负数左移
        else:
            outs.append(d[o[1] - 1])    
    print(*outs,sep='\n')

if __name__ == "__main__":
    main()