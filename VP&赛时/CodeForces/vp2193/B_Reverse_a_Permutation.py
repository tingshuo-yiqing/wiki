import sys

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    for _ in range(int(input())):
        n = int(input())

        a = list(map(int, input().split()))

        idx = n
        f = False
        for i in range(n):
            if a[i] != idx:
                r = a.index(idx)
                l = i
                while l < r:
                    a[l], a[r] = a[r], a[l]
                    l += 1
                    r -= 1
                print(*a)
                f = True
                break
            else:
                idx -= 1
        if not f:
            print(*a)
if __name__ == "__main__":
    main()