# ABC337D - Cheating Gomoku Narabe
# 题意：H×W 网格，每格为 o、x 或 .。可以将 . 改为 o，求最少操作次数使得
#       存在一行或一列中有连续 K 个 o。如果不可能则输出 -1。
# 思路：使用滑动窗口。对每一行和每一列分别处理长度为 K 的窗口：
#       统计窗口内 x 的数量（有 x 则不可能全 o）和 . 的数量（需要改的次数）。
#       取所有窗口的最小 "." 数作为答案。

H, W, K = map(int, input().split())
grid = [input().strip() for _ in range(H)]

INF = 10**9
ans = INF

# 检查每一行
for i in range(H):
    cnt_x = 0   # 窗口内 'x' 的数量
    cnt_dot = 0 # 窗口内 '.' 的数量
    for j in range(W):
        # 加入右端点
        if grid[i][j] == 'x':
            cnt_x += 1
        elif grid[i][j] == '.':
            cnt_dot += 1
        # 移除左端点（窗口长度超过 K）
        if j >= K:
            left = grid[i][j - K]
            if left == 'x':
                cnt_x -= 1
            elif left == '.':
                cnt_dot -= 1
        # 窗口长度恰好为 K 时判断
        if j >= K - 1:
            if cnt_x == 0:
                ans = min(ans, cnt_dot)

# 检查每一列
for j in range(W):
    cnt_x = 0
    cnt_dot = 0
    for i in range(H):
        if grid[i][j] == 'x':
            cnt_x += 1
        elif grid[i][j] == '.':
            cnt_dot += 1
        if i >= K:
            left = grid[i - K][j]
            if left == 'x':
                cnt_x -= 1
            elif left == '.':
                cnt_dot -= 1
        if i >= K - 1:
            if cnt_x == 0:
                ans = min(ans, cnt_dot)

print(-1 if ans == INF else ans)