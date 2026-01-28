import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, k, t = map(int, input().split())

    a = sorted(list(map(int, input().split())))

    if sum(a[:k]) < t:  # 最坏情况
        print(-1)
        sys.exit()
    
    res = n - k
    su = cnt = 0
    for i in range(k-1, -1, -1):
        su += a[i]
        cnt += 1
        if su >= t:
            print(cnt + res)
            break

if __name__ == "__main__":
    main()