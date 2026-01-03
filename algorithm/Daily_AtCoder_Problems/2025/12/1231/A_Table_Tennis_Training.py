import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, a, b = map(int, input().split())

    dif = b - a

    if dif % 2 == 0:
        print(dif // 2)
    else:
        c = a - 1
        d = n - b
        if c <= d:
            ans = c + 1 + (dif - 1) // 2  # 可以改变奇偶性
        else:
            ans = 1 + d + (dif - 1) // 2
        print(ans)
if __name__ == "__main__":
    main()