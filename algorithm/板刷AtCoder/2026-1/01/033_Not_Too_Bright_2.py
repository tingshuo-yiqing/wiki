import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    c, d = map(int, input().split())

    if c == 1 or d == 1:
        print(c * d)
    else:
        print(((c + 1) // 2) * ((d + 1) // 2))

if __name__ == "__main__":
    main()