import sys
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

def main():
    g = [list(map(int, input().split())) for _ in range(4)]

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    n = 4

    for i in range(n):
        for j in range(n):
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    if g[i][j] == g[x][y]:
                        print("CONTINUE")
                        sys.exit()
    print("GAMEOVER")
    
if __name__ == "__main__":
    main()