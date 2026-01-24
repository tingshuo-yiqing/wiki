import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = [int(input()) for _ in range(n)]

    s = set()
    s.add(1)

    cur = 1
    for i in range(1, n + 1):
        cur = a[cur - 1]
        if cur == 2:
            print(i)
            sys.exit(0)
        if cur in s:
            print(-1)
            sys.exit(0)
        s.add(cur)

if __name__ == "__main__":
    main()