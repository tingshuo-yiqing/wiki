import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, m = map(int, input().split())    

    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    dir = [(0, 0), (0, 1), (1, 0), (1, 1)]

    d = 0
    for i in range(n-1):
        for j in range(m-1):
            if a[i][j] != b[i][j]:
                time = b[i][j] - a[i][j]
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    a[x][y] += time
                d += abs(time)
    
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print("No")
                sys.exit(0)
    
    print("Yes")
    print(d)


if __name__ == "__main__":
    main()