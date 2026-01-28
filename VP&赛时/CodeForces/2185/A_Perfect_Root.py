import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n = int(input())

        for i in range(1, n + 1):
            print(i, end=' ')
        print()

if __name__ == "__main__":
    main()