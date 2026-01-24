import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

MAXN = 2 * 10**5 + 10

def main():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    vised = [-1] * MAXN 
    vised[1] = 0

    cur = 1 # 起始点
    for i in range(1, m + 1):
        cur = a[cur - 1]
        if vised[cur] != -1:
            k = i - vised[cur]  # 循环节长度
            r = (m - i) % k   # 去掉引子后的纯循环节长度
            for _ in range(r):  # 最终还要走的步数
                cur = a[cur - 1]
            break
        vised[cur] = i

    print(cur)

if __name__ == "__main__":
    main()