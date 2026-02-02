import sys
from math import inf
if 1:
    inp = lambda: sys.stdin.readline().strip()

    II = lambda: int(inp())
    MII = lambda: map(int, inp().split())
    LII = lambda: list(MII())

    Max = lambda x, y: x if x > y else y
    Min = lambda x, y: x if x < y else y

def main():
    n = II()
    A = sorted(LII())

    q = II()
    B = [II() for _ in range(q)]

    s = []
    for i, x in enumerate(B):
        s.append((x, i))
    s.sort()

    ans = [0] * q

    ci = 0
    for x, oi in s:
        # 两两之间对比
        while ci < n - 1:
            cur = abs(x - A[ci])
            nxt = abs(x - A[ci + 1])
            if cur >= nxt:  # 注意两个相同的元素要移动
                ci += 1
            else:
                break
        ans[oi] = abs(x - A[ci])

    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()