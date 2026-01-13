import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, q = map(int, input().split())

    a = list(map(int, input().split()))

    off = 0

    outs = []
    for _ in range(q):
        o = list(map(int, input().split()))

        if o[0] == 1:
            ia = (o[1] + off - 1) % n
            ib = (o[2] + off - 1) % n
            a[ia], a[ib] = a[ib], a[ia]
        elif o[0] == 2:
            off = (off + (n - 1)) % n   # 右移一位等于左移n-1位
        else:
            idx = (o[1] + off - 1) % n
            outs.append(a[idx])

    print(*outs, sep='\n')
if __name__ == "__main__":
    main()