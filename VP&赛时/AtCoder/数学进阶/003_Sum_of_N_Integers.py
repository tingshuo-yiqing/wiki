import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    a = list(map(int, input().split()))

    print(sum(a))

if __name__ == "__main__":
    main()