import sys
from itertools import permutations

Min = lambda x, y: x if x < y else y
Max = lambda x, y: x if x > y else y

inp = lambda:sys.stdin.readline().strip()

II = lambda: int(inp())
MII = lambda: map(int, inp().split())
LII = lambda: list(MII())

def main():
    n, k = MII()

    w = [LII() for _ in range(n)]

    ans = 0
    for p in permutations(range(n)):
        vised = [False] * n
        c = 0
        #! 置换环计数
        for i in range(n):
            if not vised[i]:
                c += 1
                cur = i
                while not vised[cur]:
                    vised[cur] = True
                    cur = p[cur]

        #! 可在k次交换以内得到排列p
        if k >= n - c:
            #! 取模实现环形遍历
            s = 0
            for i in range(n):
                s += w[p[i]][p[(i + 1) % n]]  #! 使用排列p进行计算
            ans = Max(ans, s)

    print(ans)

if __name__ == "__main__":
    main()
