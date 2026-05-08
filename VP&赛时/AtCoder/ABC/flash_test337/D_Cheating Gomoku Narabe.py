"""
题意: H×W网格，每个格子为'o'/'x'/'.'，可将'.'改成'o'。问是否能得到连续K个'o'（横/竖），求最小修改次数。
思路: 对每行每列分别做滑动窗口，维护窗口内'x'个数和'.'个数。若窗口内无'x'，则操作次数取'.'个数的最小值。
"""
def solve() -> None:
    H, W, K = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]

    INF = 10 ** 9
    ans = INF

    # 横向滑动 (仅当 K <= W 时)
    if K <= W:
        for i in range(H):
            row = grid[i]
            cnt_x = 0
            cnt_dot = 0
            for j in range(K):
                if row[j] == 'x':
                    cnt_x += 1
                elif row[j] == '.':
                    cnt_dot += 1
            if cnt_x == 0:
                ans = min(ans, cnt_dot)
            for j in range(K, W):
                left = row[j - K]
                if left == 'x':
                    cnt_x -= 1
                elif left == '.':
                    cnt_dot -= 1
                right = row[j]
                if right == 'x':
                    cnt_x += 1
                elif right == '.':
                    cnt_dot += 1
                if cnt_x == 0:
                    ans = min(ans, cnt_dot)

    # 纵向滑动 (仅当 K <= H 时)
    if K <= H:
        for j in range(W):
            cnt_x = 0
            cnt_dot = 0
            for i in range(K):
                if grid[i][j] == 'x':
                    cnt_x += 1
                elif grid[i][j] == '.':
                    cnt_dot += 1
            if cnt_x == 0:
                ans = min(ans, cnt_dot)
            for i in range(K, H):
                top = grid[i - K][j]
                if top == 'x':
                    cnt_x -= 1
                elif top == '.':
                    cnt_dot -= 1
                bottom = grid[i][j]
                if bottom == 'x':
                    cnt_x += 1
                elif bottom == '.':
                    cnt_dot += 1
                if cnt_x == 0:
                    ans = min(ans, cnt_dot)

    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    solve()