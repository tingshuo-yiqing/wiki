import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n, q = map(int, input().split())

    s = list(input())

    off = 0
    for _ in range(q):
        o, x = map(int, input().split())

        if o == 1:
            # off = (off - x) % n  # 右移
            off = (off - x % n + n) % n  # 右移
        else:
            idx = (x - 1 + off) % n
            print(s[idx])

if __name__ == "__main__":
    main()