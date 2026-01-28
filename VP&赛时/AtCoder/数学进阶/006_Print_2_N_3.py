import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    print(2 * n + 3)

if __name__ == "__main__":
    main()