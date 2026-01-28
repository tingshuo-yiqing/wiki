import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, q = map(int, input().split())

    cnt = [1] * (n + 1)

    outs = []
    mi = 1
    for _ in range(q):
        x, y = map(int, input().split())

        ans = 0
        for i in range(mi, x + 1):
            ans += cnt[i]
        
        outs.append(ans)
        cnt[y] += ans
        mi = Max(x + 1, mi)

    print(*outs, sep='\n')


if __name__ == "__main__":
    main()