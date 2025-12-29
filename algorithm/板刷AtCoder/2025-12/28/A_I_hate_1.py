import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    
    if n == 1:  # 特判1
        print(1)
        print(1)
        sys.exit(0)

    print(n // 2)
    print(*list(range(2, n + 1, 2)))

if __name__ == "__main__":
    main()