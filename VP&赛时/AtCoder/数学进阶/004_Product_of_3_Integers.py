import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    a = list(map(int, input().split()))

    print(a[0] * a[1] * a[2])

if __name__ == "__main__":
    main()